# Cribado R2 — evidencia y alcance

Fecha: 2026-10-26. Revisor: asistente de IA por instrucción del equipo.

## Resultado

148 registros: **95 incluir**, **53 excluir**.

| Código | Exclusiones |
|---|---:|
| E1 | 0 |
| E2 | 0 |
| E3 | 50 |
| E4 | 3 |
| E5 | 0 |
| E6 | 0 |

## Protocolo aplicado

Fuente base: INSTRUCCIONES_CRIBADO.md e I1–I7. Prevalece la instrucción del usuario del 26 de octubre: E3 ampliado a tarea incidental/fuera de alcance y criterio estricto de clase explícita + cifra del detector + tarea central de detección con cajas. Una mejora relativa numérica cuenta; FPS, tamaño del dataset, PSNR/SSIM o R² de un ajuste no sustituyen una métrica de desempeño del detector.

E1: publicación no primaria/revisada; E2: sensores sin visión; E3: clase/tarea fuera de alcance o no confirmada; E4: cifra de desempeño no confirmada; E5: texto completo inaccesible; E6: duplicado dentro de los 148. Cuando faltan tanto clase como cifra se prioriza E3. No se aplica E5 automáticamente al fallar una descarga: conforme al criterio operativo pedido, se decide por E3/E4 según la evidencia del resumen y las secciones recuperadas.

Los metadatos Scopus identifican los 148 como Article, en inglés, de 2021–2026. No se hallaron DOI repetidos entre los registros con DOI. Esto no constituye una verificación editorial independiente de la indexación de cada revista.

## Independencia y límites

Durante este pase no se imprimieron ni consultaron para decidir decision_R1/motivo_R1 ni las notas de R1. La extracción de evidencia conservó únicamente id, título, DOI, resumen, palabras clave y metadatos. La edición/validación preservó todas las otras celdas sin utilizar sus valores para decidir.

Limitación de cegamiento: esta conversación ya contenía antes del encargo un resumen de R1 y sus notas. No es posible garantizar cegamiento retrospectivo absoluto del mismo asistente. Las decisiones aquí se justifican por evidencia bibliográfica y el protocolo estricto solicitado; para independencia humana formal hace falta revisión por una persona que no haya visto R1.

Este es un pase mixto: resúmenes, secciones de PDF/HTML completos y fragmentos indexados. No se declara lectura de 148 textos completos. TC significa consulta de secciones pertinentes del texto completo, no lectura exhaustiva de cada página; INDEX significa evidencia del cuerpo obtenida vía buscador sin recuperación íntegra; PREVIEW/ficha no se cuenta como texto completo.

No se calculan discrepancias ni decisiones finales. Los campos discrepancia, decision_final y motivo_final quedan exactamente como estaban. Las inclusiones/exclusiones son juicios R2, pendientes de conciliación y R3.

## Casos con consulta adicional

