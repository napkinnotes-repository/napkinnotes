from __future__ import annotations

import hashlib
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


BASE_DIR = Path(__file__).resolve().parents[1]

IMAGES_DIR = BASE_DIR / "images"
THEME_IMAGES_DIR = BASE_DIR / "theme" / "images"
OUTPUT_DIR = BASE_DIR / "certificados"

LOGO_PATH = THEME_IMAGES_DIR / "nn_logo.png"
FIRMA_PATH = IMAGES_DIR / "firma.png"

WEB_URL = "https://napkinnotes.es"
WEB_LABEL = "napkinnotes.es"
VERIFY_EMAIL = "napkiin.notes@proton.me"

SIGNER_NAME = "Duvier Suárez Fontanella"
SIGNER_ROLE = "En nombre del Comité Editorial de Napkin Notes"

DEFAULT_ROLE = "Colaborador editorial de Napkin Notes"

REQUIRED_FIELDS = {
    "title",
    "author",
    "date",
}


# Paleta cálida/editorial.
PAPER = colors.HexColor("#FBF7EE")
PAPER_SOFT = colors.HexColor("#FFFDF8")
INK = colors.HexColor("#1F2933")
INK_DARK = colors.HexColor("#111827")
MUTED = colors.HexColor("#6B7280")
MUTED_DARK = colors.HexColor("#4B5563")
BORDER = colors.HexColor("#C8A96A")
BORDER_SOFT = colors.HexColor("#E8DCC2")
ACCENT = colors.HexColor("#8A6A32")


def check_required_files() -> None:
    missing = []

    for label, path in (
        ("logo", LOGO_PATH),
        ("firma", FIRMA_PATH),
    ):
        if not path.exists():
            missing.append(f"- Falta {label}: {path}")

    if missing:
        raise FileNotFoundError("\n".join(missing))


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug or "certificado"


def read_front_matter(markdown_path: Path) -> dict[str, object]:
    text = markdown_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError(f"{markdown_path}: no tiene front matter YAML al inicio.")

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)

    if not match:
        raise ValueError(f"{markdown_path}: front matter YAML inválido.")

    data = yaml.safe_load(match.group(1)) or {}

    if not isinstance(data, dict):
        raise ValueError(f"{markdown_path}: el front matter no es un diccionario válido.")

    return data


def should_generate_certificate(article: dict[str, object]) -> bool:
    value = article.get("certificate", True)

    if isinstance(value, bool):
        return value

    return str(value).strip().lower() in {"true", "yes", "1", "si", "sí"}


def validate_article(article: dict[str, object], path: Path) -> None:
    missing = REQUIRED_FIELDS - set(article.keys())

    if missing:
        fields = ", ".join(sorted(missing))
        raise ValueError(f"{path}: faltan campos obligatorios: {fields}")

    empty = [
        field
        for field in REQUIRED_FIELDS
        if not str(article.get(field, "")).strip()
    ]

    if empty:
        fields = ", ".join(sorted(empty))
        raise ValueError(f"{path}: campos vacíos: {fields}")


def normalize_date_for_code(value: object) -> str:
    text = str(value).strip()

    try:
        dt = datetime.strptime(text, "%Y-%m-%d")
        return dt.strftime("%Y%m%d")
    except ValueError:
        cleaned = re.sub(r"[^0-9A-Za-z]+", "", text)
        return cleaned[:8] or "nodate"


def format_date(value: object) -> str:
    months = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }

    text = str(value).strip()

    try:
        dt = datetime.strptime(text, "%Y-%m-%d")
        return f"{dt.day} de {months[dt.month]} de {dt.year}"
    except ValueError:
        return text


def generate_certificate_code(article: dict[str, object], article_path: Path) -> str:
    title = str(article["title"]).strip()
    author = str(article["author"]).strip()
    date_code = normalize_date_for_code(article["date"])

    relative_path = article_path.relative_to(BASE_DIR).as_posix()

    raw_id = f"{title}|{author}|{date_code}|{relative_path}"
    digest = hashlib.sha1(raw_id.encode("utf-8")).hexdigest()[:6].upper()

    return f"NN-COL-{date_code}-{digest}"


def draw_centered_text(
    pdf: canvas.Canvas,
    text: str,
    y: float,
    font_name: str,
    font_size: int,
    color: colors.Color = INK,
) -> None:
    width, _ = landscape(A4)

    pdf.setFillColor(color)
    pdf.setFont(font_name, font_size)
    pdf.drawCentredString(width / 2, y, text)


def draw_wrapped_centered_text(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    max_width: float,
    font_name: str,
    font_size: int,
    leading: int,
    color: colors.Color = INK,
) -> float:
    words = text.split()
    lines: list[str] = []
    current_line = ""

    pdf.setFont(font_name, font_size)

    for word in words:
        candidate = f"{current_line} {word}".strip()

        if pdf.stringWidth(candidate, font_name, font_size) <= max_width:
            current_line = candidate
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    pdf.setFillColor(color)

    for line in lines:
        pdf.drawCentredString(x, y, line)
        y -= leading

    return y


