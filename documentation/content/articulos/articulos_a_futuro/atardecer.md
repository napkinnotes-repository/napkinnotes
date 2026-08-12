---
title: ¿Por qué es naranja el atardecer?
author: María Pérez Garrote
date: 2026-08-13
layout: articles
slug: el-atardecer
status: hidden # published si ya está listo
category: Física # categoría con mayúscula inicial
tags: # tags con minúscula inicial
  - Física
  - Óptica
summary: El cielo cambia de color a lo largo del día. Comenzamos el día con un precioso color anaranjado, después se tiñe de azul y, cuando llega el atardecer, volvemos a ver los colores cálidos en el ocaso. Detrás de este festival cromático se esconde un fenómeno físico interesantísimo. Lo explicamos en esta servilleta.
image: images/atardecer_Salamanca.jpg
---

[TOC]


Para entender el cambio de color en el cielo necesitamos saber de qué está hecha nuestra atmósfera. Ésta se compone de diferentes gases: 78.084% de nitrógeno, 20.946% de oxígeno, 0.934% de argón, 0.042% de dióxido de carbono, y una pequeña cantidad de otras moléculas y gases nobles <a class="nn-cite" href="#ref-1">[1]</a>. Cuando la luz interactúa con estos átomos y moléculas sufre un fenómeno físico llamado dispersión, esto es, la descomposición de la radiación en sus diferentes longitudes de onda por la acción del medio de propagación <a class="nn-cite" href="#ref-2">[2]</a>. Si la dispersión de la luz se produce por partículas cuyo tamaño es mucho menor que la longitud de onda de la radiación incidente, hablamos de **dispersión de Rayleigh** o Rayleigh *scattering* en inglés <a class="nn-cite" href="#ref-3">[3]</a>. Esto es precisamente lo que ocurre en nuestra atmósfera.


## La ecuación para la dispersión de Rayleigh

Revisemos algunos conceptos de óptica para entender con más profundidad cómo se produce la dispersión de Rayleigh. Imaginemos que tenemos un haz incidente proveniente del Sol, polarizado en el eje $z$: $E_{inc} = \hat{z}E_i$, y propagándose en la dirección $x$ (figura 1), que choca con un átomo o molécula de la atmósfera de radio $a$ y permitividad $\epsilon_s$. La permitividad del aire la denotaremos como $\epsilon_0$ y su permeabilidad magnética como $\mu_0$. La luz incidente polariza los átomos de la atmósfera y los convierte en pequeños dipolos. El campo eléctrico que produce un pequeño dipolo en la lejanía es aproximadamente <a class="nn-cite" href="#ref-4">[4]</a>:

<!-- Fórmula dipolo -->
$$
E_\theta \cong -k^2 \mu_0 \epsilon_0 \left(\frac{\epsilon_s-\epsilon_0}{\epsilon_s+2\epsilon_0}\right)\frac{a^3}{r}E_i e^{-ikr} \text{sin}(\theta).
$$
Notemos que, por la geometría del problema, las demás componentes del campo eléctrico en coordenadas esféricas son cero. Para el campo magnético tenemos simplemente $H_\theta=\sqrt{\epsilon_0/\mu_0}E_\theta$.

<!-- Imagen geometria -->
<figure class="nn-article-figure">
  <img src="{static}/images/geometry.jpeg">
  <figcaption>
    Figura 1. Geometría para estudiar la dispersión de Rayleigh.
  </figcaption>
</figure>


Podemos calcular la potencia dispersada integrando el vector de Poynting $\langle S \rangle = \frac{1}{2} \mathcal{Re} \{ \mathbf{E}\times\mathbf{H}^* \}$ en el ángulo sólido:
<!-- Fórmula potencia -->
$$
P_S = \frac{4\pi}{3}\sqrt{\frac{\epsilon_0}{\mu_0}}\left(\frac{\epsilon_s-\epsilon_0}{\epsilon_s+2\epsilon_0}\right)^2\left(\frac{2\pi}{\lambda}\right)^4a^6 |E_i|^2.
$$

## Los colores del cielo
Si nos fijamos en la ecuación anterior vemos que la potencia dispersada es inversamente proporcional a la longitud de onda a la cuarta $1/\lambda^4$. Esto significa que, en la atmósfera, la radiación con longitud de onda más corta (violeta y azul) se dispersa más que aquella con longitud de onda mayor (roja y naranja). Esta es la clave para entender por qué a lo largo del día vemos diferentes colores en el cielo. 

