---
title: "¿Es posible robarle energía a un planeta? ¿Y a un agujero negro?"
author: Gabriel Sánchez Pérez
date: 2026-11-05
layout: articles
status: hidden
slug: prueba-gabri1
category: Física
tags:
  - gravitación
  - relatividad general
  - agujeros negros
  - asistencia gravitacional
  - mecánica orbital
summary: "¿Podemos utilizar la gravedad para obtener energía sin gastar combustible? Las sondas espaciales llevan décadas haciéndolo gracias a los planetas. Más sorprendente todavía: la relatividad general permite extraer energía de un agujero negro en rotación."
image: images/gabri-gravedad/Kerr3.jpeg
certificate: false
---
[TOC]

Imaginad que queremos enviar una nave espacial hasta los confines del sistema solar. La manera más evidente de hacerlo consiste en construir un cohete suficientemente potente, cargarlo de combustible y acelerar hasta alcanzar la velocidad deseada. Sin embargo, existe una alternativa mucho más ingeniosa: aprovechar el movimiento de los planetas para acelerar nuestra nave sin necesidad de encender sus motores.

Este procedimiento, conocido como *asistencia gravitacional*, se ha utilizado en numerosas misiones espaciales. Las sondas Voyager, por ejemplo, aprovecharon sus encuentros con los planetas gigantes para modificar sus trayectorias y adquirir velocidades que habrían sido mucho más difíciles de alcanzar utilizando únicamente combustible.

<p style="text-align: center;">
  <img src="/images/gabri-gravedad/asistencia1.jpeg" alt="Asistencia gravitacional de la Voyager 1 a su paso por Júpiter. Marzo de 1979." style="display: block; max-width: 100%; height: auto; margin: 0 auto;">
</p>
<p style="text-align: center; color: var(--muted); font-size: 0.92rem;">
  Asistencia gravitacional de la Voyager 1 a su paso por Júpiter. Marzo de 1979.
</p>

Pero aquí surge una pregunta interesante. Si nuestra nave aumenta su energía cinética sin utilizar sus motores, ¿de dónde procede esa energía? ¿Acaso podemos obtenerla gratuitamente gracias a la gravedad? La respuesta es que **la nave le roba una pequeñísima cantidad de energía orbital al planeta**. Y no se trata de una metáfora: el planeta pierde energía y la nave la gana, respetando escrupulosamente las leyes de conservación de la física.

Lo verdaderamente sorprendente es que podemos llevar esta idea mucho más lejos. En 1969, el físico y matemático Roger Penrose propuso un mecanismo mediante el cual sería posible extraer energía de un agujero negro en rotación. En determinadas circunstancias, una partícula podría acercarse a un agujero negro y escapar con más energía de la que tenía inicialmente.

¿Cómo es posible? ¿De dónde sale esa energía adicional? ¿Podemos utilizar un agujero negro como si fuera una gigantesca batería cósmica? En la napkin de hoy estudiaremos dos mecanismos que, aunque pertenecen a teorías físicas distintas, comparten una misma idea: **la gravedad puede permitirnos transferir energía desde un cuerpo masivo hacia otro mucho más pequeño**.

Comencemos por el caso más familiar.

---

## Asistencia gravitacional

### ¿Cómo acelerar una nave sin encender los motores?

Supongamos que una nave espacial se aproxima a Júpiter. Debido a la atracción gravitatoria del planeta, la velocidad de la nave aumenta a medida que se acerca. Sin embargo, cuando comienza a alejarse, la gravedad vuelve a frenarla.

Si despreciamos otros cuerpos celestes y consideramos que Júpiter permanece prácticamente inmóvil, la conservación de la energía mecánica nos dice que

$$
E=\frac12 mv^2-\frac{GMm}{r}=\text{constante},
$$

donde \(m\) es la masa de la nave, \(M\) la masa de Júpiter, \(r\) la distancia entre ambos cuerpos, \(v\) la velocidad de la nave y \(G\) la constante de gravitación universal.

