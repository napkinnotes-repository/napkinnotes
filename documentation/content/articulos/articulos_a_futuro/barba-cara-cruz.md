---
title: Cara o cruz, o como el azar también tiene sesgos          # vuestro título
author: David Barba González               # mismo nombre que en la tarjeta de autor
date: 2026-10-22          # formato YYYY-MM-DD
layout: articles
slug: prueba-barba
status: hidden            # published si ya está listo
category: Estadística             # categoría con mayúscula inicial
tags:                     # tags con minúscula inicial
  - probabilidad
  - estadística
  - bli bli
summary: "¿Es realmente justo lanzar una moneda al aire? Aunque solemos asumir que cara y cruz tienen la misma probabilidad, la física y la estadística revelan un pequeño sesgo que puede inclinar el resultado. Descubre por qué ocurre y compruébalo con dos aplicaciones interactivas."
image: images/barba-caracruz/shekel.jpeg # imagen principal del artículo  ¡¡¡¡¡¡¡¡TIENE QUE SER JPEG EL FORMATO!!!!!
certificate: false
---

[TOC]

¿Cuántas situaciones de nuestra vida se deciden por azar? Decisiones profesionales o financieras; resultados electorales en los que la victoria se decide por un puñado de votos; enfermedades causadas por mutaciones genéticas aleatorias; o algunos resultados deportivos en caso de empate; son muestra de que el azar está muy presente en nuestra vida diaria. Sin ir más lejos, estáis leyendo esta servilleta, acerca del azar, porque un algoritmo me enseñó un vídeo corto que despertó mi interés.

El caso más paradigmático de fortuna, en este caso binaria, es el lanzamiento de una moneda al aire. Ponemos una moneda en el pulgar, la lanzamos al aire girando sobre sí misma, y la cazamos con la mano, sin que caiga al suelo. El resultado viene dado por qué lado de la moneda mira hacia arriba. En este juego, que se utiliza para decidir muchísimas situaciones en el mundo humano, todos asumimos que la probabilidad de que salga cara (o cruz) es exactamente 0.5. El número de veces que sale cara se aproximará cada vez más al 50% cuantas más veces la lancemos.  

Pero, ¿y si eso no es así? ¿Podría existir un sesgo que, independientemente de la moneda, hiciese que uno de los lados esté ligeramente favorecido? Veámoslo.

## Distribución binomial de probabilidad
Lo primero que vamos a hacer es entender el modelo matemático que explica una apuesta a cara o cruz. El juego consiste en un experimento (aleatorio) con dos posibles resultados: A (cara) y B (cruz). Llamemos $p$ a la probabilidad de que el resultado sea A. Uno de los axiomas de la teoría de la probabilidad afirma que
$$
0\leq p \leq 1,
$$
donde si $p=0$ nunca puede salir cara, y si $p=1$ siempre sale cara. Un segundo axioma impone que cuando lanzamos una moneda al aire, siempre sale algo, ya sea cara o cruz. Por tanto,
$$
p+q=1
$$
donde $q\geq0$ es la probabilidad de que salga cruz.

Ahora nos hacemos la siguiente pregunta: ¿cuál es la probabilidad de que, si lanzo una secuencia de $M$ monedas al aire, salga $N$ veces cara? Trabajemos un ejemplo concreto, en el que tiramos $M=5$ veces una moneda. ¿Cuál es la probabilidad de que salga cara $N=3$ veces? Para calcularla tendríamos que escribir todos los resultados posibles (AAAAA, AAAAB, AAABA, etc.), contar todos  los que tienen 3 veces la letra A (por ejemplo ABABA), y después multiplicar por la probabilidad de cada uno. 

La probabilidad de que la secuencia ABABA se dé es $P(ABABA)=pqpqp=p^3 q^2$. En realidad, cualquier secuencia con 3 caras y 2 cruces tiene la misma probabilidad de ocurrir si lanzamos una moneda 5 veces, porque nos da igual el orden de aparición de caras o cruces. 

