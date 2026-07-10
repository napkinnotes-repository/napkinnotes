---
title: "La rebelión de los fractales I I: crea tu propio fractal y descubre su dimensión"
author: Paz Albares Vicente
date: 2026-07-16
layout: articles
slug: prueba-interactivo
status: hidden
category: Matemáticas
tags:
  - fractales
  - matemáticas
summary: La naturaleza posee una estructura profundamente fractal. ¡Vamos a comprobarlo! En esta servilleta te enseñamos un truco muy sencillo para calcular la dimensión fractal de todo lo que te rodea. Desde descubrir las formas que dibuja la leche en tu café por las mañanas hasta entender por qué un paseo por la playa siempre parece más largo de lo que dice el mapa.
image: images/nombre_de_la_imagen.png
---

[TOC]

¡Bienvenido a la segunda servilleta sobre fractales! En el [artículo anterior](https://napkinnotes.es/la-rebelion-de-los-fractales-i-y-si-las-dimensiones-tuvieran-decimales) nos adentramos, desafiando la intuición, en el universo de las dimensiones fraccionarias y la geometría fractal. Descubrimos que a figuras ideales como el triángulo de Sierpinski o el copo de nieve de Koch les gusta vivir en un lugar de dimensiones intermedias, son más que una línea, pero menos que una superficie plana. A estos objetos los llamamos fractales.

Sin embargo, estas figuras, que denominamos autosimilares, tienen una pequeña trampa. Son fractales matemáticos perfectos, que se construyen aplicando una “receta” concreta y repitiéndola de forma idéntica hasta el infinito. Pero, salgamos un momento de la pantalla del ordenador y miremos a nuestro alrededor. Las nubes no son esferas perfectas, las montañas no son conos o pirámides regulares y las hojas de los helechos no repiten un patrón algorítmico exacto. ¿Significa eso que la geometría fractal no puede representar la realidad? Todo lo contrario, significa que necesitamos una herramienta diferente para medir la rugosidad del mundo. ¡Bienvenidos al método definitivo para calcular la dimensión de cualquier objeto: el **método de box-counting** (o conteo de cajas, si lo traducimos)!

## ¿Cuánto mide la costa de Gran Bretaña? 

En 1967, B. Mandelbrot publicó un artículo con un título más que curioso: *¿Cuánto mide la costa de Gran Bretaña?* <a class="nn-cite" href="#ref-1">[1]</a>. A primera vista, la respuesta parece sencilla, basta con consultar un mapa oficial o una base de datos cartográfica y buscar el número de kilómetros. Pero Mandelbrot, apoyándose en estudios previos del geógrafo Lewis Richardson, demostró que el problema es mucho más profundo de lo que parece: la longitud de una costa depende exclusivamente del tamaño de la regla que uses para medirla.

- Si utilizas una regla muy grande, de decenas de kilómetros por ejemplo, sólo capturas la forma general del litoral, y pasarás por alto bahías y golfos pequeños o penínsulas menores. El resultado es una costa relativamente “suave” y corta.
- Si reduces la escala y mides con una regla de un metro, te verás obligado a rodear cada curva, cada roca y cada recodo. La longitud total crece considerablemente.
- Y si sigues afinando la medida, usando una regla cada vez más pequeña, el nivel de detalle aumenta sin parar.

![Britain-fractal-coastline-combined]({static}/images/Britain-fractal-coastline-combined.png)

*Fig. 1: Costa de la isla de Gran Bretaña, medida con reglas de 200, 100 y 50 km, respectivamente. Fuente: Avsa y Acadac, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Britain-fractal-coastline-combined.jpg), licencia CC BY-SA 3.0.*

Si llevamos este proceso al límite matemático y usamos una regla infinitamente pequeña, la longitud de la costa tiende a infinito. La isla de Gran Bretaña ocupa un espacio limitado y definido en el océano, pero su frontera es infinitamente larga. ¿A qué nos recuerda este comportamiento? ¡Coincide exactamente con lo que le sucedía al copo de nieve de Koch! A lo mejor estos objetos no son tan diferentes…

Mandelbrot llegó entonces a la conclusión de que intentar medir la longitud de un objeto real no tiene sentido, ya que depende del instrumento y de su escala. Lo relevante no es su longitud, sino el grado de irregularidad de su forma, su “rugosidad”. Para capturar esa idea, reformuló la manera de entender la dimensión geométrica, dando lugar a herramientas como el método de *box-counting*.

## Dibuja tu propia curva fractal

