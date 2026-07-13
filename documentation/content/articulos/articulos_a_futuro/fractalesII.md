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
image: images/cabecera_fractalesIIv2.png
---

[TOC]

¡Bienvenido a la segunda servilleta sobre fractales! En el [artículo anterior](https://napkinnotes.es/la-rebelion-de-los-fractales-i-y-si-las-dimensiones-tuvieran-decimales) nos adentramos, desafiando la intuición, en el universo de las dimensiones fraccionarias y la geometría fractal. Descubrimos que a figuras ideales como el triángulo de Sierpinski o el copo de nieve de Koch les gusta vivir en un lugar de dimensiones intermedias, son más que una línea, pero menos que una superficie plana. A estos objetos los llamamos fractales.

Sin embargo, estas figuras, que denominamos autosimilares, tienen una pequeña trampa. Son fractales matemáticos perfectos, que se construyen aplicando una “receta” concreta y repitiéndola de forma idéntica hasta el infinito. Pero, salgamos un momento de la pantalla del ordenador y miremos a nuestro alrededor. Las nubes no son esferas perfectas, las montañas no son conos o pirámides regulares y las hojas de los helechos no repiten un patrón algorítmico exacto. ¿Significa eso que la geometría fractal no puede representar la realidad? Todo lo contrario, significa que necesitamos una herramienta diferente para medir la rugosidad del mundo. ¡Bienvenidos al método definitivo para calcular la dimensión de cualquier objeto: el **método de box-counting** (o conteo de cajas, si lo traducimos)!

## ¿Cuánto mide la costa de Gran Bretaña? 

En 1967, B. Mandelbrot publicó un artículo con un título más que curioso: *¿Cuánto mide la costa de Gran Bretaña?* <a class="nn-cite" href="#ref-1">[1]</a>. A primera vista, la respuesta parece sencilla, basta con consultar un mapa oficial o una base de datos cartográfica y buscar el número de kilómetros. Pero Mandelbrot, apoyándose en estudios previos del geógrafo Lewis Richardson, demostró que el problema es mucho más profundo de lo que parece: la longitud de una costa depende exclusivamente del tamaño de la regla que uses para medirla.

- Si utilizas una regla muy grande, de decenas de kilómetros por ejemplo, sólo capturas la forma general del litoral, y pasarás por alto bahías y golfos pequeños o penínsulas menores. El resultado es una costa relativamente “suave” y corta.
- Si reduces la escala y mides con una regla de un metro, te verás obligado a rodear cada curva, cada roca y cada recodo. La longitud total crece considerablemente.
- Y si sigues afinando la medida, usando una regla cada vez más pequeña, el nivel de detalle aumenta sin parar.


<figure class="nn-article-figure">
  <img src="{static}/images/Britain-fractal-coastline-combined.png" alt="Britain-fractal-coastline-combined">
  <figcaption>
Fig. 1: Costa de la isla de Gran Bretaña, medida con reglas de 200, 100 y 50 km, respectivamente. Fuente: Avsa y Acadac, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Britain-fractal-coastline-combined.jpg), licencia CC BY-SA 3.0.
  </figcaption>
</figure>


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
.fractal-app{
font-family:sans-serif;
width:95%;
max-width:600px;
margin:15px auto;
text-align:center;
color:#1e293b;
background:#fff;
padding:20px;
border-radius:12px;
box-shadow:0 10px 25px rgba(0,0,0,.05);
box-sizing:border-box;
}

.fractal-app canvas{
background:#fff;
border:2px solid #e2e8f0;
cursor:crosshair;
touch-action:none;
display:block;
width:100%;
height:auto;
border-radius:8px;
margin:0 auto 15px;
box-sizing:border-box;
user-select:none;
-webkit-user-select:none;
transition:.25s;
box-shadow:inset 0 0 20px rgba(0,0,0,.03);
}

.fractal-app canvas:hover{
border-color:#94a3b8;
}

.fractal-controls{
margin-top:15px;
display:flex;
justify-content:center;
width:100%;
}

.fractal-btn-group{
width:100%;
display:flex;
gap:8px;
flex-wrap:wrap;
justify-content:center;
align-items:center;
}

.fractal-app button{
padding:10px 14px;
font-weight:bold;
background:#fff;
border-radius:6px;
cursor:pointer;
font-size:.85em;
border:2px solid transparent;
-webkit-tap-highlight-color:transparent;
}

.fractal-app button:active{
transform:scale(.97);
}

.fractal-clear{
color:#475569;
border-color:#cbd5e1!important;
}

.fractal-calc{
color:#b81424;
border-color:#b81424!important;
}

