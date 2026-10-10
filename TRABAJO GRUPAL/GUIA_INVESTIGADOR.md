# Guía del investigador — estado del proyecto

Documento de orientación y seguimiento. Resume **qué se está construyendo, dónde está cada
cosa, qué se decidió y por qué, y qué falta**. Pensado para leerse de principio a fin una vez
y consultarse por secciones después.

**Última actualización:** 2026-10-09

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
│   └── 04_DEPENDENCIAS.md        ← qué bloquea qué y ruta crítica
│
├── doc-borrador/                 ← el artículo en construcción
│   └── Esqueleto_Paper_EPP_YOLO26.docx
│
├── referencias/                  ← TODA la bibliografía (30 PDFs)
│   ├── TABLA_SEGUIMIENTO.md      ← inventario con ID, procedencia y uso previsto
│   ├── TABLA_SEGUIMIENTO.csv     ← la misma tabla, filtrable
│   └── README.md                 ← DOI y URL de descarga de las halladas en búsqueda
│
├── Arnold/   Javier/   eladio/   ← solo documentos propios (síntesis, notas)
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
│   └── dataset_unificado/        ← 20 944 img · enlaces, no copias
│       ├── data.yaml             ← configuración para YOLO26
│       ├── manifiesto.csv        ← trazabilidad imagen → origen
│       └── estadisticas.json     ← conteos por fuente y partición
│
└── dataset/                      ← datos crudos del experimento (6,1 GB)
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

### A. Bibliografía y revisión sistemática 🟡 en curso

| Hito | Estado |
|---|---|
| Pregunta de revisión | ✅ definida |
| Criterios I1-I7 y E1-E6 | ✅ definidos |
| Cadenas de búsqueda | ✅ escritas para Scopus y WoS |
| Búsqueda en Scopus | ✅ ejecutada — **158 registros**, exportados con resumen |
| Búsqueda en WoS | ⬜ **bloqueada** — sin acceso institucional |
| Cribado título/resumen | ✅ primer tamizaje — 10 excluidos, 148 pasan |
| Cribado texto completo | ⬜ pendiente, lo hace el equipo |
| Esqueleto del artículo | ✅ generado en `doc-borrador/` |
| Diagrama de flujo | ⬜ a medio llenar |

**Inventario de referencias:** **30 PDFs unificados** en `referencias/`, con identificador
estable. 26 cumplen los criterios I1-I7; 20 están confirmadas en la búsqueda de Scopus.
Otras 6 están identificadas pero sin descargar (editor bloquea). Sumando las metodológicas
(PRISMA, datasets, YOLO26) se superan las 25 exigidas con margen.

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
| Roboflow Combined v8 | 44 002 | 6,54 : 1 | entrenamiento (escala + clases negativas) |
| **Construction-PPE** | 1 416 | **1,37 : 1** | refuerzo de chaleco — el mejor balanceado |
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

### D. Redacción 🔴 sin empezar

Esqueleto IMRyD discutido y mapeado, pero no hay texto. **La redacción es 100% humana por
decisión del equipo** (ver sección 6).

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
| D9 | Referencias unificadas en `referencias/` con ID estable | Evita duplicados entre carpetas y permite citarlas por número. La procedencia se conserva en la tabla de seguimiento |
| D10 | Esquema de **2 clases positivas** (`casco`, `chaleco`) | Es lo que promete el título. Los tres datasets fusionan sin ruido de etiqueta, y el desbalance mejora de 6,6:1 a 4,8:1. El experimento de cumplimiento con clases negativas queda como extensión |
| D11 | Se conservan las particiones originales de cada fuente | No re-particionar evita mezclar imágenes que los autores separaron deliberadamente |
| D12 | Entrenar en Kaggle, desplegar en el VPS | Ninguna máquina disponible tiene GPU. El VPS (12 núcleos, 46 GB, sin GPU) no entrena, pero sirve la demo de la defensa |
| D13 | Despliegue versionado en el repositorio, no editado en el servidor | Hace reproducible el despliegue, que es parte del criterio de reproducibilidad (3 pts) |
| D14 | **Tres modelos**: YOLOv8n (línea base simple), YOLO11n (comparador directo), YOLO26n (propuesto) | La guía pide "el método simple" como línea base; comparar solo contra YOLO11 no satisface esa lectura. Con tres se cubren ambas interpretaciones |
| D15 | Protocolo idéntico aplicado como diccionario único | Impide que se cuele un hiperparámetro distinto entre modelos. Es lo que hace legítima la comparación |
| **D17** | No se usa `--chv-externo`: CHV permanece repartido en las tres particiones | Coherencia con D16. Usarlo exigiría reentrenar los tres modelos, y el aporte ya no lo promete. Queda como trabajo futuro, con el script preparado |
| **D16** | **El aporte declarado se ajusta a lo medido**, no al revés | El esqueleto prometía modo NMS-free y generalización entre datasets; el experimento no midió ninguna. En vez de correr experimentos extra con el parcial a 4 semanas, se declara lo demostrado: *YOLO26 supera a dos generaciones previas con un 19 % menos de parámetros, bajo protocolo idéntico*. Lo descartado pasa a trabajo futuro |

