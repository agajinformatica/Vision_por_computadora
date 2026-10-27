> **Estado vigente (2026-10-27, tarde): 75 incluidos / 73 excluidos.** De los 23 casos
> reincorporados por evidencia (C0 revocado), 5 quedaron sin PDF accesible — paywall
> confirmado por el equipo, sin presupuesto — y se reclasificaron a E5. Son los mismos 148
> estudios, sin búsqueda de nuevos papers. Ver [estado auditado](<../metodologia Prisma/4-resultados/CIERRE_AUDITADO.md>). Los recuentos anteriores (80/68, 58/90, 74/74) son históricos.

# Checklist de redacción — Esqueleto_Paper_EPP_YOLO26.docx

Instrumento de seguimiento, **no texto del paper**. Un ítem por unidad de redacción, con
criterio de cierre. Las cifras están incrustadas para no tener que ir a buscarlas.

**Redacción: 100% humana.** Última actualización: **2026-10-10** — cifras de 3.2 y 3.3 auditadas

| Estado | Significa |
|---|---|
| 🟢 | escribible hoy, sin dependencias |
| 🟡 | escribible con huecos marcados `⟦ ⟧` |
| 🔴 | bloqueado por la corrida o por una decisión |

Convención para huecos: escribir `⟦dato pendiente: X⟧` en el docx. Al cerrar, buscar `⟦`
y verificar que no queda ninguno.

---

## 0 · Portada 🟢

- [ ] Nombres y apellidos completos de los tres integrantes, en el orden acordado
- [ ] Correo de contacto único (decidir cuál)
- [ ] Afiliación verificada: *Maestría en Inteligencia Artificial · Universidad Nacional Mayor de San Marcos*
- [ ] Título definitivo confirmado (hoy: *Detección de casco y chaleco de seguridad en obras de construcción mediante YOLO26*)

---

## 1 · Resumen 🟡  ·  150-200 palabras  ·  se escribe AL FINAL

> Desbloqueado en lo técnico: el resultado principal ya existe (**mAP50 0,8592**). Sigue
> conviniendo escribirlo al final, cuando Discusión esté cerrada.

Los seis elementos en este orden. Cada uno es un ítem porque la rúbrica los busca uno por uno.

- [ ] Problema (seguridad en obra, incumplimiento de EPP)
- [ ] Datos (corpus unificado, 20 944 imágenes, tres fuentes)
- [ ] Método (YOLO26 + protocolo idéntico contra dos generaciones previas)
- [ ] **Resultado principal con su cifra** ← sin esto el resumen no cumple
- [ ] Conclusión en una frase
- [ ] Recuento de palabras entre 150 y 200
- [ ] Palabras clave: de 3 a 5, separadas por punto y coma

---

## 2 · Introducción 🟡  ·  ~1,3 páginas  ·  Rúbrica: problema y justificación (5 pts)

> **✔ DECIDIDO el 2026-10-09 (D16): se ajusta el texto a lo medible.**
>
> El esqueleto prometía *modo NMS-free* y *generalización entre datasets*. El experimento no
> midió ninguna de las dos: CHV quedó repartido en train/val/test, y no se comparó NMS contra
> NMS-free. En lugar de correr experimentos adicionales, se ajusta el aporte declarado.
>
> **Aporte definitivo, para el párrafo (c):**
>
> *YOLO26 supera a dos generaciones previas en detección de casco y chaleco con un 19 % menos
> de parámetros, bajo protocolo idéntico, sobre un corpus unificado de tres fuentes heterogéneas.*
>
> Las dos promesas descartadas pasan a **trabajo futuro** en la Discusión. Declarar lo que no
> se midió, en lugar de omitirlo, juega a favor.

- [x] ✔ **Decisión tomada (D16)**: se ajusta el texto. Aporte definitivo en el recuadro de arriba
- [ ] (a) El problema de visión planteado y su relevancia para la seguridad en obra
- [ ] (a) Dato de contexto con cita (informe HSE, ref. 10) — magnitud del problema, no opinión
- [ ] (b) Antecedentes **integrados en la prosa**, no listados
- [ ] (b) Mención de la revisión sistemática previa como antecedente (ref. 12, *AI Review* 2024)
- [ ] (b) Al menos una frase que identifique el hueco que este trabajo cubre
- [ ] (c) Objetivo del trabajo, explícito
- [ ] (c) Aporte, usando la frase fijada en D16 — **no prometer NMS-free ni generalización**
- [ ] Todas las citas de esta sección existen en la lista de Referencias
- [ ] Extensión ≈ 1,3 páginas

