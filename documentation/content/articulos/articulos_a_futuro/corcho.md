---
title: "¿Qué tan rápido sale el corcho de una botella de champán?"
author: "Duvier Suárez Fontanella"
date: 2026-03-01
layout: articles
status: published
category: "Dinámica de Fluidos"
tags: ["física", "termodinámica", "champán", "supersónico"]
summary: "Cada descorche de champán es una pequeña demostración de física: gases comprimidos, termodinámica y un corcho convertido en proyectil. Un simple pop esconde presión interna, expansión rápida y un chorro de CO₂ que puede cruzar la barrera del sonido."
image: images/corcho.png
---

[TOC]



## ¿Un brindis o un experimento de balística doméstica?

¿Cuánta física cabe en el sonido de un corcho saliendo de una botella de champán?

Más de la que parece.

A primera vista, una botella de champán en la mesa parece un objeto pacífico: elegante, inmóvil, casi diplomático. Pero esa serenidad es engañosa. En su interior hay CO₂ disuelto, gas comprimido y una presión de varios bares esperando el menor descuido para convertir el brindis en una demostración de mecánica clásica.

Una botella típica de champán puede contener una presión interna del orden de **5–7 atm**, dependiendo de la temperatura, el contenido de CO₂ y las condiciones de almacenamiento. Un valor representativo es

$$
P_0 \sim 6\,\text{atm}.
$$

La presión relevante para empujar el corcho es la diferencia entre la presión interna y la atmosférica. Por tanto, si la botella está a unas 6 atm absolutas, la sobrepresión efectiva es aproximadamente

$$
\Delta P \sim 5\,\text{atm} \approx 5\times10^5\,\text{Pa}.
$$

Si se usa directamente una presión manométrica cercana a 6 bar, el resultado cambia poco para una estimación de orden de magnitud. En ambos casos estamos hablando de una fuerza considerable aplicada sobre un área muy pequeña.

Podemos estimar esa fuerza mediante

$$
F = \Delta P\,A,
$$

donde el área efectiva del cuello de la botella es

$$
A = \pi r^2,
$$

con un radio típico

$$
r \approx 9\times10^{-3}\,\text{m}.
$$

Entonces

$$
A \approx 2.54\times10^{-4}\,\text{m}^2.
$$

Usando $\Delta P \approx 5\times10^5\,\text{Pa}$,

$$
F \approx (5\times10^5)(2.54\times10^{-4}) \approx 130\,\text{N}.
$$

Si tomamos $\Delta P \approx 6\times10^5\,\text{Pa}$, obtenemos

$$
F \approx 150\,\text{N}.
$$

Así que una estimación razonable es

$$
F \sim 130\text{–}150\,\text{N}.
$$

Esto equivale aproximadamente al peso de una masa de **13–15 kg** concentrado sobre un área comparable al cuello de la botella. Es decir: no es exactamente un misil, pero tampoco es una sugerencia amable.

Y sí: todo eso está intentando expulsar el corcho hacia tu lámpara del salón.

---

## El corcho como proyectil educado, pero proyectil

Mientras el bozal metálico está puesto, el corcho permanece confinado. El sistema parece en equilibrio, pero no porque falte energía: simplemente la jaula metálica y la fricción están ganando la discusión.

Cuando se retira el bozal y se empieza a girar el corcho, la situación cambia. La fricción estática deja de sostener el sistema y el gas comprimido encuentra por fin una salida. El CO₂, que hasta entonces se comportaba con cierta compostura, decide recordar que la termodinámica también tiene carácter.

Durante los primeros instantes, la expansión del gas puede aproximarse como un proceso rápido y casi adiabático:

$$
P\,V^\gamma = \text{constante},
$$

donde $\gamma$ es el índice adiabático efectivo del gas. Para el CO₂, un valor típico cerca de temperatura ambiente es aproximadamente

$$
\gamma \approx 1.3.
$$

La aproximación adiabática tiene sentido porque el proceso ocurre en escalas de tiempo muy cortas. El gas se expande mucho más rápido de lo que puede intercambiar calor de forma eficiente con el entorno.

Durante los primeros milímetros de movimiento, la presión no cae instantáneamente a la atmosférica. Por eso podemos hacer una estimación muy simple del trabajo inicial:

$$
W \approx F_0\,\Delta x.
$$

Tomemos, por ejemplo,

$$
\Delta x \approx 0.02\,\text{m}.
$$

Con una fuerza inicial de orden

$$
F_0 \sim 130\text{–}150\,\text{N},
$$

obtenemos

$$
W \sim 2.6\text{–}3.0\,\text{J}.
$$