Para entender el número de opciones que hay con $N=3$, vamos a usar una pequeña aplicación justo debajo. Vuestra tarea es "tirar" una moneda 5 veces, aunque en este caso vais a elegir el resultado de cada tirada, sabiendo que en total vamos a tener 3 caras y 2 cruces. Después de crear nuestra secuencia de monedas, vamos a ir viendo cómo contar el número total de combinaciones posibles. Para ello, debéis seleccionar "Continuar" y la propia aplicación os irá explicando el razonamiento. Tened en cuenta que en un grupo de $M$ elementos, el número posible de permutaciones entre ellos es $M!=M(M-1)(M-2)...1$, donde $M!$ es el factorial de $M$.

<style>
    #nn-combinaciones {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 40px;
    }

    #nn-combinaciones .card {
      width: 340px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background: #ffffff;
      padding: 16px 18px 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

    #nn-combinaciones .card h3 {
      margin-top: 0;
      margin-bottom: 8px;
      font-size: 20px;
    }

    #nn-combinaciones .buttons button {
      padding: 11px 18px;
      margin-right: 10px;
      border: 0;
      border-radius: 999px;
      background: var(--richcarmine);
      color: #fff;
      font-family: inherit;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }

    #nn-combinaciones .buttons button:hover:enabled {
      opacity: 0.92;
      transform: translateY(-1px);
    }

    #nn-combinaciones .buttons button:disabled {
      cursor: not-allowed;
      opacity: 0.6;
    }

    #nn-combinaciones #counter {
      margin-top: 10px;
      font-size: 14px;
      line-height: 1.4;
    }

    #nn-combinaciones #step {
      margin-top: 10px;
      font-size: 14px;
      font-weight: bold;
      min-height: 20px;
    }

    #nn-combinaciones #multiplication {
      margin-top: 10px;
      font-size: 14px;
    }

    #nn-combinaciones #permutations-count {
      margin-top: 8px;
      font-size: 14px;
      font-weight: bold;
    }

    #nn-combinaciones .slots {
      display: flex;
      gap: 8px;
      margin-top: 16px;
    }

    #nn-combinaciones .slot {
      width: 40px;
      height: 40px;
      border: 1px solid #aaa;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      background: #fafafa;
      text-align: center;
      padding: 2px;
      box-sizing: border-box;
    }

    #nn-combinaciones .cara1 { background: #ff4d4d; color: #fff; }
    #nn-combinaciones .cara2 { background: #4caf50; color: #fff; }
    #nn-combinaciones .cara3 { background: #2196f3; color: #fff; }
    #nn-combinaciones .cruz1 { background: #ffeb3b; color: #000; }
    #nn-combinaciones .cruz2 { background: #9c27b0; color: #fff; }

    #nn-combinaciones .neutral {
      background: #e0e0e0 !important;
      color: #000 !important;
    }

    #nn-combinaciones #explanation {
      margin-top: 16px;
      font-size: 14px;
      color: #444;
      line-height: 1.5;
      min-height: 80px;
    }

    #nn-combinaciones .control-buttons {
      margin-top: 16px;
      display: none;
    }

    #nn-combinaciones .control-buttons button {
      margin-right: 10px;
      padding: 11px 18px;
      font-family: inherit;
      font-size: 14px;
      font-weight: 600;
      border: 0;
      border-radius: 999px;
      background: var(--richcarmine);
      color: #fff;
      cursor: pointer;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }

    #nn-combinaciones .control-buttons button:hover:enabled {
      opacity: 0.92;
      transform: translateY(-1px);
    }

    #nn-combinaciones .control-buttons button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
    }
  </style>
<div id="nn-combinaciones">
  <div class="card">
    <h3>Combinaciones</h3>

    <p><strong>Selecciona resultado:</strong></p>

    <div class="buttons">
      <button id="btn-cara">Cara</button>
      <button id="btn-cruz">Cruz</button>
    </div>

    <p id="counter">
      Caras restantes: <strong>3</strong><br>
      Cruces restantes: <strong>2</strong>
    </p>

    <p id="step"></p>

    <p id="multiplication">
      Construcción del factorial: <strong></strong>
    </p>

    <p id="permutations-count">
      Permutaciones posibles (si todas fueran distintas): <strong>0</strong>
    </p>

    <div class="slots" id="slots">
      <div class="slot"></div>
      <div class="slot"></div>
      <div class="slot"></div>
      <div class="slot"></div>
      <div class="slot"></div>
    </div>

    <p id="explanation"></p>

    <div class="control-buttons" id="control-buttons">
      <button id="btn-continue">Continuar</button>
      <button id="btn-reset">Reiniciar</button>
    </div>
  </div>