---

## 3 · Métodos  ·  ~2,2 páginas en total  ·  Rúbrica: rigor técnico (4) + reproducibilidad (3)

Criterio global de la sección: **otra persona debe poder repetir el trabajo leyéndola**.

### 3.1 Protocolo de revisión sistemática 🟡  ·  ~0,6 pág

Insumo: `metodologia Prisma/2-protocolo/` · Reportar según PRISMA-S.

- [ ] Bases consultadas y plataforma — Scopus; **declarar WoS como no accesible**
- [ ] Fecha exacta de ejecución: **2026-10-09**
- [ ] Cadena de búsqueda **literal**, tal como se pegó en Scopus
- [ ] Filtros aplicados: `DOCTYPE "ar"`, `PUBYEAR 2021-2026`, inglés y español
- [ ] Criterios de inclusión I1-I7, enunciados
- [ ] Criterios de exclusión E1-E6, enunciados
- [ ] Nº de revisores independientes (2) y cómo se resolvieron discrepancias (un tercero)
- [ ] Cita de PRISMA 2020 (Page et al., *BMJ* n71) y de PRISMA-S (Rethlefsen et al.)
- [ ] Limitación declarada: búsqueda en una sola base
- [ ] ⟦quién ejecutó la búsqueda⟧ y ⟦formato de exportación⟧ — faltan en `CADENAS_BUSQUEDA.md`
- [ ] Cifras del embudo coherentes con la Figura 1

**Cifras disponibles:** 158 identificados en Scopus · 9 por otros métodos · 10 excluidos en
título/resumen · 148 a texto completo · **75 incluidos** (73 excluidos: 39 E3 EPP/tarea fuera de
alcance, 12 sin métrica cuantitativa, 22 texto completo inaccesible). Cribado cerrado
2026-10-26, con dos revisores independientes y dirimido; el 2026-10-27 se reabrieron 23 casos
por evidencia real de elegibilidad (C0 revocado) y luego se reclasificaron 5 de ellos a
inaccesibles por paywall confirmado. Los **75 incluidos finales tienen PDF real** en
`referencias/`. Ver `metodologia Prisma/4-resultados/CIERRE_AUDITADO.md`,
`metodologia Prisma/4-resultados/DIRIMIDO_R3.md` y `referencias/PDFS_FALTANTES.md`.

### 3.2 Conjuntos de datos 🟢  ·  ~0,4 pág

- [x] ✔ **Decidido por coherencia con D16: NO se usa `--chv-externo`.** CHV se queda
      repartido en train/val/test, que es como se entrenó. Las cifras de la Tabla 1 son las
      ya verificadas más abajo. El modo externo queda documentado como trabajo futuro: el
      script lo admite, pero exigiría reentrenar los tres modelos
- [ ] Origen de cada una de las tres fuentes, con su cita
- [ ] Nº de imágenes aportadas por fuente **después** del remapeo
- [ ] Licencias declaradas: Roboflow **CC BY 4.0** · Construction-PPE **AGPL-3.0**
      (copyleft fuerte) · CHV ⟦verificar licencia del repositorio oficial⟧
- [ ] CHV: decir que son **1 330 imágenes seleccionadas de 10 000**, no el dataset completo
- [ ] Dicho que dos de las tres fuentes no están revisadas por pares
- [x] ✔ **RESUELTO y verificado empíricamente el 2026-10-10**: el casco del Roboflow pasa de
      55 393 a 42 428 porque 55 393 = `Hardhat` 42 428 + `NO-Hardhat` 12 965. El remapeo (D10)
      toma **solo `Hardhat`**; las clases negativas se descartan por diseño, al ser un esquema
      de 2 clases positivas. Contado sobre las 44 002 etiquetas crudas: `Hardhat` 42 428 ·
      `NO-Hardhat` 12 965 · `Safety Vest` 6 448 · `NO-Safety Vest` 2 022 · `Person` 1 449 ·
      109 561 cajas en total. **No se perdió ninguna instancia en el remapeo**
- [ ] Clases: 2 positivas (`casco`, `chaleco`) y por qué solo esas
- [ ] División train/val/test y la decisión de conservar las particiones originales
- [ ] Dataset descartado (Pictor-v3) **con su motivo medido**: 39,2:1, solo 42 instancias de chaleco
- [ ] Tabla 1 construida
- [ ] Pie de la Tabla 1 redactado (describe qué muestra, no repite la tabla)

