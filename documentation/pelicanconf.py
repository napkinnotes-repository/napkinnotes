#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import os

AUTHOR = ""
SITENAME = "Napkin Notes"
SITESUBTITLE = ""
SITEURL = "https://napkinnotes.es"
RELATIVE_URLS = False


PATH = "content"

# Regional Settings
TIMEZONE = "Europe/Madrid"
DATE_FORMATS = {
    "es": "%d de %B de %Y",
}
DEFAULT_LANG = "es"

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
    
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
    "yaml_metadata",
]
MATH_JAX = {
    "auto_insert": True,
}


# Appearance
THEME = "../"
TYPOGRIFY = True
DEFAULT_PAGINATION = 10

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = True
WITH_FUTURE_DATES = True
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
EXPLORAR_URL = "explorar"
NOSOTROS_URL = "about"
# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    ("X", "https://twitter.com/napkiinnotes", "Napkin Notes en X"),
)
# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra", "extra/_redirects", "code", "articulos/template_articulos"]

#metadata de netlify
"""EXTRA_PATH_METADATA = {
    "extra/custom-about.css": {"path": "theme/custom-about.css"},
    "extra/custom.css": {"path": "theme/css/custom.css"},
    "extra/_redirects": {"path": "_redirects"},
}"""

EXTRA_PATH_METADATA = {
    "extra/custom-about.css": {"path": "theme/custom-about.css"},
    "extra/custom.css": {"path": "theme/css/custom.css"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/sitemap.xml": {"path": "sitemap.xml"},
}

#problema con indexacion en google
"""if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}

    STATIC_PATHS.append("extra/sitemap.xml")
    EXTRA_PATH_METADATA["extra/sitemap.xml"] = {"path": "sitemap.xml"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}
"""

STATIC_PATHS.append("extra/robots.txt")
EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "explorar", "404"]
TAG_SAVE_AS = ""
AUTHOR_URL = "autor/{slug}"
AUTHOR_SAVE_AS = "autor/{slug}.html"
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = False

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Release Alert"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

FREELISTS_NAME = "oracle-l"
FREELISTS_FILTER = True

# SMO
X_USERNAME = "napkiinnotes"
X_PROFILE_URL = "https://twitter.com/napkiinnotes"
TWITTER_USERNAME = "napkiinnotes"
FEATURED_IMAGE = SITEURL + "/theme/images/nn_logo.png"
CONTACT_EMAIL = "napkiin.notes@proton.me"
# Legal
SITE_LICENSE = """Contenido publicado bajo licencia <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Atribución 4.0 Internacional</a>."""
#HOSTED_ON = {"name": "GitHub Pages", "url": "https://pages.github.com/"}

# SEO
SITE_DESCRIPTION = (
    "Napkin Notes es un blog de divulgación científica y pensamiento crítico "
    "donde la física, la cosmología, las matemáticas y la vida cotidiana se explican "
    "con rigor, claridad y curiosidad."
)

# Share links at bottom of articles
# Supported: twitter, facebook, hacker-news, reddit, linkedin, email
SHARE_LINKS = [("twitter", "Twitter"), ("facebook", "Facebook"), ("email", "Email")]

# Landing Page
PROJECTS_TITLE = ""
PROJECTS = []

LANDING_PAGE_TITLE = "Napkin Notes"