</div>

  <script>
    let remainingCara = 3;
    let remainingCruz = 2;
    let nextSlot = 0;
    let steps = [];
    let placedPieces = [];
    let currentStep = 0;

    const counterEl = document.getElementById("counter");
    const stepEl = document.getElementById("step");
    const multiplicationEl = document.getElementById("multiplication");
    const permutationsCountEl = document.getElementById("permutations-count");
    const explanationEl = document.getElementById("explanation");
    const slotsEl = document.getElementById("slots");
    const btnCara = document.getElementById("btn-cara");
    const btnCruz = document.getElementById("btn-cruz");
    const controlButtons = document.getElementById("control-buttons");
    const btnContinue = document.getElementById("btn-continue");
    const btnReset = document.getElementById("btn-reset");

    function updateCounter() {
      counterEl.innerHTML =
        `Caras restantes: <strong>${remainingCara}</strong><br>` +
        `Cruces restantes: <strong>${remainingCruz}</strong>`;
    }

    function updateMultiplication() {
      const multText = steps.join(" × ");
      multiplicationEl.innerHTML =
        `Construcción del factorial: <strong>${multText}</strong>`;
      if (steps.length === 5) {
        const total = steps.reduce((acc, v) => acc * v, 1);
        permutationsCountEl.innerHTML =
          `Permutaciones posibles (si todas fueran distintas): <strong>${total}</strong>`;
      }
    }

    function getCaraIndex() {
      return placedPieces.filter(p => p.type === "cara").length + 1;
    }

    function getCruzIndex() {
      return placedPieces.filter(p => p.type === "cruz").length + 1;
    }

    function applyPieceStyle(slot, type, index) {
      slot.className = "slot";
      if (type === "cara") {
        slot.classList.add("cara" + index);
        slot.textContent = `Cara ${index}`;
      } else {
        slot.classList.add("cruz" + index);
        slot.textContent = `Cruz ${index}`;
      }
    }

    function selectOption(type) {
      const slots = slotsEl.getElementsByClassName("slot");

      if (type === "cara" && remainingCara === 0) {
        stepEl.innerText = "Ya no quedan caras.";
        return;
      }
      if (type === "cruz" && remainingCruz === 0) {
        stepEl.innerText = "Ya no quedan cruces.";
        return;
      }
      if (nextSlot >= slots.length) {
        stepEl.innerText = "Todas las ranuras están llenas.";
        return;
      }

      const slot = slots[nextSlot];
      let index = type === "cara" ? getCaraIndex() : getCruzIndex();

      applyPieceStyle(slot, type, index);
      placedPieces.push({ type, index });

      const remainingSlots = slots.length - nextSlot;
      steps.push(remainingSlots);

      stepEl.innerText =
        `En este paso tenías ${remainingSlots} opciones para colocar esta ficha.`;

      nextSlot++;

      if (type === "cara") remainingCara--;
      else remainingCruz--;

      updateCounter();
      updateMultiplication();

      if (nextSlot === slots.length) {
        btnCara.disabled = true;
        btnCruz.disabled = true;
        controlButtons.style.display = "block";
      }
    }

    btnCara.onclick = () => selectOption("cara");
    btnCruz.onclick = () => selectOption("cruz");

    // --- PASOS A, B, C, D CONTROLADOS POR UN SOLO BOTÓN ---
    btnContinue.onclick = () => {
      currentStep++;

      const total = steps.reduce((acc, v) => acc * v, 1);
      const slots = slotsEl.getElementsByClassName("slot");

      if (currentStep === 1) {
        explanationEl.innerHTML = `
          <strong>Paso A:</strong><br>
          Cada ficha tiene su propio color e identidad (Cara 1 roja, Cara 2 verde, Cara 3 azul,
          Cruz 1 amarilla, Cruz 2 lila).<br><br>
          Si todas fueran distintas, habría:<br>
          <strong>${steps.join(" × ")} = ${total}</strong> permutaciones posibles (5!).
        `;
        permutationsCountEl.innerHTML =
          `Permutaciones posibles (si todas fueran distintas): <strong>${total}</strong>`;
      }

      else if (currentStep === 2) {
        explanationEl.innerHTML += `
          <br><br><strong>Paso B:</strong><br>
          Las <strong>3 caras</strong> son idénticas entre sí. Si pierden su color,
          todas las permutaciones que las intercambian representan el mismo patrón.<br>
          Dividimos entre <strong>3! = 6</strong>.
        `;

        for (let i = 0; i < slots.length; i++) {
          if (placedPieces[i].type === "cara") {
            slots[i].classList.add("neutral");
          }
        }

        const afterCara = total / 6;
        permutationsCountEl.innerHTML =
          `Permutaciones tras considerar caras idénticas: <strong>${afterCara}</strong>`;
      }

      else if (currentStep === 3) {
        explanationEl.innerHTML += `
          <br><br><strong>Paso C:</strong><br>
          Las <strong>2 cruces</strong> también son idénticas. Si pierden su color,
          las permutaciones que las intercambian representan el mismo patrón.<br>
          Dividimos entre <strong>2! = 2</strong>.
        `;

        for (let i = 0; i < slots.length; i++) {
          if (placedPieces[i].type === "cruz") {
            slots[i].classList.add("neutral");
          }
        }

        const afterCara = total / 6;
        const afterCruz = afterCara / 2;

        permutationsCountEl.innerHTML =
          `Permutaciones tras considerar caras y cruces idénticas: <strong>${afterCruz}</strong>`;
      }

      else if (currentStep === 4) {
        const afterCara = total / 6;
        const afterCruz = afterCara / 2;

        explanationEl.innerHTML += `
          <br><br><strong>Paso D (Conclusión):</strong><br>
          Partimos de <strong>${total}</strong> permutaciones posibles si todas fueran distintas.<br>
          Al tener <strong>3 caras</strong> idénticas y <strong>2 cruces</strong> idénticas,
          dividimos:<br><br>
          <strong>${total} / (3! × 2!) = ${afterCruz}</strong><br><br>
          Hay exactamente <strong>${afterCruz} combinaciones únicas</strong>.
        `;

        btnContinue.disabled = true;
      }
    };

    // --- REINICIAR ---
    btnReset.onclick = () => {
      location.reload();
    };
  </script>

