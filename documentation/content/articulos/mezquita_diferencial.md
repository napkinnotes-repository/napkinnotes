---
title: El camino más corto no siempre es la línea recta
author: Gabriel Sánchez Pérez
date: 2026-07-23
layout: articles
slug: misterio-mezquita-washington-geometria
status: published
category: Matemáticas
tags:
  - geometría
  - geodésicas
  - mapas
  - paradojas
summary: La increíble historia de cómo una mezquita en Washington D. C. casi es demolida debido a la distorsión de los mapas planos y las leyes de la geometría esférica.
image: images/mezquita_washington.jpeg
certificate: true
---

[TOC]





En la *napkin note* de hoy os traemos una curiosa historia que combina la construcción de la mezquita más grande del hemisferio occidental con los aspectos básicos de la geometría diferencial.

La idea de construir una mezquita en Washington fue impulsada en los años 30 del siglo pasado a raíz de varias olas de inmigración desde países como Egipto a Estados Unidos. Después de la II Guerra Mundial, el embajador egipcio en EE.UU., Kamil Abdul Rahim, dio un paso decisivo para la realización de semejante obra faraónica. Contactó con representantes de todo el mundo para financiar la construcción, dejando el diseño del edificio en manos del italiano Mario Rossi.

Las obras comenzaron en 1949 dirigidas por el arquitecto estadounidense Irwin S. Porter, y en 1953 el edificio estaba prácticamente terminado. Fue entonces cuando el embajador, Rahim, visitó el complejo. Cuando llegó allí, sacó una brújula de su bolsillo, miró a Porter y le dijo: “Esta mezquita no está bien. El muro de la *Qibla* no apunta a La Meca. La Meca está al sureste y la mezquita está orientada al noreste. Antiguamente, cuando una mezquita no apuntaba exactamente a La Meca, se obligaba a demoler el edificio y hacerlo de nuevo”.

<!-- Una imagen va así -->
<figure class="nn-article-figure">
  <img src="{static}/images/Mezquita_Mapa1.png" alt="En amarillo, la orientación del edificio. En rojo, la dirección a la Meca">
  <figcaption>
    Figura 1. En amarillo, la orientación del edificio. En rojo, la dirección a la Meca (según un mapa).
  </figcaption>
</figure>

Asustado, Porter llamó a un cartógrafo de la *National Geographic Society*, quien a las pocas horas confirmó que la orientación era la correcta. ¿Qué estaba sucediendo? ¿Quién tenía razón? La solución a todo este embrollo, al igual que a la mayoría de problemas en esta vida, no podría estar en otro lugar más que en la geometría diferencial de variedades. Es broma. La geometría solo me ha causado problemas. (¡Ayuda, por favor!)

<!-- Fin de Sección -->
---


## Distancia geodésica

La pregunta que uno debe hacerse en este punto es clara: ¿Cómo se define la distancia a La Meca (o a cualquier otro punto del planeta)? Veámoslo con un ejemplo más sencillo.

Supongamos que yo, que vivo en Salamanca (una ciudad en el oeste de España), quiero ir a Madrid. Para ello puedo tomar varias rutas. En primer lugar, puedo ir en coche a Zamora, nuestra ciudad vecina, y luego ahí puedo tomar un tren a Madrid. Según Google Maps, la distancia recorrida en este caso es de unos 300 km. Pero también puedo tomar un tren hasta Bilbao, y de allí tomar un vuelo a Atenas (Grecia), y otro vuelo a Madrid. Claramente, la distancia recorrida ahora supera los 5000 km. La opción más corta es, sin lugar a dudas, tomar un autobús o tren directo desde Salamanca a Madrid (unos 200 km). 

¿Cuál es la distancia real de Salamanca a Madrid? Ya hemos visto la respuesta: 200 km, pues corresponden al camino más corto. Definiremos por tanto “distancia” como la longitud del trayecto más corto entre dos puntos.

Volviendo al problema que nos ocupa, ¿cuál es la distancia entre cualesquiera dos puntos en una esfera? (Sí, estoy asumiendo que la Tierra es esférica, ¡no soy un terraplanista de esos!). Para responder, necesitaremos realizar algunas cuentas matemáticas, pero prometo que no serán demasiado complicadas.

<!-- Fin de Sección -->
---


## El camino más corto: un argumento variacional

Para encontrar la curva más corta sobre una esfera de radio $R$, podemos recurrir al cálculo de variaciones, que es la herramienta matemática que nos permite encontrar "funciones que minimizan cosas" (en este caso, la longitud de una curva).

