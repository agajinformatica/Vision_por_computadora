# Referencias — Detección de EPP con Deep Learning (Arnold)

5 artículos primarios con metodología propia, acceso abierto (gold OA), 2021–2026.
Criterio de selección: cubrir los vacíos metodológicos que no cubren las carpetas de
Javier (4 variantes YOLO, todas de *Scientific Reports* 2026) ni Eladio (revisión e informes).

---

## 1. Fast PPE Detection for Real Construction Sites Using Deep Learning Approaches
- **Autores:** Zijian Wang, Yimin Wu, Lichao Yang, Arjun Thirunavukarasu, Colin Evison, Yifan Zhao
- **Publicación:** *Sensors*, 2021, 21(10), 3478 · 22 págs.
- **DOI:** https://doi.org/10.3390/s21103478
- **Citas:** 253 (la referencia fundacional del área)
- **Metodología:** construye el dataset **CHV** (1 330 imágenes, 6 clases: casco en 4 colores,
  persona, chaleco) considerando fondo real de obra, gestos, ángulos y distancias variadas.
  Entrena y compara **8 detectores YOLO**. Mejor mAP: YOLOv5x (86.55 %); mayor velocidad:
  YOLOv5s (52 FPS en GPU). Mide además el efecto del desenfoque facial (−7 % solo en cascos).
- **Aporta al grupo:** base histórica obligada + dataset público reutilizable.

## 2. SHEL5K: An Extended Dataset and Benchmarking for Safety Helmet Detection
- **Autores:** Munkh-Erdene Otgonbold, Munkhjargal Gochoo, Fady Alnajjar, Luqman Ali,
  Tan-Hsu Tan, Jun-Wei Hsieh, Ping-Yang Chen
- **Publicación:** *Sensors*, 2022, 22(6), 2315 · 23 págs.
- **DOI:** https://doi.org/10.3390/s22062315
- **Citas:** 61
- **Metodología:** metodología de **construcción y re-anotación de dataset** (extiende el
  Safety Helmet Dataset a 5 000 imágenes, 6 clases, corrigiendo etiquetas deficientes) y
  benchmarking multi-modelo sobre esa base.
- **Aporta al grupo:** el único paper centrado en *datos y anotación*, no en arquitectura.
  Sustento directo para justificar el diseño del dataset propio.

## 3. MRC-DETR: A High-Precision Detection Model for Electrical Equipment Protection in Power Operations
- **Autores:** Shenwang Li, Yuyang Zhou, Minjie Wang, Li Liu, Thomas Wu
- **Publicación:** *Sensors*, 2025, 25(13), 4152 · 25 págs.
- **DOI:** https://doi.org/10.3390/s25134152
- **Metodología:** arquitectura **Transformer (DETR)**, no YOLO. Recalibración multiescala
  para objetos pequeños y oclusiones en EPP de operación eléctrica (PEPPE).
  mAP50:95 = 0.793 (ropa aislante) y 0.806 (chalecos).
- **Aporta al grupo:** rompe el monocultivo YOLO; permite contrastar familias de arquitectura.

## 4. PPE-EYE: A Deep Learning Approach to Personal Protective Equipment Compliance Detection
- **Autores:** Atta Rahman, Mohammed Salih Ahmed, Khaled Naif AlBugami, Abdullah Yousef Alabbad,
  Abdullah Abdulaziz AlFantoukh, Yousef Hassan Alshaikhahmed, Ziyad Saleh Alzahrani,
  Mohammad Aftab Alam Khan, Mustafa Youldash, Saeed Matar Alshahrani
- **Publicación:** *Computers*, 2026, 15(1), 45 · 19 págs.
- **DOI:** https://doi.org/10.3390/computers15010045
- **Citas:** 8
- **Metodología:** pipeline completo de **cumplimiento** (no solo detección) con YOLO11x.
  mAP50 = 96.9 %, inferencia de 7.3 ms.
- **Aporta al grupo:** estado del arte 2026 orientado a *compliance*, que es el enfoque del trabajo.

## 5. A Fixed-Budget Study of Real–Synthetic Data Mixing for PPE Detection in Construction
- **Autores:** Ziqi Zhang, Yu Zhang, Kazuya Shide
- **Publicación:** *Buildings*, 2026, 16(10), 2034 · 20 págs. (publicado 20 may 2026)
- **DOI:** https://doi.org/10.3390/buildings16102034
- **Citas:** 0 — muy reciente; su valor es argumental, no bibliométrico.
- **Metodología:** el **diseño experimental más fuerte del conjunto**. Compara 11 ratios de
  mezcla datos reales/sintéticos bajo **presupuesto fijo** por configuración, con 3 detectores
  (YOLOv11s, Faster R-CNN, RT-DETR-L). Argumenta usar **AR@100** en vez de mAP porque en
  seguridad el falso negativo tiene costo asimétrico. Pico de rendimiento con 90 % real / 10 % sintético.
- **Aporta al grupo:** la munición para justificar *por qué* se eligió determinada métrica y
  partición de datos — justo lo que se pregunta en la sustentación.

---

## Resumen

| # | Año | Revista | Contribución metodológica | Citas |
|---|-----|---------|---------------------------|-------|
| 1 | 2021 | Sensors | Dataset CHV + benchmark de 8 YOLO | 253 |
| 2 | 2022 | Sensors | Construcción y re-anotación de dataset | 61 |
| 3 | 2025 | Sensors | Arquitectura Transformer (DETR) | 4 |
| 4 | 2026 | Computers | Pipeline de cumplimiento, YOLO11x | 8 |
| 5 | 2026 | Buildings | Diseño experimental: mezcla real/sintético, métrica AR@100 | 0 |

Todos verificados como artículos primarios (sin revisiones), acceso abierto gold,
descargados desde el editor (MDPI) el 2026-10-09.
