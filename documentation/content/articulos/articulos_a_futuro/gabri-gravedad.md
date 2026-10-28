---
title: "¿Es posible robarle energía a un planeta? ¿Y a un agujero negro?"
author: Gabriel Sánchez Pérez
date: 2026-11-05
layout: articles
status: hidden
slug: prueba-gabri
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

Pero aquí surge una pregunta interesante. Si nuestra nave aumenta su energía cinética sin utilizar sus motores, ¿de dónde procede esa energía? ¿Acaso podemos obtenerla gratuitamente gracias a la gravedad?

La respuesta es que **la nave le roba una pequeñísima cantidad de energía orbital al planeta**. Y no se trata de una metáfora: el planeta pierde energía y la nave la gana, respetando escrupulosamente las leyes de conservación de la física.

Lo verdaderamente sorprendente es que podemos llevar esta idea mucho más lejos. En 1969, el físico y matemático Roger Penrose propuso un mecanismo mediante el cual sería posible extraer energía de un agujero negro en rotación. En determinadas circunstancias, una partícula podría acercarse a un agujero negro y escapar con más energía de la que tenía inicialmente.

¿Cómo es posible? ¿De dónde sale esa energía adicional? ¿Podemos utilizar un agujero negro como si fuera una gigantesca batería cósmica?

En la napkin de hoy estudiaremos dos mecanismos que, aunque pertenecen a teorías físicas distintas, comparten una misma idea: **la gravedad puede permitirnos transferir energía desde un cuerpo masivo hacia otro mucho más pequeño**.

Comencemos por el caso más familiar.

---

## 1. Asistencia gravitacional

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

¿Dónde está entonces el truco?

La clave consiste en recordar algo que hemos pasado por alto: **Júpiter no está quieto**.

Júpiter se mueve alrededor del Sol a una velocidad aproximada de \(13\ \mathrm{km/s}\). Y, como veremos, este movimiento es precisamente lo que permite que nuestra nave gane energía.

### Todo depende del sistema de referencia

Para simplificar los cálculos, consideremos un sistema de referencia heliocéntrico, es decir, uno en el que el Sol permanece aproximadamente en reposo.

Llamemos \(\mathbf V\) a la velocidad orbital de Júpiter respecto al Sol y \(\mathbf v_i\) a la velocidad inicial de nuestra nave en ese mismo sistema de referencia.

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

**Esta es la ecuación fundamental de la asistencia gravitacional.**

Fijémonos en que el resultado depende del producto escalar entre la velocidad del planeta y el cambio de velocidad relativa de la nave. Por tanto, son posibles tres situaciones:

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

Para hacernos una idea, esta cantidad equivale aproximadamente a la energía liberada por unas 62 toneladas de TNT.

Naturalmente, hemos considerado una situación idealizada. Una desviación exacta de \(180^\circ\) no se consigue mediante un sobrevuelo hiperbólico ordinario, y la geometría real del encuentro está limitada por el tamaño del planeta y por la distancia mínima a la que puede pasar nuestra nave.

Aun así, el ejemplo ilustra perfectamente la enorme cantidad de energía que podemos obtener mediante este procedimiento.

### Pero ¿de dónde sale esa energía?

Volvamos a la cuestión fundamental. Si la nave ha ganado energía, debe haber algún otro cuerpo que la haya perdido. Ese cuerpo es Júpiter.

Durante el encuentro gravitacional, la nave no solo experimenta la atracción del planeta. Por la tercera ley de Newton, también ejerce una fuerza gravitatoria sobre él. Como consecuencia, Júpiter experimenta una variación extraordinariamente pequeña de su velocidad orbital.

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

Es una cantidad ridículamente pequeña. Sin embargo, puesto que Júpiter posee una masa gigantesca, una variación minúscula de su velocidad puede corresponder a una cantidad considerable de energía.

En efecto, para una pequeña variación de velocidad, el cambio de energía cinética del planeta es aproximadamente

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

No obstante, la conclusión resulta fascinante: **una asistencia gravitacional no es simplemente una forma ingeniosa de cambiar la trayectoria de una nave, sino un auténtico mecanismo de transferencia de energía entre cuerpos celestes**.

Y si podemos extraer energía del movimiento de un planeta, ¿podríamos hacer algo parecido con un objeto cuya gravedad es tan intensa que ni siquiera la luz puede escapar de su interior?

