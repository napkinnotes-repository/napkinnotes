---
title: "Perdimos por culpa del aire: una investigación casi seria sobre el mundial de fútbol 2026"
author: Duvier Suárez Fontanella
date: 2026-06-09
layout: articles
slug: mundial-2026-fisica-balon-aire
status: hidden
category: Física
tags:
  - fútbol
  - mundial 2026
  - física
  - aerodinámica
  - datos
summary: Una estimación sobre cómo altitud, temperatura y densidad del aire pueden cambiar el vuelo del balón en las sedes del Mundial 2026, y todo para que tengas una buena excusa si no llegas a la final.
image: images/05_mapa_rareza_estatico.png
certificated: true
---

[TOC]


Todos los equipos del Mundial 2026 jugarán con el mismo balón reglamentario, pero no jugarán contra el mismo aire o en las mismas condiciones atmosféricas.

El balon de fútbol del mundial 2026 viajará entre estadios casi al nivel del mar y otros a gran altitud; entre sedes frescas como Vancouver o Seattle y entornos cálidos como Monterrey, Dallas, Houston o Miami; entre campos abiertos, techos retráctiles y superficies temporales <a class="nn-cite" href="#ref-1">[1]</a>. Esa geografía convierte el torneo en un pequeño laboratorio físico. Aquí te daremos, cual buen perdedor, la mejor excusa en caso de que tu equipo no llegue a la final. "Perdimos por culpa del aire y de las condiciones atmosféricas" pero con un respaldo científico para que tu cuñado que le va al equipo rival no te diga más que siempre te estas quejando de nada. 


## El modelo mínimo: un balón contra el aire

Para no convertir esto en una simulación profesional, basta una ecuación. La fuerza de arrastre sobre un balón que se mueve en el aire puede escribirse como:

$$
D=\frac{1}{2}\rho C_d A v^2 .
$$

Aquí $\rho$ es la densidad del aire, $C_d$ el coeficiente de arrastre, $A$ el área frontal del balón y $v$ la velocidad del disparo <a class="nn-cite" href="#ref-3">[3]</a> y no lo digo solo yo, también lo dice la NASA <a class="nn-cite" href="#ref-4">[4]</a><a class="nn-cite" href="#ref-5">[5]</a>, bueno, más o menos pero sirve para que le digas a tu cuñado que lo dice la NASA. 

Tomando valores razonables para una pelota reglamentaria de acuerdo a la International Football Association Board <a class="nn-cite" href="#ref-2">[2]</a>,

$$
m\simeq 0.43\,\mathrm{kg}, \qquad R\simeq 0.11\,\mathrm{m}, \qquad A=\pi R^2,
$$

y un disparo fuerte de

$$
v=30\,\mathrm{m/s}=108\, \mathrm{km/h},
$$

con $C_d\simeq 0.25$, queda una regla muy útil:

$$
D \simeq 4.28\,\rho .
$$

Es decir: en este modelo de servilleta, **si cambia la densidad del aire, cambia casi directamente cuánto se frena la pelota**.

La densidad del aire no es igual en todas partes. Baja con la altitud, baja con la temperatura y cambia ligeramente con la humedad <a class="nn-cite" href="#ref-6">[6]</a><a class="nn-cite" href="#ref-7">[7]</a>. La altitud es el efecto dominante: por eso Ciudad de México y Guadalajara destacan tanto.

<figure class="nn-article-figure">
  <img src="{static}/images/01_densidad_aire_corregida.png" alt="Densidad estimada del aire por sede">
  <figcaption>
    Figura 1. La densidad estimada del aire separa claramente a Ciudad de México y Guadalajara del resto de sedes. Menor densidad implica menor arrastre y menor fuerza lateral de Magnus.
  </figcaption>
</figure>

---

## Qué cambia cuando el aire es menos denso

Un balón en aire más tenue encuentra menos resistencia, tal como a nosotros nos es más fácil movernos en el aire que en el agua por poner un ejemplo extremo.

