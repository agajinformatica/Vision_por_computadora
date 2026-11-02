> **Estado vigente (cribado cerrado, 2026-10-27): 158 identificados, 75 incluidos / 73 excluidos** (39 E3, 12 E4, 22 E5). Cifras oficiales en [RESUMEN_CRIBADO_PRISMA.docx](<../metodologia Prisma/4-resultados/RESUMEN_CRIBADO_PRISMA.docx>). Los recuentos anteriores (80/68, 58/90, 74/74) son históricos.

# Referencias — descargas y procedencia

> **Renumeración (2026-11-02):** los 75 PDFs incluidos llevan prefijo consecutivo `01`-`75` (orden del inventario original). Los 15 de contexto, en `_contexto_no_citados/`, pasaron a `C##` conservando su número antiguo. La columna `#` de las tablas de abajo ya usa los números nuevos. Equivalencias: `MAPA_RENUMERACION.csv`.

> **Carpeta única de PDFs (2026-11-02):** los 75 incluidos están aquí, sin copias en otras carpetas (se borró `4-resultados/evidencia_23/`, que eran duplicados exactos). La columna `pdf_local` de `estudios_incluidos.csv` apunta a estos archivos. `INDICE_PAPER.md` relaciona cada referencia del paper con su PDF. En `referencias/` quedan solo los 75 PDFs incluidos; los 15 restantes (estudios de contexto, descartes de etapas anteriores y el preprint arXiv de SH17, `80b_...`) están en `_contexto_no_citados/` y el paper no los cita. `TABLA_SEGUIMIENTO.csv` indica la subcarpeta.

> Documento de registro. Cada entrada lleva su **DOI** y la **URL exacta** desde la que se
> descargó el PDF, para que la obtención sea reproducible y verificable.

Descargado el **2026-10-09**. Todos cumplen los criterios I1-I7 del
[protocolo de revisión](../metodologia%20Prisma/2-protocolo/PROTOCOLO_REVISION.md):
artículo primario, revista indexada, 2021-2026, detección de objetos, casco y/o chaleco,
dominio de construcción o industrial, con métricas cuantitativas.

Numeración original del inventario del grupo (1-12 ya estaban repartidos entre
las carpetas `Arnold`, `Javier`, `eladio` y la raíz).

---

## Detección de EPP (casco + chaleco)

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| 06 ✅ | Automated non-PPE detection on construction sites using YOLOv10 and transformers | Scientific Reports · 2025 | 45 | `10.1038/s41598-025-12468-8` | nature.com/articles/s41598-025-12468-8.pdf |
| 07 ✅ | Personal Protective Equipment Detection for Construction Workers: A Novel Dataset | IEEE Access · 2024 | 33 | `10.1109/access.2024.3382817` | vía OpenAlex (localización OA) |
| 08 ✅ | Personal Protective Equipment Detection: A Deep-Learning-Based Sustainable Approach | Sustainability · 2023 | 85 | `10.3390/su151813990` | mdpi.com/2071-1050/15/18/13990/pdf |
| 14 ✅ | Domain-adaptive faster R-CNN for non-PPE identification on construction sites | Scientific Reports · 2026 | 27 | `10.1038/s41598-026-35148-7` | nature.com/articles/s41598-026-35148-7.pdf |

## Detección de casco

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| 09 ✅ | Deep Learning-Based Automatic Safety Helmet Detection System for Construction Safety | Applied Sciences · 2022 | 134 | `10.3390/app12168268` | mdpi.com/2076-3417/12/16/8268/pdf |
| 10 ✅ | Deep Learning-Based Workers Safety Helmet Wearing Detection on Construction Sites Using Multi-Scale Features | IEEE Access · 2021 | 91 | `10.1109/access.2021.3138407` | vía OpenAlex (localización OA) |
| 11 ✅ | Safety Helmet Detection Based on YOLOv5 Driven by Super-Resolution Reconstruction | Sensors · 2023 | 50 | `10.3390/s23041822` | mdpi.com/1424-8220/23/4/1822/pdf |
| C24 ⚪ | Lightweight Helmet Detection Algorithm Using an Improved YOLOv4 | Sensors · 2023 | 50 | `10.3390/s23031256` | mdpi.com/1424-8220/23/3/1256/pdf |
| 12 ✅ | Research on Safety Helmet Detection Algorithm Based on Improved YOLOv5s | Sensors · 2023 | 33 | `10.3390/s23135824` | mdpi.com/1424-8220/23/13/5824/pdf |
| 13 ✅ | Real-Time Safety Helmet Detection Using YOLOv5 at Construction Sites | Intell. Autom. Soft Comput. · 2022 | 51 | `10.32604/iasc.2023.031359` | vía OpenAlex (localización OA) |
| C29 ⚪ | Research on improved algorithm for helmet detection based on YOLOv5 | Scientific Reports · 2023 | 29 | `10.1038/s41598-023-45383-x` | nature.com/articles/s41598-023-45383-x.pdf |
| 15 ✅ | Research on helmet wearing detection method based on deep learning | Scientific Reports · 2024 | 23 | `10.1038/s41598-024-57433-z` | nature.com/articles/s41598-024-57433-z.pdf |
| C31 ✅ | A Remote-Vision-Based Safety Helmet and Harness Monitoring System | Remote Sensing · 2023 | 24 | `10.3390/rs15020347` | mdpi.com/2072-4292/15/2/347/pdf |