Sorprendentemente, la respuesta vuelve a ser afirmativa.

---

## 2. El proceso de Penrose

### ¿Puede un agujero negro perder energía?

Los agujeros negros son probablemente los objetos más fascinantes de nuestro universo. Su campo gravitatorio es tan intenso que, una vez atravesado su horizonte de sucesos, nada puede regresar al exterior, ni siquiera la luz.

Podríamos pensar, por tanto, que un agujero negro constituye una especie de prisión cósmica: todo puede entrar, pero nada puede salir.

Sin embargo, esta afirmación no implica que sea imposible extraer energía de un agujero negro. De hecho, **un agujero negro en rotación almacena una enorme cantidad de energía que, al menos en principio, podemos aprovechar**.

Para comprender cómo funciona este mecanismo, primero necesitamos recordar algunas ideas de la teoría de la relatividad general.

En 1915, Albert Einstein revolucionó nuestra comprensión de la gravedad al proponer que esta no es una fuerza convencional, sino una manifestación de la curvatura del espacio-tiempo. Los cuerpos masivos deforman la geometría que los rodea, y las partículas se mueven siguiendo las trayectorias determinadas por esa geometría.

Las famosas ecuaciones de campo de Einstein,

$$
\boxed{R_{\mu\nu}-\frac12 Rg_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu},}
$$

relacionan precisamente la geometría del espacio-tiempo, descrita por el tensor de Ricci \(R_{\mu\nu}\), el escalar de curvatura \(R\) y el tensor métrico \(g_{\mu\nu}\), con el contenido de materia y energía, representado por \(T_{\mu\nu}\).

Estas ecuaciones admiten distintas soluciones que describen diferentes configuraciones gravitatorias.

Una de las más conocidas es la solución de Schwarzschild, que describe el espacio-tiempo exterior de un cuerpo esféricamente simétrico y sin rotación. Si dicho cuerpo es un agujero negro, su horizonte de sucesos se encuentra en el llamado radio de Schwarzschild,

$$
\boxed{r_s=\frac{2GM}{c^2},}
$$

donde \(M\) es la masa del agujero negro.

Pero ¿qué ocurre si el agujero negro está girando?

En ese caso, necesitamos una solución más general: la **métrica de Kerr**, descubierta por el matemático Roy Kerr en 1963.

Y aquí es donde comienza nuestra historia.

### Un agujero negro que arrastra el espacio-tiempo

Una de las consecuencias más sorprendentes de la relatividad general es que un cuerpo en rotación puede arrastrar consigo el espacio-tiempo que lo rodea. Este fenómeno se conoce como *arrastre de referencia* o *frame dragging*.

Imaginemos que estamos cerca de un agujero negro que gira sobre sí mismo. A diferencia de lo que ocurre con un agujero negro estático, el espacio-tiempo circundante también se ve afectado por su rotación.

Para describir matemáticamente este fenómeno, consideremos la métrica de Kerr en coordenadas de Boyer-Lindquist.

A partir de ahora utilizaremos unidades geométricas, en las que \(G=c=1\), algo habitual en relatividad general.

El elemento de línea viene dado por

$$
\begin{aligned}
ds^2={}&-\left(1-\frac{2Mr}{\Sigma}\right)dt^2
-\frac{4Mar\sin^2\theta}{\Sigma}\,dt\,d\phi\\
&+\frac{\Sigma}{\Delta}\,dr^2+\Sigma\,d\theta^2\\
&+\left(r^2+a^2+\frac{2Ma^2r\sin^2\theta}{\Sigma}\right)\sin^2\theta\,d\phi^2,
\end{aligned}
$$

donde hemos definido

$$
\Sigma=r^2+a^2\cos^2\theta,
$$

$$
\Delta=r^2-2Mr+a^2,
$$

y el parámetro

$$
a=\frac JM
$$

representa el momento angular por unidad de masa del agujero negro.

No os preocupéis si la expresión parece intimidante. No necesitamos estudiar todos sus términos para comprender lo que ocurre.

Fijémonos únicamente en uno de ellos:

$$
-\frac{4Mar\sin^2\theta}{\Sigma}\,dt\,d\phi.
$$

Este término mezcla la coordenada temporal \(t\) con la coordenada angular \(\phi\). Su presencia es fundamental: **la rotación del agujero negro introduce un acoplamiento entre el tiempo y el movimiento angular**.

