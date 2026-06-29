---
title: Cuando las matemáticas desafinan # vuestro título
author: María Pérez Garrote # mismo nombre que en la tarjeta de autor
date: 2026-07-02 # formato YYYY-MM-DD
layout: articles
slug: matematicas_desafinan
status: hidden # published si ya está listo
category: Música # categoría con mayúscula inicial
tags: # tags con minúscula inicial
  - música
  - matemáticas
summary: Millones de personas escuchamos música a diario. Mientras trabajamos, practicamos algún deporte, viajamos o pasamos la aspiradora. Lo que quizás no sabías es que toda la música que escuchamos está desafinada, según Pitágoras. Explicamos por qué en este napkin notes.
image: images/portada_matematicas_desafinan.jpeg # imagen principal del artículo
---

[TOC]

Todo se remonta a la antigua Grecia. El filósofo Pitágoras de Samos encabeza una escuela filosófica en la que las matemáticas y los números son la esencia de toda la naturaleza y la vida, incluyendo la música. Por ello, se atribuye a Pitágoras el descubrimiento de la relación entre la aritmética y la escala musical, llamada afinación pitagórica. Este sistema se fundamenta en una escala musical construida sobre intervalos de quintas perfectas de razón $3/2$. Veamos las matemáticas que se esconden tras este número.


## Pitágoras inventa su escala musical
Tomemos como frecuencia de partida la nota Do (66Hz). Esta nota será nuestro primer armónico $f_1$. El segundo armónico se obtiene duplicando el primero $f_2=2*f_1$. El intervalo entre $f_1$ y $f_2$ se llama octava, y es la frecuencia que escuchamos cuando hacemos vibrar una cuerda con un punto fijo en el medio (Do pero una octava mayor con 132 Hz). El siguiente armónico es $f_3=3f_1$, y el intervalo correspondiente se llama quinta. Este tercer armónico de Do es la nota musical Sol (198 Hz). La relación de frecuencias entre el punto de partida Do y Sol es precisamente 3:2.


La quinta y la octava son intervalos muy armónicos y matemáticamente muy "puros", algo que fascinaba a Pitágoras. Partiendo de la primera nota (Do, en nuestro ejemplo), construimos la escala pitagórica obteniendo seis notas con una razón de 3:2 por encima y las restantes con la misma razón por debajo:

<p style="text-align: center;">
  Mi♭–Si♭–Fa–<strong>Do</strong>–Sol–Re–La–Mi–Si–Fa♯–Do♯–Sol♯
</p>

<div class="nn-two-images">

  <figure>
    <img src="{static}/images/armonicos_matematicas_desafinan.jpg" alt="Armónicos de una cuerda">
    <figcaption>
      Figura 1. Armónicos de una cuerda. Relaciones entre las longitudes de onda de una nota fundamental y sus armónicos principales.
    </figcaption>
  </figure>

  <figure>
    <img src="{static}/images/Circulo-quintas_matematicas_desafinan.png" alt="Círculo de quintas">
    <figcaption>
      Figura 2. Círculo de quintas. Círculo de quintas pitagórico.
    </figcaption>
  </figure>

</div>

El único problema de este método es que, si te fijas en el diagrama de la figura anterior, la escala no "cierra" el círculo de quintas. El motivo es que las doce quintas del círculo no equivalen exactamente a siete octavas. Matemáticamente, no es posible encadenar intervalos con una razón de 3:2 (la quinta) y obtener exactamente una relación de 2:1 (la octava). Es decir, no existen números enteros x e y que satisfagan la ecuación:

$$
(3/2)^x=(2/1)^y.
$$

Esta pequeña diferencia que se necesitaría para completar el círculo se llama coma pitagórica, y da lugar a la quinta del lobo. Esto puede parecer un simple dato anecdótico, pero si pensamos en los instrumentos musicales sería extremadamente difícil diseñar un piano con este sistema de quintas que no cierra. Por eso mismo en la música occidental no se utiliza este método de afinación, sino el sistema temperado.

## Todos los pianos del mundo están desafinados
El sistema temperado o temperamento igual es el sistema de afinación comúnmente utilizado en la música occidental, y se construye sobre el semitono temperado. La idea es sencilla: se toma la octava, se divide en doce partes iguales y obtenemos el semitono temperado. Al igual que con la escala pitagórica, tomamos una nota de partida (Do por ejemplo), y multiplicamos su frecuencia por $2^{1/12}$, obteniendo así una escala con intervalos equiespaciados. En la siguiente figura se muestra la diferencia entre la escala pitagórica (en verde) y el sistema temperado (en negro).

<!-- Comparacion -->
<figure class="nn-article-figure">
  <img src="{static}/images/compare_matematicas_desafinan.png" alt="Sistema temperado y pitagórico">
  <figcaption>
    Figura 3. Comparación entre el sistema temperado y el sistema pitagórico.
  </figcaption>
</figure>
<!-- Opcional: pie de foto -->
*Comparación entre el sistema temperado (en negro) y el pitagórico (en verde) para diferentes intervalos, en cents. Una octava completa equivale a 1200 cents.*

Como podréis imaginar, diseñar un piano con este sistema es muchísimo más sencillo que con la afinación pitagórica. Probablemente Pitágoras no estaría muy contento con nuestro sistema, ya que se basa en el número irracional $2^{1/12}$, lo que para él destruye la armonía del cosmos. Os dejo algunos enlaces en los que podéis escuchar estos dos sistemas, a ver si sois capaces de escuchar la diferencia! 


## Referencias

<ol class="nn-references">

  <li id="ref-1">
    RTVE. (2024). <em>Raíz de 5: La coma pitagórica, la música tiene errores matemáticos</em>.
    <a href="https://www.rtve.es/play/audios/raiz-de-5/raiz-5-coma-pitagorica-musica-tiene-errores-matematicos-04-03-24/15999318/" target="_blank" rel="noopener noreferrer">https://www.rtve.es/play/audios/raiz-de-5/raiz-5-coma-pitagorica-musica-tiene-errores-matematicos-04-03-24/15999318/</a>
  </li>

  <li id="ref-2">
    Wikipedia. (s. f.). <em>Pythagorean tuning</em>.
    <a href="https://en.wikipedia.org/wiki/Pythagorean_tuning" target="_blank" rel="noopener noreferrer">https://en.wikipedia.org/wiki/Pythagorean_tuning</a>
  </li>

  <li id="ref-3">
    Wikipedia. (s. f.). <em>Pythagorean comma</em>.
    <a href="https://en.wikipedia.org/wiki/Pythagorean_comma" target="_blank" rel="noopener noreferrer">https://en.wikipedia.org/wiki/Pythagorean_comma</a>
  </li>

</ol>
