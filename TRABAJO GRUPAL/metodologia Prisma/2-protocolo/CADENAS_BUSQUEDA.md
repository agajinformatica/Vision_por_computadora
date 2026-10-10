# Cadenas de búsqueda — Scopus y Web of Science

> Documento operativo. Las cadenas están listas para **pegar tal cual** en cada base.
> La ejecución requiere acceso institucional UNMSM; el registro de resultados lo completa
> quien ejecute la búsqueda.

Protocolo: ver [PROTOCOLO_REVISION.md](PROTOCOLO_REVISION.md)
Reporte de la búsqueda: seguir PRISMA-S (`../1-metodo/PRISMA-S_extension_busquedas_SystRev_2021.pdf`)

---

## Bloques conceptuales

La pregunta de revisión se descompone en cuatro bloques, unidos por AND:

| Bloque | Concepto | Términos |
|---|---|---|
| A | EPP objetivo | safety helmet, hard hat, hardhat, safety vest, high-visibility vest, personal protective equipment, PPE |
| B | Tarea | detect*, recognit*, object detection |
| C | Dominio | construction, worksite, construction site, building site |
| D | Técnica | deep learning, neural network, YOLO, convolutional, transformer |

Dentro de cada bloque los términos van con OR; entre bloques, AND.

---

## SCOPUS

```
TITLE-ABS-KEY (
    ( "safety helmet" OR "hard hat" OR hardhat OR "safety vest"
      OR "high-visibility vest" OR "personal protective equipment" OR PPE )
AND ( detect* OR recognit* OR "object detection" )
AND ( construction OR worksite OR "construction site" OR "building site" )
AND ( "deep learning" OR "neural network" OR YOLO OR convolutional OR transformer )
)
AND PUBYEAR > 2020 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) )
AND ( LIMIT-TO ( LANGUAGE , "English" ) OR LIMIT-TO ( LANGUAGE , "Spanish" ) )
```

- `DOCTYPE "ar"` = solo artículo de revista. **Si el docente admite congresos**, añadir
  `OR LIMIT-TO ( DOCTYPE , "cp" )`.
- Exportar en **CSV o BibTeX** con: autores, título, año, fuente, DOI, resumen, citas.

## WEB OF SCIENCE

```
TS=(
    ( "safety helmet" OR "hard hat" OR hardhat OR "safety vest"
      OR "high-visibility vest" OR "personal protective equipment" OR PPE )
AND ( detect* OR recognit* OR "object detection" )
AND ( construction OR worksite OR "construction site" OR "building site" )
AND ( "deep learning" OR "neural network" OR YOLO OR convolutional OR transformer )
)
```

Refinar después con los filtros de la interfaz:
- **Publication Years:** 2021-2026
- **Document Types:** Article
- **Languages:** English, Spanish
- **Editions:** SCI-EXPANDED, SSCI, ESCI *(decidir cuáles cuentan como "alto impacto")*

Exportar en **BibTeX** o *Tab-delimited*.

`TS=` busca en título, resumen, palabras clave de autor y Keywords Plus.

---

## Registro obligatorio por base (lo exige PRISMA-S)

Completar al ejecutar. Sin estos datos el diagrama de flujo no es reproducible:

| Campo | Scopus | Web of Science |
|---|---|---|
| Plataforma y proveedor | | |
| Fecha de ejecución | | |
| Cadena exacta usada | | |
| Filtros aplicados | | |
| **Nº de resultados** | | |
| Formato de exportación | | |
| Quién ejecutó | | |

---

## Qué hacer con las 16 referencias ya descargadas

**No se descartan.** Al ejecutar la búsqueda definitiva ocurrirá una de dos cosas con cada una:

1. **Aparece en los resultados** → se cuenta como identificada por base de datos.
   Es lo esperable: todas están en revistas indexadas y responden a los términos.
   El PDF ya descargado ahorra el paso de recuperación.
2. **No aparece** → entra por la columna de **"otros métodos"** del diagrama de flujo,
   que es exactamente para lo que existe esa columna.

En ambos casos el PDF sirve. Lo que hay que rehacer es **el registro de la búsqueda**,
no la recolección.

---

## Verificación de indexación de las revistas

Comprobar cada revista antes de darla por válida bajo el criterio I1. Son gratuitos:

- **Scopus:** https://www.scopus.com/sources — busca por título o ISSN; muestra si está
  activa en Scopus y su CiteScore.
- **Web of Science:** https://mjl.clarivate.com — Master Journal List; indica la edición
  (SCIE, SSCI, ESCI) en la que está indexada.
- **Cuartil:** https://www.scimagojr.com — SJR por área, útil para sustentar "alto impacto".

Revistas a verificar en el inventario actual: Sensors, Applied Sciences, Scientific Reports,
Remote Sensing, Buildings, Sustainability, Computers, IEEE Access, Intelligent Automation &
Soft Computing, IJERPH, Artificial Intelligence Review, Automation in Construction,
PeerJ Computer Science, Journal of Computational Design and Engineering.

> **Ojo con ESCI.** Si una revista está solo en ESCI y no en SCIE, puede discutirse si
> cuenta como "alto impacto". Conviene preguntarlo junto con la consulta sobre congresos.