Desde Napkin Notes hemos desarrollado esta herramienta interactiva que permite dibujar libremente y explorar su dimensión fractal. Ponte creativo y haz un dibujo a mano alzada, puede ser todo lo complejo que quieras, lo importante es que sea “rugoso”. Puedes levantar el lápiz de la pantalla y seguir dibujando. Cuando esté listo, presiona el botón de “Calcular dimensión fractal”, y listo, ¡acabas de construir tu primera curva fractal!. La herramienta te permite descargar tu creación si así lo deseas.

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Laboratorio Fractal Interactivo</title>
<style>
.fractal-app{font-family:sans-serif;width:95%;max-width:600px;margin:15px auto;text-align:center;color:#1e293b;background:#fff;padding:20px;border-radius:12px;box-shadow:0 10px 25px rgba(0,0,0,.05);box-sizing:border-box}
.fractal-app canvas{background:#fff;border:2px dashed #cbd5e1;cursor:crosshair;touch-action:none;display:block;width:100%;height:auto;border-radius:6px;margin:0 auto 15px;box-sizing:border-box;user-select:none;-webkit-user-select:none}
.fractal-controls{margin-top:15px;display:flex;justify-content:center;width:100%}
.fractal-btn-group{width:100%;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;align-items:center}
.fractal-app button{padding:10px 14px;font-weight:bold;background:#fff;border-radius:6px;cursor:pointer;font-size:.85em;border:2px solid transparent;-webkit-tap-highlight-color:transparent}
.fractal-app button:active{transform:scale(.97)}
.fractal-clear{color:#475569;border-color:#cbd5e1!important}
.fractal-calc{color:#b81424;border-color:#b81424!important}
.fractal-download{color:#2563eb;border-color:#2563eb!important}
.fractal-clear:hover{background:#f1f5f9}
.fractal-calc:hover{background:#fdf2f2}
.fractal-download:hover{background:#eff6ff}
.fractal-result{display:none;margin-top:15px;font-size:1.2em;font-weight:bold;color:#b81424;background:#fdf2f2;padding:12px;border-radius:8px;border:1px solid #fbd5d5;width:100%;box-sizing:border-box;line-height:1.5}
.fractal-cube{vertical-align:middle;margin-right:8px}
</style>
</head>
<body>

<div class="fractal-app">
<h3>✏️ Haz un dibujo</h3>
<canvas id="fractalCanvas" width="800" height="800"></canvas>

<div class="fractal-controls">
<div class="fractal-btn-group">
<button class="fractal-clear" id="fractalReset">🔄 Reiniciar</button>
<button class="fractal-calc" id="fractalCalculate">🔮 Calcular dimensión fractal</button>
<button class="fractal-download" id="fractalDownload">📥 Descargar</button>
</div>
</div>

<div class="fractal-result" id="fractalResult"></div>
</div>

<canvas id="fractalHidden" width="800" height="800" style="display:none"></canvas>

<script>
(function(){

const canvas=document.getElementById("fractalCanvas"),
ctx=canvas.getContext("2d"),
hidden=document.getElementById("fractalHidden"),
hctx=hidden.getContext("2d"),
result=document.getElementById("fractalResult"),
reset=document.getElementById("fractalReset"),
calc=document.getElementById("fractalCalculate"),
download=document.getElementById("fractalDownload");

let drawing=false,painted=false;

const cube=`<svg class="fractal-cube" width="24" height="24" viewBox="0 0 24 24"><polygon points="12,2 21,7.2 12,12.4 3,7.2" fill="#ff4d5a"/><polygon points="3,7.2 12,12.4 12,22 3,16.8" fill="#d92635"/><polygon points="12,12.4 21,7.2 21,16.8 12,22" fill="#b81424"/></svg>Dimensión fractal: <span style="color:#b81424"><b id="dimension">0.00</b></span>`;

function init(){
ctx.fillStyle=hctx.fillStyle="#fff";
ctx.fillRect(0,0,800,800);
hctx.fillRect(0,0,800,800);

ctx.strokeStyle=hctx.strokeStyle="#000";
ctx.lineWidth=hctx.lineWidth=2;
ctx.lineCap=hctx.lineCap="round";
ctx.lineJoin=hctx.lineJoin="round";

ctx.imageSmoothingEnabled=false;
hctx.imageSmoothingEnabled=false;

drawing=false;
painted=false;
result.style.display="none";
result.innerHTML="";
}

function pos(e){
let r=canvas.getBoundingClientRect();
return{
x:(e.clientX-r.left)*800/r.width,
y:(e.clientY-r.top)*800/r.height
};
}

canvas.addEventListener("pointerdown",e=>{
e.preventDefault();
canvas.setPointerCapture(e.pointerId);
drawing=true;
painted=true;

let p=pos(e);
ctx.beginPath();
hctx.beginPath();
ctx.moveTo(p.x,p.y);
hctx.moveTo(p.x,p.y);
});

canvas.addEventListener("pointermove",e=>{
if(!drawing)return;

let p=pos(e);
ctx.lineTo(p.x,p.y);
hctx.lineTo(p.x,p.y);
ctx.stroke();
hctx.stroke();
});

canvas.addEventListener("pointerup",()=>drawing=false);
canvas.addEventListener("pointercancel",()=>drawing=false);
canvas.addEventListener("pointerleave",()=>drawing=false);

function downloadCanvas(){
let a=document.createElement("a");
a.download="curva_fractal.png";
a.href=hidden.toDataURL("image/png");
document.body.appendChild(a);
a.click();
a.remove();
}

function calculate(){
calc.disabled=true;
result.style.display="block";
result.innerHTML="⏳ Calculando...";

if(!painted){
result.innerHTML="⚠️ ¡El lienzo está vacío, dibuja algo primero!";
calc.disabled=false;
return;
}

let data=hctx.getImageData(0,0,800,800).data,
sizes=[4,8,12,16,20,24,28,32,36],
x=[],y=[];

sizes.forEach(s=>{
let used=0;

for(let j=0;j<800;j+=s){
for(let i=0;i<800;i+=s){

let found=false;

for(let yy=0;yy<s&&!found&&j+yy<800;yy++){
for(let xx=0;xx<s&&i+xx<800;xx++){

if(data[((j+yy)*800+i+xx)*4]<128){
found=true;
break;
}

}
}

if(found)used++;

}
}

if(used){
x.push(Math.log(1/s));
y.push(Math.log(used));
}

});

let n=x.length;

if(n<2){
calc.disabled=false;
return;
}

let sx=0,sy=0,sxy=0,sxx=0;

for(let i=0;i<n;i++){
sx+=x[i];
sy+=y[i];
sxy+=x[i]*y[i];
sxx+=x[i]*x[i];
}

let d=Math.abs((n*sxy-sx*sy)/(n*sxx-sx*sx));

if(d<1)d=1;
if(d>2)d=2;

result.innerHTML=cube;
document.getElementById("dimension").innerText=d.toFixed(2);

calc.disabled=false;
}

reset.addEventListener("click",init);
calc.addEventListener("click",calculate);
download.addEventListener("click",downloadCanvas);

init();

})();
</script>

</body>
</html>


<br>
¿Cómo hemos sido capaces de determinar esta dimensión? ¡Te lo cuento en las siguientes secciones!

## De la geometría al recuento de cajas

El método de *box-counting* es un algoritmo universal <a class="nn-cite" href="#ref-2">[2]</a><a class="nn-cite" href="#ref-3">[3]</a>, nos sirve para cualquier tipo de forma, y no necesita que el objeto tenga una fórmula matemática detrás o una simetría determinada. 

Imagina que tomamos la silueta irregular de la costa de la isla de Gran Bretaña, definiendo una curva cerrada en el plano. Ahora, en ese mismo plano, ponemos una cuadrícula transparente, formada por cuadrados (*cajas*) de lado $\epsilon$. Sin mucho problema, podemos contar cuántas de estas cajas contienen parte de la curva de estudio. La pregunta es, ¿cómo varía este número de cajas al modificar el tamaño de la cuadrícula? Si te das cuentas, lo que estamos haciendo es construir una manera ingeniosa de efectuar y cuantificar un “cambio de escala” para objetos irregulares. El procedimiento es el siguiente:

1. Colocamos la cuadrícula con un tamaño de caja $\epsilon$.
2. Contamos cuántas cajas contienen, al menos, un fragmento de la curva. Llamaremos $N(\epsilon)$ a este número. 
3. Ahora duplicamos el tamaño de la curva, y contamos cuántas cajas están ocupadas por el nuevo objeto. Esto es equivalente a reducir el tamaño de la caja a la mitad $\frac{\epsilon}{2}$ (hacemos la cuadrícula más fina), y volver a contar cajas.
4. Repetimos este proceso, utilizando cuadrículas con cuadrados de lado cada vez más pequeño, lo que genera parejas de valores $(\epsilon, N)$. 

Por ejemplo, para la costa de Gran Bretaña, obtenemos lo siguiente:

![GB_3]({static}/images/GB_3.png)

*Fig. 2: Estimación de la dimensión fractal de la costa de Gran Bretaña mediante el método de box-counting.*

La información relevante aquí no es tanto el valor concreto de $N$, sino la rapidez con la que crece al aumentar la resolución. Este crecimiento sigue aproximadamente una ley potencial del tipo,
$$
N(\epsilon) \approx c\epsilon^{-d},
\tag{1}
$$
donde $d$ es la dimensión (fractal) de *box-counting* y $c$ es una constante de proporcionalidad. En lugar de suponer que esta relación se cumple exactamente, la dimensión de *box-counting* se define de forma que extrae ese posible exponente de crecimiento:
$$
d=-\lim_{\epsilon\to 0}\frac{\ln N}{\ln\epsilon}=\lim_{\epsilon\to 0} \frac{\ln N}{\ln \frac{1}{\epsilon}}
$$

## ¿Y si linealizamos?

A continuación, nos preguntamos: dado un conjunto de datos $(\epsilon,N)$, ¿cómo podemos calcular nosotros empíricamente este valor de $d$? Suponiendo que la ley potencial (1) es exacta, podemos despejar $d$ tomando logaritmos neperianos a cada lado de la igualdad
$$
N= c \epsilon^{-d}\quad\Rightarrow\quad \ln N=-d\ln \epsilon +\ln c=d\ln\left(\frac{1}{\epsilon}\right) +\ln c.
$$
Esta operación transforma la ley potencial anterior en la ecuación de una recta del tipo $y=m\cdot x+n$, donde, si comparamos coeficientes, las $x$ representan la cantidad $\ln\left(\frac{1}{\epsilon}\right)$, las $y$ son el $\ln N$, la pendiente de la recta es $m=d$ y la ordenada en el origen es $n=\ln c$. Si ahora, partiendo de nuestros datos $(\epsilon,N)$, calculamos las parejas de valores $\left(\ln \frac{1}{\epsilon},\ln N\right)$ y las representamos en un plano cartesiano ($\ln \frac{1}{\epsilon}$ en el eje $x$ y $\ln N$ en el eje $y$), estos datos deberían seguir una tendencia lineal. Los parámetros de esta recta de regresión se pueden calcular fácilmente mediante una técnica denominada *ajuste por mínimos cuadrados* <a class="nn-cite" href="#ref-4">[4]</a><a class="nn-cite" href="#ref-5">[5]</a>. La pendiente de esta recta es, aproximadamente, la dimensión fractal $d$. 

Si dibujas una línea recta perfecta en un papel y le aplicas este algoritmo, la pendiente debería dar un número próximo a $d = 1$ (si tienes muchos datos, idealmente dará 1). Si rellenas por completo una forma sólida, el espacio bidimensional se ocupará por completo y la pendiente dará $d = 2$. Para las costas reales del planeta, debido a sus entrantes y salientes, este algoritmo devuelve valores intermedios, es decir, una dimensión fraccionaria. La costa de Gran Bretaña tiene una dimensión aproximada de $1.25$, mientras que las costas de Noruega, muy accidentadas por sus fiordos, alcanzan una dimensión de *box-counting* cercana a $1.52$ <a class="nn-cite" href="#ref-1">[1]</a>. Así, las matemáticas demuestran lo que tus piernas ya sospechaban: a mayor dimensión fractal, más recodos esconde la costa y más se alarga un paseo que el mapa resumía en un simple trazo.

## Pruébalo tú mismo: ¡vayamos al laboratorio!

Te presentamos la siguiente simulación interactiva, inspirada el recurso del Proyecto Descartes <a class="nn-cite" href="#ref-6">[6]</a>, que te permitirá experimentar con el método de *box-counting* tal y como hemos explicado más arriba. Te explico cómo funciona: 

- La herramienta permite que realices un dibujo a mano alzada o bien que subas una imagen de una figura bidimensional. Esta herramienta está pensada para analizar curvas en el plano, con lo que, si subes una imagen, ésta debe ser preferiblemente en blanco y negro. Al subir una imagen compleja a color, la herramienta puede no procesar correctamente los píxeles, dando lugar a resultados erróneos. 
- Cuando el dibujo esté cargado, el programa genera una cuadrícula con cajas de tamaño $\epsilon=16\,\text{px}$ por defecto, y es capaz de determinar cuántas cajas están ocupadas por un fragmento de curva. Puedes comprobar cómo varía $N$ al modificar $\epsilon$ moviendo el deslizador “Tamaño ($\epsilon$)”.
- Coloca el deslizador en una posición de tu gusto, y presiona el botón “Registrar punto”. El punto seleccionado se registra tanto en la gráfica como en la tabla de valores. Mueve un poco el deslizador, y vuelve a pulsar “Registrar punto”. Repite este proceso unas 6-8 veces, de manera que obtengas varios puntos para distintos tamaños de caja. Es aconsejable cubrir desde escalas grandes hasta escalas pequeñas. Así podrás construir una nube de datos suficientemente representativa para observar la tendencia lineal en el gráfico, que la herramienta realice el ajuste lineal de los datos seleccionados, y así estimar la dimensión fractal del dibujo.
- Cuando la escala es demasiado grande, el recuento de cajas deja de ser fiable. En este caso aparece el mensaje “Escala omitida por saturación, prueba con otro punto”. Modifica la posición del deslizador para seguir registrando puntos.
- La herramienta permite descargar la tabla de datos en formato TXT y la representación gráfica con el ajuste lineal en formato PNG.

Deja volar tu mente, dibuja un rayo, un árbol o un laberinto, y descubre la dimensión fractal de tu propia creatividad. El mundo real es rugoso, y ahora tienes una regla matemática para medirlo.

<style>
  .fractal-app-b {
    font-family: sans-serif;
    max-width: 550px;
    margin: 20px auto;
    text-align: center;
    color: #333;
  }

  .fractal-app-b .canvas-container {
    background: #f3f4f6;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border: 1px solid #d1d5db;
    display: flex;
    flex-direction: column;
    gap: 15px;
    align-items: center;
  }

  .fractal-app-b canvas {
    background: #ffffff;
    border: 2px dashed #9ca3af;
    cursor: crosshair;
    touch-action: none;
    display: block;
    max-width: 100%;
    height: auto;
  }

  #chartCanvasB {
    background: #fafafa;
    border: 1px solid #cbd5e1;
    cursor: default;
  }

  .fractal-app-b .controls {
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: center;
    background: #fafafa;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid #e5e7eb;
    width: 100%;
    box-sizing: border-box;
  }

  .fractal-app-b .slider-box {
    display: flex;
    align-items: center;
    gap: 10px;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }

  .fractal-app-b .btn-group {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .fractal-app-b button {
    padding: 10px 15px;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
  }

  .fractal-app-b .btn-clear {
    background: #e5e7eb;
    color: #1f2937;
    border: 1px solid #9ca3af;
  }

  .fractal-app-b .btn-add {
    background: #2563eb;
    color: white;
  }

  .fractal-app-b .result-box {
    margin-top: 15px;
    font-size: 1.25em;
    font-weight: bold;
    color: #1e3a8a;
    background: #e0f2fe;
    padding: 12px;
    border-radius: 6px;
    border: 1px solid #bae6fd;
    width: 100%;
    box-sizing: border-box;
    line-height: 1.5;
  }

  .fractal-app-b input[type="range"] {
    width: 45%;
    cursor: pointer;
  }

  @media (max-width: 760px) {
    .fractal-app-b input[type="range"] {
      width: 100%;
    }
  }
</style>

<div class="fractal-app-b">
  <h3>🔬 Laboratorio dinámico de box-counting</h3>

  <p style="font-size: 0.85em; margin-bottom: 15px; line-height: 1.4;">
    1. Haz tu dibujo libremente en el lienzo blanco.<br>
    2. Mueve el deslizador y pulsa <b>“📌 Registrar punto actual”</b> en diferentes escalas para crear tu propia gráfica.
  </p>

  <div class="canvas-container">
    <div>
      <canvas id="chaosCanvasB" width="400" height="300"></canvas>
    </div>

    <div>
      <canvas id="chartCanvasB" width="400" height="220"></canvas>
    </div>
  </div>

  <div class="controls">
    <div class="slider-box">
      <label for="boxSliderB">
        <b>Escala de rejilla ε:</b> <span id="sizeValB">30</span> px
      </label>
      <input type="range" id="boxSliderB" min="8" max="100" value="30">
    </div>

    <div class="btn-group">
      <button class="btn-clear" id="resetBtnB" type="button">🗑️ Reiniciar</button>
      <button class="btn-add" id="addPointBtnB" type="button">📌 Registrar punto actual</button>
    </div>
  </div>

  <div class="result-box" id="resultTextB">
    ⚡ Haz un dibujo sobre el lienzo blanco para comenzar.
  </div>
</div>

<canvas id="hiddenCanvasB" width="400" height="300" style="display:none;"></canvas>

<script>
(function () {
  const canvas = document.getElementById("chaosCanvasB");
  const ctx = canvas.getContext("2d");

  const hiddenCanvas = document.getElementById("hiddenCanvasB");
  const hCtx = hiddenCanvas.getContext("2d");

  const chartCanvas = document.getElementById("chartCanvasB");
  const chartCtx = chartCanvas.getContext("2d");

  const slider = document.getElementById("boxSliderB");
  const sizeVal = document.getElementById("sizeValB");
  const resultText = document.getElementById("resultTextB");

  const resetBtn = document.getElementById("resetBtnB");
  const addPointBtn = document.getElementById("addPointBtnB");

  let drawing = false;
  let hasPintado = false;
  let registeredPoints = [];
  let currentBoxesCount = 0;

  function initCanvases() {
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    hCtx.fillStyle = "#ffffff";
    hCtx.fillRect(0, 0, hiddenCanvas.width, hiddenCanvas.height);

    hCtx.strokeStyle = "#000000";
    hCtx.lineWidth = 4;
    hCtx.lineCap = "round";
    hCtx.lineJoin = "round";

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

    return {
      x: clientX - rect.left,
      y: clientY - rect.top
    };
  }

  function startDrawing(e) {
    drawing = true;
    hasPintado = true;

    const pos = getPos(e);
    hCtx.beginPath();
    hCtx.moveTo(pos.x, pos.y);
  }

  function draw(e) {
    if (!drawing) return;

    const pos = getPos(e);
    hCtx.lineTo(pos.x, pos.y);
    hCtx.stroke();
    drawGrid();
  }

  function stopDrawing() {
    drawing = false;
    drawGrid();
  }

  canvas.addEventListener("mousedown", startDrawing);
  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mouseup", stopDrawing);
  canvas.addEventListener("mouseleave", stopDrawing);

  canvas.addEventListener("touchstart", function (e) {
    e.preventDefault();
    startDrawing(e);
  });

  canvas.addEventListener("touchmove", function (e) {
    e.preventDefault();
    draw(e);
  });

  canvas.addEventListener("touchend", function (e) {
    e.preventDefault();
    stopDrawing();
  });

  slider.addEventListener("input", function () {
    sizeVal.innerText = slider.value;
    drawGrid();
  });

  function drawGrid() {
    ctx.fillStyle = "#ffffff";
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

        for (let by = 0; by < boxSize && y + by < h; by++) {
          for (let bx = 0; bx < boxSize && x + bx < w; bx++) {
            const idx = ((y + by) * w + (x + bx)) * 4;

            if (
              imgData[idx] < 220 &&
              imgData[idx + 1] < 220 &&
              imgData[idx + 2] < 220
            ) {
              hasBlackPixel = true;
              break;
            }
          }

          if (hasBlackPixel) break;
        }

        if (hasBlackPixel) {
          ctx.fillStyle = "rgba(37, 99, 235, 0.22)";
          ctx.fillRect(x, y, boxSize, boxSize);
          ctx.strokeStyle = "rgba(37, 99, 235, 0.5)";
          currentBoxesCount++;
        } else {
          ctx.strokeStyle = "rgba(156, 163, 175, 0.12)";
        }

        ctx.lineWidth = 1;
        ctx.strokeRect(x, y, boxSize, boxSize);
      }
    }

    if (hasPintado && !drawing) {
      updateResultUI();
    }
  }

  function recordCurrentPoint() {
    if (!hasPintado || currentBoxesCount === 0) {
      resultText.innerHTML = "⚠️ Primero dibuja algo en el lienzo.";
      return;
    }

    const boxSize = parseInt(slider.value);
    const valX = Math.log(1 / boxSize);
    const valY = Math.log(currentBoxesCount);

    if (registeredPoints.some(function (p) { return p.size === boxSize; })) {
      resultText.innerHTML = "⚠️ El tamaño de " + boxSize + " px ya está registrado.";
      return;
    }

    registeredPoints.push({
      size: boxSize,
      x: valX,
      y: valY
    });

    registeredPoints.sort(function (a, b) {
      return a.x - b.x;
    });

    updateCalculationsAndChart();
  }

  function updateCalculationsAndChart() {
    const logX = registeredPoints.map(function (p) { return p.x; });
    const logY = registeredPoints.map(function (p) { return p.y; });
    const n = registeredPoints.length;

    if (n < 2) {
      drawNativeChart(logX, logY, null, null);
      updateResultUI();
      return;
    }

    let sX = 0;
    let sY = 0;
    let sXY = 0;
    let sXX = 0;

    for (let i = 0; i < n; i++) {
      sX += logX[i];
      sY += logY[i];
      sXY += logX[i] * logY[i];
      sXX += logX[i] * logX[i];
    }

    const denominator = n * sXX - sX * sX;

    if (denominator === 0) {
      resultText.innerHTML = "⚠️ No se pudo calcular la dimensión. Registra escalas distintas.";
      return;
    }

    const slope = (n * sXY - sX * sY) / denominator;
    const intercept = (sY - slope * sX) / n;
    const d = Math.abs(slope);

    drawNativeChart(logX, logY, slope, intercept);

    resultText.innerHTML =
      "🔲 Puntos registrados: <b>" + n + "</b><br>" +
      "🔮 Dimensión fractal: <span style='color:#ef4444;'><b>" + d.toFixed(2) + "</b></span>";
  }

  function updateResultUI() {
    const boxSize = parseInt(slider.value);
    const nPoints = registeredPoints.length;

    if (nPoints >= 2) {
      updateCalculationsAndChart();
    } else {
      resultText.innerHTML =
        "🔲 Rejilla ε: <b>" + boxSize + " px</b> | Cajas N: <b>" + currentBoxesCount + "</b><br>" +
        "<span style='font-size:0.8em; color:#555; font-weight:normal;'>" +
        "Puntos en gráfica: " + nPoints + "/2 registrados para calcular la recta." +
        "</span>";
    }
  }

  function drawNativeChart(xData, yData, slope, intercept) {
    const W = chartCanvas.width;
    const H = chartCanvas.height;

    chartCtx.clearRect(0, 0, W, H);

    const padLeft = 55;
    const padBottom = 40;
    const padRight = 25;
    const padTop = 25;

    const gW = W - padLeft - padRight;
    const gH = H - padTop - padBottom;

    chartCtx.strokeStyle = "#000000";
    chartCtx.lineWidth = 2;

    chartCtx.beginPath();
    chartCtx.moveTo(padLeft, H - padBottom);
    chartCtx.lineTo(W - padRight, H - padBottom);
    chartCtx.moveTo(padLeft, padTop);
    chartCtx.lineTo(padLeft, H - padBottom);
    chartCtx.stroke();

    chartCtx.fillStyle = "#1e293b";
    chartCtx.font = "bold 11px sans-serif";
    chartCtx.fillText("Eje X: log(1/ε)", W - padRight - 95, H - padBottom + 32);

    chartCtx.save();
    chartCtx.translate(padLeft - 40, padTop + 70);
    chartCtx.rotate(-Math.PI / 2);
    chartCtx.fillText("Eje Y: log(N)", 0, 0);
    chartCtx.restore();

    if (xData.length === 0) {
      chartCtx.strokeStyle = "#e2e8f0";
      chartCtx.lineWidth = 1;

      for (let i = 1; i <= 4; i++) {
        const cx = padLeft + (i / 5) * gW;
        const cy = H - padBottom - (i / 5) * gH;

        chartCtx.beginPath();
        chartCtx.moveTo(cx, H - padBottom);
        chartCtx.lineTo(cx, padTop);
        chartCtx.stroke();

        chartCtx.beginPath();
        chartCtx.moveTo(padLeft, cy);
        chartCtx.lineTo(W - padRight, cy);
        chartCtx.stroke();
      }

      return;
    }

    let minX = Math.min.apply(null, xData);
    let maxX = Math.max.apply(null, xData);
    let minY = Math.min.apply(null, yData);
    let maxY = Math.max.apply(null, yData);

    if (minX === maxX) {
      minX -= 0.5;
      maxX += 0.5;
    }

    if (minY === maxY) {
      minY -= 0.5;
      maxY += 0.5;
    }

    const spanX = maxX - minX;
    const spanY = maxY - minY;

    function toScreen(x, y) {
      return {
        x: padLeft + ((x - minX) / spanX) * gW,
        y: H - padBottom - ((y - minY) / spanY) * gH
      };
    }

    chartCtx.strokeStyle = "#e2e8f0";
    chartCtx.lineWidth = 1;
    chartCtx.fillStyle = "#64748b";
    chartCtx.font = "9px sans-serif";

    for (let i = 0; i <= 4; i++) {
      const factor = i / 4;
      const curX = minX + factor * spanX;
      const curY = minY + factor * spanY;
      const sPt = toScreen(curX, curY);

      chartCtx.beginPath();
      chartCtx.moveTo(sPt.x, H - padBottom);
      chartCtx.lineTo(sPt.x, H - padBottom + 5);
      chartCtx.stroke();

      chartCtx.fillText(curX.toFixed(2), sPt.x - 10, H - padBottom + 16);

      chartCtx.beginPath();
      chartCtx.moveTo(padLeft - 5, sPt.y);
      chartCtx.lineTo(padLeft, sPt.y);
      chartCtx.stroke();

      chartCtx.fillText(curY.toFixed(1), padLeft - 32, sPt.y + 3);
    }

    if (slope !== null) {
      const p1 = toScreen(minX, slope * minX + intercept);
      const p2 = toScreen(maxX, slope * maxX + intercept);

      chartCtx.strokeStyle = "#ef4444";
      chartCtx.lineWidth = 2.5;

      chartCtx.beginPath();
      chartCtx.moveTo(p1.x, p1.y);
      chartCtx.lineTo(p2.x, p2.y);
      chartCtx.stroke();
    }

    chartCtx.fillStyle = "#2563eb";

    for (let i = 0; i < xData.length; i++) {
      const pt = toScreen(xData[i], yData[i]);

      chartCtx.beginPath();
      chartCtx.arc(pt.x, pt.y, 5.5, 0, 2 * Math.PI);
      chartCtx.fill();

      chartCtx.strokeStyle = "#ffffff";
      chartCtx.lineWidth = 1.5;
      chartCtx.stroke();
    }
  }

  function resetCanvas() {
    hasPintado = false;
    drawing = false;
    registeredPoints = [];
    currentBoxesCount = 0;

    slider.value = 30;
    sizeVal.innerText = 30;

    initCanvases();

    resultText.innerHTML = "⚡ Haz un dibujo sobre el lienzo blanco para comenzar.";
  }

  resetBtn.addEventListener("click", resetCanvas);
  addPointBtn.addEventListener("click", recordCurrentPoint);

  initCanvases();
})();
</script>

**Disclaimer**: las herramientas interactivas han sido diseñadas con fines educativos y divulgativos por Paz Albares Vicente, con el soporte de modelos de inteligencia artificial para la generación y optimización de parte del código. Se recomienda usarlas con precaución y revisar los resultados obtenidos. Los resultados pueden contener errores debido a limitaciones del algoritmo, del procesamiento de imágenes o del propio dispositivo utilizado.

## Referencias

<ol class="nn-references">
  <li id="ref-1">
    Mandelbrot, B. B. (1967). How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension. <em>Science</em>, <b>156</b>(3775), 636–638.
    <a href="https://doi.org/10.1126/science.156.3775.636" target="_blank" rel="noopener noreferrer">https://doi.org/10.1126/science.156.3775.636</a>
  </li>

  <li id="ref-2">
    Falconer, K. J. (2014). <em>Fractal geometry: Mathematical foundations and applications</em> (3rd ed.). John Wiley & Sons.
  </li>

  <li id="ref-3">
    Peitgen, H. O., Jürgens, H., & Saupe, D. (2004). <em>Chaos and fractals: New frontiers of science</em> (2nd ed.). Springer-Verlag.
  </li>

  <li id="ref-4">
    Taylor, J. R. (1997). <em>An introduction to error analysis: The study of uncertainties in physical measurements</em> (2nd ed.). University Science Books.
  </li>
  
  <li id="ref-5">
    Bevington, P. R., & Robinson, D. K. (2003). <em>Data reduction and error analysis for the physical sciences</em> (3rd ed.). McGraw-Hill.
  </li>

  <li id="ref-6">
    Cabezudo Bueno, A. (2026). <em>La huella del caos: La estructura de la geometría fractal</em>. Proyecto Descartes, iCartesiLibri. <a href="https://proyectodescartes.org/iCartesiLibri/materiales_didacticos/La_huella_del_caos/index.html" target="_blank" rel="noopener noreferrer">https://proyectodescartes.org/iCartesiLibri/materiales_didacticos/La_huella_del_caos/index.html</a>
  </li>
</ol>