En particular, si \(a=0\), este término desaparece y recuperamos la solución de Schwarzschild.

Pero cuando \(a\neq0\), el espacio-tiempo posee una propiedad extraordinaria: suficientemente cerca del agujero negro, resulta imposible permanecer inmóvil respecto a un observador situado muy lejos de él.

Incluso aunque encendiéramos unos motores extremadamente potentes para intentar mantenernos en una posición angular fija, no podríamos conseguirlo en cierta región del espacio-tiempo.

Esa región recibe el nombre de **ergosfera**.

### La ergosfera: una región de la que todavía podemos escapar

Para localizar la ergosfera debemos distinguir dos superficies.

La primera es el horizonte de sucesos, determinado por la condición

$$
\Delta=0.
$$

Resolviendo la ecuación

$$
r^2-2Mr+a^2=0,
$$

obtenemos que el horizonte exterior se encuentra en

$$
\boxed{r_+=M+\sqrt{M^2-a^2}.}
$$

La segunda superficie es el llamado *límite estático*, que se obtiene imponiendo

$$
g_{tt}=0.
$$

Como

$$
g_{tt}=-\left(1-\frac{2Mr}{\Sigma}\right),
$$

la condición anterior conduce a

$$
r^2-2Mr+a^2\cos^2\theta=0.
$$

Por tanto, el límite estático exterior viene dado por

$$
\boxed{r_{\mathrm{erg}}(\theta)=M+\sqrt{M^2-a^2\cos^2\theta}.}
$$

La región comprendida entre ambas superficies,

$$
\boxed{r_+<r<r_{\mathrm{erg}}(\theta),}
$$

es la ergosfera.

Observemos que su tamaño depende de la latitud \(\theta\). En los polos, donde \(\cos^2\theta=1\), el límite estático coincide con el horizonte. En cambio, en el plano ecuatorial, donde \(\theta=\pi/2\), encontramos que

$$
r_{\mathrm{erg}}\left(\frac\pi2\right)=2M.
$$

Por consiguiente, la ergosfera se extiende más lejos del agujero negro en su región ecuatorial.

Lo verdaderamente importante es que **la ergosfera se encuentra fuera del horizonte de sucesos**, salvo en los polos, donde ambas superficies se tocan.

<p style="text-align: center;">
  <img src="/images/gabri-gravedad/Kerr1.jpeg" alt="Imagen esquemática del horizonte de eventos del agujero negro de Kerr y su ergoesfera." style="display: block; max-width: 100%; height: auto; margin: 0 auto;">
</p>
<p style="text-align: center; color: var(--muted); font-size: 0.92rem;">
  Imagen esquemática del horizonte de eventos del agujero negro de Kerr y su ergoesfera.
</p>

Esto significa que una partícula situada en su interior todavía puede escapar hacia el infinito, siempre que siga una trayectoria adecuada.

No obstante, todos los observadores físicos dentro de la ergosfera están obligados a girar en el mismo sentido que el agujero negro, como consecuencia del arrastre del espacio-tiempo.

Y es precisamente esta peculiar geometría la que hace posible el proceso de Penrose.

### Energías negativas: la clave del proceso de Penrose

Llegamos al punto más interesante del artículo.

En nuestra experiencia cotidiana, la energía de una partícula libre siempre es positiva. Una partícula con masa \(m\) y velocidad \(v\), por ejemplo, posee una energía relativista

$$
E=\gamma mc^2,
$$

donde

$$
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.
$$

Esta cantidad es necesariamente positiva.

¿Cómo es posible, entonces, que existan partículas con energía negativa cerca de un agujero negro?

La respuesta es que debemos distinguir entre la energía medida localmente por un observador y la energía conservada asociada a la simetría temporal del espacio-tiempo.

En relatividad general, si la geometría es estacionaria, existe un campo vectorial de Killing temporal \(\xi^\mu\), que permite definir una energía conservada para una partícula de cuadrimomento \(p^\mu\):

$$
\boxed{E=-p_\mu\xi^\mu.}
$$

Esta cantidad coincide con la energía que atribuimos a la partícula desde el infinito, donde el espacio-tiempo se aproxima al de Minkowski.

Para una trayectoria geodésica, su conservación puede demostrarse utilizando la ecuación de Killing,

$$
\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0.
$$

En efecto, si \(p^\mu\) es el cuadrimomento de una partícula libre, entonces