<!-- Imagen earth -->
<figure class="nn-article-figure">
  <img src="{static}/images/earth.jpeg">
  <figcaption>
    Figura 2. Dispersión de la luz del Sol por la atmósfera. Foto tomada de [Why is the Sky Blue? A Deep Dive into Rayleigh Scattering](https://medium.com/@ermal.alibali/why-is-the-sky-blue-a-deep-dive-into-rayleigh-scattering-f652f80e59e0).
  </figcaption>
</figure>

Durante las horas centrales del día, los rayos de sol se dispersan en la atmósfera, siendo violeta, azul y verde los colores más predominantes. Por ejemplo, el color azul se dispersa unas nueve veces más que el color rojo. Esto explica por qué durante el día vemos el cielo de color azul en todas las direcciones[^1]. Pero, ¿qué ocurre al amanecer y al atardecer?

[^1]: Para ser más precisos, el color azul se debe al efecto combinado de la dispersión de Rayleigh, a que el ojo humano es poco sensible al violeta y a la absorción del ultravioleta por la capa de ozono.

Durante las horas centrales del día, los rayos de sol se dispersan en la atmósfera, siendo violeta, azul y verde los colores más predominantes. Por ejemplo, el color azul se dispersa unas nueve veces más que el color rojo. Esto explica por qué durante el día vemos el cielo de color azul en todas las direcciones\footnote{Para ser más precisos, el color azul se debe al efecto combinado de la dispersión de Rayleigh, a que el ojo humano es poco sensible al violeta y a la absorción del ultravioleta por la capa de ozono.}. Pero, ¿qué ocurre al amanecer y al atardecer?

<!-- Imagen cielo azul -->
<figure class="nn-article-figure">
  <img src="{static}/images/cielo_azul.jpg">
  <figcaption>
    Figura 3. El cielo azul en los Pirineos.
  </figcaption>
</figure>

### El atardecer

Pues aquí la clave es la dirección en la que observamos los rayos de luz. Durante el día el sol está situado verticalmente sobre nosotros. En cambio, durante el amanecer y el atardecer el sol está situado sobre el horizonte y, por tanto, los rayos de luz recorren mayor recorrido por la atmósfera. Durante este recorrido las longitudes de onda cortas se dispersan mucho más que las largas. Como consecuencia, la luz que llega directamente desde el Sol ha perdido gran parte de sus componentes azules y violetas, quedando enriquecida en las longitudes de onda largas (amarillos, naranjas y rojos).

<!-- Imagen atardecer -->
<figure class="nn-article-figure">
  <img src="{static}/images/atardecer_Salamanca.jpg">
  <figcaption>
    Figura 4. Scattering Rayleigh en el cielo de Salamanca.
  </figcaption>
</figure>

## Los cielos más contaminados tienen atardeceres más bonitos.

Hay muchos factores atmosféricos que influyen en los colores del amanecer y del atardecer. Cuando hay una mayor concentración de aerosoles —por ejemplo tras una erupción volcánica, un incendio o en zonas muy contaminadas— aparece además la dispersión de Mie <a class="nn-cite" href="#ref-5">[5]</a>. Estas partículas eliminan parte de la luz azul y pueden intensificar los tonos rojizos y anaranjados del amanecer y del atardecer. De hecho, la intensidad de los colores nos puede dar una estimación de la contaminación atmosférica <a class="nn-cite" href="#ref-6">[6]</a>. A decir verdad, yo abogo por tener cielos más limpios aunque sean menos coloridos.

## Referencias

<ol class="nn-references">
  <li id="ref-1">
    <a href="https://www.noaa.gov/jetstream/atmosphere" >https://www.noaa.gov/jetstream/atmosphere</a>
  </li>

  <li id="ref-2">
    <a href="https://dle.rae.es/dispersi%C3%B3n" >https://dle.rae.es/dispersi%C3%B3n</a>
  </li>

  <li id="ref-3">
    Strutt, J. W. (1871). On the light from the sky, its polarization and colour. <em>The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 41(271), 107–120.</em>.
    <a href="https://doi.org/10.1080/14786447108640452" target="_blank" rel="noopener noreferrer">https://doi.org/10.1080/14786447108640452</a>
  </li>

  <li id="ref-4">
    Griffiths, D. J. (2017). Introduction to Electrodynamics. <em>Cambridge University Press.</em>.
    <a href=" https://doi.org/10.1017/9781108333511 " target="_blank" rel="noopener noreferrer"> https://doi.org/10.1017/9781108333511 </a>
  </li>

  <li id="ref-5">
    Mie, G. (1908). Beiträge zur Optik trüber Medien, speziell kolloidaler Metallösungen. <em>Annalen der Physik 330, 377-445</em>.
    <a href="https://doi.org/10.1002/andp.19083300302" target="_blank" rel="noopener noreferrer"> https://doi.org/10.1002/andp.19083300302 </a>
  </li>

  <li id="ref-6">
    <a href="https://revista.iaa.es/content/la-contaminaci%C3%B3n-lum%C3%ADnica" >https://revista.iaa.es/content/la-contaminaci%C3%B3n-lum%C3%ADnica</a>
  </li>
</ol>
