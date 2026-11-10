---
title: "Acertijos sobre probabilidades en contextos de indexicalidad y auto-localización — Acto I"
author: "Gabriel J. Gil Pérez"
date: 2026-11-10 # pendiente de confirmar la fecha de publicación
layout: articles
slug: prueba-gabrielJ
status: hidden
category: Filosofía # confirmar categoría admitida por el sitio
tags:
  - probabilidad
  - filosofía
  - autolocalización
  - bella durmiente
summary: "¿Saber qué día es hoy puede alterar mi confianza en que una moneda justa cayó cara o cruz?"
image: images/gabrielgil-bella_durmiente/TOC_bella_durmiente.jpeg
certificate: false
---

[TOC]


## Prólogo

Existen enunciados que son verdaderos o falsos dependiendo de quién los dice, dónde los dice y cuándo los dice. (Calma, calma, que nada de esto tiene que ver con el tan llevado y traído relativismo sobre la verdad. Se trata de algo mucho más mundano.) Por ejemplo, la afirmación «viví aquí el año pasado» es cierta solo si quien la pronuncia en efecto vivió en el lugar donde se pronuncia el año anterior. Nótese el contraste con expresiones como «Gabriel vivió en Alessandria en el año 2025», cuyo valor de verdad es independiente de quién, dónde y cuándo la enuncie. Por otro lado, conviene precisar que la distinción entre el valor de verdad que asumen «viví aquí el año pasado» y «Gabriel vivió en Alessandria en el año 2025» no deriva de subjetividad alguna. Que yo viviera aquí hace un año es un hecho objetivo, verificable, que usted también avalaría si se le proporcionara la evidencia relevante. De acuerdo con esos datos, afirmar que «viví aquí el año pasado» sería correcto en mi caso e incorrecto en el caso de quien visita hoy la ciudad por primera vez.

Este fenómeno se conoce como indexicalidad y ha dado mucho de qué hablar en lingüística y filosofía del lenguaje. En última instancia, la indexicalidad en el lenguaje tiene su origen en las creencias de auto-localización o auto-ubicación de nuestra mente, que pueden ser verdaderas o falsas según la biografía y situación espacio-temporal del implicado. En esta serie de *Napkin Notes* que inicia este artículo se abordan tres experimentos mentales en los que las creencias de auto-localización comprometen nuestra noción de probabilidad, así como el uso que hacemos de ella en estrategias de deliberación y confirmación. El objetivo es preparar el terreno para una discusión de una objeción a la interpretación de muchos mundos de la mecánica cuántica, que parece ser la opción más económica para resolver el problema de la medición. Quédense para el primer acto:

## Acto I – La bella durmiente y el cálculo de probabilidades

Imagínese que la bella durmiente se somete voluntariamente al siguiente experimento científico. Se le administra un somnífero el domingo y, según el resultado del lanzamiento de una moneda justa, se decide cuántas veces y cuándo se la despertará en el transcurso de la semana. Si la moneda cae cara, se le despertará solo el lunes. Si la moneda cae cruz, se le despertará el lunes y el martes. En cada despertar se sigue el mismo protocolo: se le hace una pregunta y se le devuelve al sueño utilizando un somnífero diferente que produce amnesia de corto plazo. Como consecuencia, cuando la bella durmiente despierta el lunes o el martes, no sabe si ya la despertaron antes, pero recuerda haberse sometido al experimento y haber sido informada de todas sus reglas. El experimento finaliza cuando se le despierta el miércoles. La pregunta que se le hace en cada despertar es: *¿cuál es tu grado de confianza en que la moneda cayó cara?*

¿Qué debería responder la bella durmiente? ¿Por qué? Tómese el lector unos minutos para elaborar una respuesta. La única pista es que, con grado de confianza en una cierta proposición, entenderemos la probabilidad que estima el agente, en este caso la bella durmiente, de que dicha proposición sea verdadera. En general, hay dos posibles respuestas con buena justificación racional. Pero no nos adelantemos, porque aquí está la enjundia del problema.

### Respuesta I: el argumento del terciero

La bella durmiente puede razonar de la siguiente manera: «Si la moneda cayó cruz, entonces tengo igual confianza en que hoy es lunes como en que hoy es martes.» En términos matemáticos, la probabilidad condicional de que sea lunes, dado que la moneda cayó cruz, es igual que la probabilidad de que sea martes, dada la misma condición; en notación,

$$
P\left( \text{lunes} \mid \text{cruz} \right) = P\left( \text{martes} \mid \text{cruz} \right)
$$

