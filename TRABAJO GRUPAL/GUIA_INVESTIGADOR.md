> **Cifras oficiales del cribado: [RESUMEN_CRIBADO_PRISMA.docx](<metodologia Prisma/4-resultados/RESUMEN_CRIBADO_PRISMA.docx>) — 158 identificados, 75 incluidos / 73 excluidos.** Si este archivo muestra otras cifras, son históricas.

> **Estado vigente (2026-10-27, tarde): 75 incluidos / 73 excluidos.** De los 23 casos
> reincorporados por evidencia (C0 revocado), 5 quedaron sin PDF accesible — paywall
> confirmado por el equipo, sin presupuesto — y se reclasificaron a E5. Son los mismos 148
> estudios, sin búsqueda de nuevos papers. Ver [estado auditado](<metodologia Prisma/4-resultados/CIERRE_AUDITADO.md>). Los recuentos anteriores (80/68, 58/90, 74/74) son históricos.

# Guía del investigador — estado del proyecto

Documento de orientación y seguimiento. Resume **qué se está construyendo, dónde está cada
cosa, qué se decidió y por qué, y qué falta**. Pensado para leerse de principio a fin una vez
y consultarse por secciones después.

**Última actualización:** 2026-11-02 (secciones del cribado sincronizadas con `RESUMEN_CRIBADO_PRISMA.docx`)

---

## 1. El encargo en una página

| | |
|---|---|
| **Título** | *Detección de casco y chaleco de seguridad en obras de construcción mediante YOLO26* |
| **Formato** | Artículo corto IMRyD, 6-8 páginas, estilo conferencia, referencias IEEE |
| **Referencias** | Mínimo **25** de revistas indexadas en Scopus/WoS |
| **Método de revisión** | **PRISMA 2020** (indicación del docente en clase) |
| **Evaluación** | **Parcial: sábado 7 nov 2026** (20%) · **Final: sábado 12 dic 2026** (40%) · ambos sobre 20 |
| **Nota mínima** | 14 · una fracción de 13,5 redondea al entero superior |
| **Integridad** | Obligatorio declarar todo apoyo de IA en redacción y código |

Fuente: `Rubrica_Plantilla_Proyecto_VC.pdf`

### Dos cuentas que conviene tener presentes

1. **"Aceptable" en todos los criterios da exactamente 12,0/20** — desaprobado. Para llegar a
   13,5 hace falta "Excelente" en criterios que sumen al menos 3,75 puntos, sin ningún
   "Insuficiente".
2. **En el examen final, comunicar pesa más que el resultado técnico**: defensa oral (6) +
   escritura (2,4) + formato (2) = 10,4 puntos, frente a 4 de rigor técnico.

---

## 2. Mapa de carpetas

```
TRABAJO GRUPAL/
├── GUIA_INVESTIGADOR.md          ← este documento
├── Rubrica_Plantilla_Proyecto_VC.pdf   ← el encargo del curso
├── CRONOGRAMA.md                 ← fechas, hitos y plan semanal
│
├── Sobre Diagramas de Flujo/     ← seguimiento visual del proceso (uso interno)
│   ├── 01_MAPA_GENERAL.md        ← los 4 frentes y cómo confluyen
│   ├── 02_FLUJO_PRISMA.md        ← el embudo de la revisión
│   ├── 03_PIPELINE_EXPERIMENTO.md ← del dato crudo al resultado
│   ├── 04_DEPENDENCIAS.md        ← qué bloquea qué y ruta crítica
│   └── LEEME.md y «Cómo cribar los 148 estudios.md»
│
├── doc-borrador/                 ← el artículo en construcción
│   └── Esqueleto_Paper_EPP_YOLO26.docx
│
├── referencias/                  ← TODA la bibliografía (75 PDFs numerados 01-75; contexto en _contexto_no_citados/ como C##)
│   ├── TABLA_SEGUIMIENTO.md      ← inventario con ID, procedencia y uso previsto
│   ├── TABLA_SEGUIMIENTO.csv     ← la misma tabla, filtrable
│   └── README.md                 ← DOI y URL de descarga de las halladas en búsqueda
│
├── APORTACIONES/                 ← documentos propios de Arnold y Javier (síntesis, notas)
│
├── metodologia Prisma/           ← la revisión sistemática, por etapas
│   ├── LEEME.md                  ← índice y estado del embudo
│   ├── 1-metodo/                 ← qué dice la norma (PDFs + plantillas)
│   ├── 2-protocolo/              ← qué decidimos nosotros
│   ├── 3-busqueda/               ← qué arrojó la búsqueda (evidencia cruda)
│   └── 4-resultados/             ← qué sacamos de ello
│
├── experimento/                  ← el prototipo
│   ├── 01_preparar_dataset.py    ← unificación a 2 clases (reproducible)
│   ├── 02_empaquetar_para_kaggle.sh ← genera el ZIP de 1,6 GB
│   ├── 03_entrenamiento_kaggle.ipynb ← compara los 3 modelos
│   ├── despliegue/               ← servicio de inferencia (VPS, puerto 8090)
│   └── dataset_unificado/        ← 20 944 img · enlaces, no copias (NO está en el repositorio: se regenera con 01_preparar_dataset.py)
│       ├── data.yaml             ← configuración para YOLO26
│       ├── manifiesto.csv        ← trazabilidad imagen → origen
│       └── estadisticas.json     ← conteos por fuente y partición
│
└── dataset/                      ← datos crudos del experimento (6,1 GB) · NO está en el repositorio (ver experimento/DATASET.md)
    ├── COMPARATIVA_DATASETS.md   ← los cuatro, medidos y comparados
    ├── ANALISIS_DATASET.md       ← análisis detallado del Roboflow
    ├── Personal Protective Equipment...v8i.yolo26/   (44 002 img)
    ├── CHV/                      (1 330 img)
    ├── Construction-PPE/         (1 416 img)
    └── Pictor-v3/                (solo etiquetas — descartado)
```