def draw_watermark(pdf: canvas.Canvas, width: float, height: float) -> None:
    pdf.saveState()
    pdf.setFillAlpha(0.055)
    pdf.setStrokeAlpha(0.055)

    watermark_width = 18.5 * cm
    watermark_height = 18.5 * cm

    pdf.drawImage(
        str(LOGO_PATH),
        (width - watermark_width) / 2,
        (height - watermark_height) / 2 - 0.15 * cm,
        width=watermark_width,
        height=watermark_height,
        preserveAspectRatio=True,
        mask="auto",
    )

    pdf.restoreState()


def draw_certificate(
    pdf: canvas.Canvas,
    article: dict[str, object],
    article_path: Path,
) -> None:
    width, height = landscape(A4)

    title = str(article["title"]).strip()
    author = str(article["author"]).strip()
    publication_date = format_date(article["date"])
    certificate_code = generate_certificate_code(article, article_path)
    role = DEFAULT_ROLE

    pdf.setTitle(f"Certificado Napkin Notes - {author}")

    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    outer_margin = 1.1 * cm

    pdf.setFillColor(PAPER_SOFT)
    pdf.roundRect(
        outer_margin,
        outer_margin,
        width - 2 * outer_margin,
        height - 2 * outer_margin,
        14,
        stroke=0,
        fill=1,
    )

    draw_watermark(pdf, width, height)

    margin = 1.45 * cm

    pdf.setStrokeColor(BORDER)
    pdf.setLineWidth(1.25)
    pdf.roundRect(
        margin,
        margin,
        width - 2 * margin,
        height - 2 * margin,
        10,
        stroke=1,
        fill=0,
    )

    pdf.setStrokeColor(BORDER_SOFT)
    pdf.setLineWidth(0.7)
    pdf.roundRect(
        margin + 0.28 * cm,
        margin + 0.28 * cm,
        width - 2 * (margin + 0.28 * cm),
        height - 2 * (margin + 0.28 * cm),
        8,
        stroke=1,
        fill=0,
    )

    # Logo superior.
    # Ajuste horizontal: (width - logo_width) / 2
    # Ajuste vertical: height - 3.25 * cm
    logo_width = 5.4 * cm
    logo_height = 2.25 * cm

    pdf.drawImage(
        str(LOGO_PATH),
        (width - logo_width) / 2,
        height - 3.25 * cm,
        width=logo_width,
        height=logo_height,
        preserveAspectRatio=True,
        mask="auto",
    )

    draw_centered_text(
        pdf,
        "Ciencia clara · ideas que caben en una servilleta",
        height - 3.95 * cm,
        "Helvetica",
        9.5,
        MUTED,
    )

    draw_centered_text(
        pdf,
        "CERTIFICADO DE COLABORACIÓN",
        height - 5.1 * cm,
        "Helvetica-Bold",
        21,
        INK_DARK,
    )

    pdf.setStrokeColor(ACCENT)
    pdf.setLineWidth(0.7)
    pdf.line(
        width / 2 - 4.0 * cm,
        height - 5.48 * cm,
        width / 2 + 4.0 * cm,
        height - 5.48 * cm,
    )

    y = height - 6.75 * cm

    institutional_text = (
        "El Comité Editorial de Napkin Notes certifica que la siguiente persona "
        "ha colaborado con la revista mediante una aportación editorial publicada "
        "en nuestro espacio de divulgación científica."
    )

    y = draw_wrapped_centered_text(
        pdf,
        institutional_text,
        width / 2,
        y,
        21.2 * cm,
        "Helvetica",
        11.6,
        16,
        MUTED_DARK,
    )

    y -= 0.58 * cm

    draw_centered_text(
        pdf,
        author,
        y,
        "Helvetica-Bold",
        29,
        INK_DARK,
    )

    y -= 1.1 * cm

    draw_centered_text(
        pdf,
        role,
        y,
        "Helvetica",
        13.5,
        INK,
    )

    box_width = 19.2 * cm
    box_height = 2.25 * cm
    box_x = (width - box_width) / 2
    box_y = y - 3.0 * cm

    pdf.setFillColor(PAPER)
    pdf.setStrokeColor(BORDER_SOFT)
    pdf.setLineWidth(0.7)
    pdf.roundRect(
        box_x,
        box_y,
        box_width,
        box_height,
        8,
        stroke=1,
        fill=1,
    )

    draw_centered_text(
        pdf,
        "Contribución publicada",
        box_y + 1.55 * cm,
        "Helvetica-Bold",
        9.5,
        ACCENT,
    )

    draw_wrapped_centered_text(
        pdf,
        f"“{title}”",
        width / 2,
        box_y + 1.05 * cm,
        box_width - 1.5 * cm,
        "Helvetica-Oblique",
        14.2,
        16,
        INK_DARK,
    )

    y = box_y - 0.75 * cm

    draw_centered_text(
        pdf,
        f"Fecha de publicación: {publication_date}",
        y,
        "Helvetica",
        10.8,
        MUTED_DARK,
    )

    y -= 0.52 * cm

    draw_centered_text(
        pdf,
        f"Código de certificado: {certificate_code}",
        y,
        "Helvetica-Bold",
        10,
        INK,
    )

    footer_y = 2.35 * cm

    pdf.setFont("Helvetica", 8.7)
    pdf.setFillColor(MUTED)

    email_text = f"Verificación: {VERIFY_EMAIL}"
    email_x = 2.25 * cm
    email_y = footer_y + 0.42 * cm

    pdf.drawString(email_x, email_y, email_text)

    email_width = pdf.stringWidth(email_text, "Helvetica", 8.7)

    pdf.linkURL(
        f"mailto:{VERIFY_EMAIL}",
        (
            email_x,
            email_y - 0.08 * cm,
            email_x + email_width,
            email_y + 0.32 * cm,
        ),
        relative=0,
    )

    web_text = f"Web: {WEB_LABEL}"
    web_x = 2.25 * cm
    web_y = footer_y - 0.02 * cm

    pdf.drawString(web_x, web_y, web_text)

    web_width = pdf.stringWidth(web_text, "Helvetica", 8.7)

    pdf.linkURL(
        WEB_URL,
        (
            web_x,
            web_y - 0.08 * cm,
            web_x + web_width,
            web_y + 0.32 * cm,
        ),
        relative=0,
    )

    signature_width = 4.9 * cm
    signature_height = 1.75 * cm
    signature_x = width - 7.7 * cm
    signature_y = footer_y + 0.58 * cm

    padding_x = 0.25 * cm
    padding_y = 0.18 * cm

    pdf.setFillColor(PAPER_SOFT)
    pdf.roundRect(
        signature_x - padding_x,
        signature_y - padding_y,
        signature_width + 2 * padding_x,
        signature_height + 2 * padding_y,
        5,
        stroke=0,
        fill=1,
    )

    pdf.drawImage(
        str(FIRMA_PATH),
        signature_x,
        signature_y,
        width=signature_width,
        height=signature_height,
        preserveAspectRatio=True,
        mask="auto",
    )

    line_y = footer_y + 0.43 * cm

    pdf.setStrokeColor(INK)
    pdf.setLineWidth(0.6)
    pdf.line(
        signature_x - 0.25 * cm,
        line_y,
        signature_x + 5.65 * cm,
        line_y,
    )

    pdf.setFillColor(INK_DARK)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(
        signature_x - 0.1 * cm,
        line_y - 0.43 * cm,
        SIGNER_NAME,
    )

    pdf.setFont("Helvetica", 8.5)
    pdf.setFillColor(MUTED_DARK)
    pdf.drawString(
        signature_x - 0.1 * cm,
        line_y - 0.83 * cm,
        SIGNER_ROLE,
    )


