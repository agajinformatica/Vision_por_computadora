# Protocolo de revisión sistemática — acta de decisiones

> **Documento de trabajo, no texto del paper.** Son tablas y códigos para decidir y
> registrar. La redacción de Métodos a partir de esto la escribe el equipo.

Proyecto: *Detección de casco y chaleco de seguridad en obras de construcción mediante YOLO26*
Última actualización: 2026-10-09

---

## 1. Pregunta de revisión  ✅ DECIDIDA

> ¿Qué arquitecturas de detección de objetos basadas en aprendizaje profundo se han
> aplicado a la detección de **casco y/o chaleco de seguridad** en entornos de
> **construcción**, sobre qué **conjuntos de datos**, y qué **desempeño** reportan?

Tres componentes acotados (tarea · EPP · dominio); la arquitectura queda libre.
Rendimiento estimado: 30-60 estudios incluibles.

## 2. Criterios de inclusión  ✅ DECIDIDOS

| Código | Criterio |
|---|---|
| I1 | Artículo primario de investigación en revista indexada en **Scopus y/o WoS** |
| I2 | Publicado entre **2021 y 2026** |
| I3 | Idioma inglés o español |
| I4 | Tarea de **detección de objetos** (con cajas delimitadoras) |
| I5 | El EPP detectado incluye **casco y/o chaleco** |
| I6 | Dominio de construcción u obra, o industrial con EPP equivalente |
| I7 | Reporta métricas cuantitativas (mAP, precisión, recall o equivalente) |

**Justificación de I2:** ventana de cinco años correspondiente a la era posterior a YOLOv5,
coherente con la selección preliminar ya realizada por el equipo.

## 3. Criterios de exclusión  ✅ DECIDIDOS

| Código | Criterio |
|---|---|
| E1 | Revisiones, editoriales, cartas, capítulos de libro, preprints sin revisión por pares |
| E2 | Solo sensores no visuales (RFID, IoT) sin componente de visión |
| E3 | EPP exclusivamente fuera de alcance (solo mascarilla, guantes o gafas) |
| E4 | Sin métricas cuantitativas de desempeño |
| E5 | Texto completo inaccesible |
| E6 | Duplicado entre bases de datos |

## 4. Decisiones pendientes  ⬜

| # | Decisión | Bloqueada por |
|---|---|---|
| P1 | ¿Se admiten actas de congreso como "revista de alto impacto"? | **Consulta al docente** |
| P2 | Bases de datos a consultar (Scopus, WoS, IEEE Xplore) | Depende de P1 |
| P3 | Cadena de búsqueda por base | Depende de P2 |
| P4 | Fecha de ejecución de la búsqueda | Depende de P3 |
| P5 | Asignación de revisores para el cribado | — |

**P1 es crítica:** si los congresos quedan excluidos, E1 debe decirlo explícitamente
e IEEE Xplore pierde buena parte de su valor, que es donde se publica lo mejor de
visión por computadora.

## 5. Cribado — asignación propuesta

PRISMA 2020 requiere cribado independiente por al menos dos revisores, con un tercero
que resuelva discrepancias. El equipo son tres personas, lo que encaja exactamente:

| Fase | Revisores independientes | Resolución de discrepancias |
|---|---|---|
| Título y resumen | 2 | el tercero |
| Texto completo | 2 | el tercero |

Se registra el acuerdo entre revisores y el número de discrepancias resueltas.

## 6. Estado de las referencias ya reunidas

Las 12 reunidas hasta ahora **no proceden de una búsqueda sistemática**: se identificaron
de forma dirigida. Entran por la columna de **"otros métodos"** del diagrama de flujo
PRISMA 2020, que es la razón por la que corresponde usar la plantilla
`PRISMA_2020_flow_diagram_new_SRs_v2.docx` y no la v1.

| Origen | Cantidad | Situación bajo los criterios |
|---|---:|---|
| Arnold (Sensors ×3, Computers, Buildings) | 5 | Pasan I1-I7 |
| Javier (Scientific Reports ×4) | 4 | Pasan I1-I7 |
| eladio — IJERPH | 1 | Pasa I1-I7 |
| eladio — *AI Review* 2024 (revisión sistemática) | 1 | **Excluido por E1**; citable como antecedente en Introducción |
| eladio — informe HSE | 1 | **Excluido por E1**; citable como contexto |
| eladio — LACCEI (actas) | 1 | **Excluido por E1**; pendiente de P1 |
| Raíz — Sustainability 2022 | 1 | Pasa I1-I7 |

## 7. Citas que NO entran al diagrama de flujo

Son referencias metodológicas, van en Métodos y no se someten a los criterios ni a la
ventana temporal:

| Referencia | Uso |
|---|---|
| Wang et al., *Sensors* 2021 (CHV) | fuente del dataset |
| Nath, Behzadan & Paal, *Autom. Constr.* 2020 (Pictor-v3) | dataset evaluado y descartado |
| Dalvi et al., 2025 (Construction-PPE) | fuente del dataset |
| Roboflow Universe, 2025 | fuente del dataset |
| Page et al., *BMJ* 2021 (n71 y n160) | método de la revisión |
| Rethlefsen et al., *Syst Rev* 2021 (PRISMA-S) | reporte de la búsqueda |
| Documentación y artículos de YOLO26 | arquitectura |

Todas cuentan para el mínimo de 25 de la rúbrica.