**Por qué `metodologia Prisma/` está dividida en cuatro etapas numeradas:** siguen el orden
real en que se ejecuta una revisión sistemática — qué dice la norma, qué decidimos nosotros,
qué arrojó la búsqueda, qué sacamos de ello. Para saber en qué punto va el trabajo basta ver
cuál es la última carpeta con contenido. Además separa lo que **no se toca** (el método) de lo
que **crece** (los resultados), y mantiene la evidencia cruda auditable, que es lo que PRISMA exige.

---

## 3. Estado por frente de trabajo

### A. Bibliografía y revisión sistemática ✅ cerrada

| Hito | Estado |
|---|---|
| Pregunta de revisión | ✅ definida |
| Criterios I1-I7 y E1-E6 | ✅ definidos |
| Cadenas de búsqueda | ✅ escritas para Scopus y WoS |
| Búsqueda en Scopus | ✅ ejecutada — **158 registros**, exportados con resumen |
| Búsqueda en WoS | ✅ **abandonada por decisión del equipo (D20)** — declarada como limitación en Métodos |
| Cribado título/resumen | ✅ primer tamizaje — 10 excluidos, 148 pasan |
| Cribado texto completo | ✅ **cerrado: 75 incluidos / 73 excluidos** — al cierre 72 con PDF local, 2 con PDF web y 1 con cuerpo indexado — hoy los 75 tienen PDF local en `referencias/`; cifras oficiales en `RESUMEN_CRIBADO_PRISMA.docx` (R1+R2+dirimido → 58/90; +23 reincorporados por evidencia real el 2026-10-27 → 80/68; −5 reclasificados a E5 por paywall confirmado → 75/73) |
| Esqueleto del artículo | ✅ generado en `doc-borrador/` |
| Diagrama de flujo | ✅ Figura 1 sincronizada con los 75 incluidos (SVG, PNG y pie del Word) |

**Inventario de referencias (histórico):** 30 PDFs unificados en `referencias/`, con
identificador estable. Quedó superado por el cribado cerrado: la regla vigente es que **el
paper cita solo estudios de los 75 incluidos** más referencias de método.

**Referencias del paper (2026-11-02):** 32 en orden de aparición — **27 artículos de revista**
(25 incluidos en el cribado, más PRISMA/BMJ y Nath; el mínimo es 25) y 5 de método (datos y
software: Roboflow, CPPE y documentación de YOLOv8, YOLO11 y YOLO26). Los PDFs citados
están todos en `referencias/` (carpeta única de PDFs; `referencias/INDICE_PAPER.md` dice qué archivo es cada referencia). **SCIE/SSCI (D19):** validado por Abel
el 2026-11-02; las revistas citadas cumplen los filtros, por lo que el mínimo de 25 está cubierto.

*Procedencia del inventario histórico de 30 PDFs (no del conjunto actual de 75):*

