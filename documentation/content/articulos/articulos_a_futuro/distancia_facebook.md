---
title: ¿Cuál es la distancia promedio entre dos personas en Facebook?
author: Duvier Suárez Fontanella
date: 2026-04-15
layout: articles
status: draft
category: Ciencia de Datos
tags:
  - redes sociales
  - teoría de grafos
  - small world
  - seis grados de separación
summary: En Facebook, los famosos seis grados de separación se reducen a poco más de cuatro saltos. La teoría de grafos explica por qué una red de miles de millones de personas puede comportarse como un mundo sorprendentemente pequeño.
image: images/face_dist.png
---

[TOC]



## De los seis grados al mundo comprimido

¿Cuántas personas te separan de alguien elegido completamente al azar en Facebook?

No de un amigo de un amigo. No de alguien de tu ciudad. No de una persona que estudió en tu universidad o trabaja en tu área. De alguien verdaderamente lejano en el grafo social: otro país, otro idioma, otro círculo, otra vida.

La respuesta parece que debería ser grande. Facebook tiene miles de millones de usuarios, así que uno esperaría que conectar dos puntos arbitrarios de esa red exigiera una cadena larga de intermediarios. Pero las redes sociales reales no se comportan como mapas geográficos. Se comportan más bien como espacios llenos de atajos.

Meta ha publicado en diversas ocasiones análisis sobre la longitud promedio de los caminos en su grafo social. La conclusión, repetida con distintos tamaños de muestra y metodologías, es bastante sorprendente: la distancia típica entre dos usuarios de Facebook está entre **4 y 4.7 saltos**.

En uno de sus estudios más citados, Facebook Research reportó en 2016 que, usando miles de millones de nodos y decenas de miles de millones de aristas, se obtenían aproximadamente los siguientes valores:

- **Distancia promedio global:** 4.57  
- **Distancia promedio entre usuarios activos en EE. UU.:** alrededor de 4.2  
- **Máxima componente conexa:** más del 99 % de la red  

Dicho sin jerga: **una persona cualquiera en Facebook puede llegar a otra mediante poco más de cuatro intermediarios**. O, para decirlo con algo de dramatismo sociológico: los famosos “seis grados de separación” han sufrido una compactificación dimensional bastante seria.

La idea de los seis grados de separación suele asociarse a Frigyes Karinthy, quien la formuló literariamente en 1929. Más tarde, en 1967, Stanley Milgram la popularizó mediante su célebre experimento de cartas enviadas entre desconocidos. Desde entonces, la imagen de que estamos separados por apenas unas pocas conexiones se convirtió en parte de la cultura popular.

Milgram encontró longitudes promedio cercanas a **5.5 pasos** para conectar a una persona inicial con un objetivo elegido. El experimento tenía sesgos importantes —muestras pequeñas, abandono de participantes, selección no completamente aleatoria—, pero capturó una intuición profunda: las redes humanas no se comportan como una colección dispersa de individuos, sino como estructuras con atajos.

Con los grafos sociales actuales, esta intuición puede formularse de forma mucho más precisa:

- La distancia promedio **no solo es menor que seis**, sino que parece **estabilizarse por debajo de cinco** en redes con miles de millones de nodos.  
- Esto no significa que todos se conozcan, ni mucho menos que todos se quieran invitar a cenar. Significa que **la estructura combinatoria del grafo permite trayectorias extremadamente cortas** entre pares de usuarios.

---

## Facebook como laboratorio de teoría de grafos

Podemos representar Facebook, en una primera aproximación, como un grafo no dirigido

$$
G = (V,E),
$$

donde:

- $V$ es el conjunto de usuarios.  
- $E$ es el conjunto de relaciones de amistad.  

La **distancia** entre dos vértices $u$ y $v$, denotada $d(u,v)$, es la longitud mínima del camino que los conecta. Si dos usuarios están conectados directamente, entonces $d(u,v)=1$. Si necesitan un amigo intermedio, entonces $d(u,v)=2$, y así sucesivamente.

El objeto que queremos estimar es la **distancia promedio**, o *average path length*:

$$
L =
\frac{1}{|V|(|V|-1)}
\sum_{u \neq v} d(u,v).
$$

Esta cantidad resume, de forma muy compacta, una propiedad global de la red: cuántos pasos hacen falta, en promedio, para ir de un nodo cualquiera a otro. Es una especie de observable macroscópico del grafo, como si la red tuviera una “longitud característica” emergente.