Ahora, si generalizamos esta cuenta, y tiramos $M$ veces la moneda, la probabilidad de que salga cara $N$ veces es
$$
P_M(N)=\frac{M!}{N!(M-N)!}p^Nq^{M-N}.
$$
Esta expresión es conocida como la [distribución binomial de probabilidad](https://napkinnotes.es/la-moneda-que-no-queria-decidir-el-mundial). Podéis comprobar justo debajo la probabilidad de una secuencia con cualquier número de monedas, y también podéis sesgar la moneda, es decir forzar que la probabilidad  $p$ de que salga cara sea distinta de $0.5$.

<style>
  #coin-probability-sidebar .nn-coin-calculate {
    margin-top: 10px;
    width: 100%;
    padding: 11px 18px;
    border: 0;
    border-radius: 999px;
    background: var(--richcarmine);
    color: #fff;
    font-family: inherit;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s ease, opacity 0.2s ease;
  }

  #coin-probability-sidebar .nn-coin-calculate:hover {
    opacity: 0.92;
    transform: translateY(-1px);
  }
</style>

<div style="display: flex; justify-content: center; width: 100%;">
<div id="coin-probability-sidebar" 
     style="border:1px solid #ddd;
            padding:16px;
            width:260px;
            background:#fafafa;
            font-family:Arial, sans-serif;">
  
  <h3 style="margin-top:0;">Cara o cruz</h3>

  <label style="font-size:14px;">Número de lanzamientos:</label>
  <input id="num-flips" type="number" min="0"
         style="width:100%;box-sizing:border-box;padding:8px;font-size:14px;margin-bottom:10px;">

  <label style="font-size:14px;">Número de caras:</label>
  <input id="num-heads" type="number" min="0"
         style="width:100%;box-sizing:border-box;padding:8px;font-size:14px;margin-bottom:10px;">

  <label style="font-size:14px;">Probabilidad de que salga cara (p):</label>
  <select id="prob-heads"
          style="width:100%;box-sizing:border-box;padding:8px;font-size:14px;margin-bottom:10px;">
    <option value="0">0.0</option>
    <option value="0.1">0.1</option>
    <option value="0.2">0.2</option>
    <option value="0.3">0.3</option>
    <option value="0.4">0.4</option>
    <option value="0.5" selected>0.5</option>
    <option value="0.6">0.6</option>
    <option value="0.7">0.7</option>
    <option value="0.8">0.8</option>
    <option value="0.9">0.9</option>
    <option value="1">1.0</option>
  </select>

  <button onclick="calcBinomialProb()" class="nn-coin-calculate">
    Calcular
  </button>

  <p id="result" 
     style="margin-top:12px;font-weight:bold;font-size:14px;"></p>
