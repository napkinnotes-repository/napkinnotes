---
title: "¿Una moneda al aire decide Mundiales?: cómo la estadística se puede usar para lo que uno quiera si la muestra es pequeña"
author: David Figueruelo Hernán
date: 2026-06-25
layout: articles
slug: la-moneda-que-no-queria-decidir-un-mundial
status: published
category: Estadística
tags:
  - fútbol
  - mundial 2026
  - penaltis
  - estadística
  - probabilidad
summary: En una tanda de penaltis, ganar el sorteo parece comprar una ventaja. Pero los Mundiales cuentan una historia bastante menos clara.
image: images/penaltis-mundial-moneda.png
---

[TOC]



## El aire ya ha hablado... ahora soñemos

Si bien en [el artículo de hace dos semanas](https://napkinnotes.es/mundial-2026-fisica-balon-aire) el enemigo era el aire -el aire de Vancouver, el de Ciudad de México; el aire caliente, el aire frío, denso o fino; en definitiva, ese aire invisible que rodea al balón y decide si una falta baja a tiempo, si un centro se queda corto o si un disparo con efecto termina obedeciendo a la física en vez de al delantero-, ahora ya hemos pasado eso y estamos ante el mayor provocador de ataques cardíacos del planeta Tierra: una tanda de penaltis en la final del Mundial.

Solo ha pasado tres veces en la historia de los Mundiales. En el Mundial de Estados Unidos 1994, cuando Baggio falló el penalti decisivo mientras *"el silencio invadía todas las casas de Italia"*. Pasó en Alemania 2006, cuando Italia se llevó el Mundial marcando Grosso el quinto penalti. Y pasó en Catar 2022, con victoria argentina, después de que Argentina y Francia decidieran que una final normal era demasiado poco para ellos.

Soñemos: *Final del Mundial 2026. New York-New Jersey Stadium, el MetLife disfrazado para la FIFA. Final España-Portugal. Minuto 124. Marcador 3-3. El árbitro pita el fin de la prórroga.
Hay jugadores sentados sobre el césped, otros caminan sin ir a ninguna parte, alguno bebe agua como si eso pudiera ayudar en algo. Los porteros se alejan hacia la portería donde va a decidirse todo. El árbitro llama a los capitanes y saca una moneda.
No hay pizarra. No hay presión alta ni tras pérdida que valga. No hay 4-3-3 ni espacios al tercer hombre. No hay mapas de calor. No hay un analista con tres pantallas diciendo que el lateral izquierdo rival suele cruzar el cuarto penalti a la derecha si antes ha mirado al portero en la carrera tres veces los jueves, pero si es domingo, como hoy, lo tira por el centro a asegurar. Hay una moneda. Tú eres el capitán. Ganas el sorteo. El árbitro te mira:* **¿Queréis tirar primero o segundo?**

---


## La intuición entra al área

La intuición dice que hay que tirar primero, siempre. Tirar primero parece mejor porque te permite golpear antes. Si marcas, el otro equipo empieza la tanda persiguiéndote. Parece una diferencia pequeña, pero las tandas de penaltis viven precisamente de las diferencias pequeñas. Un pie que llega tarde, un portero que se vence medio segundo antes, un balón cinco centímetros más a la derecha, un palo, una rodilla, una moneda. Además, hay una idea psicológica muy razonable escondida ahí: no es lo mismo tirar para adelantarte que tirar para no caerte. El penalti sigue estando a once metros, la portería sigue midiendo lo mismo y el balón no se vuelve más pesado según el marcador. Reglamentariamente, al menos. Pero la cabeza no lee reglamentos.

*Si fallo, empezamos por debajo.*

Ay, la cabeza. Piensa que si tiras segundo tus compañeros van a tener que recorrer unos cuarenta metros viendo, casi sintiendo, que van por debajo, que el otro ya ha marcado, que el estadio ya ha hecho ese ruido raro que hacen los estadios cuando huelen sangre y estadística barata.

Ay, la cabecita.

Por eso durante años se ha repetido que empezar una tanda da ventaja. Algunos análisis antiguos, publicados antes de que el Mundial de Rusia 2018 y el de Catar 2022 añadieran más tandas a la historia, hablaban de una ventaja apreciable para el equipo que tiraba primero <a class="nn-cite" href="#ref-2">[2]</a>.

---


## Treinta y cinco monedas

Una tanda mundialista no es una encuesta gigante, ni una simulación con millones de mundos paralelos o una sábana de Excel interminable donde los porcentajes se acomodan solos y uno puede sacar conclusiones con voz de notario. En los Mundiales, hasta la final de Catar 2022 incluida, ha habido 35 tandas de penaltis: treinta y cinco. Esto obliga a hablar con bastante cuidado, porque en una muestra así una final como Argentina-Francia 2022 no es solo una final absurda, preciosa, agotadora y probablemente ilegal para cualquier sistema cardiovascular, es también una fila más en una tabla pequeña. Y en una tabla pequeña cada fila pesa. 

Al mirar los datos completos hasta Catar 2022 el resultado es este:

- el equipo que tiró primero ganó 17 tandas;  
- el equipo que tiró segundo ganó 18.

Con una diferencia de una tanda la moneda se queda sin épica.

---

## El dato que estropea el titular y una explicación de estadística

Llegados aquí, el artículo fácil habría sido evidente. Algo así como *Tirar primero o segundo da igual, la ciencia lo demuestra*. Pero la ciencia, cuando se porta bien, no está para darnos titulares, sino más bien para quitarnos algunos.

El dato mundialista no permite decir que empezar la tanda de penaltis sea claramente mejor, pero tampoco peor, ni siquiera irrelevante. Solo dice que, hasta ahora, la moneda no parece haber inclinado la balanza de forma definitiva. Eso no mata la intuición, la baja del pedestal y la sienta frente a los datos, una situación donde las intuiciones suelen ponerse nerviosas. Quizá empezar dé ventaja psicológica, pero quizá esta se compense con el primer fallo, la calidad de los lanzadores, el portero, el cansancio o esa rareza de un fútbol que nunca firma contratos de comportamiento. Porque aquí las variables llevan camiseta, lloran, rezan, tienen calambres, escuchan a ochenta mil personas y caminan solas desde el círculo central hasta el punto de penalti con demasiadas cosas en la cabeza. Por eso conviene recordar algo: cuando una estadística viene con pocos datos, desconfiad. Treinta y cinco tandas suenan a mucho porque cargan décadas, finales y tragedias nacionales, pero siguen siendo pocas; basta con que dos o tres caigan del otro lado para que el porcentaje cambie de cara y parezca contar otra historia.

Si observamos una variable binaria, por ejemplo “gana quien tira primero” o “no gana quien tira primero”, cada tanda funciona como un experimento de sí/no. La proporción observada se calcula así:
$$
\hat{p} = \frac{x}{n},
$$
donde $x$ es el número de éxitos y $n$ el número total de casos. En nuestro caso: $\hat{p} = \frac{17}{35} = 0.486$, es decir, quien tiró primero ganó el $48.6$% de las tandas mundialistas. Ese dato observado es exacto, pero lo que no es exacto es la conclusión que podemos sacar de él sobre la probabilidad real de que tirar primero sea ventajoso. Por eso nos interesa medir la incertidumbre de la proporción observada. Una forma básica de hacerlo es el error estándar de la proporción, que se calcula así:
$$
EE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}.
$$
Esta fórmula no mide cuánto varía el número total de victorias, sino cuánto puede variar el porcentaje observado por efecto del azar. Sustituyendo los valores:
$$
EE(\hat{p})  \approx 0.084
$$
Eso significa que el porcentaje observado puede moverse bastante simplemente por azar. Para hacernos una idea del margen de duda, no nos quedamos solo con el 48.6%. Le sumamos y le restamos una especie de colchón estadístico, lo bastante grande como para cubrir, aproximadamente, el 95% de los casos razonables. Usamos $\hat{p} \pm 1.96 \cdot EE(\hat{p})$, es decir, si metemos el ruido dentro de la cuenta, el $48.6$% deja de parecer tan sólido y empieza a ensancharse:
$$
32 \% ≲ p ≲ 65 \%
$$
Ese rango es enorme. Y lo que significa es que, con solo 35 casos, ese $48.6$% todavía deja muchísima incertidumbre sobre la probabilidad real. Estadísticamente, los datos son compatibles con escenarios muy distintos: desde una desventaja apreciable para quien tira primero, cerca del $32$%, hasta una ventaja considerable, cerca del $65$%. Por eso no podemos convertir un 17-18 en una ley general sobre la presión psicológica.