AUTHORS = {
    "Duvier Suárez Fontanella": {
        "url": "https://produccioncientifica.usal.es/investigadores/819473/detalle",
        "role": "Creador, Desarrollador Web",
        "blurb": "Físico teórico y curioso incorregible, dedicado a rastrear las leyes secretas que gobiernan tanto al cosmos como a los detalles más triviales de la vida diaria. Sus textos buscan lo mismo que la antigua Fundación: preservar el conocimiento, iluminar lo oculto y demostrar que incluso en una servilleta puede comenzar una nueva era científica.",
        "avatar": "images/duvier.png",
        "articles_url": "autor/duvier-suarez-fontanella",
    },
    "Gretel Quintero Angulo": {
        "url": "https://www.linkedin.com/in/gretel-quintero-angulo/?originalSubdomain=de",
        "role": "Editora",
        "blurb": "Gretel es científica de formación, escritora por placer y feminista por necesidad. Observa el mundo con la precisión de quien ha sido educada en el método científico y la sensibilidad de quien encuentra en la escritura una forma de interpretar lo cotidiano. Su trabajo combina pensamiento crítico y voz propia, explorando las estructuras —visibles e invisibles— que moldean nuestras vidas.",
        "avatar": "images/gretel.png",
        "articles_url": "autor/gretel-quintero-angulo",
    },
    "David Figueruelo Hernán": {
        "url": "https://inspirehep.net/authors/1869776?ui-citation-summary=true",
        "role": "Editor, Desarrollador Web",
        "blurb": "Doctor en cosmología que busca comprender el universo y el rol de la materia y energía oscuras en él. Interesado las ecuaciones y las preguntas fundamentales: qué significa entender en física y qué es  <strong>verdad</strong> al observar solo una fracción mínima del cosmos. Trabaja interpretando las pistas que el universo nos deja en forma de datos, intentando averiguar qué historias encajan con ellas y cuáles no. Financiación: Personal investigador doctor de la UPV/EHU (2024).",
        "avatar": "images/david.jpg",
         "articles_url": "autor/david-figueruelo-hernan",       
    },
    "Gabriel Sánchez Pérez": {
        "url": "https://www.linkedin.com/in/gasape21/",
        "role": "Editor, Responsable de Redes Sociales",
        "blurb": "Gabriel es doctor en física teórica, un explorador obsesionado con la arquitectura matemática que sostiene el tejido del universo. En sus textos, se propone un desafío constante: traducir la complejidad de la física y la geometría a un lenguaje accesible, sin sacrificar ni un ápice de elegancia ni de rigor. Su enfoque busca desentrañar cómo las leyes fundamentales dan forma a nuestra realidad, convirtiendo abstracciones matemáticas en puentes hacia una comprensión profunda de la naturaleza.",
        "avatar": "images/gabriel.jpeg",
        "articles_url": "autor/gabriel-sanchez-perez",       
    },
    "Paz Albares Vicente": {
        "url": "https://portalcientifico.upm.es/es/ipublic/researcher/338845",
        "role": "Colaboradora",
        "blurb": "Paz es doctora en Física, especializada en Física Matemática, exploradora de ecuaciones no lineales y de los patrones que de ellas emergen donde menos se esperan. Modeliza fenómenos complejos e intenta descubrir y entender qué estructuras se esconden detrás, combinando la física con herramientas y el lenguaje de las matemáticas. De mente curiosa, está convencida de que tan importante es hacerse preguntas como buscar sus respuestas. Y a veces, todo comienza con una idea escrita en la cara de una servilleta.",
        "avatar": "images/paz.jpg",
        "articles_url": "autor/paz-albares-vicente",       
    },
     "María Pérez Garrote": {
        "url": "https://produccioncientifica.usal.es/investigadores/1222882/detalle",
        "role": "Colaboradora",
        "blurb": "María es estudiante de doctorado en cosmología, y le apasiona intentar desentrañar los misterios del cosmos y de la vida en general. Su trabajo consiste en estudiar los ingredientes fundamentales que conforman el universo, y de qué manera interactúan para dar lugar a las formaciones de galaxias que observamos hoy en día. Sus textos aspiran a arrojar un poco de luz sobre ese sector todavía oscuro del universo, despertando la curiosidad y el pensamiento crítico en quienes se acercan a explorarlo.",
        "avatar": "images/maria.jpeg",
        "articles_url": "autor/maria-perez-vicente",       
    },
     "Ruchika": {
        "url": "https://produccioncientifica.usal.es/investigadores/1999168/detalle",
        "role": "Colaboradora",
        "blurb": "La Dra. Ruchika es investigadora postdoctoral en la Universidad de Salamanca, antes investigadora INFN en la Universidad La Sapienza de Roma y en el IIT Bombay. Le fascinan las grandes preguntas sobre nuestro universo y estudia cómo las galaxias se alejan unas de otras y cómo también se agrupan en enormes cúmulos, dando lugar a la hermosa estructura en forma de red del cosmos. Su investigación se sitúa en el punto de encuentro entre la observación del cielo y la comprensión de las leyes más profundas de la física, estudiando dos de los grandes misterios de la ciencia actual: la materia oscura y la energía oscura. Lo que más la entusiasma es descubrir qué son realmente estos ingredientes invisibles del universo y distinguir cuidadosamente los descubrimientos verdaderamente nuevos de los efectos engañosos producidos por errores de medición.",
        "avatar": "images/Ruchika.jpeg",
        "articles_url": "autor/ruchika",       
    },
      "David Barba González": {
        "url": "https://www.linkedin.com/in/david-barba-gonz%C3%A1lez-854101215/",
        "role": "Colaborador",
        "blurb": "David es doctor en astrofísica, y actualmente trabaja como investigador postdoctoral en la Universidad Hebrea de Jerusalén. Es experto en metalurgia galáctica, es decir, en las propiedades de los sólidos y líquidos más densos y poderosos del universo, que se encuentran en los corazones de estrellas muertas. Su trabajo de investigación intenta entender cómo podemos aprender más de estos materiales a través de observaciones astronómicas, tanto a través de la luz como de otros mensajeros, como neutrinos u ondas gravitacionales.",
        "avatar": "images/barba.jpeg",
        "articles_url": "autor/david-barba-gonzalez",       
    },
}




COMMENTS_INTRO = "Comentarios"

APPLAUSE_BUTTON = True
DISPLAY_PAGES_ON_MENU = False
