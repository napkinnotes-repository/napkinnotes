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



## Sección


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