| Aportó | Referencias |
|---|---:|
| Búsqueda sistemática | 16 |
| Arnold | 5 |
| Javier | 4 |
| eladio | 4 |
| Raíz del proyecto | 1 |

### B. Datos del experimento ✅ resuelto

Cuatro datasets evaluados midiendo sus etiquetas reales, no sus fichas:

| Dataset | Imágenes | Casco:Chaleco | Papel asignado |
|---|---:|---:|---|
| Roboflow Combined v8 | 44 002 | 6,58 : 1 | entrenamiento (escala + clases negativas) |
| **Construction-PPE** | 1 416 | **1,07 : 1** | refuerzo de chaleco — el mejor balanceado |
| **CHV** | 1 330 | 1,98 : 1 | test externo, peer-reviewed, con persona |
| Pictor-v3 | 774 | 39,2 : 1 | **descartado** — solo 42 instancias de chaleco |

Este frente está por delante de lo que exige la rúbrica en esta fase.

### C. Experimento y prototipo 🟢 resuelto

| Hito | Estado |
|---|---|
| Arquitectura elegida | ✅ YOLO26 (estable desde enero 2026, NMS-free opcional) |
| Esquema de clases | ✅ 2 clases positivas: `casco`, `chaleco` |
| Unificación de datasets | ✅ script reproducible, **20 944 imágenes** generadas |
| Línea base definida | ✅ YOLOv8n simple + YOLO11n comparador |
| Notebook de entrenamiento | ✅ `03_entrenamiento_kaggle.ipynb` |
| Dataset empaquetado | ✅ ZIP de 1,6 GB listo para subir |
| Subir a Kaggle y entrenar | ✅ v5, 50 épocas, ~6 h |
| **Primer resultado** | ✅ **YOLO26n: mAP50 0,8592 · mAP50-95 0,5322** |
| Servicio de inferencia | ✅ VPS `213.136.69.236:8090` |
| Interfaz de demostración | ✅ v0.2 — dibuja las cajas, umbral ajustable |
| **Modelo desplegado y verificado** | ✅ `pesos_presentes: true`, inferencia real comprobada |

**Resultado sobre el conjunto de prueba** — detalle en `experimento/RESULTADOS.md`:

| Modelo | mAP50 | mAP50-95 | Recall | Casco | Chaleco | Parámetros |
|---|---:|---:|---:|---:|---:|---:|
| yolov8n (línea base) | 0,8415 | 0,5215 | 0,8253 | 0,9170 | 0,7661 | 3 138 246 |
| yolo11n | 0,8473 | 0,5223 | 0,8316 | 0,9181 | 0,7765 | 2 605 126 |
| **yolo26n** | **0,8592** | **0,5322** | **0,8526** | **0,9251** | **0,7933** | **2 534 372** |

YOLO26n mejora la línea base en +2,1% de mAP50 **con un 19% menos de parámetros**. La ganancia
se concentra en el chaleco (+0,0272) frente al casco (+0,0081). Tiene la precisión más baja
(0,7505) y el recall más alto: detecta más y se equivoca algo más — intercambio favorable en
seguridad, pero hay que declararlo en la Discusión.

**Demo desplegada y verificada.** Prueba real contra una imagen del conjunto de test
(etiqueta: 1 casco, 1 chaleco):

| Umbral | Detecciones | Resultado |
|---|---|---|
| 0,25 | casco ×1, chaleco ×2 | un chaleco de más, a 0,292 de confianza |
| **0,40** | casco ×1, chaleco ×1 | **exacto** |
| 0,60 | casco ×1, chaleco ×0 | pierde el chaleco |

Latencia: **~95 ms por imagen** en CPU con el modelo en memoria. La **primera** petición tarda
**~17 s** por la carga diferida del modelo.

> **Para la defensa:** hacer una petición de calentamiento diez minutos antes. 17 segundos de
> espera delante del jurado se hacen eternos. El deslizador de umbral es además un buen recurso
> para ilustrar en vivo el compromiso precisión-exhaustividad en lugar de solo explicarlo.

**Dataset unificado:**

| Partición | Imágenes | Casco | Chaleco | Razón |
|---|---:|---:|---:|---:|
| train | 14 729 | 33 099 | 7 164 | 4,62 : 1 |
| val | 4 044 | 9 512 | 1 629 | 5,84 : 1 |
| test | 2 171 | 5 089 | 1 057 | 4,81 : 1 |
| **Total** | **20 944** | **47 700** | **9 850** | **4,84 : 1** |