$$
p^\nu\nabla_\nu p^\mu=0.
$$

Por tanto,

$$
\begin{aligned}
p^\nu\nabla_\nu E
&=-p^\nu\nabla_\nu(p_\mu\xi^\mu)\\
&=-p^\nu p^\mu\nabla_\nu\xi_\mu\\
&=0,
\end{aligned}
$$

donde en la última igualdad hemos utilizado la simetría de \(p^\nu p^\mu\) y la antisimetría que impone la ecuación de Killing.

Así pues,

$$
\boxed{E=\text{constante}}
$$

a lo largo de la trayectoria de una partícula libre.

Ahora bien, existe un detalle crucial. Fuera de la ergosfera, el vector de Killing \(\xi^\mu\) es de tipo temporal. Esto garantiza que la energía conservada de una partícula física dirigida hacia el futuro sea positiva.

Sin embargo, dentro de la ergosfera ocurre algo extraordinario: el vector \(\xi^\mu\) se vuelve de tipo espacial.

Por consiguiente, el producto

$$
-p_\mu\xi^\mu
$$

ya no tiene por qué ser positivo.

Es decir, **dentro de la ergosfera pueden existir partículas con energía conservada negativa respecto al infinito**.

Esto no significa que un observador local pueda medir una energía física negativa. La energía local de una partícula sigue siendo positiva. Lo que puede cambiar de signo es la cantidad conservada asociada a las traslaciones temporales del espacio-tiempo.

Y esta distinción es exactamente lo que necesitamos para extraer energía del agujero negro.

### El ingenioso experimento de Roger Penrose

Imaginemos que enviamos una partícula hacia un agujero negro de Kerr.

La partícula posee una energía inicial \(E_0>0\), medida respecto al infinito.

Supongamos que, al penetrar en la ergosfera, la partícula se desintegra en dos fragmentos, que llamaremos \(A\) y \(B\).

La conservación del cuadrimomento exige que

$$
p_0^\mu=p_A^\mu+p_B^\mu.
$$

Contrayendo con el vector de Killing temporal, obtenemos inmediatamente la conservación de la energía:

$$
\boxed{E_0=E_A+E_B.}
$$

Hasta aquí no parece haber nada especial.

Pero recordemos que estamos dentro de la ergosfera, donde pueden existir trayectorias de energía negativa.

Penrose propuso que uno de los fragmentos, por ejemplo \(B\), podría adquirir una energía

$$
E_B<0
$$

y caer hacia el interior del agujero negro.

<p style="text-align: center;">
  <img src="/images/gabri-gravedad/Kerr2.jpeg" alt="Esquema del proceso de Penrose." style="display: block; max-width: 100%; height: auto; margin: 0 auto;">
</p>
<p style="text-align: center; color: var(--muted); font-size: 0.92rem;">
  Esquema del proceso de Penrose.
</p>

En ese caso, la conservación de la energía implica que

$$
E_A=E_0-E_B.
$$

Y, puesto que \(E_B<0\), necesariamente se cumple

$$
\boxed{E_A>E_0.}
$$

¡Acabamos de conseguir que una partícula escape con más energía de la que tenía inicialmente!

El fragmento \(A\) puede regresar al infinito transportando una cantidad de energía superior a la que introdujimos originalmente.

Por supuesto, el proceso no crea energía de la nada. La energía adicional procede de la rotación del agujero negro, que pierde masa y momento angular al absorber el fragmento de energía negativa.

Este es el **proceso de Penrose**.

### ¿Cuánta energía podemos extraer?

Para cuantificar la ganancia podemos definir la eficiencia del proceso como

$$
\eta=\frac{E_A-E_0}{E_0}.
$$

Utilizando la conservación de la energía,

$$
E_A-E_0=-E_B,
$$

obtenemos

$$
\boxed{\eta=-\frac{E_B}{E_0}.}
$$

Como \(E_B<0\), la eficiencia es positiva.

En el proceso original de Penrose, considerando la desintegración de una partícula en dos fragmentos y un agujero negro de Kerr en rotación extrema, la eficiencia máxima es

$$
\boxed{\eta_{\max}=\frac{\sqrt2-1}{2}\approx0.207.}
$$

Es decir, **podemos obtener una ganancia de energía de hasta aproximadamente un 20,7 % respecto a la energía inicial de la partícula**.

Si, por ejemplo, introdujéramos una partícula con energía