**Cifras verificadas** (`experimento/dataset_unificado/estadisticas.json`):

> ⚠ **No citar `COMPARATIVA_DATASETS.md` para la Tabla 1.** Mide de forma inconsistente entre
> fuentes: para Roboflow suma clase positiva + negativa (55 393 / 8 470), mientras que para
> Construction-PPE ya da cifras netas (1 734 / 1 618). La fuente de verdad es
> `estadisticas.json`. Sigue siendo válido para el análisis por clase y el descarte de Pictor-v3.

| Fuente | Imágenes | Casco | Chaleco | Razón |
|---|---:|---:|---:|---:|
| Roboflow Combined v8 | 18 521 | 42 428 | 6 448 | 6,58 : 1 |
| Construction-PPE | 1 113 | 1 734 | 1 618 | 1,07 : 1 |
| CHV | 1 310 | 3 538 | 1 784 | 1,98 : 1 |
| **Total** | **20 944** | **47 700** | **9 850** | **4,84 : 1** |

Cuadre verificado: 20 944 conservadas + 25 804 descartadas = **46 748**, el total de las tres
fuentes (44 002 + 1 416 + 1 330). Quedan sin usar **12 965 `NO-Hardhat` y 2 022 `NO-Safety
Vest`** del Roboflow: es el material de la extensión de cumplimiento (D10) y un argumento
concreto de trabajo futuro.

| Partición | Imágenes | Casco | Chaleco | Razón |
|---|---:|---:|---:|---:|
| train | 14 729 | 33 099 | 7 164 | 4,62 : 1 |
| val | 4 044 | 9 512 | 1 629 | 5,84 : 1 |
| test | 2 171 | 5 089 | 1 057 | 4,81 : 1 |

### 3.3 Preprocesamiento 🟢  ·  ~0,25 pág

Insumo: `experimento/01_preparar_dataset.py`

- [ ] Redimensionado a 640 × 640 y quién lo aplica (Ultralytics, en carga)
- [ ] **Regla de remapeo de clases**, explícita y repetible
- [ ] Filtrado: 25 804 imágenes descartadas por no contener ninguna clase relevante
- [ ] 10 etiquetas huérfanas de Construction-PPE ignoradas — **30 cajas (16 casco,
      14 chaleco)**. Explica por qué el crudo da 1 750 / 1 632 y el corpus 1 734 / 1 618.
      Verificado el 2026-10-10; son `train/image94*(1).txt`
- [ ] Aumento de datos — **valores reales leídos de `resultados/runs/yolo26n/args.yaml`**:

| Aumento | Valor |
|---|---|
| `mosaic` | 1.0 (desactivado en las últimas 10 épocas por `close_mosaic=10`) |
| `hsv_h` / `hsv_s` / `hsv_v` | 0.015 / 0.7 / 0.4 |
| `fliplr` | 0.5 (horizontal) |
| `scale` | 0.5 · `translate` 0.1 · `erasing` 0.4 |
| `auto_augment` | randaugment |
| Desactivados | `flipud`, `degrees`, `shear`, `perspective`, `mixup`, `cutmix`, `copy_paste` |
- [ ] Mención de que la unificación usa enlaces simbólicos (no duplica los 6 GB)
- [ ] Referencia al script por nombre, para el criterio de reproducibilidad

### 3.4 Modelo 🟢  ·  ~0,4 pág

Insumo: dict `PROTOCOLO` en `experimento/03_entrenamiento_kaggle.ipynb`

- [ ] Arquitectura: YOLO26, escala `n`
- [ ] Transfer learning desde pesos COCO (no desde cero) — dicho explícitamente
- [ ] Hiperparámetros: imgsz 640 · batch 32 · optimizer `auto` · seed 42 · patience 15 · epochs 50
- [ ] ✔ **Épocas efectivas: las 50 en los tres modelos.** `patience=15` no llegó a activarse
- [ ] ✔ **GPU: Tesla T4** (14 912 MiB utilizables) · 1 unidad, `device=0`
- [ ] ✔ **Tiempos**: yolov8n 120,4 min · yolo11n 121,9 min · yolo26n 132,9 min
- [ ] ✔ **Entorno**: Ultralytics 8.4.175 · PyTorch 2.11.0+cu128 · Python 3.13.15
- [ ] Mención de la semilla fija como condición de la comparación

