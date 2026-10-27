> **Estado vigente tras resolver C0 (2026-10-27): 80 incluidos / 68 excluidos; ningun C0 pendiente.** Se reincorporan los 23 por evidencia de elegibilidad, sin agregar estudios a los 148 originales. Ver [CIERRE_AUDITADO.md](CIERRE_AUDITADO.md) y [RESOLUCION_23_CASOS.md](RESOLUCION_23_CASOS.md). Los recuentos de 57 y C0 que siguen son historicos.

> **Estado vigente — auditoría 2026-10-27:** corpus cerrado de **57 incluidos / 91 no incluidos**. No se añaden estudios. Ver [CIERRE_AUDITADO.md](CIERRE_AUDITADO.md) y `AUDITORIA_CIERRE.csv`. Los recuentos siguientes son históricos; no usar 64, 74, 58 ni 132 como resultado actual. Se distinguen selección documental, cierre administrativo C0 y recuperación E5.

# Cribado de texto completo — comparación R1 vs R2

**Fecha:** 2026-10-26. R1 = asistente de IA (ver `NOTAS_CRIBADO_R1.md`). R2 = otra IA, cribado
independiente a partir del mismo prompt (`PROMPT_CRIBADO_R2.md`), con acceso al repositorio.

## Resultado de cada revisor (148 estudios)

| | R1 | R2 |
|---|---:|---:|
| incluir | 77 | 95 |
| excluir | 71 | 53 |

## Comparación

| | Registros |
|---|---:|
| **Coinciden** (decisión firme) | **120** |
| — de las cuales incluir | 72 |
| — de las cuales excluir | 48 |
| **Discrepancias** (pendientes de dirimir — R3) | **28** |

Columnas `discrepancia` y `decision_final`/`motivo_final` ya actualizadas en
`cribado_lote_1.csv`, `cribado_lote_2.csv` y `cribado_texto_completo.csv` para los 120 casos
sin discrepancia. Los 28 con discrepancia quedan con `decision_final` vacío, a la espera del
dirimido.

## Las 28 discrepancias, para dirimir

Ordenadas por citas. En la mayoría (23 de 28) R2 fue más permisivo que R1: incluyó estudios que
R1 excluyó por E4 (sin cifra concreta en el resumen) o E3. En 5 casos ocurrió lo contrario.

| id | citas | Título | R1 | R2 |
|---:|---:|---|---|---|
| 80 | 109 | PPE detector: A YOLO-based architecture... | excluir (E4) | incluir |
| 7 | 75 | Standardized use inspection of workers' PPE... | incluir | excluir (E3) |
| 11 | 64 | PPE detection using YOLOv8 architecture... (comparative study) | excluir (E4) | incluir |
| 12 | 63 | SHEL5K: An Extended Dataset and Benchmarking... | excluir (E4) | incluir |
| 86 | 52 | Safety Helmet Detection YOLOv5 Super-Resolution... | excluir (E4) | incluir |
| 87 | 47 | Improved YOLOX low-light small object detection: PPE tunnel... | excluir (E3) | incluir |
| 92 | 38 | Image Augmentation Techniques Non-PPE Detection YOLOv8... | excluir (E4) | incluir |
| 21 | 37 | Automatic detection safety helmet head region location... | excluir (E4) | incluir |
| 22 | 37 | Deep Learning Technique Object Detection Panoramic Video... | excluir (E4) | incluir |
| 23 | 35 | Safety Helmet Detection Algorithm Improved YOLOv5s... | excluir (E4) | incluir |
| 93 | 33 | SH17 dataset human safety and PPE detection manufacturing... | excluir (E4) | incluir |
| 94 | 31 | Automated PPE compliance monitoring industrial pose estimation... | excluir (E4) | incluir |
| 26 | 30 | DST-DETR Image Dehazing Safety Helmet Foggy Weather... | excluir (E4) | incluir |
| 95 | 30 | Real-Time PPE Non-Compliance AI Edge Cameras... | excluir (E4) | incluir |
| 100 | 25 | Real-Time Monitoring PPE Compliance Surveillance Cameras... | excluir (E3) | incluir |
| 104 | 22 | Automated construction safety reporting + VQA... | incluir | excluir (E3) |
| 36 | 21 | Detection Method Safety Helmet UAV YOLOv8... | excluir (E4) | incluir |
| 110 | 13 | Fast Robust Safety Helmet Network Swin Transformer... | excluir (E4) | incluir |
| 112 | 11 | SC-YOLO CSP YOLOv11n Sophia PPE Detection... | excluir (E3) | incluir |
| 115 | 8 | Deep learning algorithm detection PPE (PLOS ONE)... | excluir (E3) | incluir |
| 60 | 4 | CSOD-24 dataset... | excluir (E4) | incluir |
| 122 | 4 | Real-time construction safety drone hybrid attention... | incluir | excluir (E3) |
| 62 | 3 | AF-YOLOv8 helmet and vest detection... | incluir | excluir (E3) |
| 125 | 1 | YOLOv11n Neck-Level Precast + PPE Detection... | excluir (E3) | incluir |
| 132 | 1 | Intelligent Worksite PPE Compliance Detection... | excluir (E4) | incluir |
| 79 | 0 | Rapid image recognition hard hat compliance (VGG16)... | incluir | excluir (E3) |
| 141 | 0 | Noninvasive Worker Safety Monitoring AR Feedback... | excluir (E4) | incluir |
| 142 | 0 | Vision-Based Sensing PPE + Harness High-Formwork... | excluir (E3) | incluir |

## Caso a revisar aunque no sea discrepancia

**id 82** (93 citas, *"Towards on-site hazards identification of improper use of PPE"*) —
**ambos revisores lo excluyeron (E3)**, firme, sin discrepancia. Es uno de los estudios de alto
impacto que `CRIBADO_RESULTADO.md` había identificado para proteger de una lectura estricta de
I5 en la etapa de título/resumen (decisión D8). Al coincidir dos revisores independientes en
excluirlo aquí, la exclusión es más sólida que en el primer pase de R1 solo — pero como es un
caso que el equipo ya marcó como valioso, **vale la pena que alguien abra el PDF** antes de
cerrarlo definitivamente, sobre todo porque I5 (si detecta casco/chaleco específicamente) no
quedó claro en el resumen para ninguno de los dos revisores.

## Siguiente paso

Falta el **R3** (dirimido) sobre las 28 discrepancias — idealmente una persona del equipo que
abra el PDF de cada una, considerando que R1 y R3 trabajaron principalmente con resúmenes y R2 aportó evidencia adicional. El rango final de
"estudios incluidos" queda entre **72** (si R3 resuelve todas las discrepancias hacia excluir) y
**100** (si las resuelve todas hacia incluir).