Se descartaron 25 804 imágenes sin ninguna clase relevante. La unificación usa enlaces
simbólicos, no copias: no duplica los 6 GB de datos crudos.

**Es el camino crítico.** La rúbrica del parcial da 6 puntos a "prototipo que corre y arroja
un primer resultado". Sin él, el techo del parcial es 14/20 aun bordando todo lo demás.

### D. Redacción 🟡 borrador completo, con decisiones pendientes

Existe un borrador completo en `doc-borrador/Esqueleto_Paper_EPP_YOLO26.docx` (resumen de
186 palabras, secciones 1 a 4, declaración de IA y 32 referencias), **recortado a 8 páginas
en total** (2026-11-02). Pendiente:

- **Autoría.** La regla del equipo es «redacción 100% humana» (sección 6), pero la
  introducción, la sección 2.1, la declaración de IA y parte de la discusión se redactaron
  con apoyo de IA. El equipo debe decidir: reescribirlas a mano, o cambiar la regla y
  conservar la declaración. No se ha cambiado la regla.
- **Extensión.** Resuelta: 8 páginas con referencias (la rúbrica pide 6-8). Se quitó la figura de curvas de entrenamiento y se compactaron Introducción, Métodos y Discusión.
- **Referencias.** SCIE/SSCI validado (ver frente A). Cifras contrastadas con los PDFs
  (2026-11-02): los 25 estudios incluidos citados coinciden (incluidos SH17: 70,9 % de mAP50, y
  CSOD-24: mAP@0.5 de 0,982). Se corrigió la afirmación sobre versiones de
  YOLO: DAF-YOLO (ID 58) compara YOLOv12n, así que la más reciente comparada es YOLOv12n.

---

## 4. Decisiones tomadas y por qué

| # | Decisión | Razón |
|---|---|---|
| D1 | Título fijado | Cumple la guía: problema + enfoque en una línea, sin adornos |
| D2 | YOLO26 como modelo | Versión estable de Ultralytics desde enero 2026; +1,6-2,8 AP sobre YOLO11; el modo NMS-free da una pregunta de investigación real bajo oclusión |
| D3 | PRISMA solo para la revisión de literatura, no como proyecto | La rúbrica premia un trabajo experimental: dataset, prototipo, línea base y código valen 11/20 en el parcial. Una revisión sistemática no produce ninguno |
| D4 | Pregunta de revisión acotada a casco y/o chaleco en construcción | Rinde 30-60 estudios: suficiente para 25 sin volverse inmanejable |
| D5 | Ventana 2021-2026 | Era post-YOLOv5. No afecta a las citas metodológicas, que van aparte |
| D6 | Diagrama de flujo **v2**, no v1 | Incluye la columna de "otros métodos", donde entran las referencias halladas fuera de las bases |
| D7 | Pictor-v3 descartado | Solo 42 instancias de chaleco; razón casco:chaleco de 39:1 |
| D8 | I5 aplicado de forma permisiva en el cribado | El criterio estricto excluía 14 estudios de alto impacto, entre ellos uno que el propio equipo ya había seleccionado |
| D9 | Referencias unificadas en `referencias/` con ID estable (renumeradas 01-75 el 2026-11-02; ver `MAPA_RENUMERACION.csv`) | Evita duplicados entre carpetas y permite citarlas por número. La procedencia se conserva en la tabla de seguimiento |
| D10 | Esquema de **2 clases positivas** (`casco`, `chaleco`) | Es lo que promete el título. Los tres datasets fusionan sin ruido de etiqueta, y el desbalance mejora de 6,6:1 a 4,8:1. El experimento de cumplimiento con clases negativas queda como extensión. **Confirmado el 2026-11-02:** se mantienen las 2 clases; la propuesta de 4 clases del chat (con `NO-Hardhat` y `NO-Safety Vest`) se descarta para este trabajo y pasa a trabajo futuro |
| D11 | Se conservan las particiones originales de cada fuente | No re-particionar evita mezclar imágenes que los autores separaron deliberadamente |
| D12 | Entrenar en Kaggle, desplegar en el VPS | Ninguna máquina disponible tiene GPU. El VPS (12 núcleos, 46 GB, sin GPU) no entrena, pero sirve la demo de la defensa |
| D13 | Despliegue versionado en el repositorio, no editado en el servidor | Hace reproducible el despliegue, que es parte del criterio de reproducibilidad (3 pts) |
| D14 | **Tres modelos**: YOLOv8n (línea base simple), YOLO11n (comparador directo), YOLO26n (propuesto) | La guía pide "el método simple" como línea base; comparar solo contra YOLO11 no satisface esa lectura. Con tres se cubren ambas interpretaciones |
| D15 | Protocolo idéntico aplicado como diccionario único | Impide que se cuele un hiperparámetro distinto entre modelos. Es lo que hace legítima la comparación |
| **D17** | No se usa `--chv-externo`: CHV permanece repartido en las tres particiones | Coherencia con D16. Usarlo exigiría reentrenar los tres modelos, y el aporte ya no lo promete. Queda como trabajo futuro, con el script preparado |
| **D16** | **El aporte declarado se ajusta a lo medido**, no al revés | El esqueleto prometía modo NMS-free y generalización entre datasets; el experimento no midió ninguna. En vez de correr experimentos extra con el parcial a 4 semanas, se declara lo demostrado: *YOLO26 supera a dos generaciones previas con un 19 % menos de parámetros, bajo protocolo idéntico*. Lo descartado pasa a trabajo futuro |
| D18 | Las actas de congreso **no** cuentan para el mínimo de 25 referencias — solo publicaciones en revista | Respuesta del docente a P1. La ref. #C13 (antes #13; *Smart SSOMA*, LACCEI, actas) queda fuera del conteo; puede seguir citándose como contexto pero no computa como "alto impacto". No afecta a los 75 estudios incluidos de la revisión sistemática: los 148 cribados son 100 % artículos de revista (`doc_type = Article` en Scopus), ninguno es acta |
| D19 | En Web of Science solo cuentan revistas indexadas en **SCIE/SSCI**, no basta ESCI | Respuesta del docente a P2. Aplica cuando se resuelva el acceso a WoS (P4, aún bloqueado); mientras tanto no cambia nada porque la búsqueda se hizo solo en Scopus |
| D20 | Se **abandona** la gestión de acceso institucional a WoS (P4) | Decisión del equipo: el mínimo de 25 referencias está superado con margen amplio (75 al cierre del cribado, todos con PDF real), así que el costo de perseguir el acceso ya no se justifica. Se declara como **limitación de Métodos**: "la búsqueda se realizó en Scopus; no se tuvo acceso institucional a Web of Science Core Collection" |

