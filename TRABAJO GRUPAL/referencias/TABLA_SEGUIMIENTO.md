> **Estado vigente (cribado cerrado, 2026-10-27): 158 identificados, 75 incluidos / 73 excluidos** (39 E3, 12 E4, 22 E5). Cifras oficiales en [RESUMEN_CRIBADO_PRISMA.docx](<../metodologia Prisma/4-resultados/RESUMEN_CRIBADO_PRISMA.docx>). Los recuentos anteriores (80/68, 58/90, 74/74) son históricos.

# Tabla de seguimiento de referencias

Inventario unificado. Antes repartido entre `Arnold/`, `Javier/`, `eladio/` y la raíz;
desde el 2026-10-09 todas las referencias viven aquí.

Versión filtrable: `TABLA_SEGUIMIENTO.csv`

## Cómo leer las columnas

| Columna | Significado |
|---|---|
| **ID** | Nº consecutivo **01-75** de los incluidos = prefijo del PDF; `C##` = estudio de contexto no citado (conserva su ID antiguo, PDF en `_contexto_no_citados/`). **Renumerado el 2026-11-02**: la equivalencia con los IDs anteriores está en `MAPA_RENUMERACION.csv` y en la columna `id_anterior` del CSV. Los `R##` son números reservados antiguos de referencias que no se descargaron |
| **Aportó** | Quién la trajo al grupo. Se conserva para dar crédito y para rastrear duplicados |
| **Scopus** | ✅ si aparece entre los 158 resultados de la búsqueda del 2026-10-09 |
| **Criterios** | Si cumple I1-I7 del protocolo. `✳` = cumple pero el dominio no es obra |
| **Uso previsto** | En qué sección del artículo se espera citarla |

---

## Estudios que cumplen los criterios  (26)

Candidatos a **estudios incluidos** de la revisión. Alimentan la Introducción.

| ID | Referencia | Revista · Año | Aportó | Scopus | Criterios | Uso previsto |
|---|---|---|---|:--:|---|---|
| **01** | Fast PPE Detection for Real Construction Sites (dataset CHV) | Sensors · 2021 | Arnold | ✅ | cumple | Métodos (dataset) + Intro |
| **02** | SHEL5K: Extended Dataset and Benchmarking for Safety Helmet Detection | Sensors · 2022 | Arnold | ✅ | cumple | Intro |
| **C03** | MRC-DETR: detección de alta precisión en operaciones eléctricas | Sensors · 2025 | Arnold | ⚪ | cumple ✳ | Intro (arquitectura no-YOLO) |
| **03** | PPE-EYE: deep learning para cumplimiento de EPP | Computers · 2026 | Arnold | ✅ | cumple | Intro |
| **C05** | Fixed-Budget: mezcla de datos reales y sintéticos | Buildings · 2026 | Arnold | ⚪ | cumple | Métodos (métrica) + Discusión |
| **C06** | YOLOv11-SRA: cascos en minería subterránea | Scientific Reports · 2026 | Javier | ⚪ | cumple ✳ | Intro |
| **04** | AE-LFOG-YOLO: cascos con invariancia a iluminación | Scientific Reports · 2026 | Javier | ✅ | cumple | Intro + Discusión |
| **C08** | DRR-YOLOv11s: EPP ligero en centrales hidroeléctricas | Scientific Reports · 2026 | Javier | ⚪ | cumple ✳ | Intro (edge) |
| **05** | YOLOv10 multiescala: incumplimiento multiclase de EPP | Scientific Reports · 2026 | Javier | ✅ | cumple | Intro + Discusión |
| **06** | Detección de no-EPP con YOLOv10 y transformers | Scientific Reports · 2025 | búsqueda | ✅ | cumple | Intro |
| **07** | PPE Detection for Construction Workers: nuevo dataset | IEEE Access · 2024 | búsqueda | ✅ | cumple | Intro + Métodos |
| **08** | PPE Detection: enfoque sostenible con YOLOX | Sustainability · 2023 | búsqueda | ✅ | cumple | Intro |
| **09** | Sistema automático de detección de casco | Applied Sciences · 2022 | búsqueda | ✅ | cumple | Intro |
| **10** | Detección de casco con características multiescala | IEEE Access · 2021 | búsqueda | ✅ | cumple | Intro |
| **11** | Casco con YOLOv5 y superresolución | Sensors · 2023 | búsqueda | ✅ | cumple | Intro + Discusión |
| **C24** | Detección ligera de casco con YOLOv4 mejorado | Sensors · 2023 | búsqueda | ⚪ | cumple | Intro |
| **12** | Detección de casco con YOLOv5s mejorado | Sensors · 2023 | búsqueda | ✅ | cumple | Intro |
| **13** | Detección de casco en tiempo real con YOLOv5 | Intell. Autom. Soft Comput. · 2022 | búsqueda | ✅ | cumple | Intro |
| **14** | Faster R-CNN con adaptación de dominio para no-EPP | Scientific Reports · 2026 | búsqueda | ✅ | cumple | Intro + Discusión (clave) |
| **C29** | Algoritmo mejorado de detección de casco con YOLOv5 | Scientific Reports · 2023 | búsqueda | ⚪ | cumple | Intro |
| **15** | Detección de uso de casco con deep learning | Scientific Reports · 2024 | búsqueda | ✅ | cumple | Intro |
| **C31** | Monitoreo remoto de casco y arnés | Remote Sensing · 2023 | búsqueda | ✅ | cumple | Intro |
| **C32** | Edge computing en monitoreo de obra con visión | Buildings · 2022 | búsqueda | ⚪ | cumple ✳ | Discusión (despliegue) |
| **C33** | Faster R-CNN-LSTM para conductas inseguras | Applied Sciences · 2023 | búsqueda | ✅ | cumple | Intro (dos etapas) |
| **16** | Sistemas aéreos no tripulados y deep learning en seguridad | Sensors · 2023 | búsqueda | ✅ | cumple | Intro |
| **17** | Detección de cumplimiento de EPP en tiempo real | Sustainability · 2022 | raíz | ✅ | cumple | Intro + Métodos (línea base) |

