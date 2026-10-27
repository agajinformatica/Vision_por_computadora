> **Estado vigente (2026-10-27, tarde): 75 incluidos / 73 excluidos.** De los 23 casos
> reincorporados por evidencia web (abajo), 5 (ids 80, 11, 87, 94, 100) no tenían PDF local ni
> acceso alternativo verificable: el equipo intentó descargarlos y confirma paywall real, sin
> presupuesto para pagar acceso; el enlace alternativo de ResearchGate citado como evidencia
> también resultó bloqueado al reintentarlo. Se reclasifican a **excluir (E5, texto completo
> inaccesible)**, sin borrar su evidencia documentada (queda en `AUDITORIA_CIERRE.csv` y
> `RESOLUCION_23_CASOS.csv` con la nota de reclasificación). Las cifras de este documento
> (80/68) son el estado inmediatamente anterior a esta reclasificación.

# Estado auditado tras resolver los 23 casos

Fecha: 2026-10-27. **Los 23 casos C0 quedan resueltos como incluir. Corpus: 80 incluidos y 68 excluidos de los mismos 148 registros.** No se identifica ni agrega ningun estudio nuevo. Se revoca el limite de 57 por cierre administrativo: la instruccion de no buscar mas papers no permite excluir elegibles de la lista original.

Se mantienen intactas las columnas R1/R2 y sus motivos, las discrepancias historicas y los metadatos. Esta es una adjudicacion documental asistida por IA; no constituye otro revisor humano independiente. El protocolo original I1-I7 y E1-E6 sigue vigente. No se exige que el articulo use YOLO26, no hay umbral minimo de mAP, y los estudios de dataset con benchmark original son primarios. Se aceptan metricas agregadas o mejoras relativas y clases de presencia/ausencia, tal como en los 57 previos. Tener una interfaz de alertas, pose o AR no vuelve incidental el EPP cuando el detector es un objetivo principal con evaluacion propia.

## Evidencia consultada

En estos 23 se consultaron 15 PDF locales/recuperados, 2 PDF completos por web (60 y 132), 5 copias del articulo/manuscrito de autor por web (11, 80, 87, 94 y 100) y, para 93, resumen y cuerpo de la version publicada recuperados por indexacion editorial. No se presenta el preprint SH17 como version publicada ni se afirma lectura integra del PDF publicado del ID 93. Se comprobo titulo/DOI, tarea, cajas, clases y cifra. La copia de autor de 100 conserva una cabecera provisional; publicacion y cifras se corroboraron en IEEE Access. I1 se apoya en la presencia individual en la exportacion Scopus, no en una nueva auditoria de indexacion de revistas.

Resultado por los 23: **23 incluir; 0 excluir; 0 C0 pendiente**. Una exclusion E3/E4 basada en un resumen incompleto no se mantiene frente a evidencia confirmatoria del cuerpo. El registro detallado esta en RESOLUCION_23_CASOS.csv y las decisiones anteriores se conservan en el historial.

## Recuentos y limites de reporte

| Etapa real | Registros |
|---|---:|
| Scopus identificados, sin DOI repetidos detectados | 158 |
| Excluidos en filtro inicial titulo/resumen | 10 |
| Registros preseleccionados | 148 |
| Exclusiones documentales previas conservadas en este encargo | 51 (39 E3 + 12 E4) |
| Seleccionados para recuperacion o consulta adicional | 97 |
| No evaluables en recuperacion | 17 E5 (16 no recuperados + 1 PDF truncado) |
| Con evidencia de elegibilidad evaluada | 80 |
| De ellos, secciones de texto completo PDF/HTML consultadas | 79 |
| De ellos, resumen y cuerpo publicado indexado (ID 93) | 1 |
| Excluidos adicionales tras resolver estos 23 | 0 |
| **Incluidos** | **80** |

**158 = 10 + 51 + 17 + 80; 148 = 51 + 17 + 80; 68 = 39 E3 + 12 E4 + 17 E5.** E1/E2/E6: cero. E5 se cuenta una sola vez en recuperacion, no otra vez entre textos leidos. Los 9 registros historicos de otros metodos siguen como contexto y no se suman. El ID 126 conserva E5 por PDF truncado.

Resolver C0 corrige la seleccion administrativa, pero no acredita por si solo cumplimiento integral de PRISMA 2020. Las otras 51 exclusiones documentales y 17 E5 no se reabrieron en esta tarea. No se afirma que se hayan leido 148 ni 132 textos completos ni se sustituye la validacion de revisores humanos independientes. Los dos registros sin DOI siguen sin intento exhaustivo por titulo, segun la auditoria previa. La figura es un flujo adaptado al procedimiento realmente documentado, con el ID 93 identificado como evidencia indexada. Estos limites deben mantenerse al redactar Metodos.

## Calidad y extraccion posterior

El ID 22 informa la cifra citada durante entrenamiento; no tratarla como test independiente. En 87 hay mAP 86.94% en resumen/discusion frente a 86.49% en tablas. En 125 algunas medias globales no cuadran con AP por clase. En 132 hay inconsistencias en las particiones y terminologia de mAP. En 26 los incrementos anotados en la tabla de ablacion tienen problemas de escala; se conservan los valores absolutos. Estas limitaciones se registran para evaluacion de calidad, sin inventar criterios retrospectivos de exclusion. Se mantienen tambien las observaciones previas sobre 52, 71, 81 y 122.

## Trazabilidad

Se sincronizan los tres CSV, AUDITORIA_CIERRE.csv, estudios_incluidos.csv, la figura SVG/PNG y el pie/figura del Word. Solo decision_final y motivo_final cambian en las tablas de cribado. La redaccion del cuerpo del paper sigue reservada al equipo. El estado administrativo previo se conserva en historico/CIERRE_AUDITADO_57_PREVIO_A_RESOLUCION23.md.