---

## 5. Decisiones pendientes y bloqueos

| # | Pendiente | Bloqueado por | Urgencia |
|---|---|---|---|
| ~~P1~~ | ~~¿Cuentan las actas de congreso como "alto impacto"?~~ | **resuelto (D18): no, solo revista** | — |
| ~~P2~~ | ~~¿Se admiten revistas solo en ESCI, o deben estar en SCIE?~~ | **resuelto (D19): debe estar en SCIE/SSCI** | — |
| ~~P3~~ | ~~Fechas exactas~~ | **resuelto: 7 nov y 12 dic** | — |
| ~~P4~~ | ~~Acceso institucional a Web of Science~~ | **resuelto (D20): se abandona, declarado como limitación** | — |
| ~~P5~~ | ~~Regla de homologación de clases~~ | **resuelto (D10)** | — |
| ~~P6~~ | ~~Línea base del experimento~~ | **resuelto (D14)** | — |
| ~~P7~~ | ~~Asignación de revisores para el cribado~~ | **resuelto: R1 = IA, R2 = otra IA, R3 (dirimido) = IA** | — |

### Consulta al docente — respondida (2026-10-26)

> 1. Para la revisión sistemática, ¿las actas de congreso (CVPR, ICCV, ECCV, congresos IEEE)
>    cuentan como "revistas de alto impacto indexadas en Scopus/WoS" para el mínimo de 25
>    referencias, o la exigencia se limita estrictamente a publicaciones en revista?
>    **→ Estrictamente a publicaciones en revista (D18).**
> 2. En Web of Science, ¿se admiten revistas indexadas solo en ESCI, o deben estar en SCIE/SSCI?
>    **→ Debe estar en SCIE/SSCI (D19).**


### Sobre Web of Science — cerrado (D20)

La cuenta personal de Clarivate da acceso al Researcher Profile pero **no a la Core
Collection**, y la conexión no procede de la red universitaria. El equipo **decidió no seguir
persiguiendo el acceso institucional** (portal de biblioteca, VPN): el mínimo de 25 referencias
ya está superado con margen (75 al cierre del cribado), así que el costo no
se justifica.