Cuando la nave está suficientemente lejos del planeta, el término gravitatorio tiende a cero. Por tanto, si inicialmente se aproxima con rapidez \(v_i\) y finalmente se aleja con rapidez \(v_f\), necesariamente tendremos

$$
\frac12 mv_i^2=\frac12 mv_f^2,
$$

es decir,

$$
\boxed{v_i=v_f.}
$$

Parece que no hemos conseguido nada. La nave se aproxima al planeta, acelera, gira alrededor de él, vuelve a frenarse y termina alejándose con la misma rapidez con la que llegó.

¿Dónde está entonces el truco? La clave consiste en recordar algo que hemos pasado por alto: **Júpiter no está quieto**.

Júpiter se mueve alrededor del Sol a una velocidad aproximada de \(13\ \mathrm{km/s}\). Y, como veremos, este movimiento es precisamente lo que permite que nuestra nave gane energía.

### Todo depende del sistema de referencia

Para simplificar los cálculos, consideremos un sistema de referencia heliocéntrico, es decir, uno en el que el Sol permanece aproximadamente en reposo. Llamemos \(\mathbf V\) a la velocidad orbital de Júpiter respecto al Sol y \(\mathbf v_i\) a la velocidad inicial de nuestra nave en ese mismo sistema de referencia.

La velocidad de la nave respecto a Júpiter será

$$
\mathbf u_i=\mathbf v_i-\mathbf V.
$$

Después del encuentro gravitacional, la nave saldrá con una nueva velocidad relativa \(\mathbf u_f\). Como acabamos de comprobar mediante la conservación de la energía, y despreciando el minúsculo retroceso de Júpiter, se cumple que

$$
|\mathbf u_i|=|\mathbf u_f|=u.
$$

Sin embargo, esto no implica que ambos vectores sean iguales. La gravedad de Júpiter modifica la dirección de movimiento de la nave, de modo que, generalmente,

$$
\mathbf u_i\neq\mathbf u_f.
$$

Para obtener las velocidades respecto al Sol, simplemente tenemos que sumar la velocidad orbital del planeta:

$$
\mathbf v_i=\mathbf V+\mathbf u_i,
$$

$$
\mathbf v_f=\mathbf V+\mathbf u_f.
$$

Veamos qué ocurre con la energía cinética de la nave.

La variación de energía viene dada por

$$
\Delta E=\frac12 m|\mathbf v_f|^2-\frac12 m|\mathbf v_i|^2.
$$

Sustituyendo las expresiones anteriores,

$$
\Delta E=\frac12m\left(|\mathbf V+\mathbf u_f|^2-|\mathbf V+\mathbf u_i|^2\right).
$$

Desarrollando los productos escalares,

$$
\Delta E=\frac12m\left(2\mathbf V\cdot\mathbf u_f+|\mathbf u_f|^2-2\mathbf V\cdot\mathbf u_i-|\mathbf u_i|^2\right).
$$

Pero sabemos que \(|\mathbf u_i|=|\mathbf u_f|\), por lo que los términos cuadráticos se cancelan y obtenemos

$$
\boxed{\Delta E=m\mathbf V\cdot(\mathbf u_f-\mathbf u_i).}
$$

**Esta es la ecuación fundamental de la asistencia gravitacional.** Fijémonos en que el resultado depende del producto escalar entre la velocidad del planeta y el cambio de velocidad relativa de la nave. Por tanto, son posibles tres situaciones:

- Si \(\Delta E>0\), la nave gana energía.
- Si \(\Delta E<0\), la nave pierde energía.
- Si \(\Delta E=0\), la nave no experimenta ningún cambio neto de energía cinética.

En otras palabras, dependiendo de la geometría del encuentro, podemos utilizar un planeta tanto para acelerar como para frenar una nave espacial. Y lo más importante: todo esto puede conseguirse sin gastar combustible durante el encuentro gravitacional.