---

## 5. Decisiones pendientes y bloqueos

| # | Pendiente | Bloqueado por | Urgencia |
|---|---|---|---|
| P1 | ¿Cuentan las actas de congreso como "alto impacto"? | **Consulta al docente** | alta |
| P2 | ¿Se admiten revistas solo en ESCI, o deben estar en SCIE? | **Consulta al docente** | alta |
| ~~P3~~ | ~~Fechas exactas~~ | **resuelto: 7 nov y 12 dic** | — |
| P4 | Acceso institucional a Web of Science | Biblioteca UNMSM / VPN | alta |
| ~~P5~~ | ~~Regla de homologación de clases~~ | **resuelto (D10)** | — |
| ~~P6~~ | ~~Línea base del experimento~~ | **resuelto (D14)** | — |
| P6 | Línea base del experimento | Decisión del equipo | alta |
| P7 | Asignación de revisores para el cribado | Decisión del equipo | media |

### Consulta al docente, lista para enviar

> 1. Para la revisión sistemática, ¿las actas de congreso (CVPR, ICCV, ECCV, congresos IEEE)
>    cuentan como "revistas de alto impacto indexadas en Scopus/WoS" para el mínimo de 25
>    referencias, o la exigencia se limita estrictamente a publicaciones en revista?
> 2. En Web of Science, ¿se admiten revistas indexadas solo en ESCI, o deben estar en SCIE/SSCI?


### Sobre Web of Science

La cuenta personal de Clarivate da acceso al Researcher Profile pero **no a la Core
Collection**. La conexión no procede de la red universitaria. Vías por explorar, en orden:
portal de la biblioteca UNMSM, VPN institucional, o confirmar si la universidad tiene
suscripción activa.

> **Si la UNMSM no tuviera WoS, se declara como limitación en Métodos.** Buscar solo en
> Scopus es válido si se justifica. Lo que no vale es decir que se buscó donde no se buscó.

---

## 6. Cómo trabajamos

### La redacción es 100% humana

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

Son tres personas, lo que encaja con lo que PRISMA pide para el cribado: dos revisores
independientes y un tercero que resuelva las discrepancias. Conviene declararlo porque suma
rigor sin coste adicional.

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
| Sin acceso a WoS | Búsqueda incompleta | Portal de biblioteca o VPN; si no, declarar como limitación |
| 148 textos completos por evaluar | Carga alta para tres personas | El CSV viene ordenado por prioridad; lo irrelevante se resuelve en dos minutos |
| Entrenar 30 765 imágenes | Excede el límite de sesión de Colab gratuito | Submuestrear para el parcial o conseguir GPU |
| Paradigmas de anotación incompatibles | Impide fusionar datasets sin más | Entrenar en uno y evaluar en otro, o definir y documentar una regla de homologación |
| Desbalance casco/chaleco | Resultados peores en chaleco | Construction-PPE y CHV lo compensan; reportarlo como limitación |

---

## 9. Lo siguiente

En orden de urgencia:

1. **Enviar la consulta al docente** (sección 5) — desbloquea tres decisiones de golpe
2. **Arrancar el prototipo** — es el camino crítico y no depende de nada pendiente
3. **Resolver el acceso a WoS** por la biblioteca
4. **Repartir el cribado de texto completo** entre los revisores

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
