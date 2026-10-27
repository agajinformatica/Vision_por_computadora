# Dataset · cómo conseguirlo

El repositorio **no incluye las imágenes**. Los datos crudos son 6,1 GB (93 578
archivos) y tres de sus `.zip` superan el límite de 100 MB por archivo de
GitHub, así que un `git push` sería rechazado. Esta página explica las dos vías
para tenerlos.

## Vía 1 · Kaggle (recomendada, es donde se entrena)

El conjunto ya unificado está publicado como Kaggle Dataset:

    agajarnold/epp-casco-chaleco-yolo26

Es el mismo que usó el entrenamiento de `RESULTADOS.md` (50 épocas, Tesla T4,
2026-10-09). Se añade al notebook `03_entrenamiento_kaggle.ipynb` con *Add
Input* y queda montado en `/kaggle/input/`, que es de solo lectura — por eso el
notebook reescribe el `data.yaml` en `/kaggle/working`.

> **Acceso:** el dataset está en privado. Pide a @agajinformatica que te lo
> comparta o que lo haga público; con la cuenta sin permiso, *Add Input* no lo
> encuentra.

Ventaja: no descargas nada a tu equipo y entrenas con la GPU gratuita de Kaggle.

## Vía 2 · Regenerarlo desde las fuentes

Descarga las tres fuentes originales en `TRABAJO GRUPAL/dataset/`, respetando
estos nombres de carpeta, que son los que espera el script:

| Carpeta | Fuente | Licencia |
|---|---|---|
| `Personal Protective Equipment - Combined Model.v8i.yolo26/` | Roboflow Universe, PPE Combined Model v8 | CC BY 4.0 |
| `Construction-PPE/` | Construction-PPE, Ultralytics | AGPL-3.0 |
| `CHV/CHV_dataset/` | CHV — Wang et al., *Sensors* 2021, 21(10) 3478 | ver DOI 10.3390/s21103478 |

Luego:

```bash
cd "TRABAJO GRUPAL/experimento"
python3 01_preparar_dataset.py          # unifica a 2 clases: 0=casco, 1=chaleco
./02_empaquetar_para_kaggle.sh          # genera el .zip de 1,6 GB para subir a Kaggle
```

`01_preparar_dataset.py` remapea las clases de cada fuente, descarta las
imágenes sin casco ni chaleco y **conserva las particiones originales** de cada
dataset: no reparticiona, para no mezclar imágenes que los autores separaron a
propósito. Crea enlaces simbólicos en vez de copiar, así que
`dataset_unificado/` ocupa 23 MB en disco aunque su contenido real sea 1,6 GB —
`02_empaquetar_para_kaggle.sh` sigue los enlaces al comprimir.

Deja en `dataset_unificado/` tres archivos de trazabilidad:

- `data.yaml` — configuración para Ultralytics
- `estadisticas.json` — conteos por fuente y partición
- `manifiesto.csv` — cada imagen final mapeada a su archivo de origen

## Lo que debe salir

| Partición | Imágenes |
|---|---|
| train | 14 729 |
| val | 4 044 |
| test | 2 171 |
| **total** | **20 944** |

47 700 cascos y 9 850 chalecos — razón 4,84:1. Ese desbalance entre las dos
clases importa al leer los resultados por clase.

Si tus cifras no coinciden, revisa que las tres carpetas tengan los nombres
exactos de la tabla; el script salta en silencio las fuentes que no encuentra.

## Nota sobre licencias

Las tres fuentes no comparten licencia: una es CC BY 4.0, otra AGPL-3.0 y la
tercera es un dataset académico con su propio DOI. El conjunto derivado se
publicó en Kaggle etiquetado como CC BY 4.0, lo cual **no recoge la condición
AGPL-3.0** de Construction-PPE. Para uso académico del curso no es un problema
práctico, pero conviene resolverlo antes de redistribuir el conjunto fuera del
grupo o de publicarlo con el paper.