Representemos nuestra esfera usando las coordenadas esféricas estándar $(\theta, \phi)$, donde $\theta \in [0,\pi]$ es la colatitud (el ángulo desde el polo norte) y $\phi \in [0, 2\pi)$ es la longitud. En estas coordenadas, un pequeño elemento de longitud de arco $ds$ en la superficie de la esfera viene dado por:

$$
ds^2 = R^2 d\theta^2 + R^2 \sin^2 \theta d\phi^2
$$

Queremos unir dos puntos, $A$ y $B$. Como la esfera es perfectamente simétrica, siempre podemos girarla de manera que ambos puntos queden situados sobre el mismo meridiano. Es decir, ambos compartirán la misma longitud $\phi_0$.

Ahora, consideremos cualquier curva $\gamma$ que vaya de $A = (\theta_1, \phi_0)$ a $B = (\theta_2, \phi_0)$ (con $\theta_1 < \theta_2$). Podemos parametrizar esta curva expresando la longitud en función de la colatitud, es decir, $\phi = \phi(\theta)$. La longitud total $L$ de esta trayectoria será la suma de todos los pequeños trozos $ds$:

$$
L = \int_{\theta_1}^{\theta_2} \sqrt{R^2 + R^2 \sin^2 \theta \left(\frac{d\phi}{d\theta}\right)^2} d\theta = R \int_{\theta_1}^{\theta_2} \sqrt{1 + \sin^2 \theta (\phi')^2} d\theta,
$$

donde $\phi' = \frac{d\phi}{d\theta}$. Nuestro objetivo es minimizar esta integral. Fijémonos bien en el integrando:

$$
\sqrt{1 + \sin^2 \theta (\phi')^2}.
$$

Dado que el término $\sin^2 \theta (\phi')^2$ siempre es mayor o igual a cero (ya que está elevado al cuadrado y el seno al cuadrado de cualquier ángulo real es no negativo), se cumple de forma directa la siguiente desigualdad:

$$
\sqrt{1 + \sin^2 \theta (\phi')^2} \ge 1.
$$

Por lo tanto, la longitud de nuestra curva siempre estará acotada inferiormente:

$$
L \ge R \int_{\theta_1}^{\theta_2} 1 d\theta = R(\theta_2 - \theta_1).
$$

<!-- Preguntas con recuadro bonito -->
> **¿Cuándo se alcanza el valor mínimo absoluto de la longitud?**
<!-- Fin pregunta con recuadro bonito -->

Únicamente cuando el término que sumaba sea cero en todo el trayecto:

$$
\sin^2 \theta (\phi')^2 = 0 \implies \phi' = 0 \implies \phi(\theta) = \text{constante} = \phi_0.
$$

Esto significa que el camino que minimiza la distancia es aquel donde la longitud $\phi$ no varía en absoluto. En una esfera, las curvas donde la longitud es constante son los meridianos, que no son otra cosa que arcos de círculos máximos (círculos que tienen el mismo radio que la esfera y cuyo centro coincide con el centro de la Tierra). Como cualquier par de puntos en la Tierra se puede rotar para que queden sobre un mismo meridiano sin alterar las distancias, concluimos que el camino más corto entre dos puntos cualesquiera de la esfera es siempre un arco de círculo máximo.

<!-- Fin de Sección -->
---


## Las geodésicas de la métrica esférica estándar

En geometría diferencial, las curvas de menor longitud se conocen formalmente como geodésicas. Pero en lugar de definirlas solo como "los caminos más cortos", las geodésicas se definen matemáticamente a través de la métrica del espacio usando las ecuaciones de Euler-Lagrange para el funcional de energía. Resulta que, como no podía ser de otra manera, ambas definiciones coinciden.

Consideremos la métrica estándar de la esfera de radio $1$ (para simplificar los cálculos): $g = d\theta^2 + \sin^2 \theta d\phi^2$. El Lagrangiano asociado a las geodésicas es:

$$
E(\theta, \phi, \dot{\theta}, \dot{\phi}) = \frac{1}{2} \left( \dot{\theta}^2 + \sin^2 \theta \dot{\phi}^2 \right)
$$

donde los puntos denotan la derivada respecto a un parámetro afín $t$ (que podemos pensar como el tiempo si viajamos a velocidad constante). Las ecuaciones de movimiento de Euler-Lagrange para este sistema son:

$$
\frac{d}{dt}\left(\frac{\partial E}{\partial \dot{x}^i}\right) - \frac{\partial E}{\partial x^i} = 0
$$

Si las desarrollamos para nuestras dos coordenadas, obtenemos el siguiente sistema de ecuaciones diferenciales:

- Para $\theta$: $\ddot{\theta} - \sin \theta \cos \theta \dot{\phi}^2 = 0$.  
- Para $\phi$: $\frac{d}{dt}\left(\sin^2 \theta \dot{\phi}\right) = 0 \Longrightarrow \sin^2 \theta \dot{\phi} = C \quad (\text{constante})$.  

Comprobemos si nuestros candidatos a caminos más cortos, los círculos máximos (representados aquí por los meridianos con $\phi = \text{constante}$), satisfacen estas ecuaciones de las geodésicas:

- Si $\phi(t) = \phi_0$ (constante), entonces su derivada es cero: $\dot{\phi} = 0$.  
- Al sustituir $\dot{\phi} = 0$ en la segunda ecuación, obtenemos $\frac{d}{dt}(0) = 0$, lo cual se cumple trivialmente (con $C = 0$).  
- Al sustituir $\dot{\phi} = 0$ en la primera ecuación, esta se reduce a:

$$
\ddot{\theta} = 0 \implies \theta(t) = a t + b.
$$

Esto describe un movimiento a velocidad angular constante a lo largo del meridiano. Dado que las ecuaciones se satisfacen perfectamente, los meridianos son geodésicas de la esfera. Y como cualquier círculo máximo puede transformarse en un meridiano mediante una rotación (que es una isometría y conserva las geodésicas), queda demostrado que las geodésicas de la métrica estándar de la esfera son, precisamente, los círculos máximos.

<!-- Fin de Sección -->
---


## El engaño de los mapas y el misterio de la mezquita

Aquí es donde se desvela el gran misterio que casi le cuesta la demolición a la mezquita de Washington. Nuestra mente está acostumbrada a ver el mundo a través de mapas planos, generalmente utilizando la archiconocida proyección de Mercator. En estos mapas, si trazamos una línea recta entre Washington D. C. y La Meca, la trayectoria resultante apunta claramente hacia el sureste. Esta línea recta sobre el papel se conoce como loxodromia (una curva que mantiene un rumbo constante de brújula), pero no es el camino más corto en la realidad tridimensional.

<figure class="nn-article-figure">
  <img src="{static}/images/Mezquita_Mapa2.png" alt="Comparación entre la dirección geodésica y la dirección en el plano">
  <figcaption>
    Figura 2. Comparación entre la dirección geodésica (amarillo) y la dirección en el plano (rojo).
  </figcaption>
</figure>

Cuando proyectamos la verdadera distancia geodésica (la ortodromia, es decir, el arco de círculo máximo) sobre ese mismo mapa plano, la ruta no se ve recta, sino que se curva hacia el norte. De hecho, si decidieras volar desde Washington D. C. hasta La Meca siguiendo el camino más corto, despegarías con tu avión apuntando hacia el noreste, sobrevolando parte de Canadá, Groenlandia y el sur de Europa antes de descender hacia Arabia Saudita.

<div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; align-items: flex-start;">
  <figure class="nn-article-figure" style="flex: 1; min-width: 280px; margin: 0;">
    <img src="{static}/images/Mezquita_Mapa3.png" alt="Visión tridimensional del círculo máximo que une Washington con La Meca" style="width: 100%; height: auto;">
    <figcaption>
      Figura 3. Visión tridimensional del círculo máximo que une Washington con La Meca.
    </figcaption>
  </figure>

  <figure class="nn-article-figure" style="flex: 1; min-width: 280px; margin: 0;">
    <img src="{static}/images/Mezquita_Mapa4.png" alt="Desde la orientación apropiada se observa que es una verdadera línea recta" style="width: 100%; height: auto;">
    <figcaption>
      Figura 4. Desde la orientación apropiada, se observa que ésta es la verdadera línea recta.
    </figcaption>
  </figure>
</div>



Dado que las leyes islámicas dictan que el muro de la *Qibla* debe orientarse hacia La Meca siguiendo la distancia más corta posible, el arquitecto Porter y el cartógrafo de la National Geographic tenían toda la razón del mundo: para rezar mirando a La Meca desde Washington hay que mirar hacia el noreste. El embajador Rahim, víctima de la distorsión de los mapas planos, simplemente había olvidado que vivimos atrapados en la preciosa superficie curva de una esfera.

---

# Referencias

Las imágenes han sido obtenidas de Google Maps y Google Earth (© Google) y modificadas por el autor pertinentemente.