> **Se declara como limitación en Métodos**: *"la búsqueda se realizó en Scopus; no se tuvo
> acceso institucional a Web of Science Core Collection"*. Buscar solo en Scopus es válido si
> se justifica. Lo que no vale es decir que se buscó donde no se buscó.

---

## 6. Cómo trabajamos

### La redacción es 100% humana

> **Aviso (2026-11-02):** el borrador actual no cumple esta regla (ver frente D). Hay que
> decidir en equipo si se reescribe o se cambia la regla. Mientras tanto, el texto sigue
> declarado como asistido por IA.

Ningún texto del paper —resumen, introducción, métodos, resultados, discusión,
conclusiones— lo escribe una herramienta de IA. Tampoco borradores para editar.

El apoyo de IA se limita a: estructura y esqueletos, decisiones metodológicas, cadenas de
búsqueda y criterios, análisis de datos y tablas de medición, código, verificación de cifras
y referencias, y detección de huecos o incoherencias en lo que escribe el equipo.

### Y aun así se declara

La rúbrica exige declarar **todo** apoyo de IA, no solo el de redacción. El análisis de
datasets, el cribado preliminar y el código entran en esa declaración. Conviene reservar un
párrafo antes de las referencias desde ahora.

### Reparto del equipo

El equipo son cinco integrantes (Eladio Abel Condori, Eduardo Ramirez Benavides, Javier Villegas
Lainas, Juan Gonzalo Azabache Carrillo y Arnold Alvarado Giron). PRISMA pide cribado por dos
revisores independientes y un tercero que resuelva las discrepancias; en la práctica R1, R2 y R3
fueron asistentes de IA (P7) y el paper lo declara así, sin validación humana independiente.

---

## 7. Glosario

| Término | Qué significa |
|---|---|
| **IMRyD** | Introducción, Métodos, Resultados y Discusión. La estructura del artículo |
| **PRISMA 2020** | Guía para reportar revisiones sistemáticas. Define qué declarar y cómo |
| **PRISMA-S** | Extensión de PRISMA específica para reportar la estrategia de búsqueda |
| **Cribado (screening)** | Filtrar los registros hallados. Primero por título y resumen, luego por texto completo |
| **Elegibilidad** | Segunda etapa del filtrado: se lee el texto completo y cada exclusión exige motivo |
| **Diagrama de flujo** | El recuento del embudo: identificados → cribados → evaluados → incluidos |
| **Estudios incluidos** | Los que sobreviven al cribado y alimentan la Introducción |
| **mAP** | Mean Average Precision. Métrica estándar en detección de objetos |
| **Línea base** | Método simple contra el que se compara el modelo propuesto. La rúbrica lo exige |
| **NMS** | Non-Maximum Suppression. Paso que elimina detecciones duplicadas; YOLO26 permite evitarlo |
| **Clases negativas** | Etiquetas del tipo `NO-Hardhat`: marcan la ausencia del EPP, no su presencia |

---

## 8. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| ~~No haber prototipo en semana 10~~ | ~~Techo de 14/20~~ | **resuelto: hay resultados** |
| ~~Sin acceso a WoS~~ | ~~Búsqueda incompleta~~ | **resuelto (D20): se abandona, declarada como limitación en Métodos — no cambia el resultado porque el mínimo de 25 ya está superado con margen** |
| ~~148 textos completos por evaluar~~ | ~~Carga alta para tres personas~~ | **resuelto: cribado cerrado el 2026-10-27 (75 incluidos / 73 excluidos)** |
| ~~Entrenar 30 765 imágenes~~ | ~~Excede el límite de sesión de Colab gratuito~~ | **resuelto: se entrenó en Kaggle (T4) con 20 944 imágenes, ~6 h** |
| ~~Paradigmas de anotación incompatibles~~ | ~~Impide fusionar datasets sin más~~ | **resuelto (D10): remapeo a 2 clases documentado** |
| Desbalance casco/chaleco | Resultados peores en chaleco | Construction-PPE y CHV lo compensan; reportarlo como limitación |
| Regla «redacción 100% humana» incumplida por el borrador | Conflicto con la decisión del equipo y la rúbrica de IA | Decidir: reescribir a mano o cambiar la regla y mantener la declaración |
| Licencia AGPL de Construction-PPE y Kaggle privado | Bloquea la reproducibilidad (3 pts) | Revisar la licencia y publicar el dataset antes de la entrega |

---

## 9. Lo siguiente

