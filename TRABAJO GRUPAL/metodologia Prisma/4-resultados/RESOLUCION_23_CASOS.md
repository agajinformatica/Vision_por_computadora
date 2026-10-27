# Resolucion individual de los 23 casos C0

Fecha: 2026-10-27. **Los 23 casos C0 quedan resueltos como incluir. Corpus: 80 incluidos y 68 excluidos de los mismos 148 registros.** No se identifica ni agrega ningun estudio nuevo. Se revoca el limite de 57 por cierre administrativo: la instruccion de no buscar mas papers no permite excluir elegibles de la lista original.

Se mantienen intactas las columnas R1/R2 y sus motivos, las discrepancias historicas y los metadatos. Esta es una adjudicacion documental asistida por IA; no constituye otro revisor humano independiente. El protocolo original I1-I7 y E1-E6 sigue vigente. No se exige que el articulo use YOLO26, no hay umbral minimo de mAP, y los estudios de dataset con benchmark original son primarios. Se aceptan metricas agregadas o mejoras relativas y clases de presencia/ausencia, tal como en los 57 previos. Tener una interfaz de alertas, pose o AR no vuelve incidental el EPP cuando el detector es un objetivo principal con evaluacion propia.

## Evidencia consultada

En estos 23 se consultaron 15 PDF locales/recuperados, 2 PDF completos por web (60 y 132), 5 copias del articulo/manuscrito de autor por web (11, 80, 87, 94 y 100) y, para 93, resumen y cuerpo de la version publicada recuperados por indexacion editorial. No se presenta el preprint SH17 como version publicada ni se afirma lectura integra del PDF publicado del ID 93. Se comprobo titulo/DOI, tarea, cajas, clases y cifra. La copia de autor de 100 conserva una cabecera provisional; publicacion y cifras se corroboraron en IEEE Access. I1 se apoya en la presencia individual en la exportacion Scopus, no en una nueva auditoria de indexacion de revistas.

Resultado por los 23: **23 incluir; 0 excluir; 0 C0 pendiente**. Una exclusion E3/E4 basada en un resumen incompleto no se mantiene frente a evidencia confirmatoria del cuerpo. El registro detallado esta en RESOLUCION_23_CASOS.csv y las decisiones anteriores se conservan en el historial.

## Recuentos y limites de reporte

| Etapa real | Registros |
|---|---:|
| Scopus identificados, sin DOI repetidos detectados | 158 |
| Excluidos en filtro inicial titulo/resumen | 10 |
| Registros preseleccionados | 148 |
| Exclusiones documentales previas conservadas en este encargo | 51 (39 E3 + 12 E4) |
| Seleccionados para recuperacion o consulta adicional | 97 |
| No evaluables en recuperacion | 17 E5 (16 no recuperados + 1 PDF truncado) |
| Con evidencia de elegibilidad evaluada | 80 |
| De ellos, secciones de texto completo PDF/HTML consultadas | 79 |
| De ellos, resumen y cuerpo publicado indexado (ID 93) | 1 |
| Excluidos adicionales tras resolver estos 23 | 0 |
| **Incluidos** | **80** |

**158 = 10 + 51 + 17 + 80; 148 = 51 + 17 + 80; 68 = 39 E3 + 12 E4 + 17 E5.** E1/E2/E6: cero. E5 se cuenta una sola vez en recuperacion, no otra vez entre textos leidos. Los 9 registros historicos de otros metodos siguen como contexto y no se suman. El ID 126 conserva E5 por PDF truncado.

Resolver C0 corrige la seleccion administrativa, pero no acredita por si solo cumplimiento integral de PRISMA 2020. Las otras 51 exclusiones documentales y 17 E5 no se reabrieron en esta tarea. No se afirma que se hayan leido 148 ni 132 textos completos ni se sustituye la validacion de revisores humanos independientes. Los dos registros sin DOI siguen sin intento exhaustivo por titulo, segun la auditoria previa. La figura es un flujo adaptado al procedimiento realmente documentado, con el ID 93 identificado como evidencia indexada. Estos limites deben mantenerse al redactar Metodos.

## Calidad y extraccion posterior

