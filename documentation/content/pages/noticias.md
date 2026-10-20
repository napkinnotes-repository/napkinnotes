---
title: Noticias
slug: noticias
template: noticias
status: hidden
summary: "Noticias breves de ciencia y actualidad seleccionadas por Napkin Notes."

# ============================================================
# NOTICIAS
# ============================================================
# Aquí van TODAS las noticias, tanto pasadas como futuras.
# La plantilla decide automáticamente dónde mostrarlas:
# - fecha < hoy  -> "Noticias y eventos"
# - fecha >= hoy -> "Próximamente"
#
# Imagen opcional:
# imagen: "images/noticias/nombre-del-archivo.jpeg"
# Si se omite, la noticia se muestra sin imagen.
noticias:
  - fecha: "2026-10-27"
    titulo: "Noticia futura de prueba"
    imagen: "images/noticias/images.jpeg"
    texto: >-
      Este bloque sirve para anunciar una noticia futura sin crear
      una página individual.

  - fecha: "2026-10-18"
    titulo: "Noticia de prueba"
    imagen: "images/noticias/images.jpeg"
    texto: >-
      Este es un texto corto de prueba para comprobar cómo se ve una noticia dentro
      de la nueva sección.

  - fecha: "2026-10-18"
    titulo: "Segunda noticia del mismo día"
    texto: >-
      Esta segunda noticia comparte fecha con la anterior y aparecerá prácticamente
      pegada a ella.

  - fecha: "2026-10-12"
    titulo: "Otra noticia de prueba"
    texto: >-
      Esta noticia pertenece a otro día y aparecerá en un bloque separado.

# ============================================================
# EVENTOS
# ============================================================
# Aquí van TODOS los eventos, tanto pasados como futuros.
# Funcionan igual que las noticias, pero en el calendario aparecen
# con punto y texto azules.
#
# Formato:
# - fecha: "AAAA-MM-DD"
#   titulo: "Nombre del evento"
#   imagen: "images/noticias/imagen.jpeg"   # opcional
#   texto: >-
#     Descripción breve del evento.
eventos: []
---
