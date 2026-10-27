Actúa como **Revisor 2 (R2)** en una revisión sistemática PRISMA 2020 sobre detección por
visión computacional de casco y chaleco de seguridad en obras de construcción (el trabajo usa
YOLO26). Estoy en la etapa de **cribado por texto completo**: 148 estudios pasaron el cribado
de título/resumen y hay que decidir, uno por uno, si se incluyen o excluyen del corpus final.

Tienes acceso al repositorio del proyecto. Archivos relevantes:

- `TRABAJO GRUPAL/metodologia Prisma/4-resultados/INSTRUCCIONES_CRIBADO.md` — el protocolo
  completo (quién hace qué, cómo rellenar, criterios y códigos; reprodúcelos de ahí, son la
  fuente de verdad).
- `TRABAJO GRUPAL/metodologia Prisma/3-busqueda/scopus_2026-10-09.csv` — título, resumen,
  palabras clave y DOI de cada estudio (columna `Abstract`, `Author Keywords`, `Index Keywords`).
- `TRABAJO GRUPAL/metodologia Prisma/4-resultados/cribado_texto_completo.csv`,
  `cribado_lote_1.csv`, `cribado_lote_2.csv` — las tres tienen los 148 registros con columnas
  `decision_R1`/`motivo_R1` **ya rellenas por el Revisor 1**.

**No leas ni uses las columnas `decision_R1` / `motivo_R1` de esos tres archivos.** Un Revisor 1
ya cribó estos 148 de forma independiente, y tu valor está precisamente en no saber qué decidió
— al final se comparan ambos cribados y un tercer revisor dirime las discrepancias. Si las
abres, ignora esas dos columnas al decidir.

Si tienes forma de buscar el DOI o el título y leer el texto completo real (navegación web,
herramientas de búsqueda), hazlo cuando el resumen te deje en duda; es preferible a decidir solo
con el resumen. Si no tienes esa capacidad, decide con el resumen y dilo explícitamente.

## Criterios de inclusión (deben cumplirse todos)

| | |
|---|---|
| I1 | Artículo primario en revista indexada en Scopus y/o WoS |
| I2 | Publicado entre 2021 y 2026 |
| I3 | Inglés o español |
| I4 | Tarea de detección de objetos, con cajas delimitadoras |
| I5 | El EPP detectado incluye casco y/o chaleco |
| I6 | Dominio de construcción u obra, o industrial con EPP equivalente |
| I7 | Reporta métricas cuantitativas |

## Códigos de exclusión (usa el que corresponda; toda exclusión necesita uno)

| Código | Criterio |
|---|---|
| E1 | Revisión, editorial, carta, capítulo o preprint sin revisar |
| E2 | Solo sensores no visuales, sin componente de visión |
| E3 | EPP exclusivamente fuera de alcance (no es casco/chaleco, o el EPP es solo un ingrediente secundario de otra tarea: comportamiento inseguro, somnolencia, razonamiento visión-lenguaje/VQA, gestión de calidad, autorización de maquinaria, etc. — no una detección de casco/chaleco como tal) |
| E4 | Sin métricas cuantitativas de desempeño del detector (nombrar la métrica sin dar el valor no cuenta; una mejora relativa como "+2.1%" sí cuenta) |
| E5 | Texto completo inaccesible |
| E6 | Duplicado de otro registro de esta misma lista de 148 |

## Criterio operativo para decidir (importante, aplícalo de forma estricta)

El equipo quiere **minimizar el corpus final**: ante cualquier ambigüedad real, se excluye. Un
estudio se mantiene **incluir** solo si el resumen (o el texto completo, si lo consultaste)
confirma las tres cosas a la vez:

1. **Clase explícita**: nombra casco/hardhat/helmet y/o chaleco/vest/safety-vest como objeto
   detectado — no basta que diga "PPE" de forma genérica sin especificar.
2. **Cifra concreta**: da un número de desempeño del detector (mAP, precisión, recall,
   exactitud, F1, AP), aunque sea una mejora relativa.
3. **Tarea real de detección de casco/chaleco**: es un modelo de detección de objetos cuyo
   objetivo central es casco y/o chaleco — no un sistema cuyo objetivo central es otra cosa
   y el EPP aparece solo de forma incidental.

Si cualquiera de las tres no se puede confirmar → excluir, con el código E3 (si falla 1 o 3) o
E4 (si falla 2).

## Qué entregar

Rellena `decision_R2` (`incluir`/`excluir`) y `motivo_R2` (vacío si incluye; código E1-E6 si
excluye) en los tres CSV (`cribado_lote_1.csv`, `cribado_lote_2.csv`,
`cribado_texto_completo.csv`), para los 148 ids, sin tocar ninguna otra columna. Al final, un
resumen: cuántos incluir/excluir, y cuántos de cada código de exclusión. Si consultaste texto
completo real para algún caso dudoso, indícalo junto a ese id.