| ID del cribado | Nivel de evidencia | Sección / dato comprobado | Fuente |
|---:|---|---|---|
| 11 | TC web | Tabla 3, p. 8: YOLOv8x/CHV mAP50=0,929; casco/chaleco y cajas confirmados. | [https://repository.enu.kz/bitstream/handle/enu/16444/PERSON~1.PDF?isAllowed=y&sequence=1](https://repository.enu.kz/bitstream/handle/enu/16444/PERSON~1.PDF?isAllowed=y&sequence=1) |
| 12 | TC PDF local | Tablas 3 y 4: clases casco y cabeza con casco; YOLOv5x, AP de casco=0,8896. Es dataset con evaluación empírica de detectores. | referencias/02_SHEL5K-Dataset-Benchmark_Sensors-2022.pdf |
| 21 | TC web | Tabla 3: precisión 95,1%; métodos localizan región de casco con YOLOv4. | [https://pdfs.semanticscholar.org/eb04/a42293343fc68cf31a0f29ad14d770a574ba.pdf](https://pdfs.semanticscholar.org/eb04/a42293343fc68cf31a0f29ad14d770a574ba.pdf) |
| 22 | TC web | p. 5: mAP del detector de casco alrededor de 32,82%; imágenes y método con cajas confirmados. | [https://www.ijcte.org/vol14/1306-G2067.pdf](https://www.ijcte.org/vol14/1306-G2067.pdf) |
| 23 | TC PDF local | Tabla 7: YOLOv5s-Improved, mAP0.5=92,4%; mAP0.5:0.95=59,2%. | referencias/25_Helmet-Improved-YOLOv5s_Sensors-2023.pdf |
| 26 | INDEX cuerpo editorial | Tabla 6: DST-DETR mAP@0.5=0,9481 en múltiples niveles de niebla; el resumen confirma casco y detección. | [https://www.mdpi.com/1424-8220/24/14/4628](https://www.mdpi.com/1424-8220/24/14/4628) |
| 29 | TC web | Secciones 3 y 4 y tablas 2-5: clasificación DCNN/RF; no se usa su exactitud de clasificación como métrica de detector de casco con cajas. | [https://www.jstage.jst.go.jp/article/jaciii/25/1/25_40/_pdf](https://www.jstage.jst.go.jp/article/jaciii/25/1/25_40/_pdf) |
| 36 | INDEX cuerpo editorial | Conclusiones: mAP@0.5=0,975; objetivo detector de casco con YOLOv8 y UAV. | [https://www.mdpi.com/2075-5309/15/3/354](https://www.mdpi.com/2075-5309/15/3/354) |
| 37 | TC PDF local | Sección 3.1: detección/seguimiento de trabajadores y reconocimiento de atributos; tabla 3 evalúa atributos. | referencias/31_Helmet-Harness-Remote-Vision_RemoteSens-2023.pdf |
| 51 | PREVIEW editorial | Solo resumen; no cifra concreta de desempeño recuperada. | [https://www.tandfonline.com/doi/full/10.1080/09720529.2021.2011109](https://www.tandfonline.com/doi/full/10.1080/09720529.2021.2011109) |
| 60 | INDEX PDF editorial | El PDF indexado reporta mAP@0.5=0,982 y mAP@0.5:0.95=0,794; también resultados Worker With Helmet. La recuperación directa redirige a una ficha; no se afirma lectura íntegra. | [https://irojournals.com/iroiip/article/pdf/7/1/9](https://irojournals.com/iroiip/article/pdf/7/1/9) |
| 62 | PREVIEW editorial | Título y primera página aluden a casco/chaleco; resumen genérico y sin métodos/taxonomía recuperados. Se conserva exclusión estricta por clase no confirmada en la evaluación. | [https://www.researchgate.net/publication/392529527_AF-YOLOv8_a_lightweight_algorithm_suitable_for_helmet_and_vest_detection](https://www.researchgate.net/publication/392529527_AF-YOLOv8_a_lightweight_algorithm_suitable_for_helmet_and_vest_detection) |
| 80 | INDEX texto primario PMC | Sección Results y tabla 4: YOLOX-m mAP=89,84%; clases de casco por colores y chaleco. Acceso directo a PMC/PeerJ bloqueado, evidencia consultada mediante indexación del cuerpo. | [https://pmc.ncbi.nlm.nih.gov/articles/PMC9299268/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9299268/) |
| 84 | Consulta web sin TC | La búsqueda no permitió confirmar las clases concretas del detector. Decisión fundada en el resumen. | [https://doi.org/10.1007/s11042-021-11280-6](https://doi.org/10.1007/s11042-021-11280-6) |
| 86 | TC PDF local | Tabla 3: módulo SR + YOLOv5 mejorado, precisión 88,6%, recall 71,5%, AP 79,1%; PSNR/SSIM del resumen no son la evidencia de inclusión. | referencias/23_Helmet-YOLOv5-Super-Resolution_Sensors-2023.pdf |
| 87 | TC web, copia del artículo | Sección 4: PPE dark con helmet, vest, person; datos anotados con LabelImg. Resumen: mAP 86,94%. | [https://www.researchgate.net/publication/371019173_An_improved_YOLOX_approach_for_low-light_and_small_object_detection_PPE_on_tunnel_construction_sites](https://www.researchgate.net/publication/371019173_An_improved_YOLOX_approach_for_low-light_and_small_object_detection_PPE_on_tunnel_construction_sites) |
| 88 | TC web | Métodos distinguen segmentación de instancias de las cajas; aunque confirma casco y chaleco y da mAP50=66,4, no satisface la tarea estricta de I4. | [https://academic.oup.com/jcde/article/10/2/905/7069329](https://academic.oup.com/jcde/article/10/2/905/7069329) |
| 89 | PREVIEW editorial | PPE genérico y sin cifra; no se recuperó el cuerpo para confirmar clases/resultados. | [https://www.sciencedirect.com/science/article/pii/S0957417421008617](https://www.sciencedirect.com/science/article/pii/S0957417421008617) |
| 92 | TC web | Tabla 4: Non-Helmet y Non-Vest; AP50 de Non-Helmet=68,66 con PVT/brillo y media=73,12. Se confirman clases y cifra ausentes del resumen. | [https://mdpi-res.com/d_attachment/applsci/applsci-15-02631/article_deploy/applsci-15-02631.pdf](https://mdpi-res.com/d_attachment/applsci/applsci-15-02631/article_deploy/applsci-15-02631.pdf) |
| 94 | TC web, copia de autor | Tabla 4: casco AP50=0,970; chaleco AP50=0,888; métrica del detector separada de clasificación de cumplimiento. | [https://www.researchgate.net/publication/391663088_Automated_PPE_compliance_monitoring_in_industrial_environments_using_deep_learning-based_detection_and_pose_estimation](https://www.researchgate.net/publication/391663088_Automated_PPE_compliance_monitoring_in_industrial_environments_using_deep_learning-based_detection_and_pose_estimation) |
| 95 | TC web, copia del artículo | Métodos: cajas de trabajadores con casco/chaleco y tabla 5: mAP50=43%, F-score=52% tras extender dataset. | [https://www.researchgate.net/publication/382672400_Real-Time_Personal_Protective_Equipment_Non-Compliance_Recognition_on_AI_Edge_Cameras](https://www.researchgate.net/publication/382672400_Real-Time_Personal_Protective_Equipment_Non-Compliance_Recognition_on_AI_Edge_Cameras) |
| 97 | TC web | Artículo abierto: detector RFA-YOLO localiza casco, persona y ropa; se consultaron objetivo y método. El resumen reporta exactitud global 93,1%. | [https://link.springer.com/article/10.1007/s40747-023-01028-0](https://link.springer.com/article/10.1007/s40747-023-01028-0) |
| 98 | Ficha editorial | La ficha describe 9 clases sin enumerar casco/chaleco; no se infiere la taxonomía desde Roboflow. | [https://www.sciopen.com/article/10.26599/JIC.2024.9180037](https://www.sciopen.com/article/10.26599/JIC.2024.9180037) |
| 99 | PREVIEW editorial | Solo resumen con cifras y PPE genérico; taxonomía no confirmada. | [https://link.springer.com/article/10.1007/s13369-023-08700-0](https://link.springer.com/article/10.1007/s13369-023-08700-0) |
| 100 | TC web, copia del artículo | Métodos: Helmet, NoHelmet, Vest, NoVest; tabla 6: PPE-YOLO mAP 92,36 y 66,70 en dos tests. | [https://www.researchgate.net/publication/383520448_Real-Time_Monitoring_of_Personal_Protective_Equipment_Compliance_in_Surveillance_Cameras](https://www.researchgate.net/publication/383520448_Real-Time_Monitoring_of_Personal_Protective_Equipment_Compliance_in_Surveillance_Cameras) |
| 105 | PREVIEW editorial | Resumen y destacados; no se recuperaron cifras de exactitud ni taxonomía de resultados. | [https://www.tandfonline.com/doi/abs/10.1080/15623599.2023.2171836](https://www.tandfonline.com/doi/abs/10.1080/15623599.2023.2171836) |
| 107 | TC web | Secciones de anotación/métodos y métricas consultadas: cajas y PPE genérico, sin clase casco/chaleco explícita en el texto recuperado. | [https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2023.1225478/pdf](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2023.1225478/pdf) |
| 110 | INDEX cuerpo editorial | Introducción/aporte y resultados: mAP 96,30% Pictor-v3 y 94,70% SHWD para detector de casco. | [https://www.mdpi.com/2075-5309/14/3/688](https://www.mdpi.com/2075-5309/14/3/688) |
| 112 | TC web | Tabla 1, fila This study, y metodología: Boots, Glass, Gloves, Helmet, Person, Vest; mAP50=96,3–97,6%. | [https://mdpi-res.com/d_attachment/buildings/buildings-15-02854/article_deploy/buildings-15-02854.pdf](https://mdpi-res.com/d_attachment/buildings/buildings-15-02854/article_deploy/buildings-15-02854.pdf) |
| 115 | TC HTML + INDEX tabla primaria | Secciones Experiment and results y tabla 3: casco mAP50=64,8%; chaleco=72,3% con MFD-YOLO. Tabla numérica recuperada por indexación del PDF primario. | [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0322115](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0322115) |
| 121 | PDF localizado, TC no recuperado | PDF IAENG localizado; intentos de apertura agotaron el tiempo de espera. No se confirmó cifra. | [https://www.iaeng.org/IJCS/issues_v52/issue_10/IJCS_52_10_11.pdf](https://www.iaeng.org/IJCS/issues_v52/issue_10/IJCS_52_10_11.pdf) |
| 123 | INDEX cuerpo editorial | Sección 3.2 y conclusiones: detector de casco con mAP50=0,9679, pero el objetivo/novedad declarados son asesoramiento con LLM; exclusión E3 por tarea central. | [https://www.mdpi.com/2078-2489/16/10/824](https://www.mdpi.com/2078-2489/16/10/824) |
| 124 | Búsqueda sin TC confirmatorio | Se localizó referencia a un número de revista, sin recuperar el artículo completo para confirmar clases y cifras. |  |
| 125 | INDEX cuerpo editorial | Tabla comparativa, fila This study: SG hardhat, vest, worker, mAP50 PPE=93,6–96,8%. PPE es uno de los dos objetivos experimentales de detección, no una entrada incidental de un sistema de razonamiento. | [https://www.mdpi.com/2075-5309/16/9/1728](https://www.mdpi.com/2075-5309/16/9/1728) |
| 127 | Ficha/resumen editorial | Resumen disponible; no clases explícitas de casco/chaleco. | [https://ascelibrary.com/toc/jcemd4/152/8](https://ascelibrary.com/toc/jcemd4/152/8) |
| 131 | PREVIEW | Resumen y vista pública localizados; no confirmación de clases de la evaluación. | [https://doi.org/10.1007/s00371-025-04233-9](https://doi.org/10.1007/s00371-025-04233-9) |
| 132 | TC web | p. 3, resultados: mAP alrededor de 85%, recall 88%, precisión 90%; exactitud casco 88%, chaleco 94%; anotaciones con cajas. | [https://itegam-jetia.org/journal/index.php/jetia/article/download/3224/1419/](https://itegam-jetia.org/journal/index.php/jetia/article/download/3224/1419/) |
| 133 | Ficha/resumen editorial | No taxonomía ni cifras concretas en evidencia recuperada. | [https://www.sciencedirect.com/science/article/pii/S1051200426002691](https://www.sciencedirect.com/science/article/pii/S1051200426002691) |
| 134 | Búsqueda sin TC confirmatorio | DOI/título localizados en índices, sin cuerpo que confirme clases. | [https://doi.org/10.32738/JEPPM-2026-147](https://doi.org/10.32738/JEPPM-2026-147) |
| 135 | Ficha y acceso editorial fallido | Ficha de autores y resumen; apertura del artículo dio 403. No se infieren clases desde CSSID. | [https://scholar.its.ac.id/en/publications/adaptive-feature-concatenation-in-yolov8n-for-construction-site-s/](https://scholar.its.ac.id/en/publications/adaptive-feature-concatenation-in-yolov8n-for-construction-site-s/) |
| 137 | PREVIEW editorial, no TC publicado | La disponibilidad de datos nombra SHWD; no se considera sustituto de métodos/clases. Se encontró preprint vinculado con valores diferentes y no se mezcló con la versión publicada. | [https://link.springer.com/article/10.1007/s00530-026-02574-6](https://link.springer.com/article/10.1007/s00530-026-02574-6) |
| 141 | INDEX cuerpo editorial | Sección 3.1 y tabla 2: mAP test=0,763 y AP no safety vest=0,404; cajas, casco/chaleco y evaluación propia del detector. AR es la interfaz del detector de PPE, sin otra tarea de riesgo/razonamiento. | [https://www.mdpi.com/2313-576X/12/4/90](https://www.mdpi.com/2313-576X/12/4/90) |
| 142 | INDEX cuerpo editorial | Sección de dataset: helmet, no-helmet, harness, no-harness, safety hook; detector YOLO-ILB con mAP50=0,939. Detección multicategoría es objetivo explícito junto a cumplimiento del arnés. | [https://www.mdpi.com/1424-8220/26/13/4147](https://www.mdpi.com/1424-8220/26/13/4147) |
| 148 | Consulta web sin TC confirmatorio | No se recuperó texto completo que confirme clases y cifra de desempeño del detector. | [https://doi.org/10.7717/peerj-cs.3891](https://doi.org/10.7717/peerj-cs.3891) |

## Registro individual de R2

| ID | Decisión R2 | Código | Justificación / alcance |
|---:|---|---|---|
| 1 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 2 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 3 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 4 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 5 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 6 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 7 | excluir | E3 | Objetivo central: clasificar conductas de uso mediante series temporales y 1D-CNN; 0,9467 corresponde a conductas, no al detector de casco. |
| 8 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 9 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 10 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 11 | incluir |  | Tabla 3, p. 8: YOLOv8x/CHV mAP50=0,929; casco/chaleco y cajas confirmados. |
| 12 | incluir |  | Tablas 3 y 4: clases casco y cabeza con casco; YOLOv5x, AP de casco=0,8896. Es dataset con evaluación empírica de detectores. |
| 13 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 14 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 15 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 16 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 17 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 18 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 19 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 20 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 21 | incluir |  | Tabla 3: precisión 95,1%; métodos localizan región de casco con YOLOv4. |
| 22 | incluir |  | p. 5: mAP del detector de casco alrededor de 32,82%; imágenes y método con cajas confirmados. |
| 23 | incluir |  | Tabla 7: YOLOv5s-Improved, mAP0.5=92,4%; mAP0.5:0.95=59,2%. |
| 24 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 25 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 26 | incluir |  | Tabla 6: DST-DETR mAP@0.5=0,9481 en múltiples niveles de niebla; el resumen confirma casco y detección. |
| 27 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 28 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 29 | excluir | E3 | El texto consultado evalúa principalmente clasificación de imágenes mediante DCNN y random forest; no confirma detección del casco con cajas y una métrica propia de localización. |
| 30 | excluir | E3 | El objetivo central es identificar intrusiones/autorización por el color del casco; además no hay cifra del detector en el resumen. |
| 31 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 32 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 33 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 34 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 35 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 36 | incluir |  | Conclusiones: mAP@0.5=0,975; objetivo detector de casco con YOLOv8 y UAV. |
| 37 | excluir | E3 | El aporte es reconocimiento de atributos/estado de seguridad sobre trabajadores detectados, no localización de casco con cajas. El texto completo confirma esta distinción. |
| 38 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 39 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 40 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 41 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 42 | excluir | E3 | Reconocimiento de gestos e interacción con maquinaria; el casco sirve para autorizar al operador. |
| 43 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 44 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 45 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 46 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 47 | excluir | E3 | Clasificación del uso correcto mediante cápsulas y relación espacial; el resumen no confirma un detector de casco con cajas ni cifra de ese detector. |
| 48 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 49 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 50 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 51 | excluir | E4 | El resumen menciona precisión/recall cualitativos sin valores; la página editorial accesible repite el resumen y no permitió confirmar cifras de resultados. |
| 52 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 53 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 54 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 55 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 56 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 57 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 58 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 59 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 60 | incluir |  | El PDF indexado reporta mAP@0.5=0,982 y mAP@0.5:0.95=0,794; también resultados Worker With Helmet. La recuperación directa redirige a una ficha; no se afirma lectura íntegra. |
| 61 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 62 | excluir | E3 | El resumen usa PPE genérico. El título sugiere casco/chaleco y la vista previa los menciona como contexto, pero no se recuperaron métodos/clases para confirmar los objetos efectivamente detectados según la regla estricta. |
| 63 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 64 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 65 | excluir | E3 | La contribución central es gestión remota de calidad mediante PDCA y modelado 3D; el detector de casco es un componente secundario. |
| 66 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 67 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 68 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 69 | excluir | E4 | El registro exacto presenta un dataset con casco y anotaciones, pero el resumen no reporta ninguna cifra de desempeño de un detector. No se equipara automáticamente con otro artículo/dataset de nombre similar hallado en la web. |
| 70 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 71 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 72 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 73 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 74 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 75 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 76 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 77 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 78 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 79 | excluir | E3 | El resumen especifica clasificación de imágenes VGG16, no detección de casco con cajas delimitadoras. |
| 80 | incluir |  | Sección Results y tabla 4: YOLOX-m mAP=89,84%; clases de casco por colores y chaleco. Acceso directo a PMC/PeerJ bloqueado, evidencia consultada mediante indexación del cuerpo. |
| 81 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 82 | excluir | E3 | Identificación de peligros por razonamiento con grafos de escena; PPE genérico y métricas de identificación de peligros, no detector específico de casco/chaleco. |
| 83 | excluir | E3 | Sistema de identificación de peligros que combina trabajadores, PPE, maquinaria y clima; el resumen no confirma casco/chaleco como clases ni cifra de su detector. |
| 84 | excluir | E3 | El resumen combina fuego, PPE y evacuación sin identificar casco/chaleco entre los objetos detectados; no se confirmó la clase en texto completo. |
| 85 | excluir | E3 | Objetivo central: predecir gravedad del riesgo/estado del trabajador con postura, actividad, herramientas y peligros. Las cifras corresponden a gravedad, no a detección de casco/chaleco. |
| 86 | incluir |  | Tabla 3: módulo SR + YOLOv5 mejorado, precisión 88,6%, recall 71,5%, AP 79,1%; PSNR/SSIM del resumen no son la evidencia de inclusión. |
| 87 | incluir |  | Sección 4: PPE dark con helmet, vest, person; datos anotados con LabelImg. Resumen: mAP 86,94%. |
| 88 | excluir | E3 | El texto completo define explícitamente una propuesta de segmentación por instancias/píxeles, diferenciada de la detección por cajas exigida en I4. |
| 89 | excluir | E3 | El resumen no especifica casco/chaleco como clases y tampoco ofrece cifra concreta; no se recuperó texto que cierre esas dos ambigüedades. Se aplica primero E3. |
| 90 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 91 | excluir | E3 | Integración lingüística y visual con razonamiento normativo para identificar peligros; no detector central de casco/chaleco. |
| 92 | incluir |  | Tabla 4: Non-Helmet y Non-Vest; AP50 de Non-Helmet=68,66 con PVT/brillo y media=73,12. Se confirman clases y cifra ausentes del resumen. |
| 93 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 94 | incluir |  | Tabla 4: casco AP50=0,970; chaleco AP50=0,888; métrica del detector separada de clasificación de cumplimiento. |
| 95 | incluir |  | Métodos: cajas de trabajadores con casco/chaleco y tabla 5: mAP50=43%, F-score=52% tras extender dataset. |
| 96 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 97 | incluir |  | Artículo abierto: detector RFA-YOLO localiza casco, persona y ropa; se consultaron objetivo y método. El resumen reporta exactitud global 93,1%. |
| 98 | excluir | E3 | El resumen describe PPE genérico y entrada a zonas peligrosas; no confirma casco/chaleco entre las nueve clases del detector. |
| 99 | excluir | E3 | El resumen confirma detector y cifras, pero no identifica casco/chaleco como clases. La vista previa editorial no permitió verificar la taxonomía. |
| 100 | incluir |  | Métodos: Helmet, NoHelmet, Vest, NoVest; tabla 6: PPE-YOLO mAP 92,36 y 66,70 en dos tests. |
| 101 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 102 | excluir | E3 | El resumen describe PPE genérico, segmentación y detección de trabajadores con/sin PPE; no confirma casco/chaleco como objetos detectados con cajas. |
| 103 | excluir | E3 | Detección de anomalías de comportamiento mediante GAN; no detección central de casco/chaleco. |
| 104 | excluir | E3 | El objetivo central es VQA, interpretación normativa y generación de informes; la detección de PPE es un componente de ese sistema. |
| 105 | excluir | E3 | El resumen no identifica las clases casco/chaleco y solo da velocidad, no cifra de exactitud del detector. No se recuperaron resultados completos; prioridad E3. |
| 106 | excluir | E3 | Extracción de información normativa y grafos de escena para identificar peligros; no detector central de casco/chaleco. |
| 107 | excluir | E3 | Las secciones de datos y métodos consultadas describen PPE y cajas genéricas, pero no especifican casco/helmet/hardhat ni chaleco/vest como clases. No se infiere la clase a partir del contexto de trabajo en altura. |
| 108 | excluir | E3 | El objetivo central es detectar somnolencia por rasgos faciales/oculares; PPE solo aparece como contexto de una clase. |
| 109 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 110 | incluir |  | Introducción/aporte y resultados: mAP 96,30% Pictor-v3 y 94,70% SHWD para detector de casco. |
| 111 | excluir | E3 | OpenPose define regiones de cabeza/tronco y un clasificador neuronal estima presencia de PPE; el resumen no confirma localización de casco/chaleco mediante detector con cajas ni cifra concreta. |
| 112 | incluir |  | Tabla 1, fila This study, y metodología: Boots, Glass, Gloves, Helmet, Person, Vest; mAP50=96,3–97,6%. |
| 113 | excluir | E3 | Conductas anormales en laboratorio y PPE de laboratorio, fuera del dominio/clases de interés. |
| 114 | excluir | E3 | Evalúa incentivos y cumplimiento conductual mediante clasificación de actividades; no desempeño de un detector de casco/chaleco. |
| 115 | incluir |  | Secciones Experiment and results y tabla 3: casco mAP50=64,8%; chaleco=72,3% con MFD-YOLO. Tabla numérica recuperada por indexación del PDF primario. |
| 116 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 117 | excluir | E3 | Detector general de 28 categorías de seguridad, materiales, andamios y acciones; el resumen no identifica casco/chaleco como clases centrales. |
| 118 | excluir | E3 | La tarea es cartografiar residuos/materiales reciclables con GIS; PPE es una categoría de residuo. |
| 119 | excluir | E3 | Razonamiento visión-lenguaje, VQA y evaluación contextual del riesgo; no detector central de casco/chaleco. |
| 120 | excluir | E3 | Detecta exclusivamente guantes/manos; clases fuera del alcance. |
| 121 | excluir | E4 | El resumen confirma detector de casco pero no aporta valor numérico; se localizó el PDF editorial, pero su recuperación agotó el tiempo de espera y no se pudieron confirmar resultados. |
| 122 | excluir | E3 | El resumen menciona casco y una exactitud global, pero no confirma localización con cajas ni separa detección de objetos de reconocimiento espaciotemporal; se excluye por ambigüedad de I4/tarea. |
| 123 | excluir | E3 | Las secciones consultadas sitúan la novedad en una herramienta de recomendaciones con LLM; el detector de casco alimenta el asesoramiento. Se aplica la regla estricta que excluye PPE como componente de otra tarea central. |
| 124 | excluir | E3 | El resumen habla de PPE genérico sin identificar casco/chaleco y sin valores de desempeño; no se confirmó el contenido completo. Prioridad E3. |
| 125 | incluir |  | Tabla comparativa, fila This study: SG hardhat, vest, worker, mAP50 PPE=93,6–96,8%. PPE es uno de los dos objetivos experimentales de detección, no una entrada incidental de un sistema de razonamiento. |
| 126 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 127 | excluir | E3 | El resumen informa SODA y métricas globales, pero no nombra casco/chaleco como objetos efectivamente detectados; no se confirmó la taxonomía en texto completo. |
| 128 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 129 | excluir | E3 | Objetivo central: asociar identidad de trabajadores y conductas mediante CV-RFID; PPE es una entrada al emparejamiento multimodal. |
| 130 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 131 | excluir | E3 | El resumen y la vista disponible describen PPE genérico sin especificar casco/chaleco como clases de la evaluación. |
| 132 | incluir |  | p. 3, resultados: mAP alrededor de 85%, recall 88%, precisión 90%; exactitud casco 88%, chaleco 94%; anotaciones con cajas. |
| 133 | excluir | E3 | El resumen describe PPE genérico en química/salud, sin confirmar casco/chaleco ni cifras de desempeño del detector. Prioridad E3. |
| 134 | excluir | E3 | El resumen da cifras pero solo para PPE y personas genéricos, sin especificar casco/chaleco; no se recuperó texto completo confirmatorio. |
| 135 | excluir | E3 | El resumen da mAP y dataset CSSID, pero no identifica casco/chaleco como objetos detectados. El nombre de un dataset no sustituye la confirmación de clases. |
| 136 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 137 | excluir | E3 | El resumen del artículo publicado no especifica las clases. La página editorial nombra SHWD, pero no se recuperaron métodos/resultados publicados que confirmen la taxonomía; no se transfiere evidencia de una versión preprint diferente. |
| 138 | excluir | E3 | VQA para cumplimiento de seguridad en escaleras, no detección central de casco/chaleco. |
| 139 | excluir | E3 | YOLO detecta trabajadores y EfficientNet clasifica regiones; el resultado central es una puntuación de riesgo/proximidad, sin casco/chaleco explícitos ni cifra de su detector. |
| 140 | excluir | E3 | Marco general de riesgo contextual, actividades, intrusión y proximidad; no confirma clases explícitas de casco/chaleco como objetivo central. |
| 141 | incluir |  | Sección 3.1 y tabla 2: mAP test=0,763 y AP no safety vest=0,404; cajas, casco/chaleco y evaluación propia del detector. AR es la interfaz del detector de PPE, sin otra tarea de riesgo/razonamiento. |
| 142 | incluir |  | Sección de dataset: helmet, no-helmet, harness, no-harness, safety hook; detector YOLO-ILB con mAP50=0,939. Detección multicategoría es objetivo explícito junto a cumplimiento del arnés. |
| 143 | excluir | E3 | Marco unificado de conductas, posturas, seguimiento e intrusión; PPE genérico y sin cifra concreta del detector de casco/chaleco. |
| 144 | excluir | E3 | PPE significa estimación del perfil de potencia en fibra óptica; no equipo de protección personal. |
| 145 | excluir | E3 | Reconocimiento y explicación de eventos con grafos de evidencia; no detección central de casco/chaleco con cajas. |
| 146 | incluir |  | Resumen Scopus: confirma casco y/o chaleco, modelo de detección y cifra de desempeño (incluida mejora relativa); dominio de construcción/industrial equivalente. |
| 147 | excluir | E3 | Marco multimodal de inspección, evaluación de riesgos y recomendaciones; PPE es una entidad de entrada, no detector central de casco/chaleco. |
| 148 | excluir | E3 | El resumen no especifica casco/chaleco y R²=0,981 es ajuste del modelo tamaño-rendimiento, no una cifra de desempeño del detector. Prioridad E3. |

## Verificación de la edición

Se comprobaron 74 filas en cada lote y 148 en el consolidado; decisiones por ID idénticas entre archivos. Se compararon las celdas y también el texto CSV enmascarando exclusivamente las dos columnas R2: encabezados, orden, resto de celdas, comillas, BOM y saltos de línea originales preservados.

No se modificaron los documentos de protocolo, los valores R1 ni los campos de conciliación.