## Contexto técnico: despliegue, arquitecturas alternativas y plataformas

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| C32 ⚪ | Investigation of Edge Computing in Computer Vision-Based Construction Monitoring | Buildings · 2022 | 24 | `10.3390/buildings12122167` | mdpi.com/2075-5309/12/12/2167/pdf |
| C33 ✅ | Faster R-CNN-LSTM Construction Site Unsafe Behavior Recognition Model | Applied Sciences · 2023 | 29 | `10.3390/app131910700` | mdpi.com/2076-3417/13/19/10700/pdf |
| 16 ✅ | Unmanned Aerial Systems and Deep Learning for Safety and Health Activity Monitoring | Sensors · 2023 | 48 | `10.3390/s23156690` | mdpi.com/1424-8220/23/15/6690/pdf |

---

## Cobertura temática

Se buscó diversidad deliberada para que la revisión no sea quince variantes de YOLOv5:

| Enfoque | Referencias |
|---|---|
| YOLO (v4, v5, v10, YOLOX) | 06, 08, 09, 11, C24, 12, 13, C29, 15 |
| **Faster R-CNN / dos etapas** | 14, C33 |
| **Transformers** | 06 |
| **Adaptación de dominio** | 14 |
| **Edge computing** | C32 |
| **Plataformas aéreas (UAV)** | 16 |
| **Dataset propio** | 07, 08 |

La #14 merece atención especial: adaptación de dominio para identificación de **no-EPP**.
Es la más cercana al análisis de generalización cruzada entre datasets que planteamos.

## Pendientes — bloqueados por el editor

Identificados y relevantes, pero su editor no permite descarga automatizada
(renderiza el PDF en el visor sin enviarlo como adjunto):

| Referencia | Revista · Año | Citas | DOI |
|---|---|---:|---|
| Pose guided anchoring for detecting proper use of PPE | Automation in Construction · 2021 | 86 | `10.1016/j.autcon.2021.103828` |
| PPE detector: a YOLO-based architecture | PeerJ Computer Science · 2022 | 105 | `10.7717/peerj-cs.999` |
| An improved YOLOX approach for low-light and small object detection: PPE on tunnel construction sites | JCDE · 2023 | 41 | `10.1093/jcde/qwad042` |
| Deep learning-based framework for monitoring PPE on construction sites | JCDE · 2023 | 37 | `10.1093/jcde/qwad019` |
| A Novel Implementation of an AI-Based Smart Construction Safety Inspection Protocol in the UAE | IEEE Access · 2021 | 73 | `10.1109/access.2021.3135662` |
| Safety Helmet Wearing Detection Model Based on Improved YOLO-M | IEEE Access · 2023 | 41 | `10.1109/access.2023.3257183` |

Se descargan abriendo el DOI en el navegador y usando el botón de descarga del visor.
Las dos de *Automation in Construction* y *PeerJ* son las de mayor impacto de la lista
y conviene recuperarlas.

## Procedencia y verificación

### Identificación preliminar (OpenAlex)

Las 16 referencias se localizaron mediante la API de **OpenAlex**, con los términos del protocolo:

```
title_and_abstract.search:("safety helmet" OR hardhat OR "hard hat" OR "safety vest"
  OR "protective equipment") AND (detection OR detector)
  AND (construction OR worksite OR "construction site")
filter: from_publication_date:2021-01-01, type:article, is_oa:true
sort:   cited_by_count:desc
```

Resultados: 267. Se cribaron los 100 más citados, excluyendo revisiones y trabajos sin
componente de visión por computadora.

### Verificación contra la búsqueda definitiva en Scopus (2026-10-09)

La búsqueda sistemática se ejecutó después en **Scopus** con la cadena del protocolo
(ver [CADENAS_BUSQUEDA.md](../metodologia%20Prisma/2-protocolo/CADENAS_BUSQUEDA.md)), con **158 resultados**
exportados a `metodologia Prisma/3-busqueda/scopus_2026-10-09.csv`.

Al cruzar ambas listas por DOI:

| | Referencias de esta carpeta |
|---|---:|
| ✅ Presentes en los 158 de Scopus | **13 de 16** |
| ⚪ No presentes | 3 de 16 |

Las marcadas con ✅ en las tablas de arriba quedan como **identificadas por base de datos**
en el diagrama de flujo PRISMA. Las marcadas con ⚪ entran por la columna de
**"otros métodos"**, que la norma contempla expresamente.

Las tres no presentes y el motivo probable:

| # | Referencia | Motivo |
|---|---|---|
| C24 | Lightweight Helmet Detection YOLOv4 | Términos o indexación no capturados por la cadena |
| C29 | Research on improved algorithm for helmet detection YOLOv5 | Ídem |
| C32 | Investigation of Edge Computing in CV-Based Construction Monitoring | Trata monitoreo general, no detección de EPP |

**Ninguna se descarta por esto.** Figurar en una columna u otra del diagrama no afecta
su validez como referencia ni su cumplimiento de los criterios I1-I7.

### Estado de Web of Science — cerrado (D20)

**Abandonado por decisión del equipo**, no solo pendiente: la cuenta personal de Clarivate da
acceso al Researcher Profile pero no a la Core Collection, y la conexión no procede de la red
institucional. Se decidió no seguir el acceso por biblioteca/VPN porque el mínimo de 25
referencias ya está superado con margen (75 al cierre del cribado, solo de la revisión sistemática en Scopus). **Se
declara como limitación en Métodos**: la búsqueda se realizó en Scopus, sin acceso
institucional a WoS Core Collection.