Para un disparo de $30\,\mathrm{m/s}$, el modelo da aproximadamente un frenado de:

- **Ciudad de México:** $D\simeq 3.91\,\mathrm{N}$.
- **Guadalajara:** $D\simeq 4.18\,\mathrm{N}$.
- **Vancouver:** $D\simeq 5.15\,\mathrm{N}$.

La diferencia entre Ciudad de México y Vancouver ronda el **24% de arrastre inicial**. En fútbol, esa no es una corrección decorativa: puede afectar la distancia, la caída y la sensación de golpeo.

<figure class="nn-article-figure">
  <img src="{static}/images/02_arrastre_disparo_corregido.png" alt="Arrastre aerodinámico estimado para un disparo de 30 m/s">
  <figcaption>
    Figura 2. Fuerza de arrastre estimada para un disparo fuerte. El Azteca aparece como el escenario donde el balón debería frenarse menos.
  </figcaption>
</figure>

Por otro lado hay un matiz bonito, el aire tenue no solo reduce el frenado, sino que también reduce la fuerza lateral responsable de la curva del balón. De forma esquemática, el efecto Magnus, que así es como se llama, escala como

$$
L \sim \frac{1}{2}\rho C_L A v^2 .
$$

Así que el estadio donde la pelota “vuela más” no tiene por qué ser el estadio donde “curva más”. En aire menos denso, a igualdad de golpeo y giro, el balón debería conservar mejor su velocidad, pero también curvarse algo menos.


<figure class="nn-article-figure">
  <img src="{static}/images/17_alcance_vs_curva_cuadrantes.png" alt="Mapa relativo del comportamiento del balón en las sedes del Mundial 2026">
  <figcaption>
    Figura 3. Mapa relativo del comportamiento del balón en las sedes del Mundial 2026. El eje horizontal mide penetración aerodinámica o alcance relativo; el eje vertical mide deriva lateral efectiva. El modelo compara el mismo disparo bajo distintas condiciones atmosféricas.
  </figcaption>
</figure>

---

## Un índice de "rareza" física

Para ordenar las sedes podemos definir un índice comparativo de rareza física a lo Napkin Notes es decir sin mucho formalismo pero que nos permita tener una estimación de cuán raro será el bote o volar del balón respecto a la media de los estadios, llamémosle a este $R$ como no podía ser de otra manera, y combinará seis ingredientes: altitud, temperatura, humedad, viento, tipo de estadio y superficie.

No es un modelo predictivo profesional. No dice dónde habrá más goles ni quién jugará mejor. Solo responde a una pregunta: **¿qué sedes se alejan más de un entorno medio para el balón?**

El resultado es claro:

<figure class="nn-article-figure">
  <img src="{static}/images/04_indice_rareza_corregido.png" alt="Índice de rareza física del balón">
  <figcaption>
    Figura 4. Ranking de rareza física. México domina la parte atmosférica; varias sedes estadounidenses y canadienses aparecen por la combinación de superficie temporal, techo o condiciones locales.
  </figcaption>
</figure>


La rareza no siempre empuja en la misma dirección. En Ciudad de México el balón debería frenarse menos. En Vancouver el aire es más denso y puede frenarla más. En Dallas o Seattle la pregunta interesante no es solo el aire: también es la superficie.

> **¿En qué estadio del Mundial 2026 puede cambiar más el comportamiento del balón?**

La respuesta corta es: **el Estadio Azteca, en Ciudad de México**, si hablamos de vuelo, frenado y curva. Si incluimos el bote, aparecen otras sedes interesantes por la superficie temporal o adaptada.

<figure class="nn-article-figure">
  <img src="{static}/images/05_mapa_rareza_estatico.png" alt="Mapa físico del Mundial 2026: índice de rareza del balón por sede">
  <figcaption>
    Figura 5. Las 16 sedes del Mundial 2026 vistas como un mapa físico: no solo importa dónde están, sino qué aire rodea al balón.
  </figcaption>