</div>

<script>
function logFactorial(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += Math.log(i);
  }
  return sum;
}

function logBinomial(n, k) {
  return logFactorial(n) - logFactorial(k) - logFactorial(n - k);
}

function calcBinomialProb() {
  const n = parseInt(document.getElementById("num-flips").value);
  const k = parseInt(document.getElementById("num-heads").value);
  const p = parseFloat(document.getElementById("prob-heads").value);

  if (isNaN(n) || isNaN(k) || k > n || n < 0 || k < 0) {
    document.getElementById("result").innerText = "Ingresa números válidos (k ≤ n).";
    return;
  }

  // log(P) = log(C(n,k)) + k log(p) + (n-k) log(1-p)
  const logP =
    logBinomial(n, k) +
    k * Math.log(p) +
    (n - k) * Math.log(1 - p);

  const P = Math.exp(logP);

  document.getElementById("result").innerText =
    `P(${k} caras en ${n} lanzamientos con p=${p}) = ${P} (${(P * 100).toFixed(6)}%).`;
}
</script>
</div>


## Determinismo
En realidad, el lanzamiento de una moneda es un proceso determinista, gobernado por la mecánica clásica. Si conocemos las condiciones iniciales y las características físicas de la moneda (masa y tamaño), podemos predecir con un 100% de precisión el resultado del lanzamiento. La aleatoriedad que le asignamos a este proceso proviene de una variabilidad enorme al producirse un pequeño cambio en las condiciones iniciales del lanzamiento. 

El modelo predictivo clásico del lanzamiento de una moneda fue desarrollado por Diaconis, Holmes y Montgomery (DHM)<a class="nn-cite" href="#dhs">[1]</a>. La cadena argumental es la siguiente: la probabilidad de que al capturar la moneda con la mano el resultado sea cara es proporcional al porcentaje del tiempo de vuelo que la moneda pasa con ese lado mirando hacia arriba. A su vez, este tiempo viene dado por el ángulo $\psi_0$ que forma el vector normal a la superficie de la moneda $\vec{n}$ con el vector momento angular $\vec{M}$ en el momento de lanzamiento de la moneda. Podéis ver ambos vectores en la Figura 1.

