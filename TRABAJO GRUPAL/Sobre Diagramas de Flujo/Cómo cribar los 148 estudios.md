Revisión sistemática · PRISMA 2020

# Cómo cribar los 148 estudios

Guía operativa para la segunda etapa del cribado. Qué hay que decidir en cada estudio, con qué criterios, y por qué hacen falta dos personas revisando lo mismo por separado.

Detección de casco y chaleco · YOLO26 Maestría en IA · UNMSM Fecha tope: 1 de noviembre

## 01 Dónde estamos

La búsqueda en Scopus devolvió **158 registros**. La primera etapa —leer solo título y resumen— ya está hecha y descartó 10. Quedan **148 estudios** por evaluar leyendo el texto completo. Eso es lo que toca ahora.

Identificación 158 + 9 Scopus, más 9 halladas por otras vías

→

— Duplicados, al sumar WoS

Etapa 1 · Hecha 158 Cribados por título y resumen

→

10 7 por E3 · 3 por E1

Etapa 2 · Toca ahora 148 A evaluar leyendo el texto completo

→

? Cada uno con su código E1–E6

Resultado ? Estudios incluidos — los que se citan en la Introducción

## 02 Por qué son dos etapas

Piénsalo como buscar piso entre 158 anuncios. Nadie visita 158 pisos; pero tampoco descartas uno por el anuncio si hay duda, porque podrías perderte el bueno.

Etapa 1 · completada

#### Título y resumen

Rápida y permisiva. Lees la ficha, no el paper. **Ante la duda, pasa.** Solo se descarta lo inequívoco.

Descartar aquí un estudio válido es un error irreversible; leer de más un texto completo solo cuesta tiempo.

Etapa 2 · pendiente

#### Texto completo

Lenta y estricta. Lees el artículo y compruebas lo que el resumen no decía.

**Cada exclusión exige su motivo por escrito**, con código. Ese recuento va al diagrama de flujo y es lo que PRISMA obliga a reportar.

## 03 Las siete preguntas

Abres el PDF y respondes esto. **Siete síes → `incluir`.** Un solo no → `excluir`, con su código.

| Criterio | Pregunta |
| --- | --- |
| I1 | ¿Es un artículo primario en revista indexada en Scopus o WoS? |
| I2 | ¿Se publicó entre 2021 y 2026? |
| I3 | ¿Está en inglés o español? |
| I4 | ¿Detecta objetos con cajas delimitadoras? No vale clasificar la imagen entera. |
| I5 | ¿El EPP que detecta incluye casco y/o chaleco? |
| I6 | ¿Es de construcción u obra, o industria con EPP equivalente? |
| I7 | ¿Reporta métricas cuantitativas: mAP, precisión, recall? |

### Códigos de exclusión

| Código | Se excluye porque… |
| --- | --- |
| E1 | Es una revisión, editorial, carta, capítulo o preprint sin revisar |
| E2 | Usa solo sensores no visuales (RFID, IoT), sin visión por computadora |
| E3 | El EPP está fuera de alcance: solo mascarilla, guantes o gafas |
| E4 | No da ninguna métrica numérica de desempeño |
| E5 | No se consiguió el texto completo |
| E6 | Es un duplicado de otro ya revisado |

**El motivo no es opcional.** «No sirve» no vale. El recuento por código es justo lo que rellena la casilla «excluidos con razones» del diagrama PRISMA.

## 04 Por qué dos personas

Esta es la parte que más se malinterpreta. **R1 y R2 revisan los 148 cada uno, por separado y sin hablar entre ellos.** No se reparten 74 y 74 — eso sería dividir el trabajo, no validarlo.

Revisor 1\
los 148

Revisor 2\
los 148

¿Coinciden las dos decisiones?

Sí → decisión firme No → lo dirime el Revisor 3

Al final se cuenta cuántas discrepancias hubo. Ese número se declara en el artículo: *«dos revisores independientes; N discrepancias resueltas por un tercero»*. Es la prueba de que el filtro fue real y no el criterio de una sola persona.

Hay un atajo: repartirse `lote_1` y `lote_2`, 74 cada uno. Es defendible si el tiempo aprieta, pero entonces **no se puede declarar cribado independiente** — habría que escribir que cada estudio lo evaluó un solo revisor. Menos riguroso. Conviene decidirlo antes de empezar, no después.

## 05 Cómo se rellena

En `cribado_texto_completo.csv`, cada fila es un estudio. La columna `a_verificar_segun_resumen` dice qué quedó sin confirmar en la etapa 1: eso es lo primero que hay que mirar en el PDF.

| Columna | Qué se escribe |
| --- | --- |
| decision_R1 | `incluir` o `excluir` |
| motivo_R1 | El código E1–E6. Obligatorio si se excluye |
| decision_R2 | Lo mismo, rellenado por la otra persona |
| motivo_R2 | El código E1–E6 |
| discrepancia | `sí` / `no`, al comparar |
| decision_final | La firme, tras dirimir |

### Ritmo realista

Un texto claramente fuera de alcance se resuelve en dos minutos; uno pertinente exige lectura, unos diez o quince. En conjunto son entre **8 y 12 horas por revisor**: repartido hasta el 1 de noviembre, unas 3 o 4 horas semanales por persona.

## 06 Antes de empezar

1. Decidir quién es **R1**, **R2** y **R3**.
2. Decidir si se criba de forma independiente (lo riguroso) o repartido por lotes (lo rápido).
3. Conseguir los PDF. Hay 30 descargados de los 148; los que estén tras muro de pago se excluyen con **E5**, que es una razón legítima y se reporta.
4. Empezar por el principio del archivo: viene ordenado por prioridad, con los más citados y de mayor confianza arriba.

Los criterios I1–I7 y E1–E6 están definidos en `2-protocolo/PROTOCOLO_REVISION.md`. El resultado de la etapa 1 y sus cifras, en `4-resultados/CRIBADO_RESULTADO.md`. Las cifras de esta página corresponden a la búsqueda en Scopus del 9 de octubre de 2026; la búsqueda en Web of Science sigue pendiente de acceso institucional.