Podemos verlo de otra forma:

> **Si de verdad quien tira primero tuviera una probabilidad real de ganar el $60$% de las veces, ¿qué probabilidad tendría una muestra de 35 tandas de detectar esa ventaja con un test cuyos falsos positivos fueran como mucho el $5$%?**

Si en realidad quien tira primero ganara el $60$% de las veces, la variable que queremos observar sería:
$$
X \sim \mathrm{Binomial}(35, 0.6),
$$
donde $X$ es el número de tandas ganadas por quien tira primero en una muestra de $35$. Para detectar esa ventaja con un test cuyos falsos positivos sean como mucho el $5$%, comparamos contra la hipótesis de que no hay ventaja, que llamamos $H_0$ y que es tal que $H_0: p = 0.5$.
Como aquí la pregunta es si tirar primero da ventaja, un test binomial unilateral al $5$% rechaza esa hipótesis si el resultado es suficientemente alto. En este caso, aproximadamente si:
$$
X \geq 23.
$$
En palabras más sencillas, la probabilidad de que eso ocurra si tirar primero te diera ventaja para ganar el $60$% de las veces es:
$$
P(X \geq 23 \mid p = 0.6) \approx 0.306
$$
Es decir, lo detectaríamos aproximadamente el $31$% de las veces. Dicho de otra forma: **habría aproximadamente un $69$% de probabilidades de no detectarlo, aunque la ventaja sí que existiera.**