def generate_certificate(article: dict[str, object], article_path: Path) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    author = str(article["author"]).strip()
    certificate_code = generate_certificate_code(article, article_path)

    filename = f"{slugify(certificate_code)}-{slugify(author)}.pdf"
    output_path = OUTPUT_DIR / filename

    pdf = canvas.Canvas(str(output_path), pagesize=landscape(A4))
    draw_certificate(pdf, article, article_path)
    pdf.showPage()
    pdf.save()

    return output_path


def resolve_article_paths(args: list[str]) -> list[Path]:
    if not args:
        raise ValueError(
            "No se recibieron artículos. Uso: "
            "python documentation/content/scripts/generate_certificates_from_articles.py "
            "documentation/content/articulos/archivo.md"
        )

    paths: list[Path] = []

    # BASE_DIR = documentation/content
    # repo_root = raíz real del repo
    repo_root = BASE_DIR.parents[1]

    for arg in args:
        raw_path = Path(arg)

        if raw_path.is_absolute():
            path = raw_path
        else:
            candidate_from_repo = repo_root / raw_path
            candidate_from_content = BASE_DIR / raw_path

            if candidate_from_repo.exists():
                path = candidate_from_repo
            elif candidate_from_content.exists():
                path = candidate_from_content
            else:
                path = candidate_from_repo

        if not path.exists():
            raise FileNotFoundError(f"No existe el artículo: {path}")

        if path.suffix.lower() != ".md":
            raise ValueError(f"No es un archivo Markdown .md: {path}")

        paths.append(path)

    return paths


def main() -> int:
    try:
        check_required_files()

        article_paths = resolve_article_paths(sys.argv[1:])

        generated_files: list[Path] = []
        skipped_files: list[Path] = []

        for article_path in article_paths:
            article = read_front_matter(article_path)

            if not should_generate_certificate(article):
                skipped_files.append(article_path)
                continue

            validate_article(article, article_path)

            output_path = generate_certificate(article, article_path)
            generated_files.append(output_path)

    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Certificados generados: {len(generated_files)}")

    for output_path in generated_files:
        print(f"- {output_path.relative_to(BASE_DIR)}")

    if skipped_files:
        print(f"Artículos omitidos: {len(skipped_files)}")

        for path in skipped_files:
            print(f"- {path.relative_to(BASE_DIR)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