En ausencia de rozamiento con el aire, el vector $\vec{M}$ no depende del tiempo, debido al principio de conservación del momento angular. Sin embargo, en general $\vec{n}$ sí varía con el tiempo durante el vuelo (excepto si $\psi_0=0$), y va a [precesar](https://napkinnotes.es/eclipse-caza#que-es-un-eclipse) alrededor de $\vec{M}$. Para entender el modelo DHM vamos a comentar dos valores extremos del ángulo $\psi_0$:

- Si $\psi_0=0$, entonces la moneda está girando sobre su propia normal (como un paraguas cuando gira alrededor de su mástil), es decir $\vec{n}\parallel\vec{M}$. Si lanzamos así la moneda, el resultado va a ser siempre el mismo: vamos a obtener aquel lado que estuviera hacia arriba en el lanzamiento.

- Si $\psi_0=\pi/2$, la moneda gira sobre un eje perpendicular a la normal, $\vec{n}\perp\vec{M}$. En este caso, la probabilidad de ambos resultados es exactamente 0.5.

<figure class="nn-article-figure">
    <img src="{static}/images/barba-caracruz/coin.jpeg" alt="">
  <figcaption>
    Figura 1. Condiciones iniciales del lanzamiento de una moneda precesante, incluyendo el vector normal a la superficie de la moneda y el vector momento angular..
  </figcaption>
</figure>

En valores intermedios $0<\psi_0<\pi/2$, la probabilidad es variable (ver figura 3 de <a class="nn-cite" href="#dhs">[1]</a>). En particular, si $\psi_0<\pi/4$ la probabilidad de que salga el mismo lado desde que se lanzó es igual a 1, resultado utilizado por magos y aficionados a las apuestas desde tiempos inmemoriales.

Un corolario interesante de este resultado es que, si los seres humanos no somos perfectamente precisos al lanzar una moneda al aire, y ocurre que $\psi_0\neq\pi/2$, esperamos que haya un sesgo: si la moneda enseñaba el lado cara, es más probable que el resultado sea cara. Utilizando cámaras de alta resolución, y utilizando 27 lanzamientos hechos por humanos, Diaconis, Holmes y Montgomery midieron el ángulo inicial $\psi_0$ y usando su modelo, infirieron una probabilidad $p(\textrm{mismo lado})\approx0.51$.

## El experimento
En 2023, F. Bartoš et al. <a class="nn-cite" href="#cointossers">[2]</a> lanzaron 350.757 monedas al aire y anotaron el lado inicial y el resultado final. Se aseguraron de utilizar muchos lanzadores, distintos tipos de moneda y denominación, para asegurar variabilidad tanto en el lanzamiento como en las caractarísticas físicas de la moneda. Curiosamente, no encontraron ningún tipo de sesgo que favorezca cara o cruz en el lanzamiento, en ese sentido el azar exacto del 50% sigue vigente.   Sin embargo, obtuvieron 178.079 resultados en los que el lado inicial y el final eran el mismo. Podéis comprobar vosotros mismos en la aplicación de arriba la probabilidad de que eso ocurra, asumiendo que el resultado final es independiente del lado inicial ($p(\textrm{mismo lado})=0.5$). Es un resultado prácticamente imposible, sobre todo comparado con los resultados más probables que están en torno a 175.378 veces ($M/2$) en las que coincide el lado inicial con el final. En otras palabras, $p(\textrm{mismo lado})=0.5077$. La evidencia bayesiana --este concepto lo dejamos para otra servilleta-- es enorme a favor de que existe un sesgo a favor de conservar el lado inicial.

Otro resultado interesante es que el sesgo --según DHS el ángulo $\psi_0$-- varía en función del lanzador, y en general observan que los lanzadores aprenden, y mejoran, acercándose más a $\psi_0=\pi/2$ cuantas más monedas lancen.

Este experimento ha confirmado la existencia de un sesgo favorable al lado inicial que ya había sido predicho por <a class="nn-cite" href="#dhs">[1]</a>. Lo que no ha sucedido todavía es una confirmación experimental del modelo DHS. Para lo cual haría falta lanzar una cantidad de monedas similar a la de <a class="nn-cite" href="#cointossers">[2]</a>, pero no solo medir el resultado del lanzamiento sino también medir --o controlar usando una máquina que lance la moneda de forma automática-- el ángulo $\psi_0$. Solo así podríamos evaluar experimentalmente la relación entre la probabilidad y el ángulo inicial. 

## Referencias

  <li id="dhs">
    P. Diaconis, S. Holmes y R. Montgomery (2007). Dynamical Bias in the Coin Toss, <em>Society for Industrial and Applied Mathematics review</em>, 49, 2, 211-235. 
    <a href="https://www.stat.berkeley.edu/~aldous/157/Papers/diaconis_coinbias.pdf" target="_blank" rel="noopener noreferrer">https://www.stat.berkeley.edu/~aldous/157/Papers/diaconis_coinbias.pdf</a>
  </li>

  <li id="cointossers">
    F. Bartoš et al. (2025). Fair Coins Tend to Land on the Same Side They Started: Evidence from 350,757 Flips. <em>Journal of the American Statistical Association</em>, 120, 552, 2118-2127.
    <a href="https://doi.org/10.1080/01621459.2025.2516210" target="_blank" rel="noopener noreferrer">https://doi.org/10.1080/01621459.2025.2516210</a>
  </li>
