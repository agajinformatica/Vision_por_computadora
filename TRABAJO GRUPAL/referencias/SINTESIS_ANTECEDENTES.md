# Síntesis de los 30 PDFs — material para la Introducción

> **Cómo se produjo esto.** Se extrajo el texto de los 30 PDF con `pdftotext` y se fichó de
> cada uno: resumen, conjunto de datos empleado y cifras de desempeño reportadas. Las fichas
> recogen **lo que cada artículo declara de sí mismo en su resumen**, no una lectura completa
> del texto. Para citar un hallazgo fino —y no solo el resultado principal— hay que abrir el
> PDF. Las cifras están transcritas tal como aparecen.
>
> Generado el 2026-10-10.

---

## 1. Fichas

### Fuentes de los conjuntos de datos del experimento

| ID | Qué es | Datos | Cifra declarada |
|---|---|---|---|
| **01** | CHV, Sensors 2021. Entrena y compara **8 detectores YOLO** sobre 6 clases: casco en 4 colores, persona y chaleco | CHV, 1 330 img | YOLOv5x **86,55 % mAP**; YOLOv5s 52 FPS. Caída de 7 % en casco con rostros difuminados |
| **02** | SHEL5K, Sensors 2022. Dataset de 5 000 img con 6 clases **solo de casco**, probado sobre YOLOv3/v4/v5, Faster R-CNN y YOLOR | SHEL5K | mAP por clase ≈ 0,80 en la peor (rostro) |

### El enfoque dominante: detectores de una etapa sobre imagen de obra

| ID | Qué hace | Datos | Cifra |
|---|---|---|---|
| **20** | ApplSci 2022. YOLO en tiempo real para casco en obra; compara variantes de YOLOv5 | 5 000 img de cascos, 60/20/20 | **YOLOv5x 92,44 % mAP**, funciona con poca luz |
| **27** | IASC 2022. Cinco variantes de YOLOv5 para casco; contexto de Pakistán y marco normativo OSHA | propio | YOLOv5n 70,4 FPS; mejor mAP en variantes mayores |
| **35** | Sustainability 2022. YOLOv3/v4/v7 para **casco y chaleco de alta visibilidad** | propio, **11 000 img / 88 725 etiquetas** | **97 % mAP**, 25 FPS |
| **34** | Sensors 2023. Dron (UAS) + aprendizaje profundo; compara Faster R-CNN y YOLOv3 | 7 041 img | Faster R-CNN **93,1 %** vs YOLOv3 **89,8 %** de precisión |

### Mitigación de dificultades del dominio

**Objeto pequeño y multiescala**

| ID | Qué hace | Cifra |
|---|---|---|
| **21** | IEEE Access 2021. Añade una **cuarta escala de detección** y atención en el tronco de YOLOv5; aumento dirigido y transferencia | **92,2 % mAP, +6,3 pp** sobre el original; 3,0 ms por imagen a 640×640 |
| **09** | SciRep 2026. YOLOv10 con ODConv, EMA-BiFPN, **cuatro escalas** y pérdida MPDIoU; 5 categorías de incumplimiento | **92,49 mAP@50**, 70,04 mAP@50:95, 57,28 FPS. **Las mayores ganancias, en objeto pequeño** |
| **25** | Sensors 2023. YOLOv5s con GAM y CBAM, anclas recalculadas con K-means++ | mejora sobre YOLOv5s base |
| **29** | SciRep 2023. YOLOv5 + atención ECA + BiFPN + cabeza desacoplada | **95,9 %, +3,0 pp** sobre YOLOv5 |

**Oclusión y objetos densos**

| ID | Qué hace | Cifra |
|---|---|---|
| **30** | SciRep 2024. BiFEL-YOLOv5s: BiFPN + Focal-EIoU y **sustitución de NMS por Soft-NMS** para objetos ocluidos | +0,9 pp de precisión media, **+2,8 pp de exhaustividad** |
| **03** | Sensors 2025. MRC-DETR, transformador con atención de borde multiescala para **objetos pequeños y ocluidos**; destilación para despliegue en el borde | **95,9 % AP50**, +3,4 pp |
| **31** | RemoteSens 2023. Transformador de reconocimiento de atributos para casco y arnés; robusto a pose, oclusión y fondo | supera al estado del arte en exactitud |

**Iluminación y resolución**

| ID | Qué hace | Cifra |
|---|---|---|
| **07** | SciRep 2026. AE-LFOG-YOLO: módulo invariante a iluminación y anclas evolutivas; túnel | **94,83 % mAP@0,5**; +35,7 % de rango operativo |
| **06** | SciRep 2026. YOLOv11-SRA: SAConv, autocalibración rectangular y ASFF; **minería subterránea, poca luz** | **82 % mAP@0,5** sobre CUMT-HelmeT |
| **23** | Sensors 2023. Reconstrucción por **super-resolución antes de detectar** | PSNR 29,420; SSIM 0,855 |