### 3.5 Línea base 🟢  ·  ~0,25 pág

Insumo: decisión D14 de `GUIA_INVESTIGADOR.md`

- [ ] YOLOv8n declarado como **línea base simple** (es lo que pide la rúbrica, literal)
- [ ] YOLO11n declarado como **comparador directo** de generación anterior
- [ ] Justificación de por qué se declaran dos y no una
- [ ] Mismo protocolo para los tres, dicho de forma que se entienda que es un único diccionario

### 3.6 Métricas de evaluación 🟢  ·  ~0,3 pág

- [ ] Métrica principal nombrada (mAP50-95) y **por qué se eligió** ← la justificación es criterio explícito
- [ ] mAP50, precisión y recall como métricas secundarias
- [ ] Argumento del **peso del recall**: en seguridad el falso negativo no cuesta lo mismo que el falso positivo
- [ ] Métricas desagregadas por clase, anunciadas aquí
- [ ] Si se reportan por tamaño de objeto, decirlo aquí (régimen de objeto pequeño en el casco)
- [ ] Conjunto sobre el que se reporta: test, nunca visto en entrenamiento

### Figura 1 — Diagrama de selección auditado ✅

- [x] Adaptación documentada del flujo: selección documental, recuperación y evidencia consultada separadas; C0 revocado
- [x] Recuentos verificados contra los CSV: 158 = 10 + 51 + 22 + 75; sin suma de bibliografía de contexto
- [x] SVG y PNG generados; figura incorporada en el docx
- [x] Pie actualizado a 75 estudios; comprobación visual de la figura realizada

La sección 3.1 de Métodos sigue pendiente de redacción humana. No afirmar cumplimiento integral de PRISMA ni independencia humana de los pases de IA: ver CIERRE_AUDITADO.md.

---

## 4 · Resultados 🟢  ·  ~1,8 páginas  ·  reportar SIN interpretar

> **Desbloqueado el 2026-10-09 a las 21:05.** Cifras en `experimento/RESULTADOS.md`;
> 96 figuras en `experimento/resultados/runs/`.

**Tabla 2 — evaluación sobre el conjunto de prueba (2 171 imágenes):**

| Modelo | Papel | mAP50 | mAP50-95 | Precisión | Recall | Parámetros |
|---|---|---:|---:|---:|---:|---:|
| yolov8n | Línea base simple | 0,8415 | 0,5215 | 0,7586 | 0,8253 | 3 138 246 |
| yolo11n | Comparador directo | 0,8473 | 0,5223 | 0,7647 | 0,8316 | 2 605 126 |
| **yolo26n** | **Modelo propuesto** | **0,8592** | **0,5322** | 0,7505 | **0,8526** | **2 534 372** |

**Tabla 3 — desagregado por clase (mAP50):**

| Modelo | Casco | Chaleco | Brecha |
|---|---:|---:|---:|
| yolov8n | 0,9170 | 0,7661 | 0,1509 |
| yolo11n | 0,9181 | 0,7765 | 0,1416 |
| yolo26n | 0,9251 | 0,7933 | **0,1318** |

**Cifras para el texto:** mejora sobre la línea base **+0,0177 de mAP50 (+2,1 %)** con
**un 19 % menos de parámetros**. Ganancia en chaleco **+0,0272** frente a casco **+0,0081**.

- [ ] Tabla 2 — los tres modelos en la misma métrica
- [ ] Pie de la Tabla 2
- [ ] Tabla 3 — desagregado por clase (casco vs chaleco)
- [ ] Pie de la Tabla 3
- [ ] Figura 2 — matriz de confusión (+ pie)
- [ ] Figura 3 — curvas de entrenamiento (+ pie)
- [ ] Figura 4 — ejemplos de predicción, **con aciertos y fallos** (+ pie)
- [ ] Texto que guía la lectura de cada tabla y figura sin repetir todos los valores
- [ ] Cifra de la mejora sobre la línea base, en puntos y en porcentaje
- [ ] Brecha casco vs chaleco, reportada como dato
- [ ] Ninguna interpretación se ha colado en esta sección

---

## 5 · Discusión 🟢  ·  ~1,2 páginas  ·  Rúbrica: discusión y análisis (2,6 pts)