De aquí, siguiendo la definición de la probabilidad condicional P( A | B ) = P( A & B ) / P( B ), y cancelando el denominador común, se obtiene que:

$$
P\left( \text{lunes} \cap \text{cruz}\right) = P\left( \text{martes} \cap \text{cruz} \right) \tag{1}
$$

Es decir, la probabilidad de que hoy sea lunes y la moneda haya caído cruz es igual a la probabilidad de que sea martes y la moneda haya caído cruz.

Ahora bien, supongamos que la bella durmiente se despierta el lunes y se le comunica qué día es. Entonces puede hacer otro razonamiento: «Siendo lunes, tengo igual confianza en que la moneda cayó cara como en que cayó cruz.» Esto quiere decir que la probabilidad condicional de que la moneda haya caído cara, dado que es lunes, es igual que la probabilidad de que haya caído cruz, dada la misma condición; o sea,

$$
P\left( \text{cara} \mid \text{lunes} \right) = P\left( \text{cruz} \mid \text{lunes} \right)
$$

Otra vez, siguiendo la definición de la probabilidad condicional, la expresión anterior nos conduce a:

$$
P\left( \text{lunes} \cap \text{cara} \right) = P\left( \text{lunes} \cap \text{cruz} \right) \tag{2}
$$

En palabras, diríamos que la probabilidad de que hoy sea lunes y la moneda haya caído cara es igual a la probabilidad de que sea lunes y la moneda haya caído cruz.

De [1] y [2], se obtiene que

$$
P\left( \text{lunes} \cap \text{cara} \right) = P\left( \text{lunes} \cap \text{cruz} \right) = P\left( \text{martes} \cap \text{cruz} \right) \tag{3}
$$

lo cual refleja que *lunes & cara*, *lunes & cruz* y *martes & cruz* tendrían igual probabilidad a los ojos de la bella durmiente. Y como los eventos anteriores agotan el espacio de posibilidades,

$$
P\left( \text{lunes} \cap \text{cara} \right) + P\left( \text{lunes} \cap \text{cruz} \right) + P\left( \text{martes} \cap \text{cruz} \right) = 1 \tag{4}
$$

Por lo tanto, la probabilidad que asigna la bella durmiente a la proposición de interés es P(cara) = ⅓. Ese debería ser entonces su grado de confianza en que la moneda cayera cara. Quien defiende este razonamiento se conoce como *terciero* <a class="nn-cite" href="#ref-1">[1]</a>.

### Respuesta II: el argumento del mediero

Más corta e intuitiva. La probabilidad de que la moneda cayera cara es P(cara) = ½. ¡Siempre lo fue! Si la bella durmiente se comporta racionalmente, antes de dormirse el domingo y antes de que se lance la moneda, debería asignar un grado de confianza en que la moneda caerá cara igual a dicha probabilidad. Más aún, dado que la bella durmiente no adquiere información relevante cuando despierta, siendo todos sus despertares idénticos dentro del experimento, ese grado de confianza debería mantenerse igual a ½ en cada posible entrevista. Como diría el conejo de la suerte: eso es todo, chicos. En el debate sobre este tema, esta es la postura del *mediero* <a class="nn-cite" href="#ref-2">[2]</a>.

¿Y entonces? ¿Quién tiene razón? ¿Con quién está el lector?

Lamento revelar que el debate entre tercieros y medieros no está resuelto y que hay literatura técnica que aún lo explora.<a class="nn-cite" href="#ref-3">[3]</a><a class="nn-cite" href="#ref-4">[4]</a> De hecho, no solo se discuten estas dos posiciones, sino al menos otras dos que obviaré en este artículo para mantener el foco en la ambigüedad que surge al asignar probabilidades en un contexto de auto-localización. Baste decir que el mediero aquí representado es solo un arquetipo dentro de un grupo heterogéneo, y que hay quien considera que el terciero y el mediero responden correctamente a preguntas diferentes. El lector interesado puede consultar la bibliografía especializada, que se referencia al final del artículo.

A continuación, damos otra mirada al problema para sembrar la duda en ese lector más pragmático que suele decantarse por el mediero.

### La defensa del terciero

 Llegado a este punto, el terciero despliega dos estrategias. Por un lado, refuerza su argumento apelando solo a la intuición, nada de álgebra. Por el otro —y por aquello de que la mejor defensa es el ataque— encuentra consecuencias contraintuitivas de la respuesta del mediero.

Vamos con la primera línea de fuego.<a class="nn-cite" href="#ref-3">[3]</a>