**Ligereza y despliegue en el borde**

| ID | Qué hace | Cifra |
|---|---|---|
| **24** | Sensors 2023. YOLOv4 con tronco PP-LCNet, convolución separable y pérdida SIoU | **92,98 %**, **−83 % de tamaño**, +88 % de velocidad |
| **08** | SciRep 2026. DRR-YOLOv11s para central hidroeléctrica | **−37,58 % de parámetros**, 93,46 % mAP@0,5, 160 FPS |
| **32** | Buildings 2022. Modelo de color de casco embebido en **Raspberry Pi** | 0,861 mAP |
| **13** | LACCEI 2026. YOLOv8 + cómputo en el borde en **pymes peruanas**, alineado con la **R.M. 050-2013-TR** | 94,6 % precisión, 92,8 % exhaustividad, 38 ms/fotograma |

### El chaleco, la clase desatendida

| ID | Qué dice | Cifra |
|---|---|---|
| **15** | IEEE Access 2024. **Abre declarando el vacío**: la investigación se ha centrado en el casco y ha pasado por alto la ropa reflectante. Dataset propio de 4 categorías + AL-YOLOv5 con atención y pérdida SEIoU | **+0,9 AP** en la categoría con pocos datos, +0,4 mAP global. Reduce falsos positivos en ropa reflectante |
| **16** | Sustainability 2023. Faster R-CNN sobre **CHVG** (8 clases: 4 colores de casco, cabeza, persona, chaleco, gafas) | **96 % mAP** sobre 1 699 img anotadas |
| **04** | Computers 2026. YOLO11x sobre CHVG con aumento y ajuste fino | **96,9 % mAP50**, 7,3 ms frente a 170 ms de trabajos previos sobre el mismo conjunto |

### Detección del incumplimiento (clases negativas)

| ID | Qué hace | Cifra |
|---|---|---|
| **14** | SciRep 2025. YOLOv10 y transformadores sobre cámaras de vigilancia y corporales; 5 clases de ausencia | Swin+YOLOv10, **AP50 medio 87,32 %** |
| **28** | SciRep 2026. Faster R-CNN con **adaptación de dominio** para 5 categorías de ausencia. Señala que **las instancias reales de incumplimiento son escasas porque la norma obliga a usar el equipo** | **86,84 % mAP**, **+14 pp** sobre Faster R-CNN supervisado |

### Metodología experimental

| ID | Qué hace | Por qué importa aquí |
|---|---|---|
| **05** | Buildings 2026. Protocolo **controlado** de mezcla real/sintético: conjunto de prueba fijo real, once configuraciones de tamaño constante, y **repetición con varias semillas** | **La pieza metodológica clave.** Usa **exhaustividad media (AR@100) como métrica orientada a seguridad**, y demuestra que una ventaja observada en **una sola ejecución no se sostiene al repetir con semillas distintas** |

### Revisión previa y contexto

| ID | Qué aporta |
|---|---|
| **12** | AI Review 2024. **Revisión sistemática** de enfoques, algoritmos, conjuntos de datos y tecnologías. Señala barreras: variabilidad entre industrias y entornos, coste computacional en tiempo real, identificación de personas, ética y ciberseguridad. Concluye que el avance **exige desarrollar conjuntos de datos públicos** adecuados. Excluida del embudo por E1, citable como antecedente |
| **10** | HSE 2023. Informe anual. **Cifras globales de Gran Bretaña, no sectoriales**: 123 trabajadores muertos en accidentes laborales en 2021/22; 1,8 M de casos de enfermedad laboral; 36,8 M de jornadas perdidas. Contiene la frase que respalda la afirmación cualitativa: el sector de la construcción sigue siendo uno de los de mayor riesgo del país |
| **11** | IJERPH 2023. Marco para registrar y analizar actos y condiciones subestándar junto con la productividad (Last Planner System). **Sin componente de visión**: contexto de gestión |
| **33** | ApplSci 2023. Faster R-CNN + LSTM, dos flujos espacio-temporales para conducta insegura. Útil si se menciona la dimensión temporal |

---

## 2. Lo que el conjunto permite afirmar

Tres hallazgos agregados, cada uno verificable sobre las fichas de arriba.

**El casco domina y el chaleco va a remolque.** De los 29 estudios experimentales del inventario,
**unos 15 trabajan únicamente sobre el casco**; el chaleco aparece en torno a 11, y casi siempre
como una clase más dentro de un conjunto multiclase, nunca como el problema central. La
referencia **15 abre su artículo declarando exactamente ese vacío**, lo que permite sostener la
afirmación con una cita y no solo con un recuento propio.

