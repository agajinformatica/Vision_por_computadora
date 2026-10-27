# Cribado por texto completo — instrucciones

148 estudios que superaron el cribado por título y resumen. Esta es la **segunda etapa**:
lenta y estricta, al contrario que la primera.

## Archivos

| Archivo | Para quién |
|---|---|
| `cribado_texto_completo.csv` | la tabla completa, donde se consolida |
| `cribado_lote_1.csv` | 74 registros |
| `cribado_lote_2.csv` | 74 registros |

Los lotes conservan el orden de prioridad: primero los de alta confianza y más citados.

## Quién hace qué

PRISMA exige **dos revisores independientes** y un tercero que resuelva discrepancias.

| Fase | Acción |
|---|---|
| 1 | **R1 y R2 criban los 148 cada uno, por separado y sin consultarse** |
| 2 | Se comparan: donde coincidan, decisión firme |
| 3 | **R3 dirime** solo los casos en desacuerdo |
| 4 | Se cuenta cuántas discrepancias hubo — ese número se reporta |

> El punto es que sean **independientes**. Si se cribala a dos manos mirando la misma
> pantalla, el procedimiento pierde su razón de ser y no se puede declarar como tal.

## Cómo rellenar

| Columna | Qué poner |
|---|---|
| `decision_R1` / `decision_R2` | `incluir` o `excluir` |
| `motivo_R1` / `motivo_R2` | **obligatorio si se excluye**: el código E1-E6 |
| `discrepancia` | `si` / `no` — se calcula al comparar |
| `decision_final` | la firme, tras dirimir |
| `motivo_final` | código E1-E6 si se excluye |

La columna `a_verificar_segun_resumen` indica qué quedó sin confirmar en la primera etapa.
Es lo primero que hay que mirar en el texto completo.

## Códigos de exclusión

| Código | Criterio |
|---|---|
| **E1** | Revisión, editorial, carta, capítulo o preprint sin revisar |
| **E2** | Solo sensores no visuales, sin componente de visión |
| **E3** | EPP exclusivamente fuera de alcance (solo mascarilla, guantes o gafas) |
| **E4** | Sin métricas cuantitativas de desempeño |
| **E5** | Texto completo inaccesible |
| **E6** | Duplicado |

**Cada exclusión necesita su código.** No vale "no sirve". El recuento por motivo va al
diagrama de flujo y es lo que PRISMA exige reportar.

## Criterios de inclusión, para tener a mano

| | |
|---|---|
| I1 | Artículo primario en revista indexada en Scopus y/o WoS |
| I2 | Publicado entre 2021 y 2026 |
| I3 | Inglés o español |
| I4 | Tarea de detección de objetos, con cajas delimitadoras |
| I5 | El EPP detectado incluye casco y/o chaleco |
| I6 | Dominio de construcción u obra, o industrial con EPP equivalente |
| I7 | Reporta métricas cuantitativas |

## Ritmo realista

Un texto claramente fuera de alcance se resuelve en **2 minutos**; uno pertinente exige
lectura, unos **10-15**. Estimando una mezcla razonable, son entre **8 y 12 horas por revisor**.

El cronograma marca el **1 de noviembre** como fecha tope. Repartido en tres semanas,
son unas 3-4 horas semanales por persona.

## Al terminar

Consolidar en `cribado_texto_completo.csv` y avisar. Con eso se calculan:

- Número de evaluados en texto completo
- Excluidos por cada motivo E1-E6
- **Estudios incluidos** — los que alimentan la Introducción
- Discrepancias entre revisores

Y queda listo el diagrama de flujo con números reales.

## Correccion del cierre administrativo — 2026-10-27

C0 queda revocado: no pertenece al protocolo. Los 23 casos se resolvieron como incluir aplicando I1–I7 y la regla operativa de clase explicita, cifra y tarea central con cajas. El corpus actual es 80 incluidos y 68 excluidos (39 E3, 12 E4, 17 E5). R1/R2 y sus discrepancias se conservan como antecedentes; esta correccion final asistida por IA no acredita independencia humana. Ver CIERRE_AUDITADO.md y RESOLUCION_23_CASOS.md para evidencia, limites y recuentos reales. La version anterior del cierre se conserva en historico/.