$$
E_0=100\ \mathrm J,
$$

podríamos recuperar idealmente hasta

$$
E_A\approx120.7\ \mathrm J.
$$

Los \(20.7\ \mathrm J\) adicionales procederían de la energía de rotación del agujero negro.

Este límite corresponde al proceso original bajo condiciones ideales. Existen otras variantes, como el proceso de Penrose colisional o el magnético, que pueden presentar eficiencias diferentes. Además, conseguir una desintegración con las velocidades relativas necesarias resulta extremadamente difícil desde el punto de vista físico.

### ¿De verdad pierde energía el agujero negro?

Podemos demostrarlo utilizando las leyes de conservación.

Además de la energía, un agujero negro de Kerr posee momento angular \(J\).

Como consecuencia de la simetría axial del espacio-tiempo, existe otro vector de Killing,

$$
\psi^\mu=\left(\frac{\partial}{\partial\phi}\right)^\mu,
$$

que permite definir el momento angular conservado de una partícula:

$$
L=p_\mu\psi^\mu.
$$

En coordenadas de Boyer-Lindquist, las dos cantidades conservadas toman la forma

$$
E=-p_t,\qquad L=p_\phi.
$$

Cuando una partícula de energía negativa atraviesa el horizonte, el cambio de energía del agujero negro viene dado por

$$
\Delta(Mc^2)=E_B<0.
$$

Por tanto,

$$
\boxed{\Delta M=\frac{E_B}{c^2}<0.}
$$

Es decir, la masa del agujero negro disminuye.

Además, el fragmento absorbido posee momento angular negativo respecto al sentido de rotación del agujero negro, por lo que

$$
\Delta J=L_B<0.
$$

De este modo, el agujero negro pierde tanto energía como momento angular.

Existe, sin embargo, una restricción fundamental. La energía y el momento angular de la partícula absorbida deben satisfacer

$$
E_B-\Omega_H L_B\geq0,
$$

donde \(\Omega_H\) es la velocidad angular del horizonte.

En unidades geométricas,

$$
\Omega_H=\frac{a}{r_+^2+a^2}.
$$

Esta desigualdad garantiza que el proceso es compatible con las propiedades físicas del horizonte de sucesos y, en particular, con el teorema de aumento de su área.

Puesto que \(E_B<0\), también debe cumplirse \(L_B<0\) (tomando positivo el sentido de rotación del agujero negro).

Por tanto, **la extracción de energía está necesariamente acompañada de una disminución del momento angular del agujero negro**.

En cierto sentido, estamos frenando su rotación.

Y esto nos lleva a una última pregunta.

### ¿Podemos extraer toda la energía de rotación de un agujero negro?

Un agujero negro de Kerr posee una cantidad de energía asociada a su momento angular.

Para estudiar cuánta energía podemos extraer, es útil introducir el concepto de *masa irreducible*, \(M_{\mathrm{irr}}\).

Esta cantidad está relacionada con el área \(A\) del horizonte de sucesos mediante

$$
\boxed{A=\frac{16\pi G^2}{c^4}M_{\mathrm{irr}}^2.}
$$

El teorema del área de Hawking establece que, bajo las hipótesis clásicas habituales, el área total de los horizontes de sucesos no puede disminuir.

En consecuencia, la masa irreducible de un agujero negro no puede reducirse mediante un proceso clásico de extracción de energía.

Para un agujero negro de Kerr, la masa irreducible viene dada por

$$
M_{\mathrm{irr}}=M\sqrt{\frac{1+\sqrt{1-\chi^2}}{2}},
$$

donde

$$
\chi=\frac{cJ}{GM^2}
$$

es el parámetro adimensional de rotación, que satisface

$$
0\leq|\chi|\leq1.
$$

En el caso de un agujero negro sin rotación, \(\chi=0\), obtenemos

$$
M_{\mathrm{irr}}=M.
$$

Por tanto, no existe energía de rotación disponible para ser extraída.

En cambio, para un agujero negro en rotación extrema, \(|\chi|=1\), resulta que

$$
M_{\mathrm{irr}}=\frac M{\sqrt2}.
$$

La cantidad máxima de energía que podríamos extraer, suponiendo un proceso ideal reversible que mantuviera constante la masa irreducible, sería

$$
E_{\mathrm{ext}}=(M-M_{\mathrm{irr}})c^2.
$$

En el caso extremo,

