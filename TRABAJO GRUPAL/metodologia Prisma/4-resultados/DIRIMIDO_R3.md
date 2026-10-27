> **Estado vigente tras resolver C0 (2026-10-27): 80 incluidos / 68 excluidos; ningun C0 pendiente.** Se reincorporan los 23 por evidencia de elegibilidad, sin agregar estudios a los 148 originales. Ver [CIERRE_AUDITADO.md](CIERRE_AUDITADO.md) y [RESOLUCION_23_CASOS.md](RESOLUCION_23_CASOS.md). Los recuentos de 57 y C0 que siguen son historicos.

> **Estado vigente — auditoría 2026-10-27:** corpus cerrado de **57 incluidos / 91 no incluidos**. No se añaden estudios. Ver [CIERRE_AUDITADO.md](CIERRE_AUDITADO.md) y `AUDITORIA_CIERRE.csv`. Los recuentos siguientes son históricos; no usar 64, 74, 58 ni 132 como resultado actual. Se distinguen selección documental, cierre administrativo C0 y recuperación E5.

# Cribado de texto completo — dirimido (R3)

**Quién dirimió:** asistente de IA, actuando como R3, por pedido del equipo, con instrucción
explícita de minimizar el corpus final ante cualquier ambigüedad real.
**Base:** las 28 discrepancias de `COMPARACION_R1_R2.md`, revisadas una por una contra el
resumen/título de Scopus (no el PDF completo).

## Resultado

| | Registros |
|---|---:|
| Dirimidas hacia **excluir** | 26 |
| Dirimidas hacia **incluir** | 2 |
| Total discrepancias | 28 |

**Totales finales del cribado de texto completo: 74 incluir / 74 excluir** (de 148 evaluados).

## Las 2 que se dirimieron hacia incluir

- **id 62** — *AF-YOLOv8: a lightweight algorithm suitable for helmet and vest detection*. El
  **título mismo** nombra "helmet and vest detection"; el resumen da mAP 91.2% y +1.4% sobre la
  base. Cumple las tres condiciones sin ambigüedad real — la exclusión de R2 (E3) no se sostiene
  contra el texto.
- **id 122** — *Real-time construction safety monitoring using a drone based deep hybrid
  attention model*. Nombra explícitamente "helmets, harnesses, and lifelines" como lo detectado
  y da una cifra (99.9% de exactitud). A pesar del nombre poco convencional del método, cumple
  las tres condiciones; no hay un código E1-E6 que justifique excluirlo solo por el estilo de
  redacción del resumen.

## Las 26 que se dirimieron hacia excluir

**Por E4 (sin cifra de desempeño del detector)** — 16 casos: id 11, 12, 21, 22, 23, 26, 36, 60,
80, 86, 92, 93, 94, 95, 110, 132, 141. En todos, el resumen nombra la métrica o dice "mejora" sin
dar nunca un valor, o (casos 60 y 93) la cifra que sí aparece no corresponde específicamente a
casco/chaleco sino a un conjunto más amplio de clases o es solo revisión de calidad del dataset.

**Por E3 (EPP o tarea fuera de alcance)** — 10 casos: id 7, 87, 100, 104, 112, 115, 125, 79, 142,
y de nuevo 93 se solapa con ambos motivos.

Tres casos merecen explicación porque **revierten la decisión original de R1** (que los había
incluido):

- **id 7** — *Standardized use inspection of workers' PPE*. La cifra de desempeño (94.67%) que
  da el resumen **no es del detector de casco/gancho** (YOLOv5), sino de un clasificador
  posterior (1D-CNN) que evalúa "comportamiento inseguro" a partir de series de tiempo. El EPP
  es solo un ingrediente de entrada; no hay una métrica de detección de casco en el resumen.
- **id 79** — *Rapid image recognition for construction worker hard hat compliance (VGG16)*. Usa
  **clasificación de imagen completa** (VGG16: ¿lleva o no casco?, sí/no), no detección con
  cajas delimitadoras. Falla I4 por definición del protocolo, aunque el resto (casco explícito,
  cifras explícitas) esté perfecto.
- **id 104** — El propio resumen dice que el sistema va **más allá** de "identification of
  helmets or vests" (lo que hacen los sistemas existentes) hacia "PPE según el tipo de trabajo".
  No queda confirmado que las clases detectadas en este estudio sean específicamente casco/chaleco.

## Nota de transparencia

Este dirimido histórico de R3 se hizo **sin abrir los PDF reales**. R2 sí consultó secciones completas y evidencia indexada, como consta en sus notas; no corresponde equiparar ambos procedimientos. Es la decisión más
razonable con la evidencia disponible (resumen + título + palabras clave), aplicando de forma
consistente las reglas I1-I7/E1-E6 y la instrucción de minimizar ante la duda — pero no
sustituye una verificación humana. Si antes de cerrar el embudo PRISMA alguien del equipo quiere
revisar algún caso puntual con el PDF real, los candidatos con más citas a revisar primero son
**id 80 (109 citas)** y **id 93 (33 citas)**, por su peso para la Introducción del paper.

## Actualización 2026-10-26 (tarde) — reclasificación por E5

Tras el dirimido, se descargaron los PDF reales de los 74 incluidos. De esos, **16 no se
pudieron recuperar** (14 tras paywall real confirmado al intentar bajarlos, 2 sin DOI) — ver
`referencias/PDFS_FALTANTES.md`. Por decisión del equipo, esos 16 se **reclasificaron de
incluir a excluir con motivo E5** (texto completo inaccesible) en vez de quedar como incluidos
sin verificación real.

**Cifra final del cribado de texto completo: 58 incluidos / 90 excluidos** (45 E3 · 29 E4 · 16
E5), de 148 evaluados. Los 58 incluidos finales tienen su PDF real en `referencias/`.

IDs reclasificados a E5: 2, 18, 24, 25, 38, 46, 55, 61, 62, 66, 67, 70, 74, 76, 78, 96.