</figure>

---
## Conclusiones

El modelo no pretende adivinar goles ni explicar derrotas (bueno esto último quizás sí), pero sí deja una idea clara, el balón no viaja en el vacío. Cada sede le ofrece un entorno distinto, y eso cambia cuánto se frena, cuánto conserva su velocidad y cuánto puede desviarse lateralmente.

El efecto más robusto es la densidad del aire. Por eso Ciudad de México aparece como el caso más extremo: allí la pelota encuentra menos resistencia y puede comportarse de forma distinta a como lo haría en estadios cercanos al nivel del mar. Otros factores, como el viento, la temperatura o la superficie, añaden matices más inciertos, pero también más interesantes. 

Así que, si en 2026 tu equipo pierde, no corras a culpar al delantero, revisa antes la densidad del aire. Admitámoslo, sigue siendo una excusa; pero es bastante más elegante cuando viene con $\rho$, $C_d$ y Napkin Notes.

---

## Anexo mínimo: datos clave

| Sede | Estadio | Altitud [m] | $\rho$ [kg/m<sup>3</sup>] | Drag a 30 m/s [N] | Índice R |
|---|---|---:|---:|---:|---:|
| Ciudad de México | Estadio Azteca | 2240 | 0.915 | 3.91 | 75.8 |
| Guadalajara | Estadio Akron | 1598 | 0.977 | 4.18 | 51.3 |
| Monterrey | Estadio BBVA | 500 | 1.089 | 4.66 | 49.7 |
| Dallas | AT&T Stadium | 184 | 1.132 | 4.84 | 45.7 |
| Seattle | Lumen Field | 45 | 1.198 | 5.12 | 44.4 |
| Vancouver | BC Place | 34 | 1.205 | 5.15 | 40.3 |

---

## Referencias

<ol class="nn-references">
  <li id="ref-1">
    FIFA. <em>FIFA World Cup 2026 stadium information: official addresses, capacities and maps</em>.
    <a href="https://gpcustomersupportfwc2026.tickets.fifa.com/hc/en-gb/articles/28784010437021-2-What-are-the-official-addresses-stadium-capacities-and-maps-of-the-FIFA-World-Cup-2026-stadiums" target="_blank" rel="noopener noreferrer">FIFA stadium information</a>
  </li>

  <li id="ref-2">
    IFAB. <em>Laws of the Game, Law 2: The Ball</em>.
    <a href="https://www.theifab.com/laws/latest/the-ball/" target="_blank" rel="noopener noreferrer">IFAB Law 2</a>
  </li>

  <li id="ref-3">
    NASA Glenn Research Center. <em>Drag Equation</em>.
    <a href="https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/" target="_blank" rel="noopener noreferrer">NASA Glenn: drag equation</a>
  </li>

  <li id="ref-4">
    NASA Glenn Research Center. <em>Drag on a Soccer Ball</em>.
    <a href="https://www.grc.nasa.gov/www/k-12/airplane/socdrag.html" target="_blank" rel="noopener noreferrer">NASA Glenn: soccer ball drag</a>
  </li>

  <li id="ref-5">
    NASA Glenn Research Center. <em>Lift of a Soccer Ball</em>.
    <a href="https://www.grc.nasa.gov/WWW/K-12/airplane/soclift.html" target="_blank" rel="noopener noreferrer">NASA Glenn: soccer ball lift</a>
  </li>

  <li id="ref-6">
    NASA Glenn Research Center. <em>Earth Atmosphere Model: Metric Units</em>.
    <a href="https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html" target="_blank" rel="noopener noreferrer">NASA Glenn: atmosphere model</a>
  </li>

  <li id="ref-7">
    Time and Date / CustomWeather. <em>Climate and Weather Averages</em>.
    <a href="https://www.timeanddate.com/weather/" target="_blank" rel="noopener noreferrer">Climate averages</a>
  </li>
</ol>