Si una fracción significativa de esa energía se convierte en energía cinética del corcho, podemos escribir

$$
\frac{1}{2}mv^2 \approx W.
$$

Para un corcho típico de masa

$$
m \approx 7\times10^{-3}\,\text{kg},
$$

la velocidad estimada sería

$$
v \approx \sqrt{\frac{2W}{m}}.
$$

Con $W \sim 3\,\text{J}$,

$$
v \approx \sqrt{\frac{6}{0.007}} \approx 29\,\text{m/s}.
$$

Esto equivale a unos

$$
v \approx 100\,\text{km/h}.
$$

Ahora bien: esta es una estimación idealizada. En una botella real hay pérdidas, fricción, deformación del corcho, rotación, disipación y una transferencia de energía que no es perfectamente eficiente. Por eso una velocidad más prudente para el corcho está en el rango

$$
10\,\text{m/s} \lesssim v \lesssim 30\,\text{m/s}.
$$

En condiciones especialmente desfavorables —botella caliente, agitada o mal manipulada—, el corcho puede acercarse a la parte alta de ese rango. Suficiente para ser gracioso en un cálculo, pero bastante poco gracioso si la trayectoria termina en un ojo.

---

## El gas sí se toma en serio lo de ser supersónico

El corcho puede salir rápido, pero normalmente no alcanza velocidades supersónicas. El gas, en cambio, juega en otra liga.

Cuando la presión interna es suficientemente alta, el CO₂ sale por el cuello de la botella mediante una expansión muy rápida. En estas condiciones puede aparecer **flujo ahogado**, es decir, un régimen en el que la velocidad del gas en la garganta alcanza la velocidad local del sonido:

$$
v_{\text{gas}} \approx c_s.
$$

Para CO₂, la velocidad del sonido depende de la temperatura. A temperatura ambiente se puede estimar como

$$
c_s \sim 260\,\text{m/s}.
$$

Durante el descorche, sin embargo, el gas se enfría bruscamente al expandirse. En el chorro frío que sale de la botella, la velocidad del sonido puede estar más cerca de

$$
c_s \sim 230\text{–}240\,\text{m/s}.
$$

Esto importa porque la expansión puede generar estructuras típicas de flujos supersónicos, como ondas de choque y discos de Mach. Dicho en lenguaje menos técnico: el corcho hace *pop*, pero el CO₂ intenta hacer una maqueta barata de una tobera de cohete.

Así que la frase correcta es:

**El corcho no suele ser supersónico; el gas que lo acompaña sí puede serlo.**

Y esa distinción es importante. Mezclar la velocidad del corcho con la velocidad del chorro de gas es como confundir una piedra lanzada con el escape de un motor: ambos salen del mismo drama, pero no con la misma dinámica.

---

## La botella como una cámara de expansión en miniatura

Podemos refinar un poco el modelo. A medida que el corcho avanza una distancia $x$, el volumen disponible para el gas aumenta. Si el área efectiva del cuello es $A$, el volumen pasa aproximadamente de $V_0$ a

$$
V(x) = V_0 + A x.
$$

Para una expansión adiabática idealizada,

$$
P(x) = P_0
\left(
\frac{V_0}{V_0 + A x}
\right)^\gamma.
$$

La fuerza sobre el corcho será entonces

$$
F(x) = P(x)\,A.
$$

La velocidad de salida tras recorrer una longitud efectiva $L$ puede estimarse mediante el trabajo realizado por esa fuerza:

$$
v =
\sqrt{
\frac{2}{m}
\int_0^L P(x)\,A\,dx
}.
$$

Este modelo ya muestra algo importante: la fuerza no permanece constante durante todo el movimiento. La presión cae a medida que el gas se expande, de modo que el corcho recibe un impulso fuerte al comienzo y luego una contribución decreciente.

Por eso el cálculo simple con

$$
W \approx F_0\,\Delta x
$$

sirve como estimación inicial, pero no debe interpretarse como una descripción exacta de todo el proceso.

En la práctica, para condiciones normales de apertura, una estimación razonable para el corcho es

$$
v \sim 10\text{–}30\,\text{m/s}.
$$

Valores alrededor de

$$
v \sim 30\,\text{m/s}
$$

ya corresponden a un descorche bastante energético. Por encima de eso entramos en escenarios más extremos, asociados a botellas calientes, agitadas o manipuladas sin demasiado cariño por la conservación del momento lineal.

---

## Temperatura: el verdadero villano elegante

La temperatura importa muchísimo.

A mayor temperatura, menor solubilidad del CO₂ en el líquido y mayor presión en el espacio de gas bajo el corcho. En términos prácticos:

