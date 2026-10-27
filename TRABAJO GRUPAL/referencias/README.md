> **Estado vigente 2026-10-27:** corpus cerrado de **57 estudios**. Auditoría y figura completadas, sin nuevas inclusiones; ID 126 excluido por PDF truncado. Se separan 74 no retenidos en selección documental y 17 no evaluables en recuperación. Los 9 de otros métodos no se suman. Ver [cierre auditado](<../metodologia Prisma/4-resultados/CIERRE_AUDITADO.md>). Los recuentos anteriores que difieran son históricos.

# Referencias — descargas y procedencia

> Documento de registro. Cada entrada lleva su **DOI** y la **URL exacta** desde la que se
> descargó el PDF, para que la obtención sea reproducible y verificable.

Descargado el **2026-10-09**. Todos cumplen los criterios I1-I7 del
[protocolo de revisión](../metodologia%20Prisma/2-protocolo/PROTOCOLO_REVISION.md):
artículo primario, revista indexada, 2021-2026, detección de objetos, casco y/o chaleco,
dominio de construcción o industrial, con métricas cuantitativas.

La numeración continúa la del inventario del grupo (1-12 ya estaban repartidos entre
las carpetas `Arnold`, `Javier`, `eladio` y la raíz).

---

## Detección de EPP (casco + chaleco)

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| 14 ✅ | Automated non-PPE detection on construction sites using YOLOv10 and transformers | Scientific Reports · 2025 | 45 | `10.1038/s41598-025-12468-8` | nature.com/articles/s41598-025-12468-8.pdf |
| 15 ✅ | Personal Protective Equipment Detection for Construction Workers: A Novel Dataset | IEEE Access · 2024 | 33 | `10.1109/access.2024.3382817` | vía OpenAlex (localización OA) |
| 16 ✅ | Personal Protective Equipment Detection: A Deep-Learning-Based Sustainable Approach | Sustainability · 2023 | 85 | `10.3390/su151813990` | mdpi.com/2071-1050/15/18/13990/pdf |
| 28 ✅ | Domain-adaptive faster R-CNN for non-PPE identification on construction sites | Scientific Reports · 2026 | 27 | `10.1038/s41598-026-35148-7` | nature.com/articles/s41598-026-35148-7.pdf |

## Detección de casco

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| 20 ✅ | Deep Learning-Based Automatic Safety Helmet Detection System for Construction Safety | Applied Sciences · 2022 | 134 | `10.3390/app12168268` | mdpi.com/2076-3417/12/16/8268/pdf |
| 21 ✅ | Deep Learning-Based Workers Safety Helmet Wearing Detection on Construction Sites Using Multi-Scale Features | IEEE Access · 2021 | 91 | `10.1109/access.2021.3138407` | vía OpenAlex (localización OA) |
| 23 ✅ | Safety Helmet Detection Based on YOLOv5 Driven by Super-Resolution Reconstruction | Sensors · 2023 | 50 | `10.3390/s23041822` | mdpi.com/1424-8220/23/4/1822/pdf |
| 24 ⚪ | Lightweight Helmet Detection Algorithm Using an Improved YOLOv4 | Sensors · 2023 | 50 | `10.3390/s23031256` | mdpi.com/1424-8220/23/3/1256/pdf |
| 25 ✅ | Research on Safety Helmet Detection Algorithm Based on Improved YOLOv5s | Sensors · 2023 | 33 | `10.3390/s23135824` | mdpi.com/1424-8220/23/13/5824/pdf |
| 27 ✅ | Real-Time Safety Helmet Detection Using YOLOv5 at Construction Sites | Intell. Autom. Soft Comput. · 2022 | 51 | `10.32604/iasc.2023.031359` | vía OpenAlex (localización OA) |
| 29 ⚪ | Research on improved algorithm for helmet detection based on YOLOv5 | Scientific Reports · 2023 | 29 | `10.1038/s41598-023-45383-x` | nature.com/articles/s41598-023-45383-x.pdf |
| 30 ✅ | Research on helmet wearing detection method based on deep learning | Scientific Reports · 2024 | 23 | `10.1038/s41598-024-57433-z` | nature.com/articles/s41598-024-57433-z.pdf |
| 31 ✅ | A Remote-Vision-Based Safety Helmet and Harness Monitoring System | Remote Sensing · 2023 | 24 | `10.3390/rs15020347` | mdpi.com/2072-4292/15/2/347/pdf |

## Contexto técnico: despliegue, arquitecturas alternativas y plataformas

| # | Referencia | Revista · Año | Citas | DOI | URL de descarga |
|---|---|---|---:|---|---|
| 32 ⚪ | Investigation of Edge Computing in Computer Vision-Based Construction Monitoring | Buildings · 2022 | 24 | `10.3390/buildings12122167` | mdpi.com/2075-5309/12/12/2167/pdf |
| 33 ✅ | Faster R-CNN-LSTM Construction Site Unsafe Behavior Recognition Model | Applied Sciences · 2023 | 29 | `10.3390/app131910700` | mdpi.com/2076-3417/13/19/10700/pdf |
| 34 ✅ | Unmanned Aerial Systems and Deep Learning for Safety and Health Activity Monitoring | Sensors · 2023 | 48 | `10.3390/s23156690` | mdpi.com/1424-8220/23/15/6690/pdf |

---

## Cobertura temática

Se buscó diversidad deliberada para que la revisión no sea quince variantes de YOLOv5:

| Enfoque | Referencias |
|---|---|
| YOLO (v4, v5, v10, YOLOX) | 14, 16, 20, 23, 24, 25, 27, 29, 30 |
| **Faster R-CNN / dos etapas** | 28, 33 |
| **Transformers** | 14 |
| **Adaptación de dominio** | 28 |
| **Edge computing** | 32 |
| **Plataformas aéreas (UAV)** | 34 |
| **Dataset propio** | 15, 16 |

La #28 merece atención especial: adaptación de dominio para identificación de **no-EPP**.
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
| 24 | Lightweight Helmet Detection YOLOv4 | Términos o indexación no capturados por la cadena |
| 29 | Research on improved algorithm for helmet detection YOLOv5 | Ídem |
| 32 | Investigation of Edge Computing in CV-Based Construction Monitoring | Trata monitoreo general, no detección de EPP |

**Ninguna se descarta por esto.** Figurar en una columna u otra del diagrama no afecta
su validez como referencia ni su cumplimiento de los criterios I1-I7.

### Estado de Web of Science — cerrado (D20)

**Abandonado por decisión del equipo**, no solo pendiente: la cuenta personal de Clarivate da
acceso al Researcher Profile pero no a la Core Collection, y la conexión no procede de la red
institucional. Se decidió no seguir el acceso por biblioteca/VPN porque el mínimo de 25
referencias ya está superado con margen (74 solo de la revisión sistemática en Scopus). **Se
declara como limitación en Métodos**: la búsqueda se realizó en Scopus, sin acceso
institucional a WoS Core Collection.