La analogía no es perfecta, pero es tentadora: igual que en física estadística no queremos conocer la trayectoria microscópica de cada molécula para hablar de temperatura, en teoría de redes muchas veces no necesitamos inspeccionar cada amistad individual para extraer propiedades globales. Basta con saber cómo se organiza la estructura colectiva.

---

## Cómo medir distancias en un monstruo de miles de millones de nodos

En una red pequeña, la distancia promedio puede calcularse recorriendo todos los pares de nodos. En Facebook, sin embargo, eso sería computacionalmente inviable: estamos hablando de miles de millones de vértices y decenas de miles de millones de aristas.

El sumatorio anterior es elegante, sí. Pero evaluarlo literalmente sería una forma bastante cara de calentar centros de datos.

Por eso se utilizan técnicas aproximadas y distribuidas, como:

- búsquedas tipo **BFS** desde subconjuntos de vértices,  
- **muestreo aleatorio** de nodos,  
- estimadores probabilísticos de vecindades,  
- algoritmos distribuidos inspirados en métodos como **HyperANF**.  

La idea general es estimar la distribución de distancias sin tener que calcular todos los caminos mínimos entre todos los pares posibles.

En vez de preguntar “¿cuál es la distancia exacta entre cada par de usuarios?”, se pregunta algo más razonable computacionalmente: “si tomo muestras representativas de la red, ¿cómo se distribuyen las distancias?”. A partir de ahí se reconstruye una estimación robusta de $L$.

Este cambio de perspectiva es crucial. En grafos de esta escala, la pregunta matemática sigue siendo limpia, pero la respuesta requiere estadística, algoritmos distribuidos y bastante respeto por la memoria RAM.

---

## La física de los mundos pequeños

El comportamiento observado en Facebook encaja con la física y matemática de las **redes de mundo pequeño**, introducidas formalmente por Watts y Strogatz en 1998. Estas redes combinan dos propiedades que, juntas, son muy potentes:

1. **Alto agrupamiento local**, medido mediante un coeficiente de clustering elevado.  
2. **Caminos globales cortos**, con una distancia promedio que crece lentamente con el tamaño de la red.  

Una forma esquemática de expresar esta segunda propiedad es

$$
L \sim \log N,
$$

donde $N$ es el número de nodos de la red. Esta relación no debe interpretarse como una predicción exacta sin constantes, base logarítmica ni estructura de grado. Más bien indica el punto esencial: **la distancia promedio crece muy despacio cuando el número de nodos aumenta**.

Por ejemplo, aunque $N \sim 10^9$, el crecimiento logarítmico hace que el tamaño efectivo del mundo social sea muchísimo menor que el tamaño bruto de la red. No vivimos en un grafo donde haya que atravesar millones de nodos para llegar de una persona a otra. Vivimos, combinatoriamente hablando, en una red llena de túneles.

Para que esto ocurra se necesitan dos ingredientes:

- **Conectividad local fuerte:** comunidades de amigos, familias, colegas, universidades, barrios o grupos profesionales.  
- **Enlaces de largo alcance:** contactos que conectan regiones sociales o geográficas muy distintas.  

La coexistencia de ambos ingredientes produce una geometría peculiar. Localmente, la red parece muy agrupada: tus amigos suelen conocerse entre sí. Globalmente, sin embargo, unos pocos enlaces entre comunidades lejanas reducen drásticamente las distancias.

Esa es la gracia de los mundos pequeños: no eliminan la estructura local, sino que la perforan con atajos.

---

## Hubs, comunidades y atajos improbables

Facebook cumple de forma bastante natural los requisitos de una red de mundo pequeño. Por un lado, abundan las comunidades altamente conectadas: grupos familiares, amistades de colegio, círculos universitarios, colegas de trabajo, comunidades locales o redes profesionales.

Por otro lado, existen enlaces menos locales: antiguos compañeros de universidad, colaboraciones internacionales, migraciones, contactos de congresos, amigos de amigos o esa persona que aceptaste en 2012 y ya no sabes exactamente por qué.

Estos enlaces de largo alcance actúan como **atajos** en el grafo. Aunque sean relativamente pocos, reducen de forma drástica la distancia promedio $L$.

Desde el punto de vista de teoría de redes, esta propiedad está relacionada con varios rasgos estructurales:

