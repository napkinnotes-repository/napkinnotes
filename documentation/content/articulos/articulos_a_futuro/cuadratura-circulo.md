---
title: Sobre la imposibilidad de cuadrar el círculo
author: Gabriel Sánchez Pérez
date:  2026-08-20
layout: articles
slug: prueba-articulo-gabri
status: hidden
category: Matemáticas
tags: 
   - geometría
summary: "Desde pequeños nos han enseñado que hay tareas fáciles, otras menos sencillas, y otras que
directamente son imposibles. En la *Napkin* de hoy hablaremos de una de estas últimas: la imposibilidad de cuadrar el círculo."
image: images/cuadratura-circulo-gabri.jpeg
---

[TOC]

Muchos han sido los intentos de cuadrar un círculo con los métodos de la Antigüedad clásica, es decir, construir con "regla y compás" un cuadrado de área igual a la de un círculo dado. Desde hace casi 150 años se sabe que es una tarea completamente imposible, al igual que muchas otras, como la trisección del ángulo o la duplicación del cubo (los tres problemas délicos). ¡Comencemos!


## Trascendencia de $\pi$ y Teorema de Lindemann-Weierstrass

Como paso previo imprescindible para demostrar la imposibilidad de la cuadratura del círculo, primero vamos a demostrar que el número $\pi$ es irracional y trascendente sobre $\mathbb{Q}$. Esta parte del artículo es técnica, pero muy recomendable para aquellos lectores que seáis tan amantes de las matemáticas como yo. Si os parece demasiado engorrosa, podéis saltar directamente a la [Sección 2](#imposibilidad-de-cuadrar-un-círculo).

Como sabéis, que un número sea irracional significa que no se puede poner como cociente de dos números enteros. La trascendencia es una propiedad algo menos conocida, pero viene a significar que el número en cuestión no es solución de ninguna ecuación algebraica sobre cierto cuerpo (en nuestro caso, $\mathbb{Q}$). Lo contrario a ser trascendente es ser algebraico. 

Fijémonos que todo número trascendente es necesariamente irracional. En efecto, supongamos que un número trascendente $p$ es racional. Entonces $p=\displaystyle\frac{a}{b}$ para ciertos enteros $a$ y $b$. Construimos el polinomio $P(x)=bx-a$, y como tiene por raíz a $p$, entonces $p$ es algebraico. Habiendo llegado a una contradicción, es claro que todo número trascendente es irracional. Por consiguiente, es suficiente con que probemos la trascendencia de $\pi$, la cual una vez demostrada veremos en la Sección 2 que implica la imposibilidad de cuadrar un círculo con regla y compás.

Antes de enunciar y demostrar el Teorema de Lindemann-Weierstrass comenzaremos por dos resultados intermedios previos.

**Lema 1**
Dados $c(i) \neq 0 \ \forall i\in\mathbb{Z}\cap [1,r]$, sean $\{y(k)_1,..., y(k)_{m(k)}\}$ las raíces de un polinomio con coeficientes enteros $T_k(x)=v(k) x^{m(k)}+...+u(k)$ $\forall k\in[1,r]$ y con $u(k), v(k)\neq 0$. Entonces si $y(k)_i\neq y(u)_v$ con $(k, i)\neq (u, v)$, se tiene que $\sum_{i=1}^r{c(i)(e^{y(i)_1}+...+e^{y(i)_{m(i)}})}\neq 0$.

*Demostración*

En primer lugar la expresión final del enunciado puede ser escrita como
$S=\sum_{k=1}^n\beta_k e^{\alpha_k}\neq 0,$
donde $n_0=0$, $n=n_r$, $n_i=\sum_{k=1}^i m(k)$ con $i=1, ..., r$, $\alpha_{n_i+j}=y(i+1)_j$ con $0\leq i\leq r-1$, $1\leq j\leq m(i+1)$ y $\beta_{n_i+j}=c(i+1)$. Supongamos que $S=0$ para llegar a una contradicción. Sea ahora
$f_i(x):=\frac{l^{np}(x-\alpha_1)^p...(x-\alpha_n)^p}{(x-\alpha_i)},$
con $l$ entero y construyamos $I_i(s)=\int_0^s e^{s-x}f_i(x) dx=e^s\sum_{j=0}^{np-1}f_i^{(j)}(0)-\sum_{j=0}^{np-1}f_i^{(j)}(s)$ integrando por partes. En caso de que $s$ sea complejo integramos en un contorno cerrado que pase por la recta real y usamos el Teorema de Cauchy. Ahora evaluemos la suma
$J_i=\sum_{k=1}^n \beta_k I_i(\alpha_k)=\sum_{j=0}^{np-1}f_i^{(j)}(0)\sum_{k=1}^n\beta_ke^{\alpha_k}-\sum_{k=1}^n\sum_{j=0}^{np-1}\beta_k f_i^{(j)}(\alpha_k),$
por lo que
$J_i=-\sum_{k=1}^n\sum_{j=0}^{np-1}\beta_kf_i^{(j)}(\alpha_k)$, donde en la última igualdad hemos usado la hipótesis del absurdo. Si $j\geq p$ entonces $f_i^{(j)}(\alpha_k)$ es un entero algebraico múltiplo de $p!$. Si $j<p-1$ es claro que $f_i^{(j)}(\alpha_k)=0$ y si $j=p-1$ y $k=i$ entonces $f_i^{(j)}(\alpha_k)=l^{np}(p-1)!\prod_{m\neq i}(\alpha_m-\alpha_i)$. Este entero no es divisible por $p$ haciendo uso del famoso Pequeño Teorema de Fermat. Por tanto $J_i$ es divisible por $(p-1)!$. Ahora, reescribiendo $J_i$ como sigue:
$J_i=-\sum_{j=0}^{np-1}\sum_{t=0}^{r-1}c(t+1)(f_i^{(j)}(\alpha_{n_t+1})+...+f_i^{(j)}(\alpha_{n_{t+1}})),$
y usando el Teorema Fundamental de polinomios simétricos, se puede probar que $J_i$ es un polinomio $G(\alpha_i)$, por lo que $\vert{}J_1...J_n\vert{}$ es un entero divisible por $(p-1)!^n$. La contradicción llega del hecho de que $\vert{}I_i(\alpha_k)\vert{}\leq \vert{}\alpha_k\vert{} e^{\vert{}\alpha_k\vert{}}F_i(\vert{}\alpha_k\vert{})$ donde $F_i(x)$ es el polinomio cuyos coeficientes son los de $f_i(x)$ en valor absoluto. Pero entonces $J_i\leq\sum_{k=1}^n\vert{}\alpha_k\beta_k\vert{}e^{\vert{}\alpha_k\vert{}}F_i(\vert{}\alpha_k\vert{})$ por lo que de alguna forma $\vert{}J_1...J_n\vert{}$ está acotado superiormente por cierto $N^p$, lo cual contradice la desigualdad anterior ya que $p$ es arbitrario y la cota inferior supera a la superior para $p$ suficientemente grande.

**Lema 2** 
Si $b(1),...,b(n)$ son naturales y $y(1),...,y(n)$ son algebraicos y diferentes, entonces $b(1)e^{y(1)}+...+b(n)e^{y(n)}\neq 0$.

*Demostración*

Construyamos un polinomio con coeficientes enteros cuyas raíces sean $y(1),...,y(n),y(n+1),...,y(N)$ y definamos $b(n+1)=...=b(N)=0$. Si suponemos que el enunciado es falso, es claro que $\prod_{\sigma\in S_N}(b(1)e^{y(\sigma(1))}+...+b(N)e^{y(\sigma(N))})=0$, donde estamos considerando todas las permutaciones. Pero si expandimos ese productorio nos aparecen términos en exponenciales simétricas y al agrupar nos vamos a encontrar con una suma semejante a la del enunciado del Lema 1. Puede probarse que se satisfacen dichas hipótesis, lo cual es contradictorio y prueba el Lema 2.

Ahora sí, estamos en disposición de demostrar el Teorema fundamental de esta sección.

**Teorema de Lindemann-Weierstrass**
Si $\alpha_1,...,\alpha_n$ son números algebraicos no nulos y $\beta_1,...,\beta_n$ son números algebraicos distintos, entonces $\alpha_1e^{\beta_1}+...+\alpha_ne^{\beta_n}\neq 0$.

*Demostración*

Se deja como ejercicio a los lectores más aventureros. Como pista, os diré que se prueba de forma muy parecida al Lema 2.

Por último, veamos que $\pi$ es un número trascendente.

**Corolario** 
El número $\pi$ es trascendente.

*Demostración* 

Basta contemplar la bella ecuación de Euler $e^{i\pi}+1=0$ y usar el teorema anterior. Si $\pi$ fuera algebraico, entonces $i\pi$ también sería algebraico (por ser $i$ algebraico). Tomando $\beta_1 = i\pi$, $\beta_2 = 0$, $\alpha_1 = 1$, $\alpha_2 = 1$, el teorema diría que $1 \cdot e^{i\pi} + 1 \cdot e^0 \neq 0$, lo cual contradice la identidad de Euler. Por lo tanto, $\pi$ debe ser trascendente.

A continuación vamos a estudiar la relación entre la trascendencia de $\pi$ y el hecho de que $\pi$ no sea “construible” con regla y compás.

---


## Imposibilidad de cuadrar un círculo

Para el tema que nos concierne, es suficiente con entender que si $a$ y $b$ son dos puntos construibles con regla y compás, entonces su cociente es construible. Esto será clave para demostrar que es imposible cuadrar el círculo.

Otro resultado fundamental es que un número real es construible si y sólo si es algebraico y el grado de su polinomio mínimo irreducible sobre $\mathbb{Q}$ es una potencia de 2. En efecto, supongamos que $\alpha \in \mathbb{R}$ es un número construible con regla y compás. En la geometría analítica del plano, partir de un conjunto de puntos iniciales equivale a trabajar en el cuerpo $\mathbb{Q}$. Cada paso de construcción con regla (intersección de rectas) implica resolver ecuaciones de primer grado, lo que no extiende el cuerpo de coeficientes. En cambio, cada paso con compás (intersección de recta y circunferencia o de dos circunferencias) requiere resolver ecuaciones de segundo grado. Por tanto, el punto o distancia $\alpha$ se alcanza tras un número finito $k$ de operaciones cuadráticas. Esto da lugar a una torre de extensiones de cuerpos: $$\mathbb{Q} = F_0 \subset F_1 \subset F_2 \subset \dots \subset F_k,$$ donde $\alpha \in F_k$ y cada extensión es de grado 2, es decir, $[F_i : F_{i-1}] = 2$ para todo $i = 1, \dots, k$. Por la propiedad multiplicativa del grado de las extensiones de cuerpo, se deduce que: $$[F_k : \mathbb{Q}] = [F_k : F_{k-1}] [F_{k-1} : F_{k-2}] \cdots [F_1 : F_0] = 2^k.$$ Puesto que $\mathbb{Q} \subseteq \mathbb{Q}(\alpha) \subseteq F_k$, el grado $[\mathbb{Q}(\alpha) : \mathbb{Q}]$ debe dividir a $[F_k : \mathbb{Q}] = 2^k$. En consecuencia, $\alpha$ debe ser un número algebraico y el grado de su polinomio mínimo irreducible sobre $\mathbb{Q}$ es de la forma $2^m$ para algún entero $m \leq k$.

Recíprocamente, si $\alpha$ es un número algebraico tal que su cuerpo de descomposición se puede obtener mediante una sucesión finita de extensiones cuadráticas (es decir, expresable mediante un número finito de sumas, restas, multiplicaciones, divisiones y raíces cuadradas). Geométricamente, cada raíz cuadrada equivale a la construcción del segmento medio proporcional entre dos longitudes dadas mediante regla y compás. Por ende, $\alpha$ es construible.

Para concluir, supongamos que es posible cuadrar el círculo con regla y compás. Es decir, dado un círculo de radio $R$, podemos construir un cuadrado de lado $L$ con regla y compás tal que $\pi R^2=L^2$, y que $R$ y $L$ son construibles. Como $\pi R^2=L^2$ entonces $\sqrt{\pi}=L/R$ es construible por serlo $R$ y $L$. Si $\sqrt{\pi}$ fuera construible, tendría que ser un número algebraico, lo que implicaría que su cuadrado $(\sqrt{\pi})^2 = \pi$ también sería algebraico. Pero esto es falso por ser $\pi$ trascendente. Con lo cual queda probada la imposibilidad de cuadrar el círculo.

---


## Otros problemas délicos

Además de la imposibilidad de cuadrar el círculo, existen otros dos problemas clásicos que se han demostrado imposibles. El primero es la duplicación del cubo, la cual no es posible porque el polinomio mínimo irreducible de $\sqrt[3]{2}$ es $x^3-2=0$, cuyo grado es 3, y 3 no es una potencia de 2. El otro problema es la trisección del ángulo, que tampoco es posible en general (aunque para algunos ángulos específicos, como el de 90º, sí existe una trisección clásica con regla y compás, mientras que para un ángulo tan simple como 60º resulta imposible). Como curiosidad final, hay otro teorema, el de Gelfond-Schneider, que garantiza que $a^b$ es trascendente si $a$ y $b$ son algebraicos, con $a \neq 0, 1$ y $b$ irracional. Junto con el Teorema de Lindemann sería consecuencia de la Conjetura de Schanuel, que por el momento no es más que eso, una conjetura. De hecho, el teorema de Gelfond es el resultado del séptimo problema de Hilbert, una lista de 23 problemas matemáticos enunciada por David Hilbert a principios del siglo pasado, de los cuales aún quedan algunos por resolver.

---


## Bibliografía

Artículos históricos originales:

Lindemann, F. (1882). "Über die Zahl $\pi$". Mathematische Annalen, 20(2), 213-225. (El articulo original en el que Ferdinand von Lindemann demostro la trascendencia de \pi).

Wantzel, L. (1837). "Recherches sur les moyens de reconnaître si un Problème de Géométrie peut se résoudre avec la regla et le compas". Journal de Mathématiques Pures et Appliquées, 1, 366-372. (Trabajo fundamental donde Pierre Wantzel demostro los criterios de construibilidad con regla y compas, imposibilitando la duplicacion del cubo y la trisección del ángulo).

Libros sobre trascendencia y teoría de números:

Baker, A. (1975). Transcendental Number Theory. Cambridge University Press. (Texto de referencia avanzado que cubre en profundidad el Teorema de Lindemann-Weierstrass, el Teorema de Gelfond-Schneider y la Conjetura de Schanuel).

Niven, I. (1956). Irrational Numbers. Carus Mathematical Monographs, Mathematical Association of America. (Una introducción muy clara y accesible sobre números irracionales y trascendentes, ideal para profundizar en las demostraciones clásicas).

Libros sobre Teoría de Galois y construcciones geométricas

Cox, D. A. (2012). Galois Theory (2.ª ed.). John Wiley & Sons. (Trata con gran detalle y rigor la relacion entre extensiones de cuerpos, polinomios minimos, numeros construibles y la imposibilidad de los tres problemas delicos).

Stewart, I. (2015). Galois Theory (4.ª ed.). CRC Press. (Un manual clásico, pedagogico y formal que explica la teoría de cuerpos aplicada a los problemas clásicos de la geometría antigua).

Historia y Problemas de Hilbert

Yandell, B. H. (2001). The Honors Class: Hilbert's Problems and Their Solvers. AK Peters/CRC Press. (Libro enfocado en la historia y resolución de los 23 problemas propuestos por David Hilbert, incluyendo el séptimo problema resuelto por Gelfond y Schneider).