Ay, la estadística. A veces no te dice quién tiene razón, solo te mira y sentencia: con tan pocos datos, no vengas tan gallito.

---

## Volvamos al centro del campo

Así que volvemos al New York-New Jersey Stadium. Final del Mundial 2026. *España. Penaltis. Tú eres el capitán. La moneda acaba de caer a tu favor. El árbitro espera. Tus compañeros también. En algún lugar, millones de personas creen que esta decisión tiene una respuesta escondida en una tabla. Primero o segundo. Ahora ya sabes algo. Sabes que la intuición pide tirar primero. Sabes que psicológicamente tiene sentido querer poner presión. Sabes que durante años se ha hablado de esa ventaja. Pero también sabes que, en los Mundiales, el dato completo hasta Catar 2022 no muestra una ventaja clara. Así que quizá la respuesta honesta no es “primero”, ni “segundo”. La respuesta honesta es más incómoda:* **Depende de quién tire... y de lo que marque.**

Esta es quizá la parte más difícil de aceptar de la estadística. Uno llega buscando una respuesta clara (¿Tirar primero o segundo?), y ella responde: *No sé, pero en ninguno de los casos deberías estar tan seguro.*

Pero aunque parezca poco, esto es muchísimo y sirve para algo más humilde: recordarte que la moneda no sabe de fútbol. Y que el balón, cuando llega al punto de penalti, tampoco sabe quién empezó. No sabe quién llega con calambres, quién ha fallado antes, quién lleva toda la vida soñando con ese disparo o quién está a punto de convertirse en una estatua o en una herida nacional. La moneda cae y se calla, dejando un silencio que invadirá todas las casas de un país.

---


## Referencias

<ol class="nn-references">

  <li id="ref-2">
    BBC Sport. (2018). <em>World Cup 2018: Penalty shootouts - who has the advantage?</em>.
    <a href="https://www.bbc.com/sport/football/44641247" target="_blank" rel="noopener noreferrer">https://www.bbc.com/sport/football/44641247</a>
  </li>

  <li id="ref-3">
    Goal.com. (2022). <em>Tandas de penales en Mundial: ¿conviene patear o atajar primero?</em>.
    <a href="https://www.goal.com/es/noticias/tandas-penales-mundial-conviene-patear-atajar-primero/bltbfeae4267974f427" target="_blank" rel="noopener noreferrer">https://www.goal.com/es/noticias/tandas-penales-mundial-conviene-patear-atajar-primero/bltbfeae4267974f427</a>
  </li>
</ol>
