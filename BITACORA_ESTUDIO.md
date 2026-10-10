# Bitácora de estudio — Visión por Computadora

## 2026-10-07 — Clase 5, laboratorio S05 (Deep Learning Intro)

**Estado: recién arrancado.** Se definió el plan y se revisó el material; el
estudiante todavía no respondió ninguna pregunta conceptual.

**Sólido:**
- Resolvió a mano el caso de 4 píxeles con permutación fija: los pesos correctos
  son los mismos cuatro números reordenados (`[0.5, 2.0, 3.0, -1.0]`). Entendió
  que con `perm` fija la red solo reordena las columnas de su matriz de pesos,
  y que por eso el revoltijo no le cuesta nada (95.39 % vs 95.58 %).
- Vio el contraste con permutación distinta por imagen: el mismo dígito produce
  salidas que saltan de 4.20 a 1.15, y ningún juego de pesos lo arregla.
- Conclusión alcanzada: el MLP necesita **consistencia posicional**, no vecindad.
  Esa es la base de la Pregunta 2.

**Flojo / sin tocar:**
- Learning rate como tamaño de paso (Pregunta 1 del lab, analogía de la sal).
- No llegó a estimar a cuánto caería la exactitud con permutación por imagen
  (queda como curiosidad, no es parte de la entrega).

**Dato de partida que ya tiene:**
- Parte 12 del notebook: MLP normal 95.58 % vs. MLP con píxeles revueltos 95.39 %
  tras 2 épocas. Casi idéntico — ese es el hecho que hay que explicar.
- Línea base de la Parte 13 ya ejecutada: 96.51 % a la época 3, 109 386 parámetros.

### Pendiente — Fase 2: las 7 corridas de la Parte 13

Un interruptor a la vez, el resto en su valor normal, `EPOCAS_TT = 3`.
**Regla acordada: predecir el número ANTES de ejecutar.**

| # | Cambio | Referencia del laboratorio en vivo | Resultado obtenido |
|---|---|---|---|
| 1 | `LR = 0.001` | se queda ~56 % | |
| 2 | `LR = 1.0` | se tambalea, termina por debajo | |
| 3 | `USAR_RELU = False` | se estanca ~92 % | |
| 4 | `LIMPIAR_GRADIENTES = False` | no aprende, la pérdida sube | |
| 5 | `NORMALIZAR = False` | se rompe, responde siempre "1" | |
| 6 | `OCULTAS = 16` | sin referencia — descubrirlo | |
| 7 | `OCULTAS = 256` | sin referencia — descubrirlo | |

Orden sugerido: 1 y 2 primero (son la Pregunta 1), luego 6 y 7 (las interesantes,
hay que razonarlas con el conteo de parámetros), y al final 4 y 5 (fallas
catastróficas, obvias de leer).

### Pendiente — Fase 3: las dos respuestas escritas (celda 68)

1. Qué pasó con las curvas con `LR` 0.001 y 1.0, explicado con la analogía de la sal.
2. Qué información ignora el MLP al aplanar la imagen, y cómo la aprovecha la CNN.

Las escribe el estudiante; el tutor solo las critica.

### Pendiente — Parte 11: el dígito propio

El estudiante tiene una foto de un **6** a bolígrafo sobre papel. Análisis hecho:
- El margen no importa (el paso 4 recorta solo a la caja del trazo).
- El reflejo de la esquina no importa (tras invertir queda más oscuro que el fondo).
- **El grosor sí**: dígito de ~600 px escalado a lado mayor 20 → factor ~1/30;
  un trazo de ~4 px queda en ~0.13 px, que `INTER_AREA` promedia a un gris de
  intensidad ≈ 33 sobre 255, contra los ~255 de MNIST.
- Opciones: rehacerlo con plumón (lo que pide el lab), o meter un `cv2.dilate`
  entre los pasos 3 y 4 (conecta con la morfología de la Clase 4).
- Falta su predicción: ¿qué dígito y con qué confianza, antes de subirla?

### Fase 4 — entrega

Mismo flujo que la Tarea 02: notebook resuelto a la raíz del repo, PDF a
`tareas_pdf/`, commit y push.