### ¿Cuánta energía podemos conseguir?

Consideremos un ejemplo sencillo en el que el movimiento se produce aproximadamente en una misma dirección. Supongamos que Júpiter se desplaza con velocidad

$$
V=13\ \mathrm{km/s}
$$

y que una nave se aproxima con una velocidad relativa al planeta de

$$
u_i=-10\ \mathrm{km/s}.
$$

Si la nave experimentara una desviación ideal de \(180^\circ\), saldría con

$$
u_f=+10\ \mathrm{km/s}.
$$

Por tanto, sus velocidades heliocéntricas serían

$$
v_i=13-10=3\ \mathrm{km/s}
$$

y

$$
v_f=13+10=23\ \mathrm{km/s}.
$$

¡Hemos pasado de \(3\) a \(23\ \mathrm{km/s}\) sin utilizar ningún motor!

Para una nave de \(1000\ \mathrm{kg}\), esto supone una ganancia de energía cinética de

$$
\Delta E=\frac12(1000)\left[(23000)^2-(3000)^2\right],
$$

es decir,

$$
\boxed{\Delta E=2.6\times10^{11}\ \mathrm J.}
$$

Para hacernos una idea, esta cantidad equivale aproximadamente a la energía liberada por unas 62 toneladas de TNT. Naturalmente, hemos considerado una situación idealizada. Una desviación exacta de \(180^\circ\) no se consigue mediante un sobrevuelo hiperbólico ordinario, y la geometría real del encuentro está limitada por el tamaño del planeta y por la distancia mínima a la que puede pasar nuestra nave.

Aun así, el ejemplo ilustra perfectamente la enorme cantidad de energía que podemos obtener mediante este procedimiento.

### Pero ¿de dónde sale esa energía?

Volvamos a la cuestión fundamental. Si la nave ha ganado energía, debe haber algún otro cuerpo que la haya perdido. Ese cuerpo es Júpiter. Durante el encuentro gravitacional, la nave no solo experimenta la atracción del planeta. Por la tercera ley de Newton, también ejerce una fuerza gravitatoria sobre él. Como consecuencia, Júpiter experimenta una variación extraordinariamente pequeña de su velocidad orbital.

Si consideramos el sistema formado por el planeta y la nave, la conservación del momento lineal implica

$$
m\Delta\mathbf v+M\Delta\mathbf V=0,
$$

donde \(M\) representa la masa del planeta. Por tanto,

$$
\boxed{\Delta\mathbf V=-\frac{m}{M}\Delta\mathbf v.}
$$

Puesto que la masa de Júpiter es aproximadamente

$$
M_J=1.9\times10^{27}\ \mathrm{kg},
$$

mientras que nuestra nave tiene una masa de apenas \(1000\ \mathrm{kg}\), la variación de velocidad del planeta es prácticamente imperceptible.

En nuestro ejemplo idealizado, el cambio de velocidad de la nave sería de \(20\ \mathrm{km/s}\), por lo que la variación correspondiente de la velocidad de Júpiter tendría un módulo del orden de

$$
|\Delta V|\approx\frac{10^3}{1.9\times10^{27}}(2\times10^4)\approx10^{-20}\ \mathrm{m/s}.
$$

Es una cantidad ridículamente pequeña. Sin embargo, puesto que Júpiter posee una masa gigantesca, una variación minúscula de su velocidad puede corresponder a una cantidad considerable de energía. En efecto, para una pequeña variación de velocidad, el cambio de energía cinética del planeta es aproximadamente

$$
\Delta E_J\approx M\mathbf V\cdot\Delta\mathbf V.
$$

Utilizando la conservación del momento lineal, obtenemos

$$
\Delta E_J\approx-m\mathbf V\cdot\Delta\mathbf v.
$$

Y, puesto que en la aproximación empleada