- [ ] (a) 🟢 Comparación con la línea base y **explicación** de la diferencia *(cifras disponibles)*
- [ ] (b) 🟢 Análisis de errores: oclusión entre trabajadores, régimen de objeto pequeño en el
      casco, efecto del desbalance 4,84:1. **Material medido disponible**: matrices de confusión
      en `runs/*_test/` y la prueba de umbral del servicio desplegado (0,25 → 1 falso positivo;
      0,40 → exacto; 0,60 → pierde el chaleco)
- [ ] (b) 🟢 **Declarar el compromiso precisión-exhaustividad**: yolo26n tiene la precisión más
      baja (0,7505) y el recall más alto (0,8526). Detecta más y se equivoca más. Favorable en
      seguridad, pero **no debe omitirse**
- [ ] (c) 🟢 Limitación: heterogeneidad de las tres fuentes y sus paradigmas de anotación
- [ ] (c) 🟢 Limitación: deformación por redimensionado a 640
- [ ] (c) 🟢 Limitación: ausencia de clase negativa para el chaleco
- [ ] (c) 🟢 Limitación: dos de los tres datasets sin revisión por pares
- [ ] (c) 🟢 Limitación: búsqueda sistemática en una sola base (WoS inaccesible)
- [ ] (c) 🟢 Limitación: escala `n` de los modelos, no `s`/`m`
- [ ] (d) 🟢 Conclusión anclada en los datos, sin afirmar más de lo medido
- [ ] (d) 🟢 **Trabajo futuro, con lo descartado por D16**: evaluación del modo NMS-free,
      generalización entre datasets manteniendo CHV como test externo (el script ya admite
      `--chv-externo`), clases negativas para cumplimiento, y escalas `s`/`m`

---

## 6 · Declaración sobre uso de IA 🟢  ·  obligatoria por rúbrica

Nadie depende de ti para esto y vale puntos. Insumo: sección 6 de `GUIA_INVESTIGADOR.md`.

- [ ] Declarar que la redacción es íntegramente humana
- [ ] Declarar el apoyo en **estructura y esqueletos**
- [ ] Declarar el apoyo en **decisiones metodológicas, cadenas de búsqueda y criterios**
- [ ] Declarar el apoyo en **análisis de datasets y tablas de medición**
- [ ] Declarar el apoyo en **código** (scripts, notebook, despliegue)
- [ ] Declarar el apoyo en **cribado preliminar** de la literatura
- [ ] Declarar el apoyo en **verificación de cifras y referencias**
- [ ] Nombrar la herramienta y el periodo de uso

---

## 7 · Referencias 🟢  ·  formato IEEE

- [ ] Mínimo **25** referencias (hoy: 30 PDFs, 26 cumplen I1-I7)
- [ ] Todas de revistas indexadas en Scopus y/o WoS
- [ ] Formato IEEE **consistente** en las 30: autores, título, revista, vol., n.º, pp., año
- [ ] Numeración en orden de primera aparición en el texto
- [ ] Toda cita del texto aparece en la lista
- [ ] Nada en la lista queda sin citar en el texto ← error más frecuente
- [ ] Referencias metodológicas incluidas: PRISMA 2020, PRISMA-S, fuentes de los 3 datasets, YOLO26
- [ ] ⟦resolver P1⟧ si entra LACCEI (actas de congreso) — consulta al docente

---

## 8 · Cierre del documento 🟡

- [ ] **Todos los bloques naranja de GUÍA eliminados** (son instrucciones, no texto)
- [ ] Todos los recuadros grises sustituidos por la tabla o figura real
- [ ] Búsqueda de `⟦` en el documento: cero resultados
- [ ] Búsqueda de `[` en el documento: solo lo que debe quedar
- [ ] Extensión total entre 6 y 8 páginas
- [ ] Todas las tablas y figuras están citadas en el texto («como muestra la Tabla 2…»)
- [ ] Numeración de tablas y figuras continua y sin saltos
- [ ] Revisión ortográfica y de concordancia
- [ ] Una lectura completa en voz alta de principio a fin

### Entregables anexos (no van dentro del docx)

- [ ] Checklist PRISMA de 27 ítems, cumplimentada
- [ ] Notebook reproducible de principio a fin
- [ ] Repositorio ordenado con los scripts citados en Métodos

---

## Panel de avance