- **Distribuciones de grado con colas pesadas**, donde algunos nodos tienen muchísimas conexiones.  
- **Hubs**, es decir, usuarios o páginas con grado muy alto.  
- **Clustering elevado**, mayor que el esperado en una red aleatoria simple tipo Erdős–Rényi.  
- **Comunidades interconectadas**, que combinan estructura modular con enlaces entre módulos.  

Aquí aparece una diferencia importante con una red completamente aleatoria. En un grafo Erdős–Rényi, las conexiones se distribuyen de manera homogénea y sin estructura social explícita. En una red humana real, en cambio, las conexiones están fuertemente correlacionadas: tus amigos tienden a conocerse entre sí, tus círculos se solapan, y algunos nodos funcionan como puentes entre comunidades.

La consecuencia es que Facebook no es simplemente “un grafo grande”. Es un grafo grande, altamente agrupado, heterogéneo y con atajos. En otras palabras: una pesadilla para quien quiera mantener una separación social limpia, pero un objeto precioso para un teórico de redes.

---

## Qué significa realmente estar a 4.57 saltos

El número **4.57** no debe leerse como si cada par de usuarios estuviera exactamente separado por 4.57 personas, cosa que además sería difícil de implementar anatómicamente. Es un promedio sobre una distribución de distancias.

Algunos pares estarán conectados por uno o dos saltos. Otros necesitarán más. Lo relevante es que la distribución está fuertemente concentrada en valores bajos, incluso cuando la red tiene un tamaño enorme.

Esto nos dice que Facebook es una red muy compacta. Su diámetro efectivo es pequeño: no porque todos estén conectados con todos, sino porque existen suficientes puentes entre comunidades como para que los caminos mínimos sean cortos.

Dicho de otro modo: la red no es densa en el sentido trivial de tener todas las conexiones posibles. Es eficiente en el sentido estructural de conectar regiones muy distintas mediante pocos pasos.

Esta distinción es importante. Una red puede ser localmente agrupada, socialmente modular y, aun así, globalmente compacta. Esa combinación es precisamente la firma de un mundo pequeño.

---

## Lo fascinante y lo inquietante de una red tan corta

La distancia promedio no es solo una curiosidad simpática. Es una cantidad estructural que controla procesos dinámicos sobre la red.

Un valor bajo de $L$ implica que muchos fenómenos pueden propagarse rápidamente:

- **Difusión de información.**  
- **Viralidad de contenidos.**  
- **Propagación de rumores.**  
- **Contagio social o cultural.**  
- **Campañas de desinformación.**  
- **Dinámicas epidémicas en redes de contacto.**  

Si una red tiene caminos muy cortos, una señal no necesita muchos pasos para alcanzar regiones muy alejadas del grafo. Esto es útil cuando se quiere compartir conocimiento, coordinar comunidades o encontrar colaboradores. También es preocupante cuando lo que se propaga es ruido, polarización o información falsa con esteroides algorítmicos.

Desde el punto de vista de ingeniería de plataformas, estas métricas también son fundamentales. La estructura de mundo pequeño permite diseñar o mejorar:

- algoritmos de recomendación basados en amigos de amigos,  
- buscadores sociales,  
- sistemas de sugerencia de contactos,  
- mecanismos de privacidad dependientes de la distancia social,  
- estrategias de detección de comunidades,  
- arquitecturas distribuidas que aprovechan la localidad del grafo.  

En este sentido, el número 4.57 no es solo una anécdota. Es una medida macroscópica de una estructura microscópica inmensa. Resume, en un solo valor, miles de millones de decisiones individuales: amistades, conocidos, vínculos familiares, antiguos compañeros, contactos laborales y conexiones improbables.

La distancia promedio entre dos personas en Facebook es, por tanto, de apenas unos pocos saltos, típicamente entre **4 y 4.7**. Esto confirma, con datos masivos, la intuición detrás de los seis grados de separación: las redes humanas son mucho más compactas de lo que su tamaño sugiere.

La razón no es mágica. Es teoría de grafos. Las comunidades locales generan clustering; los enlaces de largo alcance generan atajos; los hubs reducen distancias; y la combinación de todos estos ingredientes produce una red de mundo pequeño.

Así que sí: probablemente estás a cuatro o cinco saltos de casi cualquier persona en Facebook. Lo cual es matemáticamente fascinante, socialmente inquietante y, dependiendo de la persona, quizá también una buena razón para revisar la configuración de privacidad.