Actualizado 2026-11-02 — todo lo técnico y metodológico de la revisión sistemática está
resuelto (cribado cerrado el 2026-10-27: **75 incluidos / 73 excluidos** de 158 identificados;
Figura 1 sincronizada; P1-P7 respondidas). Cifras oficiales en
`metodologia Prisma/4-resultados/RESUMEN_CRIBADO_PRISMA.docx`.
Lo que queda, en orden de urgencia:

1. **Decidir la regla de autoría** (humana vs. asistida y declarada) — de ella depende si el
   equipo reescribe el borrador. Las limitaciones del cribado ya están declaradas en 2.1 y 4.
2. **Exposición del parcial (7 nov):** preparar las diapositivas y ensayar. Aún no existen.
3. ~~Ajustar el paper a 6-8 páginas~~ hecho: 8 páginas en total.
4. **Referencias:** ya están en estilo IEEE; solo falta una revisión final de formato contra la plantilla (SCIE/SSCI y cifras ya contrastados).
5. **Reproducibilidad (entrega final, 12 dic):** resolver la licencia AGPL de Construction-PPE
   y hacer accesible el dataset de Kaggle (hoy privado) antes de entregar el cuaderno.

---

## 10. Bitácora de avances

Registro cronológico de lo que se va completando, para sincronizar al equipo.

