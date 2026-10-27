> **Corrección de estado (2026-10-27): cribado pendiente de cierre válido.** C0 no pertenece al protocolo E1–E6. Se introdujo por una interpretación incorrecta de la instrucción de no agregar papers: esa instrucción no autoriza excluir estudios elegibles de los 148 originales. Los 23 casos C0 requieren resolución con los criterios originales. Los 57 incluidos y el flujo siguiente describen el estado provisional guardado, no un cierre metodológicamente validado. Se conservan las decisiones para mantener la trazabilidad; esta advertencia prevalece sobre las menciones de cierre en otros archivos.

# Cierre auditado del corpus documental

Fecha: 2026-10-27. Estado operativo cerrado: **57 estudios incluidos y 91 no incluidos**, de 148 registros preseleccionados. No se incorporó ningún estudio nuevo ni se reincorporó un excluido. Esta auditoría prevalece sobre los recuentos históricos de 74, 64 y 58.

## Alcance y evidencia

Por instrucción del equipo, se tomó como techo la lista previa de 58 incluidos. Se contrastaron los PDF locales mediante extracción y consulta de las secciones de métodos, anotaciones y resultados: 57 textos legibles confirman clase casco y/o chaleco (incluidas clases de ausencia), localización con cajas y cifras de desempeño; el archivo del ID 126 está truncado y no pudo analizarse con pypdf ni pdfminer. Se conserva el archivo original, pero su disponibilidad nominal no acredita texto completo utilizable. Pasa a excluir/E5.

La matriz AUDITORIA_CIERRE.csv documenta los 148 IDs, decisiones anteriores y actuales, etapa real, PDF y cifras comprobadas de los 57 retenidos. estudios_incluidos.csv es la lista operativa final y no agrega referencias.

Los pases previos no equivalen a tres revisores humanos independientes. R2 consultó secciones completas o fragmentos indexados para varios casos y la conversación ya contenía antecedentes de R1. R3 dirimió con título/resumen, por lo que su frase «igual que R1 y R2, sin abrir PDF» era incorrecta. Esta auditoría es asistida por IA, con consulta de secciones pertinentes, y no se presenta como lectura humana integral e independiente.

## Decisiones históricas con evidencia contradictoria

IDs 11, 12, 21, 22, 23, 26, 36, 60, 80, 86, 87, 92, 93, 94, 95, 100, 110, 112, 115, 125, 132, 141 y 142: la exclusión histórica por E3/E4 no es firme frente a la evidencia consignada por R2. No se sostiene que estos artículos carezcan de métricas o clases solo porque el resumen no las enumera. La selección tampoco puede exigir ahora métricas exclusivamente por clase cuando el protocolo admitía mAP agregado y mejoras relativas.

Se mantienen fuera por la instrucción actual de no ampliar el corpus, no por una supuesta deficiencia demostrada del artículo. Para no falsear el motivo, motivo_final usa **C0: no reincorporado por cierre administrativo de corpus** en esos 23 casos. C0 es un marcador de gestión explícito, no un nuevo criterio científico E1–E6 ni una exclusión tras lectura completa. R1/R2, sus motivos y las 28 discrepancias históricas se preservan íntegramente. Los demás E3/E4 se conservan como filtro documental, sin afirmar ausencia en el cuerpo no evaluado.

Esto limita la exhaustividad de la revisión: los 57 constituyen un corpus cerrado para el proyecto, no todos los estudios elegibles que arrojaría una revisión exhaustiva de los 148. Reducir el corpus por cierre del equipo introduce selección administrativa y debe declararse; no se oculta bajo PRISMA.

## Recuentos sin doble conteo

| Etapa real | Entrada | Salida o no retenidos | Continúan |
|---|---:|---:|---:|
| Scopus, registros identificados | 158 | 0 duplicados DOI detectados en exportación | 158 |
| Título/resumen, filtro inicial | 158 | 10 | 148 |
| Selección documental complementaria | 148 | 74: 39 E3 + 12 E4 + 23 C0 | 74 |
| Recuperación del subconjunto seleccionado | 74 | 17 no evaluables: 16 no recuperados + 1 PDF truncado | 57 |
| Evaluación de secciones del texto completo local | 57 | 0 exclusiones adicionales | 57 |
| Corpus final cerrado | 57 | — | **57** |

Identidades: **158 = 10 + 74 + 17 + 57**; **148 = 74 + 17 + 57**; **91 = 39 E3 + 12 E4 + 23 C0 + 17 E5**. E5 queda en recuperación, no se suma nuevamente como exclusión de texto evaluado. Los dos estudios sin DOI están no recuperados en esta copia; no consta un intento exhaustivo de localizarlos por título.

No se mantienen «132 evaluados»: restar 16 a 148 no acreditaba recuperación ni lectura de esos 132 informes. El flujo separa la selección documental inicial de la lectura de los 57 PDF utilizables. La figura es una adaptación transparente del flujo de reporte, no prueba de cumplimiento íntegro de PRISMA.

## Otros métodos y bibliografía de contexto

Los nueve registros identificados históricamente por otros métodos no tuvieron el mismo cribado estructurado y pueden solaparse con Scopus. No se suman seis automáticamente. Se conservan como bibliografía de contexto/metodológica fuera del corpus de síntesis, sin borrar PDF ni impedir citas justificadas. El total de la Figura 1 y su pie en el Word pasa de 64 a 57.

## Observaciones de calidad dentro del corpus

Los IDs 52, 71, 81 y 122 presentan inconsistencias de rotulado o cifras entre tablas/texto. Se mantienen porque aportan tarea y cifras, pero la matriz identifica la limitación. No se fabricó un criterio retrospectivo de calidad para excluirlos, ni se propone un metaanálisis con sus cifras sin resolverlas. El ID 122 sí muestra cajas y tabla 5 por casco/chaleco: la duda de R2 queda aclarada por el PDF. La integración detección/clasificación del ID 13 conserva evaluación de localización y métricas del modelo, por lo que no se excluye solo por ser de dos etapas.

## Archivos sincronizados y verificación

Consolidado y dos lotes conservan los mismos 148 IDs y decisiones por ID; solamente se modifican decision_final/motivo_final. No se alteran las columnas R1/R2, discrepancia ni datos bibliográficos. Se actualizan figura SVG/PNG y la figura incrustada/pie del Word, sin redactar la sección de Métodos ni modificar otros resultados experimentales.

No se descargaron ni añadieron artículos. No se borró bibliografía. El registro anterior permanece identificable en los documentos históricos y el respaldo local de auditoría.