$$
E_{\mathrm{ext}}=\left(1-\frac1{\sqrt2}\right)Mc^2.
$$

Es decir,

$$
\boxed{E_{\mathrm{ext}}\approx0.293Mc^2.}
$$

¡Hasta un **29,3 % de la energía total asociada a la masa de un agujero negro en rotación extrema** podría extraerse, en principio, aprovechando su rotación!

Conviene distinguir este porcentaje del 20,7 % que hemos obtenido anteriormente. El primero es el límite ideal de energía rotacional total disponible en un agujero negro extremo; el segundo corresponde a la ganancia máxima en un único evento del proceso original de Penrose, bajo las condiciones especificadas. No son dos eficiencias del mismo tipo.

Para apreciar la magnitud del resultado, consideremos un agujero negro con una masa igual a diez veces la masa del Sol,

$$
M=10M_\odot.
$$

Como

$$
M_\odot\approx1.99\times10^{30}\ \mathrm{kg},
$$

tenemos

$$
Mc^2\approx1.79\times10^{48}\ \mathrm J.
$$

Por tanto, la energía rotacional máxima extraíble sería aproximadamente

$$
\boxed{E_{\mathrm{ext}}\approx5.2\times10^{47}\ \mathrm J.}
$$

Una cantidad extraordinaria.

Naturalmente, esto no significa que podamos construir una central energética alrededor de un agujero negro y recuperar fácilmente toda esa energía. Estamos hablando de un límite teórico, y los procesos físicos reales presentan restricciones adicionales.

Pero el resultado es inequívoco: **la relatividad general permite extraer energía de rotación de un agujero negro sin violar ninguna ley de conservación**.

---

## Conclusiones

Hemos comenzado nuestro viaje con una nave espacial que se acerca a Júpiter y hemos terminado explorando una de las regiones más extremas del universo: la ergosfera de un agujero negro en rotación.

A primera vista, la asistencia gravitacional y el proceso de Penrose parecen fenómenos completamente distintos. El primero puede explicarse mediante la mecánica newtoniana, mientras que el segundo requiere recurrir a la geometría del espacio-tiempo descrita por la relatividad general.

Sin embargo, existe una conexión conceptual entre ambos.

En una asistencia gravitacional, una nave puede ganar energía a costa de modificar ligeramente el movimiento orbital de un planeta. El intercambio depende de la geometría del encuentro y del sistema de referencia desde el que describimos el movimiento.

En el proceso de Penrose, una partícula puede escapar de la ergosfera con más energía de la que tenía inicialmente, siempre que otra partícula con energía conservada negativa sea absorbida por el agujero negro. La energía adicional procede de la rotación del propio agujero negro.

En ambos casos, la conservación de la energía permanece intacta.

Y es que, aunque pueda parecer sorprendente, **extraer energía de un sistema gravitatorio no significa crear energía, sino encontrar una manera de transferirla**.

Esta es precisamente una de las ideas más hermosas de la física: mecanismos que, a primera vista, parecen imposibles terminan siendo consecuencias perfectamente legítimas de sus leyes fundamentales.

Así que ya sabéis la respuesta a las preguntas con las que comenzábamos.

¿Podemos robarle energía a un planeta? Sí, y llevamos décadas haciéndolo.

¿Podemos robársela a un agujero negro? También, al menos en principio, y la relatividad general nos explica exactamente cómo.

La gravedad no nos regala energía. Pero, si sabemos aprovecharla, puede ayudarnos a conseguirla de los lugares más insospechados del universo.

---

## Referencias

- NASA, *Basics of Space Flight*, capítulo 4, «Trajectories»: [https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/](https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/)
- Agencia Espacial Europea, «What are gravity assists?»: [https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists](https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists)
- Schnittman, J. D. (2018), *The Collisional Penrose Process*, *General Relativity and Gravitation*, 50: [https://pmc.ncbi.nlm.nih.gov/articles/PMC6894168/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6894168/)
- Stuchlík, Z., Kološ, M. y Tursunov, A. (2021), «Penrose Process: Its Variants and Astrophysical Applications», *Universe* 7(11), 416: [https://www.mdpi.com/2218-1997/7/11/416](https://www.mdpi.com/2218-1997/7/11/416)
- Christodoulou, D. (1970), «Reversible and Irreversible Transformations in Black-Hole Physics», *Physical Review Letters* 25.
