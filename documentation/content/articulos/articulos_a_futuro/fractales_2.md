---
title: aaa # vuestro título
author: aaa # mismo nombre que en la tarjeta de autor
date: 2026-03-15 # formato YYYY-MM-DD
layout: articles
slug: prueba-interactivo
status: hidden # published si ya está listo
category: aaa # categoría con mayúscula inicial
tags: # tags con minúscula inicial
  - bla
  - blabla
  - bli bli
summary: aaaaa # 1-2 frases cortas para la tarjeta del artículo
image: images/nombre_de_la_imagen.png # imagen principal del artículo
---

[TOC]



## Opcion A


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Laboratorio del Caos: Mide tu Garabato</title>
    <style>
        .fractal-app { font-family: sans-serif; max-width: 500px; margin: 20px auto; text-align: center; }
        .canvas-container { background: #f3f4f6; padding: 10px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #d1d5db; }
        canvas { background: #ffffff; border: 2px dashed #9ca3af; cursor: crosshair; touch-action: none; display: block; margin: 0 auto; }
        .controls { margin-top: 15px; display: flex; gap: 10px; justify-content: center; }
        button { padding: 10px 20px; font-weight: bold; border: none; border-radius: 4px; cursor: pointer; font-size: 0.95em; }
        .btn-clear { background: #e5e7eb; color: #1f2937; border: 1px solid #9ca3af; }
        .btn-calc { background: #2563eb; color: white; }
        .result-box { margin-top: 15px; font-size: 1.2em; font-weight: bold; color: #1e3a8a; background: #e0f2fe; padding: 12px; border-radius: 6px; min-height: 28px; }
    </style>
</head>
<body>

<div class="fractal-app">
    <div class="canvas-container">
        <!-- Lienzo blanco interactivo -->
        <canvas id="chaosCanvas" width="400" height="300"></canvas>
    </div>
    
    <div class="controls">
        <button class="btn-clear" onclick="resetCanvas()">🔄 Reiniciar</button>
        <button class="btn-calc" onclick="analyzeChaos()">📊 Analizar Caos</button>
    </div>

    <div class="result-box" id="result-text">
        ⚡ Haz un garabato abstracto o líneas cruzadas sobre el lienzo blanco.
    </div>
</div>

<script>
const canvas = document.getElementById('chaosCanvas');
const ctx = canvas.getContext('2d');
const resultText = document.getElementById('result-text');
let drawing = false;

// Configuración inicial del lienzo blanco
function initCanvas() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Configuración del trazo en negro grueso y suave
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 4;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
}
initCanvas();

// Función unificada y ultra-segura para calcular la posición del cursor o dedo
function getPos(e) {
    const rect = canvas.getBoundingClientRect();
    let clientX, clientY;
    
    if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
    } else {
        clientX = e.clientX;
        clientY = e.clientY;
    }
    
    return {
        x: clientX - rect.left,
        y: clientY - rect.top
    };
}

// Funciones principales de la acción de dibujar
function startDrawing(e) {
    drawing = true;
    ctx.beginPath();
    const pos = getPos(e);
    ctx.moveTo(pos.x, pos.y);
}

function draw(e) {
    if (!drawing) return;
    const pos = getPos(e);
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
}

function stopDrawing() {
    drawing = false;
    ctx.beginPath();
}

// Vinculación de eventos de Ratón (Ordenadores)
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseleave', stopDrawing);

// Vinculación de eventos Táctiles (Móviles y Tablets)
canvas.addEventListener('touchstart', (e) => { e.preventDefault(); startDrawing(e); });
canvas.addEventListener('touchmove', (e) => { e.preventDefault(); draw(e); });
canvas.addEventListener('touchend', (e) => { e.preventDefault(); stopDrawing(); });

// Función para limpiar la pantalla
function resetCanvas() {
    initCanvas();
    resultText.innerHTML = "⚡ Haz un garabato abstracto o líneas cruzadas sobre el lienzo blanco.";
}

// Algoritmo matemático Box-Counting para calcular la rugosidad fractal
function analyzeChaos() {
    const w = canvas.width, h = canvas.height;
    const imgData = ctx.getImageData(0, 0, w, h).data;
    const grid = Array(h).fill().map(() => new Uint8Array(w));
    let hasData = false;
    
    // Escaneo de píxeles: si no es blanco (255), es trazo del usuario
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            const idx = (y * w + x) * 4;
            if (imgData[idx] < 220 || imgData[idx+1] < 220 || imgData[idx+2] < 220) { 
                grid[y][x] = 1; 
                hasData = true; 
            }
        }
    }

    if (!hasData) {
        resultText.innerHTML = "⚠️ El lienzo está vacío. ¡Dibuja algo primero!";
        return;
    }

    // Muestreo por rejillas cuadradas decrecientes (cajas)
    const sizes = [32, 16, 8, 4];
    const logX = [], logY = [];

    sizes.forEach(s => {
        let boxesUsed = 0;
        for (let y = 0; y < h; y += s) {
            for (let x = 0; x < w; x += s) {
                let match = false;
                for (let by = 0; by < s && (y + by) < h; by++) {
                    for (let bx = 0; bx < s && (x + bx) < w; bx++) {
                        if (grid[y + by][x + bx] === 1) { match = true; break; }
                    }
                    if (match) break;
                }
                if (match) boxesUsed++;
            }
        }
        if (boxesUsed > 0) {
            logX.push(Math.log(1 / s));
            logY.push(Math.log(boxesUsed));
        }
    });

    // Regresión lineal por mínimos cuadrados para hallar la pendiente
    const n = logX.length;
    let sX = 0, sY = 0, sXY = 0, sXX = 0;
    for (let i = 0; i < n; i++) {
        sX += logX[i]; sY += logY[i];
        sXY += logX[i] * logY[i]; sXX += logX[i] * logX[i];
    }
    const d = Math.abs((n * sXY - sX * sY) / (n * sXX - sX * sX));
    
    resultText.innerHTML = `🔮 Dimensión Fractal de tu trazo: <b>${d.toFixed(2)}</b>`;
}
</script>
</body>
</html>

## Opcion B
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Laboratorio Fractal Interactivo Continuo</title>
    <style>
        .fractal-app { font-family: sans-serif; max-width: 550px; margin: 20px auto; text-align: center; color: #333; }
        .canvas-container { background: #f3f4f6; padding: 10px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #d1d5db; display: flex; flex-direction: column; gap: 15px; align-items: center; }
        canvas { background: #ffffff; border: 2px dashed #9ca3af; cursor: crosshair; touch-action: none; display: block; }
        #chartCanvas { background: #fafafa; border: 1px solid #cbd5e1; cursor: default; }
        .controls { margin-top: 15px; display: flex; flex-direction: column; gap: 12px; align-items: center; background: #fafafa; padding: 15px; border-radius: 6px; border: 1px solid #e5e7eb; width: 100%; box-sizing: border-box; }
        .slider-box { display: flex; align-items: center; gap: 10px; width: 100%; justify-content: center; }
        .btn-group { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
        button { padding: 10px 15px; font-weight: bold; border: none; border-radius: 4px; cursor: pointer; font-size: 0.9em; }
        .btn-clear { background: #e5e7eb; color: #1f2937; border: 1px solid #9ca3af; }
        .btn-add { background: #2563eb; color: white; }
        .result-box { margin-top: 15px; font-size: 1.25em; font-weight: bold; color: #1e3a8a; background: #e0f2fe; padding: 12px; border-radius: 6px; border: 1px solid #bae6fd; width: 100%; box-sizing: border-box; line-height: 1.5; }
        input[type=range] { width: 45%; cursor: pointer; }
    </style>
</head>
<body>

<div class="fractal-app">
    <h3>🔬 Laboratorio Dinámico de Box-Counting</h3>
    <p style="font-size: 0.85em; margin-bottom: 15px; line-height: 1.4;">
        1. Haz tu dibujo libremente en el lienzo blanco.<br>
        2. Mueve el deslizador y pulsa <b>"📌 Registrar Punto Actual"</b> en diferentes escalas para crear tu propia gráfica.
    </p>
    
    <div class="canvas-container">
        <!-- Lienzo de Dibujo Superior -->
        <div>
            <canvas id="chaosCanvas" width="400" height="300"></canvas>
        </div>
        
        <!-- Lienzo de la Gráfica de Interpolación Inferior -->
        <div>
            <canvas id="chartCanvas" width="400" height="220"></canvas>
        </div>
    </div>
    
    <div class="controls">
        <div class="slider-box">
            <label for="boxSlider"><b>Escala de Rejilla (ε):</b> <span id="sizeVal">30</span>px</label>
            <input type="range" id="boxSlider" min="8" max="100" value="30">
        </div>
        
        <div class="btn-group">
            <button class="btn-clear" onclick="resetCanvas()">🗑️ Reiniciar</button>
            <button id="addPointBtn" class="btn-add" onclick="recordCurrentPoint()">📌 Registrar Punto Actual</button>
        </div>
    </div>

    <div class="result-box" id="result-text">
        ⚡ Haz un dibujo sobre el lienzo blanco para comenzar.
    </div>
</div>

<!-- Lienzo espejo oculto en memoria para salvar el dibujo original -->
<canvas id="hiddenCanvas" width="400" height="300" style="display:none;"></canvas>
<script>
const canvas = document.getElementById('chaosCanvas');
const ctx = canvas.getContext('2d');
const hiddenCanvas = document.getElementById('hiddenCanvas');
const hCtx = hiddenCanvas.getContext('2d');
const chartCanvas = document.getElementById('chartCanvas');
const chartCtx = chartCanvas.getContext('2d');

const slider = document.getElementById('boxSlider');
const sizeVal = document.getElementById('sizeVal');
const resultText = document.getElementById('result-text');

let drawing = false;
let hasPintado = false;
let registeredPoints = []; 
let currentBoxesCount = 0;

function initCanvases() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    hCtx.fillStyle = '#ffffff';
    hCtx.fillRect(0, 0, hiddenCanvas.width, hiddenCanvas.height);
    
    hCtx.strokeStyle = '#000000';
    hCtx.lineWidth = 4;
    hCtx.lineCap = 'round';
    hCtx.lineJoin = 'round';
    
    drawNativeChart([], [], null, null);
}

function getPos(e) {
    const rect = canvas.getBoundingClientRect();
    let clientX = e.clientX;
    let clientY = e.clientY;
    if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
    }
    return { x: clientX - rect.left, y: clientY - rect.top };
}

canvas.addEventListener('mousedown', (e) => { drawing = true; hasPintado = true; const pos = getPos(e); hCtx.beginPath(); hCtx.moveTo(pos.x, pos.y); });
canvas.addEventListener('mousemove', (e) => { if (!drawing) return; const pos = getPos(e); hCtx.lineTo(pos.x, pos.y); hCtx.stroke(); drawGrid(); });
canvas.addEventListener('mouseup', () => { drawing = false; drawGrid(); });
canvas.addEventListener('mouseleave', () => { drawing = false; });

canvas.addEventListener('touchstart', (e) => { e.preventDefault(); drawing = true; hasPintado = true; const pos = getPos(e); hCtx.beginPath(); hCtx.moveTo(pos.x, pos.y); });
canvas.addEventListener('touchmove', (e) => { e.preventDefault(); if (!drawing) return; const pos = getPos(e); hCtx.lineTo(pos.x, pos.y); hCtx.stroke(); drawGrid(); });
canvas.addEventListener('touchend', () => { drawing = false; drawGrid(); });

slider.addEventListener('input', () => {
    sizeVal.innerText = slider.value;
    drawGrid();
});

function drawGrid() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(hiddenCanvas, 0, 0);

    if (!hasPintado) return;

    const boxSize = parseInt(slider.value);
    const w = canvas.width;
    const h = canvas.height;
    const imgData = hCtx.getImageData(0, 0, w, h).data;
    currentBoxesCount = 0;

    for (let y = 0; y < h; y += boxSize) {
        for (let x = 0; x < w; x += boxSize) {
            let hasBlackPixel = false;
            for (let by = 0; by < boxSize && (y + by) < h; by++) {
                for (let bx = 0; bx < boxSize && (x + bx) < w; bx++) {
                    const idx = ((y + by) * w + (x + bx)) * 4;
                    if (imgData[idx] < 220 && imgData[idx+1] < 220 && imgData[idx+2] < 220) { hasBlackPixel = true; break; }
                }
                if (hasBlackPixel) break;
            }

            if (hasBlackPixel) {
                ctx.fillStyle = 'rgba(37, 99, 235, 0.22)';
                ctx.fillRect(x, y, boxSize, boxSize);
                ctx.strokeStyle = 'rgba(37, 99, 235, 0.5)';
                currentBoxesCount++;
            } else {
                ctx.strokeStyle = 'rgba(156, 163, 175, 0.12)';
            }
            ctx.lineWidth = 1;
            ctx.strokeRect(x, y, boxSize, boxSize);
        }
    }

    if (hasPintado && !drawing) updateResultUI();
}

function recordCurrentPoint() {
    if (!hasPintado || currentBoxesCount === 0) {
        resultText.innerHTML = "⚠️ ¡Primero dibuja algo en el lienzo!";
        return;
    }

    const boxSize = parseInt(slider.value);
    const valX = Math.log(1 / boxSize);
    const valY = Math.log(currentBoxesCount);

    if (registeredPoints.some(p => p.size === boxSize)) {
        resultText.innerHTML = `⚠️ El tamaño de ${boxSize}px ya está registrado en la gráfica.`;
        return;
    }

    registeredPoints.push({ size: boxSize, x: valX, y: valY });
    registeredPoints.sort((a, b) => a.x - b.x);
    updateCalculationsAndChart();
}
function updateCalculationsAndChart() {
    const logX = registeredPoints.map(p => p.x);
    const logY = registeredPoints.map(p => p.y);
    const n = registeredPoints.length;

    if (n < 2) {
        drawNativeChart(logX, logY, null, null);
        updateResultUI();
        return;
    }

    let sX = 0, sY = 0, sXY = 0, sXX = 0;
    for (let i = 0; i < n; i++) {
        sX += logX[i]; sY += logY[i];
        sXY += logX[i] * logY[i]; sXX += logX[i] * logX[i];
    }
    const slope = (n * sXY - sX * sY) / (n * sXX - sX * sX);
    const intercept = (sY - slope * sX) / n;
    const d = Math.abs(slope);

    drawNativeChart(logX, logY, slope, intercept);
    resultText.innerHTML = `🔲 Puntos registrados: <b>${n}</b><br>🔮 Dimensión Fractal: <span style="color:#ef4444;"><b>${d.toFixed(2)}</b></span>`;
}

function updateResultUI() {
    const boxSize = parseInt(slider.value);
    const nPoints = registeredPoints.length;
    if (nPoints >= 2) {
        updateCalculationsAndChart();
    } else {
        resultText.innerHTML = `🔲 Rejilla (ε): <b>${boxSize}px</b> | Cajas (N): <b>${currentBoxesCount}</b><br><span style="font-size:0.8em; color:#555; font-weight:normal;">Puntos en gráfica: ${nPoints}/2 registrados para calcular la recta.</span>`;
    }
}

function drawNativeChart(xData, yData, slope, intercept) {
    const W = chartCanvas.width; const H = chartCanvas.height;
    chartCtx.clearRect(0, 0, W, H);
    
    const padLeft = 55; const padBottom = 40; const padRight = 25; const padTop = 25;
    const gW = W - padLeft - padRight; const gH = H - padTop - padBottom;

    chartCtx.strokeStyle = '#000000';
    chartCtx.lineWidth = 2;
    chartCtx.beginPath();
    chartCtx.moveTo(padLeft, H - padBottom); chartCtx.lineTo(W - padRight, H - padBottom);
    chartCtx.moveTo(padLeft, padTop); chartCtx.lineTo(padLeft, H - padBottom);
    chartCtx.stroke();

    chartCtx.fillStyle = '#1e293b';
    chartCtx.font = 'bold 11px sans-serif';
    chartCtx.fillText("Eje X: log(1/ε)", W - padRight - 80, H - padBottom + 32);
    
    chartCtx.save();
    chartCtx.translate(padLeft - 40, padTop + 45);
    chartCtx.rotate(-Math.PI / 2);
    chartCtx.fillText("Eje Y: log(N)", 0, 0);
    chartCtx.restore();

    if (xData.length === 0) {
        chartCtx.strokeStyle = '#e2e8f0'; chartCtx.lineWidth = 1;
        for(let i=1; i<=4; i++) {
            let cx = padLeft + (i/5)*gW; let cy = H - padBottom - (i/5)*gH;
            chartCtx.beginPath(); chartCtx.moveTo(cx, H-padBottom); chartCtx.lineTo(cx, padTop); chartCtx.stroke();
            chartCtx.beginPath(); chartCtx.moveTo(padLeft, cy); chartCtx.lineTo(W-padRight, cy); chartCtx.stroke();
        }
        return;
    }

    let minX = Math.min(...xData), maxX = Math.max(...xData);
    let minY = Math.min(...yData), maxY = Math.max(...yData);
    if(minX === maxX) { minX -= 0.5; maxX += 0.5; }
    if(minY === maxY) { minY -= 0.5; maxY += 0.5; }
    const spanX = maxX - minX, spanY = maxY - minY;

    function toScreen(x, y) {
        return { x: padLeft + ((x - minX) / spanX) * gW, y: H - padBottom - ((y - minY) / spanY) * gH };
    }

    chartCtx.strokeStyle = '#e2e8f0'; chartCtx.lineWidth = 1;
    chartCtx.fillStyle = '#64748b'; chartCtx.font = '9px sans-serif';

    for (let i = 0; i <= 4; i++) {
        const factor = i / 4;
        const curX = minX + factor * spanX; const curY = minY + factor * spanY;
        const sPt = toScreen(curX, curY);

        chartCtx.beginPath(); chartCtx.moveTo(sPt.x, H - padBottom); chartCtx.lineTo(sPt.x, H - padBottom + 5); chartCtx.stroke();
        chartCtx.fillText(curX.toFixed(2), sPt.x - 10, H - padBottom + 16);

        chartCtx.beginPath(); chartCtx.moveTo(padLeft - 5, sPt.y); chartCtx.lineTo(padLeft, sPt.y); chartCtx.stroke();
        chartCtx.fillText(curY.toFixed(1), padLeft - 32, sPt.y + 3);
    }

    if (slope !== null) {
        chartCtx.strokeStyle = '#ef4444'; chartCtx.lineWidth = 2.5;
        chartCtx.beginPath();
        chartCtx.moveTo(toScreen(minX, slope * minX + intercept).x, toScreen(minX, slope * minX + intercept).y);
        chartCtx.lineTo(toScreen(maxX, slope * maxX + intercept).x, toScreen(maxX, slope * maxX + intercept).y);
        chartCtx.stroke();
    }

    chartCtx.fillStyle = '#2563eb';
    for (let i = 0; i < xData.length; i++) {
        const pt = toScreen(xData[i], yData[i]);
        chartCtx.beginPath(); chartCtx.arc(pt.x, pt.y, 5.5, 0, 2 * Math.PI); chartCtx.fill();
        chartCtx.strokeStyle = '#ffffff'; chartCtx.lineWidth = 1.5; chartCtx.stroke();
    }
}

function resetCanvas() {
    hasPintado = false; drawing = false; registeredPoints = []; currentBoxesCount = 0;
    slider.value = 30; sizeVal.innerText = 30;
    initCanvases();
    resultText.innerHTML = "⚡ Haz un dibujo sobre el lienzo blanco para comenzar.";
}

initCanvases();
</script>
</body>
</html>

<!-- Texto normal -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Sub-Sección

<!-- Preguntas con recuadro bonito -->
> **¿Cuánta el gramo quillo?**
<!-- Fin pregunta con recuadro bonito -->


Fórmulas:

<!-- Fórmula en bloque: en entorno $$ $$, todo es como LaTeX -->
$$
\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + Q_{\text{abs}}
$$

<!-- Fórmula en línea de texto -->
Se puede usar $ \alpha $ como en LaTeX.

<!-- Obsoleto: mejor no usar \( ... \) -->
obsoleto: bla bla bla \(J\) lari lari lari

<!-- Subíndice fuera de entorno matemático -->
c<sub>p</sub>

<!-- Negrita y cursiva -->
Negrita y cursiva: **una paradoja**. *una paradoja*.

<!-- Lista (el espacio entre : y los - es necesario, también con la siguiente linea y el ultimo - tenedlo en cuenta-->
Presentan:

- nanani nanana nanano.  
- abc cba caracola
- Maka make maki

<!-- Citas dentro del texto -->
El texto que queréis referenciar va así <a class="nn-cite" href="#ref-1">[1]</a>.
Otra cita distinta iría así <a class="nn-cite" href="#ref-2">[2]</a>.

<!-- Fin de Sección -->
---


## Otra sección

Texto antes de la imagen.

<!-- Una imagen va así -->
![Descripción de la imagen](images/nombre_de_la_imagen.png)

<!-- Opcional: pie de foto -->
*Figura 1. Breve explicación de la imagen.*

Texto tras la imagen.

<!-- Fin de Sección -->
---


## Conclusiones

Frases finales

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
