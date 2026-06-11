---
title: "Perdimos por culpa del aire: una investigación casi seria sobre el Mundial de Fútbol 2026"
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
summary: Una estimación sobre cómo la altitud, la temperatura y la densidad del aire afectan el vuelo del balón en las sedes del Mundial de Fútbol 2026, todo ello para que tengas una buena excusa si tu equipo no llega a la final.
image: images/mundial-2026-fisica-balon-aire_cover.jpeg
certificated: true
---

[TOC]


Aunque en el Mundial de Fútbol siempre se juegue con el mismo balón reglamentario, no todos los partidos se desarrollarán bajo las mismas condiciones atmosféricas. Los balones se moverán lo mismo por estadios a nivel del mar que por otros a una gran altitud; en entornos frescos como Vancouver o Seattle, y en otros cálidos como Monterrey, Dallas, Houston o Miami; entre campos abiertos, techos retráctiles y superficies temporales <a class="nn-cite" href="#ref-1">[1]</a>. 

Esa variabilidad convierte el torneo en un inesperado laboratorio de Física. ¿El resultado del experimento? La mejor de las excusas en caso de que tu equipo no llegue a la final: "Perdimos por culpa del aire". Y, por supuesto, al afirmarlo tendrás todo el respaldo científico necesario para que tu cuñado, ese que le va al equipo rival, no pueda decirte de nuevo que siempre te quejas por gusto. 


## Modelo mínimo: el balón contra el aire

Cada vez que el balón, tras ser pateado, vuela sobre el campo experimenta, además del efecto de la fuerza de gravedad, el efecto desacelerador de la resistencia del aire. Esta resistencia, también conocida como fuerza de arrastre, puede describirse como:

$$
D=\frac{1}{2}\rho C_d A v^2 .
$$

Aquí $\rho$ es la densidad del aire, $C_d$ el coeficiente de arrastre, $A$ el área frontal del balón y $v$ la velocidad del disparo <a class="nn-cite" href="#ref-3">[3]</a>, y no lo digo solo yo, también lo dice la NASA <a class="nn-cite" href="#ref-4">[4]</a><a class="nn-cite" href="#ref-5">[5]</a>. 

Tomando valores razonables para un balón reglamentario de acuerdo a la *International Football Association Board* <a class="nn-cite" href="#ref-2">[2]</a>:

$$
m\simeq 0.43\,\mathrm{kg}, \qquad R\simeq 0.11\,\mathrm{m}, \qquad A=\pi R^2,
$$

y un disparo fuerte de:

$$
v=30\,\mathrm{m/s}=108\, \mathrm{km/h},
$$

con $C_d\simeq 0.25$, queda una regla muy útil:

$$
D \simeq 4.28\,\rho,
$$

que relaciona la fuerza de arrastre con la densidad del aire. En este modelo de servilleta, **si cambia la densidad del aire, cambia casi directamente cuánto se frena el balón**.

La densidad del aire no es igual en todas partes. Disminuye con la altitud y la temperatura, y varía ligeramente con la humedad <a class="nn-cite" href="#ref-6">[6]</a><a class="nn-cite" href="#ref-7">[7]</a>. Entre estos tres, la altitud resulta ser el efecto dominante. Por eso en la Fig. 1 la densidad del aire en Ciudad de México y Guadalajara se encuentra tan por debajo de la media.

<figure class="nn-article-figure">
  <img src="{static}/images/01_densidad_aire_corregida_arregladaDFH.png" alt="Densidad estimada del aire por sede">
  <figcaption>
    Figura 1. La densidad estimada del aire separa claramente a Ciudad de México y Guadalajara del resto de sedes. Menor densidad implica menor arrastre y menor fuerza lateral de Magnus.
  </figcaption>
</figure>

---

## ¿Qué cambia cuando el aire es menos denso?

Un balón que se mueve por un medio menos denso encuentra una menor resistencia, tal como a nosotros nos es más fácil movernos en el aire que en el agua, por poner un ejemplo extremo. Para un disparo de $30\,\mathrm{m/s}$, el modelo da aproximadamente una fuerza de frenado con los siguientes valores extremos:

- **Ciudad de México:** $D\simeq 3.91\,\mathrm{N}$.
- **Guadalajara:** $D\simeq 4.18\,\mathrm{N}$.
- **Vancouver:** $D\simeq 5.15\,\mathrm{N}$.

La diferencia entre Ciudad de México y Vancouver ronda el **24%**. En el fútbol esa no es una corrección decorativa, puede afectar el alcance del balón, el tiempo de caída y la sensación de golpeo.

<figure class="nn-article-figure">
  <img src="{static}/images/02_arrastre_disparo_corregido_arregladaDFH.png" alt="Arrastre aerodinámico estimado para un disparo de 30 m/s">
  <figcaption>
    Figura 2. Fuerza de arrastre estimada para un disparo fuerte. El Azteca aparece como el escenario donde el balón debería sentir el menor frenado.
  </figcaption>
</figure>

Por otro lado, hay un matiz interesante. En un aire más tenue no solo se reduce el efecto de frenado, sino que también disminuye la fuerza lateral responsable de la curva del balón (efecto Magnus), provocando que la trayectoria sea más recta. El efecto Magnus escala con la densidad del aire como:

$$
L \sim \frac{1}{2}\rho C_L A v^2.
$$

Así que el estadio donde el balón vuela más fácil no tiene por qué ser donde su trayectoria se curva más. En aire menos denso, a igualdad de golpeo y giro, el balón debería conservar mejor su velocidad, pero también curvarse algo menos.

