# Cribado de texto completo — notas del Revisor 1 (R1)

**Quién hizo este pase:** asistente de IA, actuando como R1, por pedido del equipo.
**Fecha:** 2026-10-26 (revisado con criterio estricto el mismo día, a pedido del equipo: *"si
hay ambigüedades exclúyelo, sin salirte de las reglas, la idea es tener la menor cantidad de
papers al final"*).
**Base usada:** título + resumen + palabras clave + tipo de documento de Scopus
(`3-busqueda/scopus_2026-10-09.csv`), **no el PDF completo** de los 148 estudios (el equipo
solo tiene 30 PDFs descargados en `referencias/`). Esto es una limitación real: el criterio
estricto de abajo decide a favor de excluir cuando el **resumen** no confirma algo, lo cual no
prueba que el **artículo completo** no lo tenga. Antes de dar el embudo PRISMA por cerrado,
alguien del equipo debería abrir el PDF de los casos "excluir" que tengan alto número de citas
o que parezcan claramente dentro de alcance, por si el resumen fue solo poco explícito.

## Resultado final

| Decisión | Registros |
|---|---:|
| **incluir** | **77** |
| **excluir** | **71** |
| Total | 148 |

| Motivo de exclusión | Registros |
|---|---:|
| E3 — EPP/tarea fuera de alcance (no se confirma casco/chaleco como objeto detectado) | 42 |
| E4 — sin cifra cuantitativa de desempeño del detector en el resumen | 29 |

## Criterio estricto aplicado (regla operativa, no cambia los códigos del protocolo)

Para que un estudio se mantenga **incluir**, el resumen debe confirmar las **tres** cosas a la vez:

1. **Clase explícita**: nombra casco/hardhat/helmet y/o chaleco/vest como objeto detectado (no
   basta "PPE" genérico).
2. **Cifra concreta**: da un número de desempeño del detector (mAP, precisión, recall, exactitud,
   F1, AP), aunque sea una mejora relativa (p. ej. "+2.1%"). No basta "buen desempeño",
   "resultados prometedores" o nombrar la métrica sin dar el valor.
3. **Tarea real de detección**: es un modelo de detección de objetos con cajas delimitadoras
   cuyo objetivo central es casco/chaleco — no un sistema cuyo objetivo central es otra cosa
   (comportamiento inseguro, somnolencia, razonamiento visión-lenguaje/VQA, gestión de calidad de
   obra, autorización de maquinaria) donde el EPP es solo un ingrediente secundario.

Si cualquiera de las tres es ambigua desde el resumen → **excluir**, usando el código E1-E6 que
mejor describe el motivo (no se inventó ningún código nuevo):

- Falla (1) o (3) → **E3** (el EPP relevante del estudio está, en los hechos, fuera del alcance
  de esta revisión — no es casco/chaleco, o no es ese el objeto de la detección).
- Falla (2) → **E4** (sin métrica cuantitativa confirmable).

## Cambios importantes frente al primer pase (más permisivo)

Este criterio es considerablemente más duro que el pase anterior (que había dejado 141 incluir).
Baja a **77**. Los cambios más notables, para que el equipo los revise con criterio propio si
lo considera necesario:

- **id 80 y 82** — excluidos ahora por E4 y E3 respectivamente. Son dos de los estudios que
  `CRIBADO_RESULTADO.md` identificó como **alto impacto** (109 y 93 citas) que el equipo decidió
  proteger aplicando I5 de forma permisiva **en la etapa de título/resumen** (decisión D8). Esa
  decisión era explícitamente para dejarlos pasar a la etapa de texto completo, no para
  incluirlos automáticamente aquí. Con el criterio estricto de esta etapa: el 80 no da ninguna
  cifra de mAP en el resumen ("yields the highest mAP" sin número) y el 82 no nombra casco/chaleco
  (solo "PPE" genérico, aunque sí da precisión 94.47% y recall 83.20%). **Recomiendo que alguien
  abra estos dos PDFs específicamente** antes de cerrarlos como excluidos, dado que el equipo ya
  los había marcado como valiosos.
- Varios papers de casco **muy claramente dentro de tema** (helmet detection en obra) quedaron
  excluidos solo porque el resumen no da una cifra concreta, aunque casi seguro la tienen en el
  cuerpo del artículo (es raro que un paper de este tipo no reporte mAP): ids 11, 12, 21, 22, 23,
  26, 29, 30, 36, 37, 47, 51, 60, 69, 86, 89, 92, 93, 94, 95, 110, 111, 114, 121, 123, 132, 139,
  141. Si el equipo quiere recuperar alguno rápido, el camino más corto es abrir el PDF y
  confirmar la cifra — no hace falta releer todo el resumen.
- La mayoría de los estudios que solo dicen "PPE" genérico sin nombrar casco/chaleco quedaron
  excluidos (E3), aun con buenas cifras: ids 82, 83, 84, 85, 87, 88, 91, 92, 93, 98, 99, 100, 102,
  105, 107, 112, 115, 117, 124, 125, 127, 129, 131, 133, 134, 135, 137, 140, 142, 143, 145, 147,
  148.
- Los casos de "EPP es un ingrediente secundario de otra tarea" (comportamiento inseguro,
  somnolencia, VQA, gestión de calidad, autorización de maquinaria) quedaron excluidos de forma
  consistente, todos con E3: ids 42, 65, 85, 103, 106, 108, 113, 118, 119, 120, 138, 144.
  (El 113 es EPP de laboratorio fuera de dominio, el 118 es EPP como residuo reciclable, el 120
  es solo guantes, el 144 es un falso positivo de sigla —"PPE" de fibra óptica—; estos cuatro son
  exclusiones seguras, no ambiguas.)

## Los 77 que quedaron incluidos

Confirman explícitamente casco y/o chaleco como clase detectada **y** una cifra de desempeño
**y** son una tarea de detección real: ids 1-10, 13-20, 24, 25, 27, 28, 31-35, 38-41, 43-46,
48-50, 52-59, 61-64, 66-68, 70-79, 81, 90, 96, 97, 101, 104, 109, 116, 122, 126, 128, 130, 136,
146.

## Siguiente paso

Este sigue siendo solo el pase de **R1**. Falta: (1) un R2 independiente (sin ver estas
decisiones) con el mismo criterio estricto, (2) comparar discrepancias, (3) un R3 que dirima, y
(4) especialmente, abrir el PDF real de los casos marcados arriba como "muy probablemente sí
cumple pero sin cifra en el resumen" antes de dar los 77 por definitivos — varios podrían
recuperarse con una lectura de 2 minutos del abstract completo o la tabla de resultados.
