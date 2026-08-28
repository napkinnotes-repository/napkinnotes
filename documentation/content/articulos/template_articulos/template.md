---
title: aaa # vuestro título
author: aaa # mismo nombre que en la tarjeta de autor
date: 2026-03-15 # formato YYYY-MM-DD
layout: articles
slug: prueba-articulo
status: hidden # published si ya está listo
category: aaa # categoría con mayúscula inicial
tags: # tags con minúscula inicial
  - bla
  - blabla
  - bli bli
summary: aaaaa # 1-2 frases cortas para la tarjeta del artículo
image: images/nombre_de_la_imagen.jpeg # imagen principal del artículo  ¡¡¡¡¡¡¡¡TIENE QUE SER JPEG EL FORMATO!!!!!
certificate: true
---

[TOC]



## Sección

<!-- Texto normal -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Sub-Sección

<!-- Preguntas con recuadro bonito -->
> **¿Cuánta el gramo quillo?**
<!-- Fin pregunta con recuadro bonito -->


Fórmulas:

<!-- Fórmula en bloque: en entorno $$ $$, todo es como LaTeX -->
$$
\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + Q_{\text{abs}}
$$

<!-- Fórmula en línea de texto -->
Se puede usar $ \alpha $ como en LaTeX.

<!-- Obsoleto: mejor no usar \( ... \) -->
obsoleto: bla bla bla \(J\) lari lari lari

<!-- Subíndice fuera de entorno matemático -->
c<sub>p</sub>

<!-- Negrita y cursiva -->
Negrita y cursiva: **una paradoja**. *una paradoja*.

<!-- Lista (el espacio entre : y los - es necesario, también con la siguiente linea y el ultimo - tenedlo en cuenta-->
Presentan:

- nanani nanana nanano.  
- abc cba caracola
- Maka make maki

<!-- Citas dentro del texto -->
El texto que queréis referenciar va así <a class="nn-cite" href="#ref-1">[1]</a>.
Otra cita distinta iría así <a class="nn-cite" href="#ref-2">[2]</a>.

<!-- Fin de Sección -->
---


## Otra sección

Texto antes de la imagen.

<!-- Una imagen va así -->
<figure class="nn-article-figure">
  <img src="{static}/images/duna.png" alt="Estructura de una duna típica">
  <figcaption>
    Figura 1. Estructura de una duna típica.
  </figcaption>
</figure>

Texto tras la imagen.

<!-- Fin de Sección -->
---


## Conclusiones

Frases finales

---


## Referencias

<ol class="nn-references">
  <li id="ref-1">
    Autor, A. (Año). Título del artículo. <em>Revista o libro</em>.
    <a href="https://doi.org/..." target="_blank" rel="noopener noreferrer">https://doi.org/...</a>
  </li>

  <li id="ref-2">
    Autor, B. (Año). Otro título. <em>Revista o libro</em>.
    <a href="https://doi.org/..." target="_blank" rel="noopener noreferrer">https://doi.org/...</a>
  </li>
</ol>