$$
T \uparrow
\quad\Longrightarrow\quad
P \uparrow
\quad\Longrightarrow\quad
F \uparrow
\quad\Longrightarrow\quad
v \uparrow.
$$

Una botella fría tiende a ser más dócil. Una botella caliente es una negociación con un sistema presurizado que tiene muy poco interés en tus planes de Nochevieja.

También influyen otros factores:

- la rugosidad del corcho,  
- su deformación dentro del cuello,  
- la fricción estática inicial,  
- la cantidad de CO₂ disuelto,  
- el volumen del espacio de gas bajo el corcho,  
- si la botella ha sido agitada,  
- la geometría exacta del cuello.  

La fricción merece una mención especial. Antes de moverse, el corcho debe vencer una resistencia inicial. Si esa resistencia es grande, el sistema puede acumular más presión efectiva antes del despegue. Cuando finalmente cede, la liberación puede ser más brusca.

En otras palabras: cada botella tiene su personalidad. Algunas son discretas. Otras parecen haber leído demasiado sobre propulsión.

---

## Qué puede salir mal, además de la dignidad

Un corcho a decenas de metros por segundo tiene energía suficiente para causar lesiones. La energía cinética típica puede estimarse como

$$
E_k = \frac{1}{2}mv^2.
$$

Para $m = 0.007\,\text{kg}$ y $v = 20\,\text{m/s}$,

$$
E_k \approx 1.4\,\text{J}.
$$

Para $v = 30\,\text{m/s}$,

$$
E_k \approx 3.2\,\text{J}.
$$

No parece mucho si uno lo compara con escalas macroscópicas, pero concentrado en un impacto pequeño puede ser suficiente para producir hematomas, cortes o lesiones oculares. El ojo humano, lamentablemente, no está optimizado para recibir proyectiles festivos.

Por eso el consejo físico y socialmente responsable es simple:

**Nunca apuntes la botella hacia una persona, un animal, una ventana o un televisor que te haya costado dinero.**

La forma segura de abrir una botella no consiste en “dejar volar” el corcho, sino en sujetarlo con firmeza, girar lentamente la botella y permitir que el gas salga de forma controlada. El sonido ideal no debería ser una explosión teatral, sino un suspiro elegante.

Menos cañón napoleónico, más mecánica de fluidos civilizada.

---

## Entonces, ¿qué tan rápido sale?

Una respuesta razonable es:

$$
v_{\text{corcho}} \sim 10\text{–}30\,\text{m/s},
$$

es decir, aproximadamente

$$
35\text{–}110\,\text{km/h}.
$$

El extremo superior corresponde a situaciones energéticas, no al descorche tranquilo de una botella bien enfriada. Para una apertura controlada, la velocidad puede ser mucho menor, porque precisamente se evita que el corcho salga disparado.

El gas, en cambio, puede alcanzar velocidades cercanas o superiores a la velocidad local del sonido:

$$
v_{\text{gas}} \sim 230\text{–}300\,\text{m/s}.
$$

Así que el descorche de champán combina dos fenómenos distintos:

- un **corcho acelerado** por presión interna,  
- un **chorro de CO₂** que puede entrar en régimen sónico o supersónico.  

La próxima vez que brindes, recuerda: no estás simplemente abriendo una botella. Estás liberando un sistema presurizado, resolviendo una miniatura de dinámica de gases y asistiendo al lanzamiento de un microproyectil carbónico cortesía de la fermentación.

Salud, pero con la botella apuntando en la dirección correcta.

---

## Apéndice: valores típicos de referencia

- **Presión interna:** 5–7 atm/bar, dependiendo de temperatura y estilo del vino.  
- **Sobrepresión efectiva:** aproximadamente 4–6 atm respecto al exterior.  
- **Radio efectivo del cuello:** $r \sim 9\,\text{mm}$.  
- **Área efectiva:** $A \sim 2.5\times10^{-4}\,\text{m}^2$.  
- **Fuerza inicial sobre el corcho:** $F \sim 130\text{–}150\,\text{N}$.  
- **Masa típica del corcho:** 6–8 g.  
- **Trabajo inicial estimado:** $W \sim 2\text{–}3\,\text{J}$.  
- **Velocidad típica del corcho:** $v \sim 10\text{–}30\,\text{m/s}$.  
- **Velocidad alta razonable:** alrededor de $30\,\text{m/s}$, equivalente a unos $100\,\text{km/h}$.  
- **Velocidad del sonido en CO₂:** aproximadamente $230\text{–}260\,\text{m/s}$, según temperatura.  
- **Velocidad del chorro de gas:** puede alcanzar régimen sónico o supersónico, del orden de $230\text{–}300\,\text{m/s}$.  

---
