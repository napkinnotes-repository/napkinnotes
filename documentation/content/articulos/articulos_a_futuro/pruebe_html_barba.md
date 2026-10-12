---
title: aaa                # vuestro título
author: aaa               # mismo nombre que en la tarjeta de autor
date: 2026-03-15          # formato YYYY-MM-DD
layout: articles
slug: prueba-barba
status: hidden            # published si ya está listo
category: Aaa             # categoría con mayúscula inicial
tags:                     # tags con minúscula inicial
  - bla
  - blabla
  - bli bli
summary: aaaaa                         # 1-2 frases cortas para la tarjeta del artículo
image: images/nombre_de_la_imagen.jpeg # imagen principal del artículo  ¡¡¡¡¡¡¡¡TIENE QUE SER JPEG EL FORMATO!!!!!
certificate: true
---

[TOC]



## HTML A

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Combinaciones</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 40px;
    }

    .card {
      width: 340px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background: #ffffff;
      padding: 16px 18px 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

    .card h3 {
      margin-top: 0;
      margin-bottom: 8px;
      font-size: 20px;
    }

    .buttons button {
      padding: 6px 12px;
      margin-right: 10px;
      border: 1px solid #888;
      border-radius: 4px;
      background: #f0f0f0;
      cursor: pointer;
      font-size: 14px;
    }

    .buttons button:hover:enabled {
      background: #e4e4e4;
    }

    .buttons button:disabled {
      cursor: not-allowed;
      opacity: 0.6;
    }

    #counter {
      margin-top: 10px;
      font-size: 14px;
      line-height: 1.4;
    }

    #step {
      margin-top: 10px;
      font-size: 14px;
      font-weight: bold;
      min-height: 20px;
    }

    #multiplication {
      margin-top: 10px;
      font-size: 14px;
    }

    #permutations-count {
      margin-top: 8px;
      font-size: 14px;
      font-weight: bold;
    }

    .slots {
      display: flex;
      gap: 8px;
      margin-top: 16px;
    }

    .slot {
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

    .cara1 { background: #ff4d4d; color: #fff; }
    .cara2 { background: #4caf50; color: #fff; }
    .cara3 { background: #2196f3; color: #fff; }
    .cruz1 { background: #ffeb3b; color: #000; }
    .cruz2 { background: #9c27b0; color: #fff; }

    .neutral {
      background: #e0e0e0 !important;
      color: #000 !important;
    }

    #explanation {
      margin-top: 16px;
      font-size: 14px;
      color: #444;
      line-height: 1.5;
      min-height: 80px;
    }

    .control-buttons {
      margin-top: 16px;
      display: none;
    }

    .control-buttons button {
      margin-right: 10px;
      padding: 6px 10px;
      font-size: 13px;
      border-radius: 4px;
      border: 1px solid #666;
      background: #f0f0f0;
      cursor: pointer;
    }

    .control-buttons button:hover {
      background: #e4e4e4;
    }
  </style>
</head>
<body>
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
</body>
</html>


--- 

## HTML B

<div id="coin-probability-sidebar" 
     style="border:1px solid #ddd;
            padding:16px;
            width:260px;
            background:#fafafa;
            font-family:Arial, sans-serif;">
  
  <h3 style="margin-top:0;">Cara o cruz</h3>

  <label style="font-size:14px;">Número de lanzamientos:</label>
  <input id="num-flips" type="number" min="0"
         style="width:100%;padding:8px;font-size:14px;margin-bottom:10px;">

  <label style="font-size:14px;">Número de caras:</label>
  <input id="num-heads" type="number" min="0"
         style="width:100%;padding:8px;font-size:14px;margin-bottom:10px;">

  <label style="font-size:14px;">Probabilidad de que salga cara (p):</label>
  <select id="prob-heads"
          style="width:100%;padding:8px;font-size:14px;margin-bottom:10px;">
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

  <button onclick="calcBinomialProb()" 
          style="margin-top:10px;width:100%;padding:8px;font-size:14px;">
    Calcular
  </button>

  <p id="result" 
     style="margin-top:12px;font-weight:bold;font-size:14px;"></p>
</div>

<script>
function factorial(n) {
  let result = 1;
  for (let i = 2; i <= n; i++) result *= i;
  return result;
}

function binomial(n, k) {
  return factorial(n) / (factorial(k) * factorial(n - k));
}

function calcBinomialProb() {
  const n = parseInt(document.getElementById("num-flips").value);
  const k = parseInt(document.getElementById("num-heads").value);
  const p = parseFloat(document.getElementById("prob-heads").value);

  if (isNaN(n) || isNaN(k) || k > n || n < 0 || k < 0) {
    document.getElementById("result").innerText = "Ingresa números válidos (k ≤ n).";
    return;
  }

  // Fórmula general: P = C(n,k) * p^k * (1-p)^(n-k)
  const prob = binomial(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);

  document.getElementById("result").innerText =
    `P(${k} caras en ${n} lanzamientos con p=${p}) = ${prob} (${(prob * 100).toFixed(6)}%).`;
}
</script>
---


## Referencias

<ol class="nn-references">
  <li id="ref-1">
    Autor, A. (Año). Título del artículo. <em>Revista o libro</em>.
    <a href="https://doi.org/..." target="_blank" rel="noopener noreferrer">https://doi.org/...</a>
  </li>

  <li id="ref-2">
    Autor, B. (Año). Otro título. <em>Revista o libro</em>.
    <a href="https://doi.org/..." target="_blank" rel="noopener noreferrer">https://doi.org/...</a>
  </li>
</ol>
