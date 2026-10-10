# Resultados del experimento

Entrenamiento ejecutado en Kaggle el **2026-10-09**, versión 5 del notebook
`agajarnold/entrenamiento-epp-yolo26`. GPU Tesla T4.

## Protocolo

Idéntico para los tres modelos — es lo que hace válida la comparación.

| Parámetro | Valor |
|---|---|
| Épocas | 50 |
| Resolución | 640 px |
| Lote | 32 |
| Optimizador | auto → AdamW (lr 0,001667) |
| Semilla | 42 |
| Paciencia | 15 |
| Dispositivo | 1 × Tesla T4 |
| Datos | 14 729 train · 4 044 val · 2 171 test |

## Tabla comparativa — evaluación sobre el conjunto de prueba

| Modelo | Papel | mAP50 | mAP50-95 | Precisión | Recall | mAP50 casco | mAP50 chaleco | Parámetros | Min. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| yolov8n | Línea base simple | 0,8415 | 0,5215 | 0,7586 | 0,8253 | 0,9170 | 0,7661 | 3 138 246 | 120,4 |
| yolo11n | Comparador directo | 0,8473 | 0,5223 | 0,7647 | 0,8316 | 0,9181 | 0,7765 | 2 605 126 | 121,9 |
| **yolo26n** | **Modelo propuesto** | **0,8592** | **0,5322** | 0,7505 | **0,8526** | **0,9251** | **0,7933** | **2 534 372** | 132,9 |

## Lectura

**YOLO26n mejora la línea base en +0,0177 de mAP50 (+2,1 %) con un 19 % menos de parámetros.**
Mejor desempeño y modelo más ligero a la vez: es el argumento central del artículo.

**La ganancia se concentra en el chaleco**, que era la clase problemática: +0,0272 sobre la
línea base, frente a +0,0081 en casco. La mejora aparece justo donde los datos eran más débiles.

**Compromiso precisión-exhaustividad.** YOLO26n tiene la precisión más baja de los tres
(0,7505 frente a 0,7647 de YOLO11n) pero el recall más alto (0,8526). Detecta más y se
equivoca algo más al hacerlo.

Para seguridad en obra ese intercambio es favorable —un casco no detectado es peor que una
falsa alarma— y conecta con el argumento de asimetría de costes del estudio de *Buildings* 2026
que está en `referencias/05_Real-Synthetic-Data-Mixing_Buildings-2026.pdf`.
**Debe declararse en la Discusión, no omitirse.**

**La brecha casco-chaleco persiste**: 0,9251 frente a 0,7933, unos 13 puntos. Es el reflejo
directo del desbalance 4,8:1 medido en los datos. Material para la sección de limitaciones.

## Archivos

| Ruta | Contenido |
|---|---|
| `resultados/entregables/comparativa_modelos.csv` | La tabla, en bruto |
| `resultados/entregables/protocolo.json` | Protocolo e hiperparámetros |
| `resultados/entregables/*_best.pt` | Pesos de los tres modelos |
| `resultados/entregables/*_results.csv` | Métricas época a época |
| `resultados/runs/<modelo>/` | Curvas de entrenamiento, matrices de confusión |
| `resultados/runs/<modelo>_test/` | Evaluación sobre el test |
| `despliegue/pesos/best.pt` | `yolo26n_best.pt`, desplegado en el VPS |

## Figuras disponibles para el artículo

En `resultados/runs/<modelo>/` y `<modelo>_test/`:

- `confusion_matrix_normalized.png` — matriz de confusión
- `results.png` — curvas de pérdida y métricas por época
- `BoxPR_curve.png` — curva precisión-exhaustividad
- `BoxF1_curve.png`, `BoxP_curve.png`, `BoxR_curve.png`
- `val_batch*_pred.jpg` — ejemplos de predicción

## Trazabilidad

Los resultados corresponden a la **versión 5** del notebook en Kaggle. El código, las salidas
y el registro completo quedan archivados ahí, y el dataset es
`agajarnold/epp-casco-chaleco-yolo26`, generado con `01_preparar_dataset.py`.