El ID 22 informa la cifra citada durante entrenamiento; no tratarla como test independiente. En 87 hay mAP 86.94% en resumen/discusion frente a 86.49% en tablas. En 125 algunas medias globales no cuadran con AP por clase. En 132 hay inconsistencias en las particiones y terminologia de mAP. En 26 los incrementos anotados en la tabla de ablacion tienen problemas de escala; se conservan los valores absolutos. Estas limitaciones se registran para evaluacion de calidad, sin inventar criterios retrospectivos de exclusion. Se mantienen tambien las observaciones previas sobre 52, 71, 81 y 122.

## Decisiones por estudio

### ID 11 — incluir

Personal protective equipment detection using YOLOv8 architecture on object detection benchmark datasets: a comparative study. DOI: 10.1080/23311916.2024.2333209.

Clases: helmet por colores; vest. Modelo: YOLOv8. Cifra: **YOLOv8x CHV mAP50=0.929; vest AP50=0.888**. Evidencia: TC copia editorial web; Tablas 2 y 3; resultados CHV.

Comparacion experimental de detectores de casco/chaleco. La cifra existe en el cuerpo aunque no en el resumen. No es revision ni mera propuesta de dataset.

[Publicacion primaria](https://doi.org/10.1080/23311916.2024.2333209). [Fuente consultada](https://www.researchgate.net/publication/379783244_Personal_protective_equipment_detection_using_YOLOv8_architecture_on_object_detection_benchmark_datasets_a_comparative_study).

### ID 12 — incluir

SHEL5K: An Extended Dataset and Benchmarking for Safety Helmet Detection. DOI: 10.3390/s22062315.

Clases: helmet; head with helmet; person with/without helmet. Modelo: YOLOv3/v4/v5, Faster R-CNN, YOLOR. Cifra: **YOLOv5x AP50 helmet=0.8896**. Evidencia: TC PDF local; Tabla 4, pagina PDF 12.

Dataset con entrenamiento y evaluacion original de detectores con cajas. Ser un articulo de dataset no es motivo E1 ni E4 cuando incluye el benchmark numerico.

[Publicacion primaria](https://doi.org/10.3390/s22062315). [Fuente consultada](Vision_por_computadora\TRABAJO GRUPAL\referencias\02_SHEL5K-Dataset-Benchmark_Sensors-2022.pdf).

### ID 21 — incluir

Automatic detection of safety helmet wearing based on head region location. DOI: 10.1049/ipr2.12231.

Clases: safety helmet. Modelo: YOLOv4 + localizacion de cabeza/OpenPose. Cifra: **Precision del metodo de uso de casco=95.1%; FP=13.7%; miss=15.8%**. Evidencia: TC PDF recuperado; Secciones 3.4 y 3.5; tabla 3.

YOLOv4 localiza el casco y el metodo evalua su uso. La pose sirve de apoyo al objetivo central de deteccion de casco; no es clasificacion de una actividad ajena.

[Publicacion primaria](https://doi.org/10.1049/ipr2.12231). [Fuente consultada](https://pdfs.semanticscholar.org/eb04/a42293343fc68cf31a0f29ad14d770a574ba.pdf).

### ID 22 — incluir

Deep Learning Technique for Object Detection from Panoramic Video Frames. DOI: 10.7763/IJCTE.2022.V14.1306.

Clases: safety helmet. Modelo: YOLOv3/Darknet-53. Cifra: **mAP del detector alrededor de 32.82% durante el entrenamiento**. Evidencia: TC PDF recuperado; Seccion IV Results and Discussion, pagina PDF 5.

Detector de casco con cajas y videos de obra. Tambien menciona trafico, pero incorpora explicitamente construccion. El protocolo no fija umbral minimo ni exige una metrica exclusiva de test. Resultado de entrenamiento marcado para calidad.

[Publicacion primaria](https://www.ijcte.org/vol14/1306-G2067.pdf). [Fuente consultada](https://www.ijcte.org/vol14/1306-G2067.pdf).

### ID 23 — incluir

Research on Safety Helmet Detection Algorithm Based on Improved YOLOv5s. DOI: 10.3390/s23135824.

Clases: safety helmet. Modelo: YOLOv5s-Improved. Cifra: **mAP50=92.4%; mAP50:95=59.2%**. Evidencia: TC PDF local; Tabla 7, pagina PDF 17.

Detector central de casco con regresion de cajas y experimento cuantitativo; la ausencia de cifras en resumen no equivale a E4.

[Publicacion primaria](https://doi.org/10.3390/s23135824). [Fuente consultada](Vision_por_computadora\TRABAJO GRUPAL\referencias\25_Helmet-Improved-YOLOv5s_Sensors-2023.pdf).

### ID 26 — incluir

DST-DETR: Image Dehazing RT-DETR for Safety Helmet Detection in Foggy Weather. DOI: 10.3390/s24144628.

Clases: safety helmet. Modelo: DST-DETR (PAOD-Net + ST-DETR). Cifra: **mAP50=0.9481; mAP50:95=0.6051**. Evidencia: TC PDF recuperado; Tablas 4 y 6, experimentos de deteccion y ablacion.

La eliminacion de niebla alimenta un detector de casco evaluado. Se usan mAP del detector y no PSNR/SSIM para inclusion.

[Publicacion primaria](https://doi.org/10.3390/s24144628). [Fuente consultada](https://mdpi-res.com/d_attachment/sensors/sensors-24-04628/article_deploy/sensors-24-04628.pdf).

### ID 36 — incluir

Detection Method for Safety Helmet Wearing on Construction Sites Based on UAV Images and YOLOv8. DOI: 10.3390/buildings15030354.

Clases: helmet; person. Modelo: YOLOv8s + UAV. Cifra: **AP50 helmet=0.968; mAP50 agregado=0.975**. Evidencia: TC PDF recuperado; Figura 8 y texto de resultados, paginas PDF 8-10.

Casco explicitamente anotado y detectado con cajas en imagenes de obras. Los emparejamientos y avisos no desplazan el objetivo de deteccion de casco.

[Publicacion primaria](https://doi.org/10.3390/buildings15030354). [Fuente consultada](https://mdpi-res.com/d_attachment/buildings/buildings-15-00354/article_deploy/buildings-15-00354.pdf).

### ID 60 — incluir

CSOD-24: Construction Site Object Detection Dataset for Safety Monitoring at Construction Site using Deep Learning. DOI: 10.36548/jiip.2025.1.009.

Clases: worker with helmet; worker without helmet. Modelo: YOLOv8 sobre CSOD-24. Cifra: **mAP50=0.982; mAP50:95=0.794; AP50:95 worker with helmet=0.666**. Evidencia: TC PDF web; Pagina PDF 20 (pagina impresa 201); seccion de validacion antes de conclusiones.

Dataset con cajas y validacion numerica propia. La deteccion de uso de casco es un objetivo explicito junto a maquinaria, no una entrada incidental a razonamiento. Se aceptan clases compuestas de trabajador con/sin casco como en el corpus previo.

[Publicacion primaria](https://doi.org/10.36548/jiip.2025.1.009). [Fuente consultada](https://irojournals.com/iroiip/article/download/775/689/1361).

### ID 80 — incluir

PPE detector: A YOLO-based architecture to detect personal protective equipment (PPE) for construction sites. DOI: 10.7717/peerj-cs.999.

Clases: hardhat de cuatro colores; vest. Modelo: YOLOX-m. Cifra: **mAP medio entre tres particiones=89.84%**. Evidencia: TC copia del articulo web; Results, tabla 4, pagina 13.

Deteccion central de EPP con cajas en construccion. El valor 89.84% es el promedio de tres combinaciones del dataset, no un unico test aislado.

[Publicacion primaria](https://doi.org/10.7717/peerj-cs.999). [Fuente consultada](https://www.researchgate.net/publication/361371242_PPE_detector_a_YOLO-based_architecture_to_detect_personal_protective_equipment_PPE_for_construction_sites).

### ID 86 — incluir

Safety Helmet Detection Based on YOLOv5 Driven by Super-Resolution Reconstruction. DOI: 10.3390/s23041822.

Clases: safety helmet. Modelo: SR residual + improved YOLOv5. Cifra: **P=88.6%; R=71.5%; AP=79.1%**. Evidencia: TC PDF local; Seccion 4.4; tabla 3, paginas PDF 10-11.

El objetivo es deteccion de casco y el detector tiene AP propio. PSNR/SSIM del resumen son metricas auxiliares, no el fundamento de inclusion.

[Publicacion primaria](https://doi.org/10.3390/s23041822). [Fuente consultada](Vision_por_computadora\TRABAJO GRUPAL\referencias\23_Helmet-YOLOv5-Super-Resolution_Sensors-2023.pdf).

### ID 87 — incluir

An improved YOLOX approach for low-light and small object detection: PPE on tunnel construction sites. DOI: 10.1093/jcde/qwad042.

Clases: helmet; vest; person. Modelo: Improved YOLOX/ConvNeXt/cuarta cabeza. Cifra: **Tabla 10: mAP=86.49%; AP helmet=90.33%; AP vest=82.12%**. Evidencia: TC copia del articulo web; Secciones 3 y 4, tablas 8-10.

Detector central de casco/chaleco para tuneles; cajas anotadas con LabelImg. Hay discrepancia interna: resumen/discusion dicen 86.94% y tablas dicen 86.49%; conservar ambos en calidad y no mezclarlos.

[Publicacion primaria](https://doi.org/10.1093/jcde/qwad042). [Fuente consultada](https://www.researchgate.net/publication/371019173_An_improved_YOLOX_approach_for_low-light_and_small_object_detection_PPE_on_tunnel_construction_sites).

### ID 92 — incluir

Effectiveness of Image Augmentation Techniques on Non-Protective Personal Equipment Detection Using YOLOv8. DOI: 10.3390/app15052631.

Clases: Non-Helmet; Non-Vest. Modelo: YOLOv8 con ViT/Swin/PVT. Cifra: **PVT brightness: AP50 Non-Helmet=68.66; Non-Vest=74.11; promedio=73.12**. Evidencia: TC PDF recuperado; Seccion 4.1.4; tablas 3 y 4, paginas PDF 13-14.

Anota regiones rectangulares de ausencia de casco/chaleco y evalua AP. Se aplica la misma aceptacion de clases de ausencia que en los 57 incluidos previos.

[Publicacion primaria](https://doi.org/10.3390/app15052631). [Fuente consultada](https://mdpi-res.com/d_attachment/applsci/applsci-15-02631/article_deploy/applsci-15-02631.pdf).

### ID 93 — incluir

SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. DOI: 10.1016/j.jnlssr.2024.09.002.

Clases: helmet; safety-vest, entre 17 clases. Modelo: YOLOv8/v9/v10. Cifra: **YOLOv9-e mAP50=70.9%**. Evidencia: Resumen y cuerpo publicado indexado; sin PDF publicado local; Resumen publicado; secciones 3 y 4, tabla 3, cuerpo editorial indexado.

Articulo primario publicado con benchmark propio de deteccion y cajas. Se usa la version de revista, no el preprint de arXiv. Scopus y el numero editorial registran 2025; el DOI contiene 2024 y no se usa ese componente para inferir el ano. Se preservan metadatos originales.

[Publicacion primaria](https://doi.org/10.1016/j.jnlssr.2024.09.002). [Fuente consultada](https://doi.org/10.1016%2Fj.jnlssr.2024.09.002).

### ID 94 — incluir

Automated PPE compliance monitoring in industrial environments using deep learning-based detection and pose estimation. DOI: 10.1016/j.autcon.2025.106231.

Clases: helmet; vest. Modelo: YOLOv7-e6 para EPP + deteccion de trabajadores y pose. Cifra: **Tabla 4: AP50 helmet=0.970; vest=0.888**. Evidencia: TC copia de autor web; Secciones 3, 4 y 5.1; tabla 4.

Detector de EPP entrenado y evaluado por separado; la pose asocia EPP con personas, manteniendo casco/chaleco como objetivo central. Astilleros y obra cumplen dominio industrial equivalente.

[Publicacion primaria](https://doi.org/10.1016/j.autcon.2025.106231). [Fuente consultada](https://www.researchgate.net/publication/391663088_Automated_PPE_compliance_monitoring_in_industrial_environments_using_deep_learning-based_detection_and_pose_estimation).

### ID 95 — incluir

Real-Time Personal Protective Equipment Non-Compliance Recognition on AI Edge Cameras. DOI: 10.3390/electronics13152990.

Clases: hard hat; personas con/sin hard hat y vest. Modelo: Detector en camaras AI edge. Cifra: **mAP IoU0.50=43%; F-score IoU0.50=52%**. Evidencia: TC PDF recuperado; Seccion 6, tabla 5 y texto de evaluacion.

Clases compuestas con cajas y clase Object: Hard hat. Su objetivo central es detectar no cumplimiento de casco/chaleco, no una conducta distinta. El protocolo no establece un piso de mAP.

[Publicacion primaria](https://doi.org/10.3390/electronics13152990). [Fuente consultada](https://mdpi-res.com/d_attachment/electronics/electronics-13-02990/article_deploy/electronics-13-02990.pdf).

### ID 100 — incluir

Real-Time Monitoring of Personal Protective Equipment Compliance in Surveillance Cameras. DOI: 10.1109/ACCESS.2024.3451117.

Clases: Helmet; NoHelmet; Vest; NoVest. Modelo: PPE-YOLO/YOLOv7; CenterNet; DAB-Deformable-DETR. Cifra: **mAP PPE-YOLO: Test I=92.36%; Test II=66.70%**. Evidencia: TC manuscrito de autor web; publicacion corroborada en IEEE; Dataset/training, tabla 3; resultados, tabla 6.

Detector central de casco/chaleco con evaluacion en dos entornos. La copia de autor tiene cabecera provisional, pero titulo/autores/resultados se corroboran con el articulo de revista IEEE Access DOI 10.1109/ACCESS.2024.3451117; no se trata como preprint sin publicar.

[Publicacion primaria](https://ieeexplore.ieee.org/abstract/document/10654263). [Fuente consultada](https://www.researchgate.net/publication/383520448_Real-Time_Monitoring_of_Personal_Protective_Equipment_Compliance_in_Surveillance_Cameras).

### ID 110 — incluir

A Fast and Robust Safety Helmet Network Based on a Mutilscale Swin Transformer. DOI: 10.3390/buildings14030688.

Clases: safety helmet. Modelo: FRSHNet/Swin Transformer. Cifra: **mAP50 Pictor-v3=0.9630; SHWD=0.9470**. Evidencia: TC PDF recuperado y HTML editorial; Seccion 3.4; tabla 1.

Detector central de casco con localizacion/regresion y pruebas en dos datasets. No se exige que todos los articulos usen YOLO26.

[Publicacion primaria](https://doi.org/10.3390/buildings14030688). [Fuente consultada](https://mdpi-res.com/d_attachment/buildings/buildings-14-00688/article_deploy/buildings-14-00688.pdf).

### ID 112 — incluir

SC-YOLO: A Real-Time CSP-Based YOLOv11n Variant Optimized with Sophia for Accurate PPE Detection on Construction Sites. DOI: 10.3390/buildings15162854.

Clases: hardhat; vest; helmet, segun dataset. Modelo: SC-YOLO/YOLOv11n + Sophia. Cifra: **VOC2007-1 mAP50=97.6%; Hardhat=96.8%; Vest=97.3%**. Evidencia: TC PDF recuperado; Secciones 4.2 y 4.3; tabla 6.

Comparacion original de detectores de EPP en obra, con cajas y resultados propios. Las clases genericas del resumen se confirman en datos y evaluacion.

[Publicacion primaria](https://doi.org/10.3390/buildings15162854). [Fuente consultada](https://mdpi-res.com/d_attachment/buildings/buildings-15-02854/article_deploy/buildings-15-02854.pdf).

### ID 115 — incluir

A deep learning-based algorithm for the detection of personal protective equipment. DOI: 10.1371/journal.pone.0322115.

Clases: helmet; vest; person. Modelo: MFD-YOLO basado en YOLOv8n. Cifra: **Tabla 3: AP50 helmet=64.8%; vest=72.3%**. Evidencia: TC PDF recuperado y HTML editorial; Experiment and results; tabla 3, pagina PDF 12.

Detector central de EPP con localizacion. Las mejoras globales del resumen y resultados por clase del cuerpo cumplen I7; no se confunden con FPS ni con cifras de otro modelo.

[Publicacion primaria](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0322115). [Fuente consultada](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0322115&type=printable).

### ID 125 — incluir

Comparative Evaluation of YOLOv11n Neck-Level Modifications for Precast Component and PPE Object Detection in Construction Environments. DOI: 10.3390/buildings16091728.

Clases: SG hardhat; vest; worker. Modelo: YOLOv11n con DSC/MSDC/FRI/DAM. Cifra: **SG mAP50=0.936-0.968; DAM hardhat AP50=0.972; vest=0.981**. Evidencia: TC PDF recuperado; Dataset SG; tablas 5 y 6.

EPP es uno de dos experimentos principales de deteccion, con entrenamiento y resultados propios; los prefabricados no convierten EPP en ingrediente incidental. La media global y AP por clase reportadas presentan incoherencias aritmeticas: registrar calidad sin inventar exclusion.

[Publicacion primaria](https://doi.org/10.3390/buildings16091728). [Fuente consultada](https://mdpi-res.com/d_attachment/buildings/buildings-16-01728/article_deploy/buildings-16-01728.pdf).

### ID 132 — incluir

INTELLIGENT WORKSITE PROTECTIVE EQUIPMENT COMPLIANCE DETECTION USING DEEP NEURAL NETWORKS. DOI: 10.5935/jetia.v12i58.3224.

Clases: hardhat/helmet; safety vest. Modelo: YOLOv8. Cifra: **mAP alrededor de 85%; P=90%; R=88%; exactitud helmet=88%, vest=94%**. Evidencia: TC PDF web; Metodologia y Result and Discussion, pagina PDF 3 (983 impresa).

La deteccion de EPP es central y se describen anotaciones con cajas y resultados del modelo. Telegram es una salida de alertas. Hay inconsistencias en tamanos de particiones y terminologia de mAP; anotarlas como calidad, no E4.

[Publicacion primaria](https://doi.org/10.5935/jetia.v12i58.3224). [Fuente consultada](https://itegam-jetia.org/journal/index.php/jetia/article/download/3224/1419/).

### ID 141 — incluir

Noninvasive Worker Safety Monitoring and Augmented Reality Feedback for Real-Time Intervention. DOI: 10.3390/safety12040090.

Clases: hardhat; no hardhat; safety vest; no safety vest. Modelo: Detector YOLO + interfaz AR. Cifra: **Test mAP50=0.763; AP50 hardhat=0.811; safety vest=0.865; no safety vest=0.404**. Evidencia: TC PDF recuperado; Seccion 3.1, tabla 1; tabla 2, pagina PDF 13.

El modelo detecta EPP con cajas y tiene evaluacion independiente del test; AR comunica las detecciones. No hay otra tarea central de razonamiento/actividad que haga incidental casco/chaleco.

[Publicacion primaria](https://doi.org/10.3390/safety12040090). [Fuente consultada](https://mdpi-res.com/d_attachment/safety/safety-12-00090/article_deploy/safety-12-00090.pdf).

### ID 142 — incluir

A Vision-Based Sensing Framework for PPE Detection and Safety Harness Compliance Recognition in High-Formwork Construction Environments Using YOLO-ILB. DOI: 10.3390/s26134147.

Clases: helmet; no-helmet; harness; no-harness; safety hook. Modelo: YOLO-ILB. Cifra: **mAP50=0.939; AP50 helmet=0.975; no-helmet=0.949**. Evidencia: TC PDF recuperado; Secciones 3 y 4; tablas 3-5, tabla 4 por clase.

La deteccion multicategoria de EPP es una contribucion principal, con casco evaluado por separado. El reconocimiento del anclaje del arnes es otra contribucion; se usan metricas del detector y no su 90.82% de cumplimiento.

[Publicacion primaria](https://doi.org/10.3390/s26134147). [Fuente consultada](https://mdpi-res.com/d_attachment/sensors/sensors-26-04147/article_deploy/sensors-26-04147.pdf).