| Bloque | Ítems | Hechos | Estado |
|---|---:|---:|---|
| 0 Portada | 4 | 0 | 🟢 |
| 1 Resumen | 7 | 0 | 🟡 |
| 2 Introducción | 10 | 1 | 🟡 |
| 3.1 PRISMA | 11 | 0 | 🟡 |
| 3.2 Datasets | 12 | 2 | 🟢 |
| 3.3 Preprocesamiento | 7 | 0 | 🟢 |
| 3.4 Modelo | 7 | 4 | 🟢 |
| 3.5 Línea base | 4 | 0 | 🟢 |
| 3.6 Métricas | 6 | 0 | 🟢 |
| Figura 1 | 4 | 4 | ✅ |
| 4 Resultados | 11 | 0 | 🟢 |
| 5 Discusión | 11 | 0 | 🟢 |
| 6 Declaración IA | 8 | 0 | 🟢 |
| 7 Referencias | 8 | 0 | 🟢 |
| 8 Cierre | 9 | 0 | 🟡 |
| **Total** | **119** | **11** | |

**Escribible hoy sin ninguna dependencia: 78 ítems.** Con el entrenamiento cerrado, se suman
Resultados (11), Discusión (11), 3.4 Modelo (7) y el Resumen en lo técnico.

**Figura 1 actualizada el 2026-10-27 (tarde):** 75 incluidos; SVG y pie del Word a resincronizar tras reclasificar 5 casos a E5 por paywall confirmado. Ver CIERRE_AUDITADO.md para alcance y límites de la evaluación documental.

---

## Cómo lo usamos

1. Eliges un bloque y lo redactas en el docx.
2. Me dices «revisemos 3.2» y yo lo contrasto ítem por ítem contra este checklist y contra
   las cifras de los archivos fuente. Señalo lo que falta o no cuadra; **no reescribo el texto**.
3. Marcamos los `[x]` y actualizamos el panel.

Orden recomendado: **3.2 → 3.3 → 3.5 → 3.6 → 6 → 7 → 3.1 → 2 → 5(c) → [corrida] → 4 → 5 → 1 → 8**

## Bitácora de revisiones

| Fecha | Bloque | Resultado |
|---|---|---|
| 2026-10-26 | 3.1 PRISMA | Cerrado el cribado de texto completo de los 148 estudios: R1 y R2 independientes + dirimido de discrepancias. **74 incluidos / 74 excluidos** en el dirimido inicial, basado en resumen/título — ver `DIRIMIDO_R3.md` |
| 2026-10-26 | 3.1 PRISMA | Descargados los PDF reales de los incluidos. Los 16 que no se pudieron recuperar (14 tras paywall, 2 sin DOI) se reclasificaron a excluidos (E5, texto completo inaccesible). **Cifra final: 58 incluidos / 90 excluidos** |
| 2026-10-27 | 3.1 PRISMA | Resolución de 23 casos "C0" con evidencia real (web/PDF): C0 revocado, **80 incluidos / 68 excluidos** |
| 2026-10-27 | 3.1 PRISMA | De esos 23, 5 (ids 80, 11, 87, 94, 100) sin PDF local ni acceso alternativo — paywall confirmado por el equipo, sin presupuesto. Reclasificados a E5. **Cifra final: 75 incluidos / 73 excluidos** (39 E3, 12 E4, 22 E5), con PDF real para los 75 |
| 2026-10-10 | Todo el artículo | Generado `REFERENCIA_PARRAFOS.md`: párrafos de referencia de todas las secciones en orden, con los irrenunciables de cada bloque. Material de lectura, no texto del paper. El párrafo (b) de la Introducción va solo como andamiaje: exige leer los PDF |
| 2026-10-10 | 3.2 · 3.3 | Auditadas las cifras contra las etiquetas crudas de las tres fuentes. Confirmada la explicación del 55 393 contando clase por clase. Localizadas las 10 etiquetas huérfanas (30 cajas) que explican el desfase de Construction-PPE. Añadido aviso: `COMPARATIVA_DATASETS.md` no sirve para la Tabla 1 |
| 2026-10-10 | 3.2 Datasets | Cerrado `--chv-externo` por coherencia con D16: no se usa. Bloque 3.2 pasa a 🟢 |
| 2026-10-09 23:35 | 2 Introducción | **D16: se ajusta el texto a lo medible.** Aporte fijado; NMS-free y generalización pasan a trabajo futuro. Actualizado también el esqueleto .docx |
| 2026-10-09 22:55 | Actualización general | Entrenamiento completado. Desbloqueados Resultados, Discusión y Resumen. Cerrados 5 huecos ⟦⟧ de 3.2 y 3.4 con datos reales. Único bloqueo restante: Figura 1 (cribado) |