.fractal-download{
color:#2563eb;
border-color:#2563eb!important;
}

.fractal-clear:hover{
background:#f1f5f9;
}

.fractal-calc:hover{
background:#fdf2f2;
}

.fractal-download:hover{
background:#eff6ff;
}

.fractal-result{
display:none;
margin-top:15px;
background:#fdf2f2;
padding:18px;
border-radius:10px;
border:1px solid #fbd5d5;
width:100%;
box-sizing:border-box;
}

.dimension-number{
font-size:3rem;
font-weight:700;
line-height:1;
color:#b81424;
}

.dimension-label{
font-size:.95rem;
color:#64748b;
margin-top:6px;
font-weight:bold;
}

.fractal-cube{
vertical-align:middle;
margin-bottom:10px;
}
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

let drawing=false,
painted=false,
mouseX=400,
mouseY=400;
const cube=`<svg class="fractal-cube" width="24" height="24" viewBox="0 0 24 24"><polygon points="12,2 21,7.2 12,12.4 3,7.2" fill="#ff4d5a"/><polygon points="3,7.2 12,12.4 12,22 3,16.8" fill="#d92635"/><polygon points="12,12.4 21,7.2 21,16.8 12,22" fill="#b81424"/></svg> <span style="color:#b81424"><b id="dimension">0.00</b></span>`;

function drawGrid(){

ctx.save();

ctx.strokeStyle="rgba(148,163,184,.08)";
ctx.lineWidth=1;

for(let i=0;i<=800;i+=40){

ctx.beginPath();
ctx.moveTo(i,0);
ctx.lineTo(i,800);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(0,i);
ctx.lineTo(800,i);
ctx.stroke();

}

ctx.restore();

}

function drawPlaceholder(){

if(painted)return;

ctx.save();

ctx.fillStyle="#94a3b8";
ctx.textAlign="center";



ctx.restore();

}

function drawCursor(){

if(drawing)return;

ctx.save();

ctx.beginPath();
ctx.arc(mouseX,mouseY,6,0,2*Math.PI);

ctx.strokeStyle="#b81424";
ctx.lineWidth=1.5;

ctx.stroke();

ctx.restore();

}

function redrawBackground(){

ctx.fillStyle="#fff";
ctx.fillRect(0,0,800,800);

drawGrid();

if(!painted){
drawPlaceholder();
}else{
ctx.drawImage(hidden,0,0);
}

drawCursor();

}
  
function init(){

ctx.fillStyle=hctx.fillStyle="#fff";
ctx.fillRect(0,0,800,800);
hctx.fillRect(0,0,800,800);

ctx.strokeStyle=hctx.strokeStyle="#000";
ctx.lineWidth=hctx.lineWidth=3;

ctx.lineCap=hctx.lineCap="round";
ctx.lineJoin=hctx.lineJoin="round";

ctx.imageSmoothingEnabled=false;
hctx.imageSmoothingEnabled=false;

drawing=false;
painted=false;

result.style.display="none";
result.innerHTML="";

redrawBackground();

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
ctx.fillStyle="#fff";
ctx.fillRect(0,0,800,800);
ctx.drawImage(hidden,0,0);


  
let p=pos(e);

ctx.strokeStyle="#000";
ctx.lineWidth=3;

hctx.strokeStyle="#000";
hctx.lineWidth=3;

ctx.beginPath();
hctx.beginPath();

ctx.moveTo(p.x,p.y);
hctx.moveTo(p.x,p.y);

});

canvas.addEventListener("pointermove",e=>{

let p=pos(e);

mouseX=p.x;
mouseY=p.y;

if(!drawing){

redrawBackground();

return;

}

ctx.lineTo(p.x,p.y);
hctx.lineTo(p.x,p.y);

ctx.stroke();
hctx.stroke();

});

canvas.addEventListener("pointerup",e=>{
drawing=false;
canvas.releasePointerCapture(e.pointerId);
});
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

result.innerHTML =
cube +
`<div class="dimension-label">
Dimensión fractal
</div>`;

const number=
result.querySelector("#dimension");
  
let start=0;
let end=d;

let duration=700;

let startTime=null;

function animate(time){

if(!startTime)
startTime=time;

let progress=
Math.min(
(time-startTime)/duration,
1
);

let value=
start+(end-start)*progress;

number.textContent=
value.toFixed(2);

if(progress<1)
requestAnimationFrame(animate);

}

requestAnimationFrame(animate); 

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


