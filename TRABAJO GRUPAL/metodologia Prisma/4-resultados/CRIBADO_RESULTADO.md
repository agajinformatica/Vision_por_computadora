# Cribado por título y resumen — resultado

> **Primer tamizaje automatizado, no una decisión del equipo.** Las decisiones de cribado
> deben ser revisadas y firmadas por dos revisores independientes con un tercero que dirima.
> Este documento es el material de partida, no el cribado final.

Fuente: `../3-busqueda/scopus_2026-10-09.csv` (158 registros)
Resultado por registro: `cribado_titulo_resumen.csv` (esta misma carpeta)
Fecha: 2026-10-09

---

## Resultado

| Decisión | Registros | % |
|---|---:|---:|
| **PASA** — alta confianza | 79 | 50,0% |
| **PASA** — con puntos a verificar | 69 | 43,7% |
| **EXCLUIR** | 10 | 6,3% |
| **Total** | **158** | |

**Excluidos en esta etapa: 10. Pasan a texto completo: 148.**

### Motivos de exclusión

| Motivo | Registros |
|---|---:|
| E3 — no trata EPP en alcance | 7 |
| E1 — revisión o survey | 3 |

---

## Por qué solo se excluyen 10

El cribado por título y resumen es **deliberadamente permisivo**: ante la duda, pasa.
Descartar aquí un estudio válido es un error irreversible; leer de más un texto completo
solo cuesta tiempo. Por eso solo se excluye lo inequívoco.

Los 69 "con puntos a verificar" **no son dudas sobre su validez**, sino datos que el
resumen no permite confirmar y que habrá que comprobar en el texto completo:

| Punto a verificar | Registros |
|---|---:|
| I5 — menciona "PPE" pero no nombra casco ni chaleco | 50 |
| I7 — no se ven métricas en el resumen | 16 |
| I4 — la detección no es explícita | 2 |
| I6 — dominio industrial, no obra | 1 |

---

## Decisión metodológica: cómo aplicar I5

Se evaluaron dos formas de aplicar el criterio I5 (*el EPP detectado incluye casco y/o chaleco*):

| | Escenario A — permisivo | Escenario B — estricto |
|---|---|---|
| Regla | Basta que el estudio trate de EPP | Debe nombrar casco o chaleco en título/resumen |
| Excluidos en cribado | 10 | 74 |
| Pasan a texto completo | 148 | 84 |

**Se adoptó el Escenario A.** El estricto es más cómodo, pero dejaría fuera 14 estudios
de alto impacto, entre ellos:

| Citas | Estudio |
|---:|---|
| 109 | PPE detector: A YOLO-based architecture to detect personal protective equipment |
| 95 | Personal Protective Equipment Detection: A Deep-Learning-Based Sustainable Approach |
| 93 | Towards on-site hazards identification of improper use of PPE |
| 90 | Construction Site Safety Management: A Computer Vision and Deep Learning approach |

El segundo de esa lista es la **referencia #16 que el equipo ya había descargado y valorado
como pertinente**. Un criterio que excluye lo que el propio equipo seleccionó está mal
aplicado: la ausencia de una palabra en el resumen no prueba la ausencia del contenido
en el estudio. Esa verificación corresponde a la etapa de texto completo, no a esta.

---

## Cómo abordar los 148

El archivo `cribado_titulo_resumen.csv` viene **ordenado por prioridad**:

1. Primero los 79 de alta confianza, de más a menos citados
2. Después los 69 a verificar, igualmente por citas
3. Al final los 10 excluidos, para auditoría

En la práctica, un texto completo claramente fuera de alcance se resuelve en dos minutos;
solo los pertinentes exigen lectura detenida. Conviene repartir el listado entre los dos
revisores respetando ese orden, de modo que lo valioso se procese primero.

**Cada exclusión en texto completo debe quedar registrada con su motivo** (código E1-E6):
ese recuento va en el diagrama de flujo y es lo que PRISMA exige reportar.

---

## Estado del diagrama de flujo

| Casilla | Valor |
|---|---|
| Identificados en bases de datos | **158** (Scopus) · WoS pendiente |
| Identificados por otros métodos | 9 |
| Duplicados eliminados | — *(se calcula al sumar WoS)* |
| Cribados por título y resumen | 158 |
| Excluidos en cribado | **10** |
| Buscados para recuperación | **148** |
| No recuperados | — |
| Evaluados en texto completo | — |
| Excluidos en texto completo, con motivo | — |
| **Estudios incluidos** | — |