$$
\Delta\mathbf v=\mathbf u_f-\mathbf u_i,
$$

resulta que

$$
\boxed{\Delta E_J\approx-\Delta E.}
$$

La energía ganada por la nave procede de la energía orbital del planeta. Para tener en cuenta exactamente el retroceso de Júpiter habría que resolver el problema de dos cuerpos con masa finita, pero la conclusión física sería la misma.

> **¿Podríamos frenar Júpiter utilizando millones de naves espaciales?**
>
> En principio, sí. Si enviáramos suficientes naves para realizar asistencias gravitacionales que extrajeran energía de Júpiter, podríamos modificar su órbita. En la práctica, necesitaríamos un número absolutamente descomunal de encuentros para producir un efecto apreciable.

No obstante, la conclusión resulta fascinante: **una asistencia gravitacional no es simplemente una forma ingeniosa de cambiar la trayectoria de una nave, sino un auténtico mecanismo de transferencia de energía entre cuerpos celestes**. Y si podemos extraer energía del movimiento de un planeta, ¿podríamos hacer algo parecido con un objeto cuya gravedad es tan intensa que ni siquiera la luz puede escapar de su interior?

Sorprendentemente, la respuesta vuelve a ser afirmativa.

---


## Conclusiones

Hemos comenzado nuestro viaje con una nave espacial que se acerca a Júpiter y hemos terminado explorando una de las regiones más extremas del universo: la ergosfera de un agujero negro en rotación. A primera vista, la asistencia gravitacional y el proceso de Penrose parecen fenómenos completamente distintos. El primero puede explicarse mediante la mecánica newtoniana, mientras que el segundo requiere recurrir a la geometría del espacio-tiempo descrita por la relatividad general.

Sin embargo, existe una conexión conceptual entre ambos. En una asistencia gravitacional, una nave puede ganar energía a costa de modificar ligeramente el movimiento orbital de un planeta. El intercambio depende de la geometría del encuentro y del sistema de referencia desde el que describimos el movimiento.

En el proceso de Penrose, una partícula puede escapar de la ergosfera con más energía de la que tenía inicialmente, siempre que otra partícula con energía conservada negativa sea absorbida por el agujero negro. La energía adicional procede de la rotación del propio agujero negro. En ambos casos, la conservación de la energía permanece intacta.

Y es que, aunque pueda parecer sorprendente, **extraer energía de un sistema gravitatorio no significa crear energía, sino encontrar una manera de transferirla**. Esta es precisamente una de las ideas más hermosas de la física: mecanismos que, a primera vista, parecen imposibles terminan siendo consecuencias perfectamente legítimas de sus leyes fundamentales.

Así que ya sabéis la respuesta a las preguntas con las que comenzábamos. ¿Podemos robarle energía a un planeta? Sí, y llevamos décadas haciéndolo.

¿Podemos robársela a un agujero negro? También, al menos en principio, y la relatividad general nos explica exactamente cómo. La gravedad no nos regala energía. Pero, si sabemos aprovecharla, puede ayudarnos a conseguirla de los lugares más insospechados del universo.

---

## Referencias

- NASA, *Basics of Space Flight*, capítulo 4, «Trajectories»: [https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/](https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/)
- Agencia Espacial Europea, «What are gravity assists?»: [https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists](https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists)
- Schnittman, J. D. (2018), *The Collisional Penrose Process*, *General Relativity and Gravitation*, 50: [https://pmc.ncbi.nlm.nih.gov/articles/PMC6894168/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6894168/)
- Stuchlík, Z., Kološ, M. y Tursunov, A. (2021), «Penrose Process: Its Variants and Astrophysical Applications», *Universe* 7(11), 416: [https://www.mdpi.com/2218-1997/7/11/416](https://www.mdpi.com/2218-1997/7/11/416)
- Christodoulou, D. (1970), «Reversible and Irreversible Transformations in Black-Hole Physics», *Physical Review Letters* 25.