<figure class="nn-article-figure">
  <img src="{static}/images/GB_3.png" alt="GB_3">
  <figcaption>
    Fig. 2: Estimación de la dimensión fractal de la costa de Gran Bretaña mediante el método de box-counting.
  </figcaption>
</figure>


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

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratorio Fractal Interactivo Continuo</title>
    <style>
        .fractal-app { font-family: sans-serif; max-width: 640px; margin: 15px auto; text-align: center; color: #1e293b; padding: 20px; box-sizing: border-box; }
        .fractal-app h3 { color: #b81424; font-size: 1.5em; margin-top: 0; margin-bottom: 15px; font-weight: bold; }
        .fractal-app p { color: #475569; }
        .canvas-container { padding: 15px; border-radius: 10px; display: flex; flex-direction: column; gap: 15px; align-items: center; }
        canvas { background: #ffffff; border: 2px dashed #cbd5e1; cursor: crosshair; touch-action: none; display: block; max-width: 100%; height: auto; border-radius: 6px; }
        #chartCanvas { 
    background: #ffffff; 
    cursor: default; 
    width: 100%; 
    max-width: 400px; 
    height: auto; 
    display: block; 
}
        .controls { margin-top: 15px; display: flex; flex-direction: column; gap: 12px; align-items: center; padding: 15px; width: 100%; box-sizing: border-box; }
        .slider-box { display: flex; align-items: center; gap: 10px; width: 100%; justify-content: center; font-weight: bold; color: #334155; }
        .btn-group { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
        button { padding: 10px 18px; font-weight: bold; background: #ffffff; border-radius: 6px; cursor: pointer; font-size: 0.9em; transition: all 0.2s ease; border: 2px solid transparent; }
        .btn-clear { color: #475569; border-color: #cbd5e1; }
        .btn-clear:hover { background: #f1f5f9; border-color: #94a3b8; }
        .btn-add { color: #b81424; border-color: #b81424; }
        .btn-add:hover { background: #fdf2f2; }
        .btn-download { color: #2563eb; border-color: #2563eb; display: inline-block; }
        .btn-download:hover { background: #eff6ff; }
        .result-box { margin-top: 15px; font-size: 1.2em; font-weight: bold; color: #b81424; background: #fdf2f2; padding: 12px; border-radius: 8px; border: 1px solid #fbd5d5; width: 100%; box-sizing: border-box; line-height: 1.5; }
        input[type=range] { width: 45%; cursor: pointer; accent-color: #b81424; }
        .welcome-screen { background: #ffffff; padding: 10px 0; display: flex; flex-direction: column; gap: 12px; align-items: center; }
        .btn-choice { color: #b81424; border-color: #b81424; font-size: 1em; min-width: 220px; padding: 12px; font-weight: bold; }
        .btn-choice:hover { background: #fdf2f2; }
        .hidden-input { display: none; }
        .main-content { display: none; }
        .privacy-notice { font-size: 0.75em; color: #64748b; margin-top: 5px; }
        .table-box { width: 100%; margin-top: 15px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; box-sizing: border-box; }
        table { width: 100%; border-collapse: collapse; font-size: 0.85em; text-align: center; }
        th { background: #f8fafc; color: #475569; font-weight: bold; padding: 10px; border-bottom: 2px solid #e2e8f0; }
        td { padding: 10px; border-bottom: 1px solid #f1f5f9; color: #334155; }
        tr:last-child td { border-bottom: none; }
        .chart-container { display: flex; justify-content: center; width: 100%; margin-top: 15px; }
        .download-dropdown { position: relative; display: none; }
        .dropdown-content { display: none; position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); background-color: #ffffff; min-width: 160px; box-shadow: 0px 8px 16px rgba(0,0,0,0.15); border-radius: 6px; border: 1px solid #cbd5e1; z-index: 10; margin-bottom: 5px; overflow: hidden; }
        .dropdown-content button { width: 100%; border: none; border-radius: 0; padding: 10px 16px; text-align: left; background: none; color: #334155; font-size: 0.85em; }
        .dropdown-content button:hover { background-color: #f1f5f9; color: #1e293b; }
        .download-dropdown.active .dropdown-content { display: block; }
    </style>
</head>
<body>
<div class="fractal-app">
    <h3>Crea tu propio fractal y descubre su dimensión</h3>
    
    <div id="welcomeScreen" class="welcome-screen">
        <button class="btn-choice" onclick="startWithDrawing()">✏️ Haz un dibujo</button>
        <button class="btn-choice" onclick="triggerImageUpload()">📁 Sube una imagen</button>
        <input type="file" id="imageInput" class="hidden-input" accept="image/*" onchange="handleImageUpload(event)">
        <p class="privacy-notice">🔒 Las imágenes se procesan localmente en tu navegador</p>
    </div>

    <div id="mainContent" class="main-content">
        <p style="font-size: 0.85em; margin-bottom: 15px; line-height: 1.4;">
            Mueve el deslizador y pulsa <b>"📌 Registrar Punto"</b> en diferentes escalas para trazar tu gráfica
        </p>
        
        <div class="canvas-container">
            <div><canvas id="chaosCanvas" width="800" height="800"></canvas></div>
        </div>
        
        <div class="controls">
            <div class="slider-box">
                <label for="boxSlider"><b>Tamaño (ϵ):</b> <span id="sizeVal">16</span>px</label>
                <input type="range" id="boxSlider" min="4" max="80" value="16">
            </div>
            <div class="btn-group">
                <button class="btn-clear" onclick="resetToWelcome()">🔄 Reiniciar</button>
                <button id="addPointBtn" class="btn-add" onclick="recordCurrentPoint()">📌 Registrar Punto</button>
                <button class="btn-clear" onclick="removeLastPoint()">↩️ Borrar último punto</button>
                <div id="downloadBtn" class="download-dropdown">
                    <button class="btn-download" onclick="toggleDropdown(event)">📥 Descargar</button>
                    <div class="dropdown-content">
                        <button onclick="triggerExport('csv')">Datos experimentales</button>
                        <button onclick="triggerExport('png')">Representación gráfica</button>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="result-box" id="result-text">⚡ Espacio en blanco listo para calcular la dimensión fractal</div>
        
        <div class="chart-container">
            <canvas id="chartCanvas" width="800" height="440"></canvas>
        </div>
        
        <div class="table-box">
            <table>
                <thead>
                   <tr>
    <th>Tamaño (ϵ)</th>
    <th>Cajas (N)</th>
    <th>log(1/ϵ)</th>
    <th>log(N)</th>
                  </tr>
                </thead>
                <tbody id="dataTableBody">
                    <tr>
                        <td colspan="2" style="color: #94a3b8; font-style: italic;">No hay escalas registradas</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<canvas id="hiddenCanvas" width="800" height="800" style="display:none;"></canvas>
<script>
const canvas = document.getElementById('chaosCanvas'); const ctx = canvas.getContext('2d');
const hiddenCanvas = document.getElementById('hiddenCanvas'); const hCtx = hiddenCanvas.getContext('2d');
const chartCanvas = document.getElementById('chartCanvas'); const chartCtx = chartCanvas.getContext('2d');
const slider = document.getElementById('boxSlider'); const sizeVal = document.getElementById('sizeVal');
const resultText = document.getElementById('result-text');
const welcomeScreen = document.getElementById('welcomeScreen'); const mainContent = document.getElementById('mainContent');
const dataTableBody = document.getElementById('dataTableBody');
const downloadBtn = document.getElementById('downloadBtn');
let drawing = false; let hasPintado = false; let registeredPoints = []; let currentBoxesCount = 0;

const cubeSVG = `<svg class="fractal-cube" width="24" height="24" viewBox="0 0 24 24" style="vertical-align:middle; margin-right:8px;"><polygon points="12,2 21,7.2 12,12.4 3,7.2" fill="#ff4d5a"/><polygon points="3,7.2 12,12.4 12,22 3,16.8" fill="#d92635"/><polygon points="12,12.4 21,7.2 21,16.8 12,22" fill="#b81424"/></svg>`;

function initCanvases() {
    ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    hCtx.fillStyle = '#ffffff'; hCtx.fillRect(0, 0, hiddenCanvas.width, hiddenCanvas.height);
    hCtx.strokeStyle = '#000000'; hCtx.lineWidth = 2; hCtx.lineCap = 'round'; hCtx.lineJoin = 'round';
    drawNativeChart([], [], null, null);
    dataTableBody.innerHTML = '<tr><td colspan="2" style="color: #94a3b8; font-style: italic;">No hay escalas registradas</td></tr>';
    downloadBtn.style.display = 'none';
}

function getPos(e) {
    const rect = canvas.getBoundingClientRect();
    let clientX = e.clientX; let clientY = e.clientY;
    if (e.touches && e.touches.length > 0) { clientX = e.touches[0].clientX; clientY = e.touches[0].clientY; }
    const scaleX = canvas.width / rect.width; const scaleY = canvas.height / rect.height;
    return { x: (clientX - rect.left) * scaleX, y: (clientY - rect.top) * scaleY };
}

canvas.addEventListener('pointerdown', (e) => {
    e.preventDefault();
    canvas.setPointerCapture(e.pointerId);

    drawing = true;
    hasPintado = true;

    const pos = getPos(e);

    hCtx.beginPath();
    hCtx.moveTo(pos.x, pos.y);

    ctx.beginPath();
    ctx.moveTo(pos.x, pos.y);
});

canvas.addEventListener('pointermove', (e) => {
    if (!drawing) return;

    const pos = getPos(e);

    hCtx.lineTo(pos.x, pos.y);
    hCtx.stroke();

    drawGrid();
});

canvas.addEventListener('pointerup', (e) => {
    drawing = false;
    canvas.releasePointerCapture(e.pointerId);
    drawGrid();
});

canvas.addEventListener('pointercancel', () => {
    drawing = false;
});

canvas.addEventListener('pointerleave', () => {
    drawing = false;
});

slider.addEventListener('input', () => { sizeVal.innerText = slider.value; drawGrid(); });

function startWithDrawing() { 
    canvas.width = 800; canvas.height = 800; hiddenCanvas.width = 800; hiddenCanvas.height = 800; 
    welcomeScreen.style.display = 'none'; mainContent.style.display = 'block'; resetCanvasState(); 
}

function triggerImageUpload() { document.getElementById('imageInput').click(); }

function handleImageUpload(event) {
    const files = event.target.files; if (!files || files.length === 0) return;
    const file = files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
            const maxW = 800; const maxH = 800; let targetW = img.width; let targetH = img.height;
            if (targetW > maxW || targetH > maxH) {
                const ratio = Math.min(maxW / targetW, maxH / targetH);
                targetW = Math.round(targetW * ratio); targetH = Math.round(targetH * ratio);
            }
            canvas.width = targetW; canvas.height = targetH; hiddenCanvas.width = targetW; hiddenCanvas.height = targetH;
            hCtx.fillStyle = '#ffffff'; hCtx.fillRect(0, 0, targetW, targetH); hCtx.drawImage(img, 0, 0, targetW, targetH);
            const imgData = hCtx.getImageData(0, 0, targetW, targetH); const data = imgData.data;
            for (let i = 0; i < data.length; i += 4) {
                const brightness = 0.34 * data[i] + 0.5 * data[i+1] + 0.16 * data[i+2];
                const color = brightness < 200 ? 0 : 255;
                data[i] = color; data[i+1] = color; data[i+2] = color; data[i+3] = 255;
            }
            hCtx.putImageData(imgData, 0, 0); welcomeScreen.style.display = 'none'; mainContent.style.display = 'block';
            hasPintado = true; registeredPoints = []; currentBoxesCount = 0; slider.value = 16; sizeVal.innerText = 16;
            hCtx.strokeStyle = '#000000'; hCtx.lineWidth = 2; hCtx.lineCap = 'round'; hCtx.lineJoin = 'round';
            drawGrid(); drawNativeChart([], [], null, null);
            dataTableBody.innerHTML = '<tr><td colspan="2" style="color: #94a3b8; font-style: italic;">No hay escalas registradas</td></tr>';
            downloadBtn.style.display = 'none';
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function resetCanvasState() {
    hasPintado = false; drawing = false; registeredPoints = []; currentBoxesCount = 0;
    slider.value = 16; sizeVal.innerText = 16; initCanvases();
    resultText.innerHTML = "⚡ Espacio en blanco listo para calcular la dimensión fractal";
}
function resetToWelcome() { document.getElementById('imageInput').value = ""; mainContent.style.display = 'none'; welcomeScreen.style.display = 'flex'; }
function drawGrid() {
    ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height); ctx.drawImage(hiddenCanvas, 0, 0);
    if (!hasPintado) return;
    const boxSize = parseInt(slider.value); const w = canvas.width; const h = canvas.height;
    const imgData = hCtx.getImageData(0, 0, w, h).data; currentBoxesCount = 0;
    for (let y = 0; y < h; y += boxSize) {
        for (let x = 0; x < w; x += boxSize) {
            let hasBlackPixel = false;
            for (let by = 0; by < boxSize && (y + by) < h; by++) {
                for (let bx = 0; bx < boxSize && (x + bx) < w; bx++) {
                    const idx = ((y + by) * w + (x + bx)) * 4; if (imgData[idx] < 128) { hasBlackPixel = true; break; }
                }
                if (hasBlackPixel) break;
            }
            if (hasBlackPixel) {
                ctx.fillStyle = 'rgba(37, 99, 235, 0.12)'; ctx.fillRect(x, y, boxSize, boxSize);
                ctx.strokeStyle = 'rgba(37, 99, 235, 0.25)'; currentBoxesCount++;
            } else { ctx.strokeStyle = 'rgba(148, 163, 184, 0.1)'; }
            ctx.lineWidth = 1; ctx.strokeRect(x, y, boxSize, boxSize);
        }
    }
    if (hasPintado && !drawing) updateResultUI();
}

function recordCurrentPoint() {
    if (!hasPintado || currentBoxesCount === 0) { resultText.innerHTML = "⚠️ ¡Lienzo vacío!"; return; }
    const boxSize = parseInt(slider.value); const valX = Math.log(1 / boxSize); const valY = Math.log(currentBoxesCount);
    if (registeredPoints.some(p => p.size === boxSize)) { resultText.innerHTML = `⚠️ El tamaño de ${boxSize}px ya está registrado`; return; }
    
    let totalW = canvas.width; let totalH = canvas.height;
    let theoreticalMaxBoxes = Math.ceil(totalW / boxSize) * Math.ceil(totalH / boxSize);
    let ratioFill = currentBoxesCount / theoreticalMaxBoxes;
    
    if (ratioFill > 0.82) {
        resultText.innerHTML = `⚠️ Escala omitida por saturación, prueba con otro punto`;
        return;
    }
    
    registeredPoints.push({ size: boxSize, x: valX, y: valY, rawCount: currentBoxesCount });
    registeredPoints.sort((a, b) => a.x - b.x);
    updateTableUI();
    updateCalculationsAndChart();
}
function updateTableUI() {
    if (registeredPoints.length === 0) {
        dataTableBody.innerHTML = '<tr><td colspan="2" style="color: #94a3b8; font-style: italic;">No hay escalas registradas</td></tr>';
        downloadBtn.style.display = 'none';
        return;
    }
    dataTableBody.innerHTML = '';
    registeredPoints.forEach(p => {
        const row = document.createElement('tr');
row.innerHTML = `
<td><b>${p.size}</b></td>
<td>${p.rawCount}</td>
<td>${p.x.toFixed(3)}</td>
<td>${p.y.toFixed(3)}</td>
`;        dataTableBody.appendChild(row);
    });
    if(registeredPoints.length >= 2) { downloadBtn.style.display = 'inline-block'; }
}

function updateCalculationsAndChart() {
    const n = registeredPoints.length;
    const logX = registeredPoints.map(p => p.x); const logY = registeredPoints.map(p => p.y);
    if (n < 2) { drawNativeChart(logX, logY, null, null); updateResultUI(); return; }
    let sX = 0, sY = 0, sXY = 0, sXX = 0;
    for (let i = 0; i < n; i++) { sX += logX[i]; sY += logY[i]; sXY += logX[i] * logY[i]; sXX += logX[i] * logX[i]; }
    const slope = (n * sXY - sX * sY) / (n * sXX - sX * sX); const intercept = (sY - slope * sX) / n; const d = Math.abs(slope);
    drawNativeChart(logX, logY, slope, intercept);
    resultText.innerHTML = `🔲 Puntos totales: <b>${n}</b><br>${cubeSVG} Dimensión Fractal: <span style="color:#b81424;"><b>${d.toFixed(2)}</b></span>`;
}

function updateResultUI() {
    const boxSize = parseInt(slider.value);
    if (registeredPoints.length >= 2) { updateCalculationsAndChart(); } 
    else { resultText.innerHTML = `🔲 Tamaño (ϵ): <b>${boxSize}px</b> | Cajas (N): <b>${currentBoxesCount}</b><br><span style="font-size:0.85em; color:#64748b; font-weight:normal;">Registra al menos 2 puntos</span>`; }
}

function drawNativeChart(xData, yData, slope, intercept) {
    const W = chartCanvas.width; const H = chartCanvas.height; chartCtx.clearRect(0, 0, W, H);
    chartCtx.save();
    chartCtx.scale(2, 2);
    const w = 400; const h = 220;
    const padLeft = 55; const padBottom = 40; const padRight = 25; const padTop = 25;
    const gW = w - padLeft - padRight; const gH = h - padTop - padBottom;
    
    chartCtx.strokeStyle = '#475569'; chartCtx.lineWidth = 1.5; chartCtx.beginPath();
    chartCtx.moveTo(padLeft, h - padBottom); chartCtx.lineTo(w - padRight, h - padBottom);
    chartCtx.moveTo(padLeft, padTop); chartCtx.lineTo(padLeft, h - padBottom); chartCtx.stroke();
    
    chartCtx.fillStyle = '#1e293b'; chartCtx.font = 'bold 11px sans-serif';
    chartCtx.fillText("log(1/ϵ)", w - padRight - 55, h - padBottom + 28);
    chartCtx.save(); chartCtx.translate(padLeft - 38, padTop + 45); chartCtx.rotate(-Math.PI / 2);
    chartCtx.fillText("log(N)", 0, 0); chartCtx.restore();

    if (xData.length === 0) {
        chartCtx.strokeStyle = '#f1f5f9'; chartCtx.lineWidth = 1;
        for(let i=1; i<=4; i++) {
            let cx = padLeft + (i/5)*gW; let cy = h - padBottom - (i/5)*gH;
            chartCtx.beginPath(); chartCtx.moveTo(cx, h-padBottom); chartCtx.lineTo(cx, padTop); chartCtx.stroke();
            chartCtx.beginPath(); chartCtx.moveTo(padLeft, cy); chartCtx.lineTo(w-padRight, cy); chartCtx.stroke();
        }
        chartCtx.restore();
        return;
    }
    let minX = Math.min(...xData), maxX = Math.max(...xData); let minY = Math.min(...yData), maxY = Math.max(...yData);
    if(minX === maxX) { minX -= 0.5; maxX += 0.5; } if(minY === maxY) { minY -= 0.5; maxY += 0.5; }
    const spanX = maxX - minX, spanY = maxY - minY;
    function toScreen(x, y) { return { x: padLeft + ((x - minX) / spanX) * gW, y: h - padBottom - ((y - minY) / spanY) * gH }; }

    chartCtx.strokeStyle = '#f1f5f9'; chartCtx.lineWidth = 1; chartCtx.fillStyle = '#64748b'; chartCtx.font = '9px sans-serif';
    for (let i = 0; i <= 4; i++) {
        const factor = i / 4; const curX = minX + factor * spanX; const curY = minY + factor * spanY; const sPt = toScreen(curX, curY);
        chartCtx.beginPath(); chartCtx.moveTo(sPt.x, h - padBottom); chartCtx.lineTo(sPt.x, h - padBottom + 4); chartCtx.stroke();
        chartCtx.fillText(curX.toFixed(2), sPt.x - 10, h - padBottom + 14);
        chartCtx.beginPath(); chartCtx.moveTo(padLeft - 4, sPt.y); chartCtx.lineTo(padLeft, sPt.y); chartCtx.stroke();
        chartCtx.fillText(curY.toFixed(1), padLeft - 26, sPt.y + 3);
    }
    if (slope !== null) {
        chartCtx.strokeStyle = '#000000'; chartCtx.lineWidth = 1; chartCtx.beginPath();
        chartCtx.moveTo(toScreen(minX, slope * minX + intercept).x, toScreen(minX, slope * minX + intercept).y);
        chartCtx.lineTo(toScreen(maxX, slope * maxX + intercept).x, toScreen(maxX, slope * maxX + intercept).y);
        chartCtx.stroke();
    }
    chartCtx.fillStyle = '#3799eb';
    for (let i = 0; i < registeredPoints.length; i++) {
        const p = registeredPoints[i]; const pt = toScreen(p.x, p.y);
        chartCtx.beginPath(); chartCtx.arc(pt.x, pt.y, 3, 0, 2 * Math.PI); chartCtx.fill();
    }
    chartCtx.restore();
}

function generateChartOnCanvas() {
    const n = registeredPoints.length;
    let sX = 0, sY = 0, sXY = 0, sXX = 0;
    const logX = registeredPoints.map(p => p.x); const logY = registeredPoints.map(p => p.y);
    for (let i = 0; i < n; i++) { sX += logX[i]; sY += logY[i]; sXY += logX[i] * logY[i]; sXX += logX[i] * logX[i]; }
    const slope = (n * sXY - sX * sY) / (n * sXX - sX * sX); const d = Math.abs(slope);

    const exportCanvas = document.createElement('canvas');
    exportCanvas.width = chartCanvas.width;
    exportCanvas.height = chartCanvas.height;
    const eCtx = exportCanvas.getContext('2d');
    
    eCtx.fillStyle = '#ffffff';
    eCtx.fillRect(0, 0, exportCanvas.width, exportCanvas.height);
    eCtx.drawImage(chartCanvas, 0, 0);
    
    eCtx.save();
    eCtx.fillStyle = 'rgba(253, 242, 242, 0.90)';
    eCtx.strokeStyle = '#fbd5d5';
    eCtx.lineWidth = 2;
    
    const boxW = 265; const boxH = 45;
    const boxX = (exportCanvas.width - boxW) / 2; const boxY = 15;
    
    eCtx.beginPath();
    eCtx.roundRect(boxX, boxY, boxW, boxH, 6);
    eCtx.fill();
    eCtx.stroke();
    
    eCtx.save();
    eCtx.translate(boxX + 15, boxY + 11);
    eCtx.fillStyle = '#ff4d5a'; eCtx.beginPath(); eCtx.moveTo(11, 0); eCtx.lineTo(20, 4.8); eCtx.lineTo(11, 9.6); eCtx.lineTo(2, 4.8); eCtx.closePath(); eCtx.fill();
    eCtx.fillStyle = '#d92635'; eCtx.beginPath(); eCtx.moveTo(2, 4.8); eCtx.lineTo(11, 9.6); eCtx.lineTo(11, 23); eCtx.lineTo(2, 18.2); eCtx.closePath(); eCtx.fill();
    eCtx.fillStyle = '#b81424'; eCtx.beginPath(); eCtx.moveTo(11, 9.6); eCtx.lineTo(20, 4.8); eCtx.lineTo(20, 18.2); eCtx.lineTo(11, 23); eCtx.closePath(); eCtx.fill();
    eCtx.restore();
    
    eCtx.fillStyle = '#b81424'; eCtx.font = 'bold 18px sans-serif'; eCtx.textBaseline = 'middle'; eCtx.textAlign = 'left';
    eCtx.fillText(`Dimensión fractal: ${d.toFixed(2)}`, boxX + 48, boxY + (boxH / 2));
    eCtx.restore();

    return exportCanvas;
}

function triggerExport(type) {
    if (registeredPoints.length < 2) return;
    document.getElementById('downloadBtn').classList.remove('active');

    const n = registeredPoints.length;
    let sX = 0, sY = 0, sXY = 0, sXX = 0;
    const logX = registeredPoints.map(p => p.x); const logY = registeredPoints.map(p => p.y);
    for (let i = 0; i < n; i++) { sX += logX[i]; sY += logY[i]; sXY += logX[i] * logY[i]; sXX += logX[i] * logX[i]; }
    const slope = (n * sXY - sX * sY) / (n * sXX - sX * sX); 
    const intercept = (sY - slope * sX) / n;

    if (type === 'csv') {
        let txtString = "==================================================\n\n";
        txtString += "[ANÁLISIS DE REGRESIÓN LINEAL LOG-LOG]\n";
        txtString += "--------------------------------------------------\n";
        txtString += `Pendiente de la Recta: ${slope.toFixed(4)}\n`;
        txtString += `Ordenada en el origen: ${intercept.toFixed(4)}\n`;
        txtString += `Puntos registrados (N): ${n}\n\n`;
        txtString += "[DATOS EXPERIMENTALES]\n";
        txtString += "--------------------------------------------------\n";
        txtString += "Escala (ϵ, en px)     Cajas (N)\n";
        txtString += "--------------------------------------------------\n";
        
        registeredPoints.forEach(p => { 
            txtString += `${p.size}                     ${p.rawCount}\n`; 
        });

        const txtBlob = new Blob([txtString], { type: 'text/plain;charset=utf-8;' });
        const txtUrl = URL.createObjectURL(txtBlob);
        const link = document.createElement("a");
        link.href = txtUrl;
        link.download = "datos_fractales.txt";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        setTimeout(() => URL.revokeObjectURL(txtUrl), 100);
    } 
    else if (type === 'png') {
        const exportCanvas = generateChartOnCanvas();
        exportCanvas.toBlob((pngBlob) => {
            if (!pngBlob) return;
            const pngUrl = URL.createObjectURL(pngBlob);
            const link = document.createElement("a");
            link.href = pngUrl;
            link.download = "grafica_fractal.png";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            setTimeout(() => URL.revokeObjectURL(pngUrl), 100);
        }, "image/png");
    } 
}

function removeLastPoint() {
    if (registeredPoints.length === 0) return;

    registeredPoints.pop();

    updateTableUI();

    if (registeredPoints.length >= 2) {
        updateCalculationsAndChart();
    } else {
        drawNativeChart([], [], null, null);
        updateResultUI();
    }
}

function toggleDropdown(event) {
    event.stopPropagation();
    const dropdown = document.getElementById('downloadBtn');
    dropdown.classList.toggle('active');
}

['click', 'touchstart'].forEach(evt => {
    document.addEventListener(evt, function() {
        const dropdown = document.getElementById('downloadBtn');
        if (dropdown) { dropdown.classList.remove('active'); }
    });
});

initCanvases();
</script>
</body>
</html>


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
