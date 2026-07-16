---
title: ¿Por qué las palomitas revientan en el microondas?
author: Duvier Suárez Fontanella
date: 2026-05-21
layout: articles
status: published
category: Termodinámica
tags:
  - física
  - termodinámica
  - microondas
  - alimentos
summary: ¿Alguna vez te has preguntado por qué explotan las palomitas, de dónde sale su forma y por qué saben tan bien? Ponte cómodo, vamos a mirar la ciencia que se esconde dentro de un grano de maíz.
image: images/palomitas.png
featured_image: images/palomitas_1.jpeg
certificate: true
---

[TOC]



## Estructura del grano

Empecemos por el protoganista de este fenómeno: el grano de maíz (*Zea mays everta*). Cada uno de ellos puede ser dividido en tres partes principales: El **endospermo**, que contiene almidón y un poco de agua (apriximadamente entre un 13 y 15 % de su masa); el **pericarpio**, una cáscara muy dura e impermeable; y el **germen** --no, no ese tipo de germen peligroso para la salud en el que estás pensando, en este caso es simplemente la parte viva de la semilla. El secreto de las palomitas está en esa pequeña cantidad de agua atrapada dentro del grano. Cuando se calienta, genera vapor y presión hasta que la cáscara no puede resistir más y explota. 

Si querías la versión corta puedes parar aquí, pero si sigues curioso y deseas enterarte de todos los detalles, déjame explicártelos en las próximas secciones.

---

## El efecto del microondas

El horno microondas opera típicamente a una frecuencia de 2.45 GHz, correspondiente a una longitud de onda de 12.2 cm. Esta radiación electromagnética interactúa con los dipolos eléctricos del agua mediante el proceso de *calentamiento dieléctrico*. Las moléculas de agua rotan en fase con el campo alterno, generando disipación térmica a escala molecular.

<!--El flujo de calor neto puede describirse de forma simplificada mediante la ecuación de difusión del calor:

$$
\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + Q_{\text{abs}}
$$

donde ρ es la densidad, c<sub>p</sub> el calor específico, k la conductividad térmica y Q<sub>abs</sub> la potencia volumétrica absorbida del campo electromagnético.-->

Al subir la temperatura, el agua dentro del grano se convierte en vapor y la presión interna aumenta como en estudiante de doctorado a puntode entregar la tesis (comentario inecesario quizás, pero, al fin y al cabo, escribir para esta página cumple también la función de entretenerme). En cualquier caso, la presión interna del grano depende de la temperatura según la ecuación de Clausius–Clapeyron:

$$
\frac{dP_v}{dT} = \frac{L P_v}{R T^2},
$$

cuya integración da lugar a:

$$
\ln \left( \frac{P_v}{P_0} \right) = - \frac{L}{R} \left( \frac{1}{T} - \frac{1}{T_0} \right),
$$

donde $L = 2.26×10^{6}$ J/kg es el calor latente de vaporización del agua y $R = 8.31$ J/mol·K la constante de los gases ideales. Calculando la presión dentro del grano para un valor típico de temperatura dentro del horno de $453$ K ($≈ 180$ °C) y  $T_0 = 373$ K, $P_0 = 1$ atm, se obtiene:

$$
P_v(453~\text{K}) \approx 9~\text{atm}
$$

que coincide con la presión crítica de ruptura observada experimentalmente para el pericarpio ($P_{rupt} ≈ 9–10$ atm). 

---

## Explosión y expansión adiabática

Una vez que la presión interna excede la resistencia del pericarpio ($P_{rupt} ≈ 9–10$ atm), se produce una fractura súbita. El vapor se expande rápidamente, realizando trabajo sobre el almidón circundante y provocando una expansión casi adiabática del gas. 

Si suponemos una expansión adiabática reversible para el vapor de agua:

$$
P V^{\gamma} = \text{constante},
$$

donde $γ ≈ 1.33$ para el vapor de agua, y, en consecuencia, el trabajo realizado por el gas durante la expansión es:

$$
W = \frac{P_i V_i - P_f V_f}{\gamma - 1}.
$$

Tomando $P_i = 9$ atm, $P_f = 1$ atm y considerando que el volumen final del gas es unas $V_f/V_i ≈ 10$ veces mayor, se obtiene un trabajo del orden de:

$$
W \sim 10^{-3}~\text{J}.
$$

A pesar de parecer pequeño, este trabajo genera en las moléculas dentro del grano velocidades de expansión del orden de varios metros por segundo, suficientes para inflar el almidón y solidificarlo instantáneamente por enfriamiento.

---
## Energía total liberada

El contenido energético total asociado al cambio de fase del agua en un solo grano es:

$$
E = m L
$$

donde $m$ es la masa de agua. Si $m ≈ 10^{-5}$ kg , entonces:

$$
E = 2.26 \times 10^{6} \times 10^{-5} = 22.6~\text{J}.
$$

De esta energía, una pequeña fracción se convierte en trabajo mecánico y sonido; el resto se disipa en forma de calor.

---

## Factores que impiden el estallido

Por nuestra experiencia, sabemos que siempre hay un par de granitos que no revientan (*“old maids”*). Esto peude deberse a una o varias de las siguientes causas:

- Bajo contenido de humedad en el grano (menos de un 10%), insuficiente para generar la presión crítica.  
- Fisuras microscópicas en el pericarpio, que permiten la fuga de vapor antes de alcanzar $P_{rupt}$.  
- Distribución térmica no uniforme que evita una presurización homogénea.

---

## Eficiencia termodinámica aproximada

Si un horno microondas de potencia $P = 800$ W opera durante $t = 120$ s:

$$
E_{\text{in}} = P t = 9.6 \times 10^{4}~\text{J}.
$$

Una bolsa de $100$ g contiene aproximadamente $N = 3000$ granos.  
Si cada uno libera $≈ 20$ J en el proceso de vaporización:

$$
E_{\text{total}} = N \times 20~\text{J} = 6.0 \times 10^{4}~\text{J}.
$$

Por tanto, la eficiencia energética del proceso es:

$$
\eta = \frac{E_{\text{total}}}{E_{\text{in}}} \approx 0.6
$$

es decir, un rendimiento del 60%, notablemente alto para un proceso de cocción doméstico basado en calentamiento dieléctrico.

---

## Lo que aprendemos de las palomitas

El estallido de las palomitas es un ejemplo fascinante de cómo principios de la física macroscópica --transferencia de calor, termodinámica del cambio de fases, elasticidad de materiales y dinámica de gases-- se manifiestan en un fenómeno tan delicioso como cotidiano. Cada grano actúa como una *microcápsula de presión* donde el agua, confinada, pasa de líquido a vapor hasta romper la envoltura, produciendo ese modesto sonido (*pop*) en el que convergen varias ramas de la física.  

---