Supongamos que los investigadores permiten a la bella durmiente repetir el experimento cuanto quiera antes de formarse una idea de cómo debería contestar a la pregunta sobre su grado de confianza en que la moneda cayera cara. De común acuerdo, se decide efectuar una batería de 1000 réplicas del experimento original para colectar suficientes datos. (1000 experimentos, mil semanas, 19,17 años: eso es compromiso con la ciencia). Los nuevos experimentos procederán de la misma manera que el original, excepto por un detalle. En lugar de formular la difícil pregunta a la bella durmiente, en cada despertar los investigadores le informarán si la moneda cayó cara o cruz para que la introduzca en una base de datos a la que tendrá acceso al concluir el último de los 1000 experimentos.

Sin perder generalidad en lo esencial, supondremos además lo que sucedió en esos mil experimentos: cayeron exactamente 500 caras y 500 cruces. Al final de la serie, la base de datos de la bella durmiente registra 1500 despertares, 500 de los cuales son despertares-cara y el resto son despertares-cruz; o sea, el doble de despertares-cruz que de despertares-cara. De modo que la bella durmiente deduce que, ante un despertar cualquiera, su confianza en que salió cruz debería duplicar su confianza en que salió cara. Siendo los dos resultados exhaustivos, su grado de confianza en que salió cara debería ser ⅓ —gústele a quien le guste y pésele a quien le pese.

Supongamos que los investigadores le ofrecieran a la bella durmiente participar en una apuesta en cada despertar de la serie de experimentos: recibe un 1€ si adivina el resultado del lanzamiento de la moneda y debe abonar 1€ en caso contrario. La bella durmiente, ignorando qué día es, obtendría ganancias si apuesta siempre por cruz y pérdidas si apuesta siempre por cara. En efecto, si eligiera siempre cruz cobraría 1000€ y pagaría 500€, correspondientes a los 1000 despertares-cruz y 500 despertares-cara, para una ganancia neta de 500€. Si eligiera siempre cara cobraría 500€ y pagaría 1000€, para una pérdida neta de 500€. El terciero puede recomendar la estrategia ganadora sobre la base de los grados de confianza de la bella durmiente, P( cruz ) = 2 P( cara ) = ⅔, a diferencia del mediero, para el cual P( cara ) = P( cruz ) = ½.

#### Segunda línea de fuego.

Hay una consecuencia indeseable de la respuesta del contrario. El mediero considera que

$$
P\left( \text{cara} \right) = P\left( \text{cruz} \right) = \frac{1}{2} \tag{5}
$$

Como la bella durmiente solo se despierta una vez cuando la moneda cae cara

$$
P\left( \text{cara} \cap \text{lunes} \right) = \frac{1}{2} \tag{6}
$$

y como se despierta dos veces cuando cae cruz

$$
P\left( \text{cruz} \cap \text{lunes} \right) + P\left( \text{cruz} \cap \text{martes} \right) = \frac{1}{2} \tag{7}
$$

Usando la expresión [7], y la [1], que el mediero también acepta, se obtiene que

$$
P\left( \text{cruz} \cap \text{lunes} \right) = \frac{1}{4} \tag{8}
$$

*Cara & lunes* y *cruz & lunes* son eventos excluyentes que agotan el espacio de posibilidades del lunes, por lo que

$$
P\left( \text{lunes} \right) =  P\left( \text{cara} \cap \text{lunes} \right) + P\left( \text{cruz} \cap \text{lunes} \right)
$$

Expandiendo la probabilidad condicional de cara dado lunes,

$$
P\left( \text{cara} \mid \text{lunes} \right) = \frac{P\left( \text{cara} \cap \text{lunes} \right)}{P\left( \text{cara} \cap \text{lunes} \right) + P\left( \text{cruz} \cap \text{lunes} \right)} = \frac{2}{3} \tag{9}
$$

Y he aquí el problema: para sostener que P( cara ) = 1/2 el mediero debe aceptar que P( cara | lunes ) = 2/3.<a class="nn-cite" href="#ref-2">[2]</a> Pero… ¿cómo puede ser? Saber que es lunes no debería hacer más probable que la moneda cayera cara en vez de cruz. Al contrario, ¡debería ser irrelevante! Tampoco debería sesgar en modo alguno el grado de confianza de la bella durmiente en uno de los resultados del lanzamiento de la moneda, precisamente porque el despertar del lunes es consistente con ambos.

### Auto-localización y probabilidades

