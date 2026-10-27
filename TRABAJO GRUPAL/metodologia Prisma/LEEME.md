> **Estado vigente 2026-10-27:** corpus cerrado de **57 estudios**. Auditoría y figura completadas, sin nuevas inclusiones; ID 126 excluido por PDF truncado. Se separan 74 no retenidos en selección documental y 17 no evaluables en recuperación. Los 9 de otros métodos no se suman. Ver [cierre auditado](<4-resultados/CIERRE_AUDITADO.md>). Los recuentos anteriores que difieran son históricos.

# Metodología PRISMA — organización de la carpeta

Las cuatro subcarpetas siguen **el orden en que se ejecuta una revisión sistemática**.
Para entender en qué punto está el trabajo, basta mirar cuál es la última con contenido.

```
1-metodo/      →  2-protocolo/  →  3-busqueda/  →  4-resultados/
qué dice           qué decidimos     qué arrojó      qué sacamos
la norma           nosotros          la búsqueda     de ello
```

---

## 1-metodo/ — material de referencia

Lo que define el método. **No se modifica**: se consulta.

| Archivo | Para qué |
|---|---|
| `PRISMA_2020_statement_BMJ_n71.pdf` | La declaración oficial. Es lo que se cita |
| `PRISMA_2020_explanation_elaboration_BMJ_n160.pdf` | Manual de uso, ítem por ítem con ejemplos |
| `PRISMA-S_extension_busquedas_SystRev_2021.pdf` | Cómo reportar la estrategia de búsqueda |
| `PRISMA_2020_declaracion_ESPANOL_RevEspCardiol.pdf` | Traducción oficial al español |
| `PRISMA_2020_anexo_ESPANOL_checklist.pdf` | Checklist y diagrama de flujo en español |
| `CONTENIDO.md` | Descripción de cada documento y plantilla |
| `plantillas/` | Checklist de 27 ítems y los 4 diagramas de flujo, para rellenar |

> De los diagramas de flujo corresponde usar **`new_SRs_v2`**: es el que incluye la columna
> de "otros métodos", donde entran las referencias halladas fuera de las bases de datos.

## 2-protocolo/ — nuestras decisiones

Lo que el equipo decide **antes** de buscar. Es lo que hace reproducible la revisión.

| Archivo | Contenido |
|---|---|
| `PROTOCOLO_REVISION.md` | Pregunta de revisión, criterios I1-I7 y E1-E6, decisiones pendientes, asignación de revisores |
| `CADENAS_BUSQUEDA.md` | Cadenas traducidas a sintaxis Scopus y WoS, y el registro obligatorio por base |

## 3-busqueda/ — evidencia cruda

Lo que devolvió cada base, **sin procesar**. Es la prueba de que la búsqueda se ejecutó.
Los nombres llevan la fecha porque PRISMA-S exige declararla.

| Archivo | Contenido |
|---|---|
| `scopus_2026-10-09.csv` | 158 registros con resumen, 33 campos |
| *(pendiente)* `wos_AAAA-MM-DD.csv` | Bloqueado por falta de acceso institucional |

## 4-resultados/ — lo que vamos obteniendo

Lo que sale de procesar la evidencia. **Esta carpeta crece conforme avanza el trabajo.**

| Archivo | Estado |
|---|---|
| `CRIBADO_RESULTADO.md` | ✅ Resultado del cribado por título y resumen |
| `cribado_titulo_resumen.csv` | ✅ Decisión y motivo para cada uno de los 158 |
| *(pendiente)* `combinado_sin_duplicados.csv` | Al sumar WoS |
| *(pendiente)* `cribado_texto_completo.csv` | Etapa 2, con motivos E1-E6 por exclusión |
| *(pendiente)* `estudios_incluidos.csv` | Lista final que alimenta la Introducción |
| *(pendiente)* `diagrama_flujo_PRISMA.docx` | Plantilla v2 rellenada con los números reales |
| *(pendiente)* `checklist_27_items.docx` | Checklist cumplimentada, se entrega con el artículo |

---

## Estado actual del embudo

| Etapa | Valor |
|---|---|
| Identificados en bases de datos | **158** (Scopus) · WoS pendiente |
| Identificados por otros métodos | 9 |
| Duplicados eliminados | — *(al sumar WoS)* |
| Excluidos en cribado título/resumen | **10** |
| Buscados para recuperación | **148** |
| Evaluados en texto completo | — |
| Excluidos en texto completo, con motivo | — |
| **Estudios incluidos** | — |