## Fuera de los criterios — citables como contexto  (3)

Excluidas por **E1** (no son artículos primarios de revista). Se citan en la Introducción
como antecedente o contexto, pero **no entran al diagrama de flujo** como estudios incluidos.

| ID | Referencia | Revista · Año | Aportó | Scopus | Criterios | Uso previsto |
|---|---|---|---|:--:|---|---|
| **C10** | HSE Annual Report and Accounts 2022-23 | HSE (informe de gobierno) · 2023 | eladio | ⚪ | NO (E1) | Intro (contexto) |
| **C12** | Revisión sistemática de cumplimiento de EPP con visión | Artificial Intelligence Review · 2024 | eladio | ✅ | NO (E1) | Intro (antecedente) |
| **C13** | Smart SSOMA: gestión de seguridad con visión y edge | LACCEI (actas) · 2026 | eladio | ⚪ | NO (E1) — confirmado por D18 (docente: actas no cuentan para el mínimo de 25) | Intro (contexto local), sin contar en el mínimo |

## Pendientes de verificar  (1)

Requieren lectura del texto completo para confirmar el criterio señalado.

| ID | Referencia | Revista · Año | Aportó | Scopus | Criterios | Uso previsto |
|---|---|---|---|:--:|---|---|
| **C11** | Framework: trabajo productivo y actos/condiciones inseguras | IJERPH · 2023 | eladio | ⚪ | dudoso (I4) | Intro (contexto) |

---

## Referencias identificadas pero no descargadas

Relevantes, con su editor bloqueando la descarga automatizada. Los números antiguos 17, 18, 19, 22 y 26 (aquí `R17`, `R18`, `R19`, `R22`, `R26`)
estaban reservados para ellas; ya no corresponden a ningún PDF.

| ID | Referencia | Revista · Año | Citas | DOI |
|---|---|---|---:|---|
| R17 | An improved YOLOX approach for low-light and small object detection: PPE on tunnel construction sites | JCDE · 2023 | 41 | `10.1093/jcde/qwad042` |
| R18 | Deep learning-based framework for monitoring PPE on construction sites | JCDE · 2023 | 37 | `10.1093/jcde/qwad019` |
| R19 | PPE detector: a YOLO-based architecture | PeerJ Comp. Sci. · 2022 | 105 | `10.7717/peerj-cs.999` |
| R22 | A Novel Implementation of an AI-Based Smart Construction Safety Inspection Protocol in the UAE | IEEE Access · 2021 | 73 | `10.1109/access.2021.3135662` |
| R26 | Safety Helmet Wearing Detection Model Based on Improved YOLO-M | IEEE Access · 2023 | 41 | `10.1109/access.2023.3257183` |
| — | Pose guided anchoring for detecting proper use of PPE | Autom. Constr. · 2021 | 86 | `10.1016/j.autcon.2021.103828` |

---

## Resumen

| | |
|---|---:|
| Referencias en la carpeta | **30** |
| Cumplen criterios I1-I7 | 26 |
| Confirmadas en Scopus | 20 |
| Identificadas sin descargar | 6 |
| Mínimo exigido por la rúbrica | 25 |

**Se supera el mínimo con margen**, y eso sin contar las referencias metodológicas
(PRISMA, datasets, YOLO26), que también computan.

## Procedencia por integrante

| Aportó | Referencias |
|---|---:|
| búsqueda | 16 |
| Arnold | 5 |
| Javier | 4 |
| eladio | 4 |
| raíz | 1 |

> Las carpetas `Arnold/`, `Javier/` y `eladio/` conservan sus documentos propios
> (síntesis, notas); solo se unificaron los PDFs de referencias.