Nótese que a pesar del desacuerdo, tanto medieros como tercieros consideran que las creencias de auto-localización desempeñan un papel esencial en la descripción del problema —en los dos casos, de manera contraria a la intuición—. Por ejemplo, ya hemos visto que el mediero debería aceptar que P( cara | lunes ) = ⅔. En otras palabras, saber que es lunes (o sea, tener *certeza* de su auto-localización temporal), cambia la confianza inicial de la bella durmiente en que la moneda cayó cara, i.e., P( cara ) = ½. El terciero también acepta que P( cara ) = ⅓ ≠ P( cara | lunes ) = ½, como también acepta que el grado de confianza de la bella durmiente antes de que se lanzara la moneda, el domingo, debió haber sido ½. Por lo tanto, según el terciero, es la *incertidumbre* de su auto-localización temporal lo que altera el modo en que la bella durmiente modula su confianza en un resultado u otro del lanzamiento de la moneda.

Con el objetivo de ilustrar mejor la forma en que opera la auto-localización temporal para el terciero, introduciremos otro participante en el experimento, al que llamaremos “el príncipe”, que es inmune al amnésico utilizado por los investigadores para borrar la memoria de cada despertar y conoce de dicha inmunidad. La diferencia entre el príncipe y la bella durmiente es precisamente que él siempre sabe si es lunes o martes, mientras que ella no. Pongamos que el príncipe también se somete a 1000 experimentos para recoger datos. A diferencia de la bella durmiente, cada vez que la moneda cae cruz y es martes, el príncipe evita registrar el resultado del lanzamiento. ¡Ya lo hizo el lunes! La bella durmiente no puede darse ese lujo porque no sabe si es lunes o martes, y por ende, desconoce si es la primera o la segunda vez que estaría introduciendo cruz en la base de datos. Obviamente, al finalizar la batería de experimentos de prueba, el príncipe obtiene que la frecuencia relativa de cara es ½. La bella durmiente coincidiría con él si después del último experimento eliminara de un teclazo la mitad de las realizaciones de cruz registradas en su base de datos. Claro está, esto afectaría la pregunta que realmente le interesa contestar, que es: *¿cuál es tu grado de confianza en que la moneda cayó cara?* Para responder correctamente, la bella durmiente no debe calcular la frecuencia relativa con que la proposición “la moneda cayó cara el domingo” (P1) es cierta —que es lo que estaría haciendo el príncipe— sino la frecuencia relativa con que la proposición “hoy sé que la moneda cayó cara el domingo” (P2) lo es. La primera proposición tiene frecuencia relativa ½ debido a que P1 constituye la misma proposición el lunes o el martes. En cambio, “hoy sé que la moneda cayó cruz el domingo” (P3) se convierte en “el lunes sé que la moneda cayó cruz el domingo” el lunes y en “el martes sé que la moneda cayó cruz el domingo” el martes, dos proposiciones diferentes que contribuyen a la frecuencia relativa total de P3.

Cuando preguntan al príncipe el lunes, que lleva registro de la frecuencia relativa de P1, su grado de confianza asume el valor ½. Por el contrario, cuando le preguntan a la bella durmiente, que se concentra en la frecuencia relativa de P2, su grado de confianza resulta ⅓. Nótese que el martes el príncipe tendría completa certeza de que la moneda cayó cruz el domingo porque ha adquirido información relevante al despertarse: el hecho de que es martes. No obstante, esta es una distinción que no viene a cuento en nuestro análisis. Lo importante es que, en igualdad de condiciones de incertidumbre sobre el resultado del lanzamiento de la moneda (o sea, en el despertar del lunes), el príncipe y la bella durmiente difieren en su grado de confianza en que la moneda cayó cara el domingo. El origen de esa diferencia está en que la bella durmiente ignora su localización temporal, mientras que el príncipe no.

*Continuará…*

## Referencias

<ol class="nn-references">
<li id="ref-1">Elga, A. «Self-Locating Belief and the Sleeping Beauty Problem». <em>Analysis</em>, 60(2), 143–147 (2000).</li>
<li id="ref-2">Lewis, D. «Sleeping Beauty: Reply to Elga». <em>Analysis</em>, 61(3), 171–176 (2001).</li>
<li id="ref-3">Titelbaum, M. G. «Ten Reasons to Care About the Sleeping Beauty Problem». <em>Philosophy Compass</em>, 8(11), 1003–1017 (2013).</li>
<li id="ref-4">Bourget, D. y Chalmers, D. J. (eds.). «Sleeping Beauty». <em>The 2020 PhilPapers Survey</em> (2020). <a href="https://survey2020.philpeople.org/survey/results/5170">https://survey2020.philpeople.org/survey/results/5170</a></li>
</ol>