<figure class="nn-article-figure">
  <img src="{static}/images/17_alcance_vs_curva_cuadrantes.png" alt="Mapa relativo del comportamiento del balón en las sedes del Mundial 2026">
  <figcaption>
    Figura 3. Mapa relativo del comportamiento del balón en las sedes del Mundial 2026. El eje horizontal mide penetración aerodinámica o alcance relativo; el eje vertical mide deriva lateral efectiva. El modelo compara el mismo disparo bajo distintas condiciones atmosféricas.
  </figcaption>
</figure>

---

## Un índice de "rareza física" para las sedes del Mundial

Podemos ordenar las sedes con ayuda de un índice comparativo de "rareza física" definido a lo *Napkin Notes*: sin un rigor excesivo, pero que nos permita tener una estimación de cuán diferente (o raro) será el vuelo del balón respecto a la media de los estadios en una sede concreta. Lo denotaremos por $R$ y combinará seis ingredientes: altitud, temperatura, humedad, viento, tipo de estadio y superficie del terreno. 

<figure class="nn-article-figure">
  <img src="{static}/images/04_indice_rareza_corregido_arregladoDFH.png" alt="Índice de rareza física del balón">
  <figcaption>
    Figura 4. Ranking de rareza física. México domina la parte atmosférica; varias sedes estadounidenses y canadienses aparecen por la combinación de superficie, techo o condiciones locales.
  </figcaption>
</figure>

Naturalmente, este no es un modelo predictivo profesional. No pretende adivinar goles ni explicar derrotas (bueno, esto último quizás sí), sino responder a una pregunta: **¿qué sedes se alejan más de un entorno medio para el balón?** 

La desviación será mayor cuanto mayor sea $R$. Por tanto, la respuesta es clara: el comportamiento más alejado de la media se ve en **el Estadio Azteca, en Ciudad de México**, donde se esperan vuelos de mayor alcance y trayectoria más recta. En general, los estadios de México dominan en la rareza debido a sus condiciones atmosféricas y de altitud, mientras que varias sedes estadounidenses y canadienses también tienen un índice relativamente alto gracias a la combinación del clima local con otros factores como la superficie o el techado del estadio. Estos últimos añaden al problema matices más inciertos, pero también más interesantes acerca de cómo la ubicación geográfica influye en el comportamiento del balón. 

Así que si en este Mundial tu equipo pierde, no corras a culpar al delantero, revisa antes la densidad del aire para esa sede. Admitámoslo, sigue siendo una excusa, pero es bastante más elegante cuando viene con $\rho$, $C_d$ y *Napkin Notes*.   

<figure class="nn-article-figure">
  <img src="{static}/images/05_mapa_rareza_estatico.png" alt="Mapa físico del Mundial 2026: índice de rareza del balón por sede">
  <figcaption>
    Figura 5. Las 16 sedes del Mundial 2026 y sus índices de rareza.
  </figcaption>
</figure>

---

## Anexo mínimo: datos clave

<table class="nn-compact-table">
  <thead>
    <tr>
      <th>Sede</th>
      <th>Estadio</th>
      <th>Altitud<br><small>[m]</small></th>
      <th>&rho;<br><small>[kg/m<sup>3</sup>]</small></th>
      <th>Drag<br><small>30 m/s</small><br><small>[N]</small></th>
      <th>Índice<br><small>R</small></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="nowrap">CDMX</span></td>
      <td><span class="nowrap">Azteca</span></td>
      <td><span class="nowrap">2240</span></td>
      <td><span class="nowrap">0.915</span></td>
      <td><span class="nowrap">3.91</span></td>
      <td><span class="nowrap">75.8</span></td>
    </tr>
    <tr>
      <td><span class="nowrap">Guadalajara</span></td>
      <td><span class="nowrap">Akron</span></td>
      <td><span class="nowrap">1598</span></td>
      <td><span class="nowrap">0.977</span></td>
      <td><span class="nowrap">4.18</span></td>
      <td><span class="nowrap">51.3</span></td>
    </tr>
    <tr>
      <td><span class="nowrap">Monterrey</span></td>
      <td><span class="nowrap">BBVA</span></td>
      <td><span class="nowrap">500</span></td>
      <td><span class="nowrap">1.089</span></td>
      <td><span class="nowrap">4.66</span></td>
      <td><span class="nowrap">49.7</span></td>
    </tr>
    <tr>
      <td><span class="nowrap">Dallas</span></td>
      <td><span class="nowrap">AT&amp;T</span></td>
      <td><span class="nowrap">184</span></td>
      <td><span class="nowrap">1.132</span></td>
      <td><span class="nowrap">4.84</span></td>
      <td><span class="nowrap">45.7</span></td>
    </tr>
    <tr>
      <td><span class="nowrap">Seattle</span></td>
      <td><span class="nowrap">Lumen Field</span></td>
      <td><span class="nowrap">45</span></td>
      <td><span class="nowrap">1.198</span></td>
      <td><span class="nowrap">5.12</span></td>
      <td><span class="nowrap">44.4</span></td>
    </tr>
    <tr>
      <td><span class="nowrap">Vancouver</span></td>
      <td><span class="nowrap">BC Place</span></td>
      <td><span class="nowrap">34</span></td>
      <td><span class="nowrap">1.205</span></td>
      <td><span class="nowrap">5.15</span></td>
      <td><span class="nowrap">40.3</span></td>
    </tr>
  </tbody>
</table>

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