| Fecha | Avance |
|---|---|
| 2026-10-09 | Reunidas 16 referencias nuevas en `referencias/`, con DOI y URL documentados |
| 2026-10-09 | Descargados y **medidos** 4 datasets; Pictor-v3 descartado con justificación numérica |
| 2026-10-09 | Definidos pregunta de revisión y criterios I1-I7 / E1-E6 |
| 2026-10-09 | Escritas las cadenas de búsqueda para Scopus y WoS |
| 2026-10-09 | **Búsqueda ejecutada en Scopus: 158 registros** exportados con resumen |
| 2026-10-09 | Cribado por título y resumen: 10 excluidos, 148 pasan a texto completo |
| 2026-10-09 | Verificadas 13 de 16 referencias contra los resultados de Scopus |
| 2026-10-09 | Generado el esqueleto del artículo en `doc-borrador/` |
| 2026-10-09 | Reorganizada `metodologia Prisma/` en cuatro etapas numeradas |
| 2026-10-09 | Unificadas las 30 referencias en `referencias/` con ID estable y tabla de seguimiento |
| 2026-10-09 | Fijado el esquema de 2 clases; **dataset unificado de 20 944 imágenes** generado y verificado |
| 2026-10-09 | Creada `Sobre Diagramas de Flujo/` con 4 diagramas Mermaid de seguimiento del proceso |
| 2026-10-09 | Servicio de inferencia desplegado en el VPS, puerto 8090, sin alterar el stack existente |
| 2026-10-09 | Definida la línea base (3 modelos); dataset empaquetado y notebook de entrenamiento listo |
| 2026-10-09 | Fechas confirmadas: parcial 7 nov, final 12 dic. Cronograma con hitos creado |
| 2026-10-09 | Corrida real lanzada en Kaggle (v5, 50 épocas). Interfaz de la demo rehecha con visualización de detecciones |
| 2026-10-09 | **Entrenamiento completado. YOLO26n gana: mAP50 0,8592 frente a 0,8415 de la línea base** |
| 2026-10-09 | Pesos de YOLO26n desplegados en el VPS; demo verificada con inferencia real (~95 ms/imagen) |
| 2026-10-09 | D16: aporte del artículo ajustado a lo medido. Esqueleto .docx y checklist actualizados |
| 2026-10-10 | D17: se descarta `--chv-externo` por coherencia con D16. Bloque 3.2 del checklist cerrado |
| 2026-10-26 | Cribado de texto completo cerrado: **74 estudios incluidos** de los 148 evaluados, con dos revisores independientes y dirimido de discrepancias (basado en resumen, limitación declarada — ver `metodologia Prisma/4-resultados/DIRIMIDO_R3.md`) |
| 2026-10-26 | **P1 y P2 respondidas por el docente** (D18, D19): las actas de congreso no cuentan para el mínimo de 25 referencias (solo revista); en WoS debe ser SCIE/SSCI, no basta ESCI. No afecta a los 74 de la revisión sistemática (son 100 % artículos de revista); sí confirma la exclusión ya aplicada a la ref. #13 (LACCEI, actas) |
| 2026-10-26 | **D20: se abandona el acceso institucional a WoS (P4)**, declarado como limitación en Métodos. El mínimo de 25 ya está superado con margen, no se justifica seguir persiguiéndolo |
| 2026-10-26 | Descargados los PDF reales de los 74 incluidos: 58 conseguidos (6 vía script + 38 manualmente por el equipo + 14 ya existentes), 16 sin acceso (14 tras paywall, 2 sin DOI). Esos 16 se **reclasificaron a excluidos (E5)** en vez de dejarlos sin verificar. **Cifra final del cribado: 58 incluidos / 90 excluidos**, todos los 58 incluidos con PDF real en `referencias/` |
| 2026-10-27 | Resolución de 23 casos "C0": evidencia real (PDF/web) reincorpora 23 estudios que habían quedado excluidos por ambigüedad de resumen. C0 revocado. **80 incluidos / 68 excluidos** — ver `CIERRE_AUDITADO.md` y `RESOLUCION_23_CASOS.md` |
| 2026-10-27 | De esos 23, el equipo intentó descargar los 5 que seguían sin PDF local (ids 80, 11, 87, 94, 100) y confirma **paywall real, sin presupuesto**; el enlace de ResearchGate citado como evidencia también resultó bloqueado al reintentarlo. Reclasificados a excluidos (E5). **Cifra final: 75 incluidos / 73 excluidos** (39 E3, 12 E4, 22 E5), con PDF real para los 75 |
| 2026-11-02 | **Cribado dado por final**: `RESUMEN_CRIBADO_PRISMA.docx` fija las cifras oficiales (158 → 75 incluidos / 73 excluidos). Corregido el recuento de PDF: 72 locales, 2 web (IDs 60 y 132) y 1 cuerpo indexado (ID 93). Figura 1, avisos y resúmenes sincronizados en el repositorio |
| 2026-11-02 | Se cierra la discrepancia de clases: el alcance del paper es **2 clases positivas** (`casco`, `chaleco`), según D10. La opción de 4 clases queda como limitación y trabajo futuro; el Esqueleto ya lo declara así |
| 2026-11-02 | Documentación alineada a 2 clases, sin reentrenar: `Paper_Borrador_hasta_Introduccion_YOLO26_EPP.docx` (resumen, vacío en la literatura, objetivo y declaración de IA) pasa de 4 a 2 clases y usa las cifras del experimento (20 944 imágenes, mAP50 0,8592). `Avance_Semana4` queda como registro histórico del plan inicial. Pendiente: referencia de Construction-PPE en el Borrador |
| 2026-11-02 | **Paper único**: `doc-borrador/Esqueleto_Paper_EPP_YOLO26.docx` es el manuscrito oficial. Se fusionó en él la introducción y las 38 referencias del Borrador de `TrabajoFinal` (ahora en `TrabajoFinal/archivo/`), se escribió la sección 2.1 (revisión PRISMA) y la declaración de IA, y se validaron las cifras contra el cribado y el experimento. **Regla: la literatura citada sale solo de los 75 incluidos en el cribado**; las únicas referencias externas son de método (PRISMA, datasets, software). 32 referencias en orden de aparición (27 de revista, 5 de método). Se quitaron las citas de contexto (siniestralidad, Perú, revisiones) y las que no están en el cribado. Pendiente: confirmar la redacción final con el equipo |
| 2026-11-02 | **PDFs renumerados**: los 75 incluidos de `referencias/` llevan prefijo consecutivo 01-75; los 15 de contexto pasan a `C##`. Nombres y números actualizados en estudios_incluidos.csv, AUDITORIA_CIERRE.csv, RESOLUCION_23_CASOS, VERIFICACION_CIERRE.json, NOTAS_CRIBADO_R2.md, INDICE_PAPER, TABLA_SEGUIMIENTO, README, SINTESIS y REFERENCIA_PARRAFOS. Mapa en `referencias/MAPA_RENUMERACION.csv` |
| 2026-11-02 | **Revisión de incongruencias** en documentación y paper: Figura 1 (SVG/PNG y Word) sin «WoS pendiente» ni «72 PDF locales»; pie de la Figura 2 declara el umbral de confianza 0,001 y la Discusión se ajusta a lo que muestra esa matriz; propiedades del Word corregidas. Sin cambios en datos ni resultados del experimento |
| 2026-11-02 | **Métrica principal = mAP50-95** (opción 1): el paper la declara en 2.5 y la destaca en resumen, resultados y discusión; el mAP50 queda como comparación con la literatura. Solo cambió el texto; las cifras salen de la misma evaluación |
