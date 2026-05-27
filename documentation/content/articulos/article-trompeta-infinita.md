---
title: El pintor y la trompeta 
author: David Figueruelo Hernán
date: 2026-04-15
layout: articles
status: published
category: Matemáticas
tags: 
  - infinito
  - cálculo
  - paradojas
summary: Un hombre trajeado aparece en tu taller con una trompeta de vidrio transparente que se estrecha sin terminar nunca y una condición, su superficie debe verse completamente roja...
Lo que parece un encargo extraño acaba revelando una lección sobre el infinito.
image: images/cuerno.png
---

[TOC]


## El encargo


Imagina que eres un humilde pintor en tu pequeño taller de Tívoli, donde las fachadas ocres retienen el calor del sol y la calle empedrada desciende lentamente hacia el murmullo constante del río Aniene. Tus días transcurren entre cal, pigmentos y madera antigua. Restauras frescos que el tiempo ha ido apagando, devuelves color a puertas vencidas por los inviernos, retocas santos desvaídos que observan en silencio desde capillas en penumbra. La vida es sencilla, previsible, hasta que una mañana la campanilla de la puerta rompe el aire con un timbre más seco de lo habitual.  

En el umbral aparece un hombre trajeado, gafas oscuras pese a la sombra del taller, un maletín impecable en la mano. No sonríe. No se presenta. Solo examina el espacio como si evaluara algo invisible. Después, con un gesto medido, deposita sobre tu mesa el objeto de su visita.  

Lo observas sin comprender del todo. Comienza ancho, casi familiar, pero pronto se afina mientras se extiende hacia la derecha, cada vez más delgado, cada vez más largo. La forma parece huir de sí misma, escapar en una dirección que no promete final alguno. Sigues su perfil con la vista esperando que termine en algún punto razonable, pero no hay borde, no hay límite. Solo una prolongación que parece negarse a concluir.  

Antes de marcharse, el hombre pronuncia el nombre con una solemnidad que no admite preguntas: el cuerno de Gabriel.  

Desde el punto de vista matemático, la forma no es caprichosa. Se obtiene al girar la curva y = 1/x para x ≥ 1 alrededor del eje horizontal. El resultado es un sólido de revolución que se extiende indefinidamente mientras su radio disminuye. Es infinito en longitud, pero cada vez más fino.  

El encargo parece simple: la escultura, ahora trasparente, deberá verse completamente roja. Piensas en lo obvio. Bastará con calcular cuánta pintura necesitas para cubrirla por fuera.  

> **¿Cuánta pintura necesitas para pintar una trompeta infinita?**

Tu intuición responde con rapidez: infinita. Si el objeto no termina nunca, tampoco lo hará la superficie que debes cubrir. Pero aún tienes esperanza, pues sabes que las matemáticas no siempre obedecen al sentido común.

---

## Matématicas y otras preguntas

¿Qué significa realmente pintar algo? Cuando pintas, cubres la superficie exterior con una capa de grosor positivo, por pequeña que sea. La cantidad de pintura necesaria es proporcional al área. A mayor superficie, mayor consumo. Hasta ahora, todo coincide con tu experiencia.  

Pero esta trompeta no es una pared ni una estatua convencional. Es otra cosa.  

En el caso del cuerno de Gabriel, el área viene dada por la fórmula de las superficies de revolución:

$$
A = 2\pi \int_1^{\infty} \frac{1}{x} \sqrt{1 + \left(\frac{1}{x^2}\right)^2} \, dx
$$

La expresión puede parecer abstracta, pero su significado es claro: estamos sumando infinitos fragmentos diminutos de superficie. Llamas a tu matemático de confianza y, tras unos minutos de silencio, te explica el resultado: esa integral diverge. Es la manera elegante que tienen los matemáticos de afirmar que el área es infinita.  

Aunque el radio se haga cada vez más pequeño, la longitud infinita compensa esa reducción. La superficie nunca deja de acumularse. Siempre hay un nuevo tramo que añadir.  

En términos prácticos eso significa que no existe una cantidad finita de pintura que permita cubrir completamente el exterior. Siempre quedará un segmento por pintar, por pequeño que sea.  

Miras el objeto en tu taller. Está ahí, sólido, tangible, casi frágil. Pero si intentas pintarlo por fuera, jamás terminarás. Cada litro adicional solo retrasará lo inevitable.  

Durante un momento el encargo parece imposible. Sin embargo, el hombre trajeado no especificó el método, solo el resultado. Quiere la trompeta roja. La escultura es completamente transparente. Desde fuera, nadie distinguiría si el color está en la superficie o en el interior.  

Entonces surge una idea. En lugar de cubrir el exterior, decides llenar la trompeta de pintura roja y sellarla. A primera vista parece aún peor; si cubrir el área requiere pintura infinita, llenar el interior debería ser todavía más costoso. Pero ahora el problema ya no es el área, sino el volumen.

El volumen del cuerno de Gabriel se calcula también con integrales:

$$
V = \pi \int_1^{\infty} \left(\frac{1}{x}\right)^2 dx,
$$

es decir,

$$
V = \pi \int_1^{\infty} \frac{1}{x^2} dx.
$$

A diferencia de la anterior, esta integral sí converge:

$$
\int_1^{\infty} \frac{1}{x^2} dx = 1.
$$

Por tanto,

$$
V = \pi.
$$

La trompeta se extiende hasta el infinito, pero el volumen total contenido en su interior es finito. Exactamente π unidades cúbicas. Puedes llenarla completamente con una cantidad limitada de pintura.  

Volumen finito. Área infinita. A esto se le puede llamar *una paradoja*.

---

## Un trabajo bien hecho

Has resuelto el encargo. Desde fuera, la pieza se ve roja, uniforme, impecable. El hombre trajeado regresa, asiente en silencio, paga y desaparece sin añadir una palabra.  

Pero lo que te llevas no es solo el pago. Es la lección.  

Un mismo objeto puede tener área superficial infinita y volumen finito porque ambas magnitudes miden propiedades distintas. El infinito no actúa igual sobre todas las dimensiones.  

Tu intuición te decía que si algo es infinito, todo en él debía serlo. El cuerno de Gabriel demuestra que no. Superficie y volumen pueden separarse de manera radical cuando entra en juego el infinito.  

El infinito no contradice la lógica. Solo contradice nuestras expectativas.  

Y ahora, cada vez que sostienes un pincel, sabes que incluso aquello que parece perfectamente manejable puede ocultar una estructura que desborda el sentido común. Un día más en Tivoli.