**Las cifras reportadas no son comparables entre sí.** Van de **82 % a 97 % de mAP**, pero
medidas sobre conjuntos distintos: CHV, SHEL5K, CUMT-HelmeT, CHVG, y un número alto de
**corpus propios no publicados** —los estudios 03, 06, 07, 08, 09, 13, 15, 29, 34 y 35 entrenan
cada uno sobre datos construidos para la ocasión—. Un lector no puede ordenar esos resultados
en una tabla: no miden lo mismo. Esto es lo que da sentido a un experimento con protocolo
compartido como el de este trabajo.

**La comparación de una sola ejecución es frágil, y hay quien ya lo ha demostrado.** La
referencia **05** repite su comparación central con varias semillas y encuentra que la ventaja
observada en una única corrida **no se mantiene**. Es simultáneamente el mejor apoyo para el
argumento metodológico de la Introducción y la fuente que obliga a declarar, en la Discusión,
que este trabajo también corrió una sola vez por modelo.

---

## 3. Mapa para el párrafo (b)

Cuatro movimientos, con lo que hay que leer en cada uno.

| Movimiento | Qué afirmar | Citas | Qué abrir para el dato fino |
|---|---|---|---|
| 1. El enfoque dominante | Los detectores de una etapa se han consolidado como el enfoque estándar sobre imagen de obra | **20, 27, 35, 01** | 20 (92,44 %) y 35 (97 %, casco **y** chaleco) ya traen su cifra en el resumen |
| 2. Las dificultades del dominio | La línea posterior ataca objeto pequeño, oclusión e iluminación con modificaciones arquitectónicas | **21, 09** (escala) · **30, 03** (oclusión) · **07, 06** (iluminación) | 30 es el más útil: sustituye NMS por Soft-NMS por la oclusión, que enlaza con tu trabajo futuro |
| 3. La revisión previa | Qué concluye y qué vacío señala | **12** | **Hay que leerlo.** El resumen da las barreras; la conclusión sobre datasets públicos es la que te interesa |
| 4. Las dos observaciones | El chaleco desatendido · las comparaciones no comparables | **15** (lo declara) · **05** (lo demuestra) · recuento propio | 15: la frase de apertura. 05: la sección de semillas repetidas |

---

## 4. Recomendación

**Ordena por problema, no por cronología ni por arquitectura.** La tentación al tener treinta
artículos es contar la historia de YOLOv3 a YOLOv11. No lo hagas: produce un párrafo que
enumera y no argumenta. Organízalo como lo tienes planteado —enfoque dominante, dificultades
del dominio, vacío— porque así cada grupo de citas sostiene una afirmación en lugar de ocupar
una línea.

**Cita dos o tres por afirmación, no diez.** Tienes material para quince citas en el párrafo (b)
y no debes usarlas todas ahí. Las que no entren tienen sitio: las de despliegue en el borde
(24, 08, 32, 13) encajan mejor en la justificación de la escala `n`, y las de incumplimiento
(14, 28) en el trabajo futuro, cuando expliques por qué las clases negativas quedan fuera.

**Las dos observaciones del cierre son tu puente, y conviene que estén apoyadas de forma
distinta.** La primera —el chaleco desatendido— va con la cita de 15, que la declara
textualmente, más tu propio recuento del inventario. La segunda —las comparaciones no
atribuibles— va con 05, que no la declara sino que la demuestra experimentalmente. Esa
asimetría es buena: una afirmación respaldada por quien la dice y otra por quien la prueba.

**No escribas que nadie ha hecho esto antes.** Escribe que las comparaciones existentes se
realizan sobre conjuntos y protocolos distintos, lo que impide atribuir las diferencias a la
arquitectura. Es más modesto, es verificable con tus propias fichas, y es exactamente el hueco
que tu experimento llena.

**Dos cosas que debes verificar antes de citar.**

- **La referencia 10 no te da la cifra que el párrafo (a) necesita.** Sus números son globales
  de Gran Bretaña y de todos los sectores: 123 muertes laborales en 2021/22. Sí respalda la
  afirmación cualitativa de que la construcción es uno de los sectores de mayor riesgo. Si
  quieres una cifra sectorial, necesitas otra fuente —el HSE publica estadísticas de
  construcción por separado— y, dado el contexto de la referencia 13, las estadísticas
  peruanas del MTPE serían más pertinentes para justificar la relevancia local.
- **La referencia 12 hay que leerla entera.** Es la única revisión sistemática del inventario y
  es la que sostiene el movimiento 3. Su resumen da las barreras, pero el vacío concreto que
  debes citar está en sus conclusiones.
