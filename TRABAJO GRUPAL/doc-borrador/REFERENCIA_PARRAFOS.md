# Párrafos de referencia — material de lectura

> **Qué es esto y qué no es.** Material de referencia para leer, evaluar e interpretar antes
> de redactar. **No es el texto del artículo** y no está pensado para copiarse: el lineamiento
> del proyecto (sección 6 de `GUIA_INVESTIGADOR.md`) se mantiene — la redacción del paper es
> íntegramente humana. Este archivo es andamiaje; el texto que vaya al .docx lo escribes tú.
>
> Bajo cada bloque, los **irrenunciables**: lo que tu versión debe conservar aunque la
> reformules entera, porque los pide la rúbrica o porque sostienen una cifra verificada.
>
> Generado el 2026-10-10 · cifras de `experimento/RESULTADOS.md` y `estadisticas.json`

**Marcadores de cita:** van como `[n]` provisionales; la numeración definitiva depende del
orden de aparición en el documento final. Los huecos `⟦ ⟧` marcan datos que solo tú puedes
cerrar.

---

## Resumen  ·  150-200 palabras  ·  se escribe AL FINAL

> El incumplimiento en el uso de equipo de protección personal es un factor recurrente en la
> siniestralidad del sector de la construcción, y su vigilancia manual resulta inviable a la
> escala de una obra activa. Este trabajo evalúa YOLO26, la generación más reciente de la
> familia de detectores de una sola etapa, en la detección de casco y chaleco de seguridad.
> Se construyó un corpus unificado de 20 944 imágenes a partir de tres conjuntos de datos
> públicos heterogéneos, homogeneizados a dos clases positivas, y se entrenaron tres
> detectores —YOLOv8n como línea base simple, YOLO11n como comparador de la generación
> anterior y YOLO26n como modelo propuesto— bajo un protocolo idéntico de 50 épocas,
> resolución de 640 píxeles y semilla fija. Sobre un conjunto de prueba de 2 171 imágenes no
> vistas, YOLO26n alcanza una mAP50 de 0,8592 frente a 0,8415 de la línea base, una mejora de
> 2,1 % obtenida con un 19 % menos de parámetros, y concentra su ganancia en la clase chaleco,
> la peor representada en los datos. Los resultados indican que la nueva generación aporta una
> mejora consistente sin coste en tamaño de modelo.
>
> **Palabras clave:** detección de objetos; equipo de protección personal; seguridad en la
> construcción; YOLO26; aprendizaje profundo

**Irrenunciables**

- Los seis elementos, en orden: problema · datos · método · **resultado con su cifra** · conclusión.
- La cifra tiene que estar. Un resumen sin número no cumple el criterio.
- Entre 150 y 200 palabras. El de arriba tiene 193; si recortas, no sacrifiques la cifra.

---

## 1. Introducción  ·  ~1,3 páginas  ·  Rúbrica: problema y justificación (5 pts)

> **Reescrito el 2026-10-10** tras fichar los 30 PDF (`referencias/SINTESIS_ANTECEDENTES.md`).
> El párrafo (b) ya no es andamiaje: las afirmaciones y las cifras proceden de lo que cada
> artículo declara en su resumen. Aun así, **abre los PDF de 12 y 15 antes de citarlos**: son
> los dos que sostienen el argumento central y merecen lectura propia.
>
> Las citas van como `[ref. NN]`, el identificador del inventario, **no** el número IEEE final.
> La correspondencia está al final de esta sección.

**(a) El problema y su relevancia**

> La construcción figura de forma persistente entre los sectores de mayor riesgo laboral. El
> organismo británico de seguridad y salud contabilizó 123 trabajadores fallecidos en
> accidentes laborales durante el ejercicio 2021/22 en el conjunto de las actividades
> económicas, y sitúa a la construcción entre las industrias de mayor riesgo del país
> [ref. 10]. ⟦Si consigues la cifra sectorial —el mismo organismo publica estadísticas de
> construcción por separado— o la estadística peruana del MTPE, sustituye aquí: una cifra
> específica del sector sostiene mejor el párrafo que una agregada⟧. Una proporción relevante
> de esos siniestros se relaciona con la ausencia o el uso incorrecto del equipo de protección
> personal, y en particular del casco y del chaleco de alta visibilidad, cuya obligatoriedad
> está normativamente establecida —en el caso peruano, por la R.M. 050-2013-TR [ref. 13]—.
> La verificación de su uso, sin embargo, sigue descansando en la inspección visual humana, un
> procedimiento laborioso y propenso al error [ref. 16] que en la práctica resulta
> discontinuo, dependiente de la disponibilidad de personal y de trazabilidad limitada
> [ref. 13]. Automatizar esa verificación sobre las imágenes que las obras ya capturan
> convierte un control intermitente en uno continuo, y constituye por ello un problema de
> visión por computadora cuyas consecuencias recaen directamente sobre la seguridad de las
> personas.

**(b) Antecedentes — primer párrafo: el enfoque y sus refinamientos**

> La detección automática de equipo de protección ha seguido de cerca la evolución de los
> detectores de objetos de propósito general, y los modelos de una sola etapa se han
> consolidado como el enfoque dominante sobre imagen de obra. Trabajos representativos de esa
> consolidación reportan precisiones medias del 92,44 % sobre un conjunto de cinco mil
> imágenes de cascos [ref. 20] y del 97 % sobre un corpus propio de once mil imágenes que
> incluye casco y chaleco de alta visibilidad [ref. 35], mientras que la comparación
> sistemática de ocho variantes de una misma familia sobre un conjunto de obra con seis clases
> situó el mejor resultado en el 86,55 % [ref. 01]. Una línea posterior se ha concentrado en
> las dificultades propias del dominio más que en la arquitectura general. El tamaño reducido
> del casco en planos generales ha motivado la incorporación de escalas de predicción
> adicionales y mecanismos de atención, con mejoras de 6,3 puntos sobre el modelo de partida
> [ref. 21] y ganancias concentradas específicamente en los objetos más pequeños [ref. 09]. La
> oclusión mutua entre trabajadores ha llevado a sustituir la supresión de no máximos por
> variantes más permisivas, con un aumento de 2,8 puntos en exhaustividad [ref. 30], y a
> explorar arquitecturas basadas en transformadores para objetos pequeños y parcialmente
> ocultos [ref. 03]. Las condiciones de iluminación adversas han dado lugar a módulos
> invariantes a la iluminación evaluados en túneles [ref. 07] y en minería subterránea
> [ref. 06]. Un tercer grupo ha priorizado el despliegue sobre hardware limitado, reduciendo
> el tamaño del modelo en un 83 % con una pérdida mínima de precisión [ref. 24].

**(b) Antecedentes — segundo párrafo: la revisión previa y el vacío**

> Una revisión sistemática reciente del campo recorre estos enfoques, algoritmos y conjuntos de
> datos, e identifica como barreras la variabilidad entre industrias y entornos, el coste
> computacional del procesamiento en tiempo real y los problemas de identificación de personas,
> para concluir que el avance de estas soluciones exige el desarrollo de conjuntos de datos
> públicos adecuados [ref. 12]. Dos observaciones se desprenden de esta literatura y motivan el
> presente trabajo. La primera es que el chaleco recibe una atención sensiblemente menor que el
> casco: de los estudios revisados, en torno a la mitad abordan únicamente la detección del
> casco, y el chaleco aparece casi siempre como una clase más dentro de un esquema multiclase
> y no como el problema central, un desequilibrio que la literatura ya ha señalado
> explícitamente [ref. 15] y que los conjuntos de datos disponibles reproducen. La segunda es
> que las cifras reportadas, pese a su aparente homogeneidad, no son comparables entre sí:
> oscilan entre el 82 % y el 97 % de precisión media, pero se miden sobre conjuntos distintos
> y, en una proporción considerable de los casos, sobre corpus construidos específicamente para
> cada estudio y no publicados. A ello se añade que la mayoría de las comparaciones entre
> arquitecturas se realizan mediante una única ejecución por modelo; un trabajo que repitió su
> comparación con varias semillas encontró que la ventaja observada en una sola corrida no se
> mantenía al promediar las repeticiones [ref. 05]. En conjunto, estas condiciones dificultan
> atribuir las diferencias observadas a la arquitectura y no al experimento.

**(c) Objetivo y aporte** — ajustado a D16: nada de NMS-free ni generalización

> Este trabajo evalúa YOLO26 en la detección conjunta de casco y chaleco de seguridad, y lo
> compara con dos generaciones previas de la misma familia bajo un protocolo de entrenamiento
> estrictamente idéntico. La contribución es triple. En primer lugar, se construye y documenta
> un corpus unificado de 20 944 imágenes procedentes de tres fuentes heterogéneas,
> homogeneizadas mediante una regla de correspondencia reproducible, que mejora el desbalance
> entre ambas clases respecto a cualquiera de las fuentes por separado. En segundo lugar, se
> aporta una comparación controlada entre tres generaciones de detectores en la que la única
> variable es la arquitectura, lo que permite atribuir las diferencias observadas a ella y no a
> las condiciones del entrenamiento. En tercer lugar, se cuantifica la mejora obtenida —en
> desempeño agregado y desagregado por clase— y se documenta el compromiso entre precisión y
> exhaustividad que introduce el modelo más reciente, cuya interpretación resulta
> especialmente relevante en un dominio donde el coste de los dos tipos de error no es
> simétrico.

**Correspondencia de los identificadores**

| En el texto | Referencia |
|---|---|
| ref. 01 | Wang et al., *Sensors*, 2021 — CHV |
| ref. 03 | MRC-DETR, *Sensors*, 2025 |
| ref. 05 | *Buildings*, 2026 — mezcla real/sintético con semillas repetidas |
| ref. 06 | YOLOv11-SRA, *Sci. Rep.*, 2026 — minería subterránea |
| ref. 07 | AE-LFOG-YOLO, *Sci. Rep.*, 2026 — túnel |
| ref. 09 | YOLOv10 multiescala, *Sci. Rep.*, 2026 |
| ref. 10 | HSE, informe anual 2022/23 |
| ref. 12 | *AI Review*, 2024 — revisión sistemática |
| ref. 13 | LACCEI, 2026 — pymes peruanas, R.M. 050-2013-TR |
| ref. 15 | *IEEE Access*, 2024 — ropa reflectante |
| ref. 16 | *Sustainability*, 2023 — CHVG, Faster R-CNN |
| ref. 20 | *Appl. Sci.*, 2022 — YOLOv5x |
| ref. 21 | *IEEE Access*, 2021 — multiescala |
| ref. 24 | *Sensors*, 2023 — YOLOv4 ligero |
| ref. 30 | *Sci. Rep.*, 2024 — BiFEL-YOLOv5s, Soft-NMS |
| ref. 35 | *Sustainability*, 2022 — casco y chaleco, 11 000 img |

**Irrenunciables**

- Los tres movimientos encadenados: problema → antecedentes → objetivo y aporte.
- Las citas **integradas en la prosa**, nunca como lista.
- El aporte **exactamente el de D16**. Si prometes NMS-free o generalización, Resultados no lo entrega.
- El párrafo (b) debe **nombrar el vacío**, no solo describir lo hecho. Las dos observaciones del
  cierre son ese vacío y son el puente al párrafo (c).
- **No escribas que nadie lo ha hecho antes.** Escribe que las comparaciones existentes usan
  conjuntos y protocolos distintos. Es más modesto, verificable y describe mejor tu aporte.

**Verifica antes de citar**

- ⚠ **ref. 10 no da la cifra sectorial.** Sus 123 fallecidos son de todas las actividades
  económicas de Gran Bretaña. Lo que sí respalda es la afirmación cualitativa sobre el riesgo
  del sector. No le atribuyas un dato de construcción que no contiene.
- ⚠ **ref. 12 y ref. 15 merecen lectura completa.** Son las dos que sostienen el argumento; lo
  que aquí se usa procede de sus resúmenes.
- El recuento «en torno a la mitad» es tuyo, sobre tu inventario. Si lo afinas al cerrar el
  cribado de texto completo, puedes dar la proporción exacta sobre los estudios incluidos, que
  es mucho más fuerte.

---

## 2. Métodos

### 2.1 Protocolo de revisión sistemática (PRISMA 2020)

> La revisión de la literatura se condujo siguiendo la declaración PRISMA 2020 [P1], y la
> estrategia de búsqueda se reporta conforme a su extensión PRISMA-S [P2]. La pregunta de
> revisión indagó qué arquitecturas de detección de objetos basadas en aprendizaje profundo se
> han aplicado a la detección de casco y chaleco de seguridad en entornos de construcción,
> sobre qué conjuntos de datos y con qué desempeño reportado.
>
> La búsqueda se ejecutó el 9 de octubre de 2026 en Scopus, sobre los campos de título,
> resumen y palabras clave, con la siguiente expresión: ⟦pegar la cadena literal de
> CADENAS_BUSQUEDA.md⟧. Se aplicaron los filtros de tipo de documento —artículo de revista—,
> ventana temporal 2021-2026 e idioma inglés o español. La búsqueda arrojó 158 registros, que
> se exportaron con su resumen. ⟦quién ejecutó la búsqueda y en qué formato se exportó⟧.
> **No se pudo consultar Web of Science por falta de acceso institucional**, limitación que se
> declara explícitamente y que se discute en la Sección 4.
>
> Los criterios de inclusión exigieron: artículo primario en revista indexada en Scopus o Web
> of Science (I1), publicado entre 2021 y 2026 (I2), en inglés o español (I3), que abordara una
> tarea de detección de objetos con cajas delimitadoras (I4), cuyo equipo detectado incluyera
> casco o chaleco (I5), en dominio de construcción o industrial equivalente (I6), y que
> reportara métricas cuantitativas de desempeño (I7). Se excluyeron revisiones, editoriales y
> material sin revisión por pares (E1), estudios basados exclusivamente en sensores no visuales
> (E2), los centrados en equipo fuera del alcance (E3), los carentes de métricas (E4), aquellos
> cuyo texto completo resultó inaccesible (E5) y los duplicados entre bases (E6).
>
> El cribado se organizó en dos etapas. En la primera, sobre título y resumen, el criterio I5
> se aplicó de forma deliberadamente permisiva: dado que una palabra ausente del resumen no
> prueba la ausencia del contenido en el estudio, se optó por trasladar esa verificación a la
> lectura del texto completo. Esta decisión excluyó 10 registros y mantuvo 148 para la segunda
> etapa; la alternativa estricta habría excluido 74, entre ellos ⟦14⟧ estudios de alto impacto.
> En la segunda etapa se evaluó el texto completo, registrando el motivo de cada exclusión
> conforme a los códigos E1-E6. Ambas etapas fueron realizadas por dos revisores de forma
> independiente, y las discrepancias se resolvieron por un tercer revisor ⟦confirmar que así
> se ejecutó, y reportar el número de discrepancias resueltas⟧. El proceso completo, con los
> recuentos de cada etapa, se resume en la Figura 1.

**Irrenunciables**

- **Fecha exacta, base y cadena literal.** Sin los tres, la búsqueda no es reproducible.
- **Declarar que WoS no se consultó.** Decir que se buscó donde no se buscó es lo único grave.
- Los códigos I1-I7 y E1-E6 enunciados, no solo referenciados.
- **Dos revisores y un tercero que dirime**, con el número de discrepancias.
- La justificación del I5 permisivo: es una decisión metodológica fuerte y te defiende sola.
- ⚠ El cribado de texto completo **aún no está cerrado**. Hasta el 1 de noviembre, los
  recuentos finales y la Figura 1 van con huecos.

**Pie de la Figura 1**

> Figura 1. Diagrama de flujo PRISMA 2020 del proceso de identificación, cribado y selección
> de los estudios incluidos en la revisión. Se emplea la variante para revisiones nuevas con
> registro de fuentes adicionales a las bases de datos.

### 2.2 Conjuntos de datos

**(1) Las fuentes**

> El corpus experimental se construyó a partir de tres conjuntos de datos públicos,
> seleccionados porque cada uno compensa una carencia de los otros. El primero, *Personal
> Protective Equipment – Combined Model* v8 [1], aporta la escala: 44 002 imágenes anotadas
> con catorce clases relacionadas con el equipo de protección. El segundo, *Construction-PPE*
> [2], contribuye 1 416 imágenes con la mejor representación del chaleco de todo el material
> evaluado, con una razón casco:chaleco de 1,07:1 frente a 6,58:1 del primero. El tercero, CHV
> (*Color Helmet and Vest*) [3], aporta 1 330 imágenes —seleccionadas por sus autores de un
> conjunto inicial de 10 000— en un dominio de obra homogéneo y con la anotación más densa,
> además de ser el único de los tres publicado en una revista revisada por pares. Los otros dos
> proceden de repositorios abiertos sin revisión externa, lo que se asume como limitación del
> corpus.

**(2) Esquema de clases**

> Las anotaciones de las tres fuentes se homogeneizaron a un esquema de dos clases positivas,
> `casco` y `chaleco`, que es el alcance que declara este trabajo. La decisión responde a tres
> razones: las tres fuentes se fusionan bajo ese esquema sin introducir ruido de etiqueta; el
> desbalance entre ambas clases mejora de 6,58:1 en la fuente mayoritaria a 4,84:1 en el corpus
> unificado; y las clases que marcan la ausencia del equipo, presentes solo en parte de las
> fuentes, exigirían un planteamiento de cumplimiento normativo que excede el objetivo aquí
> propuesto. La regla de correspondencia se detalla en la Sección 2.3. Tras el remapeo, el
> corpus consta de 20 944 imágenes, con 47 700 instancias de casco y 9 850 de chaleco, según
> resume la Tabla 1. Las licencias de las fuentes son CC BY 4.0 [1] y AGPL-3.0 [2], esta última
> de tipo copyleft fuerte, y ⟦licencia de CHV: verificar en el repositorio oficial⟧.

**(3) Particiones**

> Se conservaron las particiones de entrenamiento, validación y prueba definidas originalmente
> por los autores de cada fuente, en lugar de reagrupar el material y volver a dividirlo. La
> razón es evitar que imágenes separadas de forma deliberada por los autores —por ejemplo,
> fotogramas próximos de una misma escena— acaben repartidas entre entrenamiento y prueba, lo
> que inflaría artificialmente el desempeño. El corpus resultante se divide en 14 729 imágenes
> de entrenamiento, 4 044 de validación y 2 171 de prueba, con razones casco:chaleco de 4,62:1,
> 5,84:1 y 4,81:1 respectivamente. Las 25 804 imágenes que no contenían ninguna de las dos
> clases positivas se descartaron.

**(4) El descarte**

> Se evaluó un cuarto conjunto, Pictor-v3 [4], que finalmente se descartó. Del subconjunto de
> acceso público solo se distribuyen las etiquetas de 774 imágenes, y su medición directa
> arroja 1 646 instancias de casco frente a 42 de chaleco: una razón de 39,2:1, muy inferior a
> la de cualquier otra fuente considerada, con solo 41 de 2 497 trabajadores anotados portando
> chaleco. El conjunto resulta por tanto útil para la detección de casco o de trabajadores,
> pero inservible para el objetivo de este trabajo. Sus etiquetas se conservan como evidencia
> del descarte.

**Pie de la Tabla 1**

> Tabla 1. Conjuntos de datos empleados en la construcción del corpus, con el número de
> imágenes antes y después del remapeo a dos clases, las instancias por clase y la razón entre
> ambas. La última fila corresponde al conjunto evaluado y descartado.

**Irrenunciables**

- El **argumento de por qué tres fuentes**, antes de las cifras.
- Las cifras **post-remapeo** (no las de `COMPARATIVA_DATASETS.md`, que mide inconsistentemente).
- Las **licencias** y que dos fuentes no están revisadas por pares.
- El descarte **con su cifra medida**: las 42 instancias hacen todo el trabajo.
- La justificación de las particiones **por fuga de datos**, que es el argumento fuerte.

### 2.3 Preprocesamiento

**(1) Homogeneización**

> La unificación de las tres fuentes exigió una correspondencia explícita entre sus esquemas de
> etiquetado original y las dos clases finales. En *PPE Combined Model* se tomó la clase
> `Hardhat` como `casco` y `Safety Vest` como `chaleco`, descartando las clases que señalan la
> ausencia del equipo. En *Construction-PPE* la correspondencia fue directa desde `helmet` y
> `vest`. En CHV, que distingue el casco por color, las cuatro clases cromáticas se colapsaron
> en una sola clase `casco`, y `vest` pasó a `chaleco`. Las imágenes que tras esta operación no
> contenían ninguna de las dos clases positivas —25 804 en total— se descartaron del corpus;
> las etiquetas que quedaron vacías por la eliminación de clases no relevantes se conservaron
> como ejemplos negativos, que contribuyen a reducir los falsos positivos. Se ignoraron además
> diez archivos de etiqueta de *Construction-PPE* sin imagen asociada, lo que supone treinta
> cajas excluidas. Todo el proceso está implementado en un único script,
> `01_preparar_dataset.py`, que genera el corpus mediante enlaces simbólicos en lugar de
> copias, de modo que la operación es repetible sin duplicar el almacenamiento.

**(2) Transformaciones de entrada**

> Las imágenes se redimensionan a 640 × 640 píxeles en el momento de la carga, por el propio
> marco de entrenamiento, sin reescalado previo en disco. El aumento de datos se aplicó con la
> configuración estándar del marco, idéntica para los tres modelos comparados: composición en
> mosaico, desactivada en las diez últimas épocas; perturbación en el espacio HSV con factores
> de 0,015, 0,7 y 0,4 para tono, saturación y valor; reflexión horizontal con probabilidad 0,5;
> escalado de 0,5, traslación de 0,1 y borrado aleatorio de 0,4, junto con *RandAugment*. Se
> mantuvieron desactivadas la reflexión vertical, la rotación, el cizallamiento, la deformación
> en perspectiva y las operaciones de mezcla de imágenes.

**Irrenunciables**

- La regla de remapeo **clase por clase**.
- Los **valores numéricos** de los aumentos. «La configuración por defecto» no es reproducible.
- Que los aumentos son **idénticos para los tres modelos**.
- Las 25 804 descartadas y las 10 huérfanas: explican el paso de 46 748 a 20 944.

### 2.4 Modelo

> Se empleó YOLO26 en su escala más ligera, `n`, un detector de una sola etapa de la familia
> YOLO. El entrenamiento no se realizó desde cero: los tres modelos comparados partieron de
> pesos preentrenados sobre COCO, de modo que la adaptación al dominio se produce por ajuste
> fino sobre el corpus descrito. El protocolo de entrenamiento se definió una única vez y se
> aplicó sin variación a los tres modelos: 50 épocas, resolución de entrada de 640 píxeles,
> lotes de 32 imágenes, optimizador seleccionado automáticamente por el marco —que resolvió en
> AdamW con una tasa de aprendizaje inicial de 0,001667— y semilla aleatoria fija en 42. Se
> configuró una paciencia de 15 épocas para la detención temprana, que no llegó a activarse en
> ninguno de los tres casos: los tres modelos completaron las 50 épocas. El entrenamiento se
> ejecutó en una única GPU NVIDIA Tesla T4, con tiempos de 120,4, 121,9 y 132,9 minutos para
> YOLOv8n, YOLO11n y YOLO26n respectivamente. El entorno de ejecución fue Ultralytics 8.4.175
> sobre PyTorch 2.11.0 con CUDA 12.8 y Python 3.13.15. La semilla fija y la aplicación de un
> único conjunto de hiperparámetros son las dos condiciones que permiten atribuir las
> diferencias observadas a la arquitectura y no al procedimiento de entrenamiento.

**Irrenunciables**

- **Transfer learning desde COCO**, dicho explícitamente. La guía del curso lo pregunta.
- Todos los hiperparámetros, **incluida la tasa de aprendizaje** (0,001667) y el optimizador real (AdamW).
- **Las 50 épocas se completaron**: la paciencia no se activó. Si no lo dices, queda la duda.
- El hardware y las versiones del entorno.
- La frase que cierra: semilla fija + protocolo único = atribución legítima a la arquitectura.

### 2.5 Línea base

> La comparación se articula sobre dos referencias de distinta naturaleza. La primera, YOLOv8n,
> actúa como línea base simple: es una arquitectura ampliamente adoptada, disponible en la
> misma escala que el modelo propuesto y sin ninguna modificación respecto a su configuración
> original. La segunda, YOLO11n, es el comparador directo de la generación inmediatamente
> anterior, y permite situar la mejora obtenida frente al estado previo de la misma familia de
> detectores. Declarar ambas responde a dos preguntas distintas: la primera establece el punto
> de partida que cualquier propuesta debe superar; la segunda determina si la ganancia procede
> de la nueva generación o simplemente del esquema de entrenamiento adoptado. Los tres modelos
> se entrenaron con un único conjunto de hiperparámetros, definido una sola vez y aplicado sin
> variación, de forma que ninguna diferencia observada pueda atribuirse a la configuración.

**Irrenunciables**

- La expresión **«línea base simple»**, literal: es la que pide la rúbrica.
- La **función distinta de cada referencia**, que es lo que justifica declarar dos.

### 2.6 Métricas de evaluación

> El desempeño se reporta mediante la precisión media promediada sobre umbrales de solapamiento
> de 0,50 a 0,95 (mAP50-95), que se adopta como métrica principal por dos motivos: es la medida
> estándar en la literatura de detección de objetos, lo que permite situar los resultados frente
> a trabajos previos, y al promediar sobre múltiples umbrales penaliza las localizaciones
> imprecisas, no solo las clasificaciones erróneas. Se acompaña de mAP50, más permisiva con la
> precisión de la caja y por ello más comparable con los trabajos que solo reportan ese valor,
> junto con la precisión y la exhaustividad agregadas. Entre estas dos últimas, la exhaustividad
> recibe una interpretación privilegiada: en un sistema de vigilancia de seguridad, un
> trabajador sin casco que el modelo no detecta constituye un riesgo no advertido, mientras que
> una detección espuria solo genera una verificación innecesaria. El coste de ambos errores no
> es simétrico, y la medida que los distingue es la exhaustividad. Todas las métricas se
> reportan además desagregadas por clase, dado que el desbalance del corpus hace esperable un
> comportamiento distinto en casco y en chaleco. La evaluación se realiza sobre el conjunto de
> prueba, compuesto por 2 171 imágenes que ninguno de los modelos vio durante el entrenamiento.

**Irrenunciables**

- **El porqué de la métrica**, no solo su nombre. Es criterio explícito y es lo que más se olvida.
- El **coste asimétrico** con un caso concreto, no en abstracto.
- Que la evaluación es sobre **test no visto**.
- ⚠ **No anuncies métricas por tamaño de objeto**: el notebook no las calcula. El argumento del
  casco como objeto pequeño va en la Discusión.

---

## 3. Resultados  ·  ~1,8 páginas  ·  reportar SIN interpretar

**(1) Desempeño agregado**

> La Tabla 2 recoge el desempeño de los tres modelos sobre el conjunto de prueba de 2 171
> imágenes. El orden es consistente en las dos métricas principales: YOLO26n obtiene la mAP50
> más alta, 0,8592, seguido de YOLO11n con 0,8473 y de la línea base YOLOv8n con 0,8415; en
> mAP50-95 los valores son 0,5322, 0,5223 y 0,5215 respectivamente. La diferencia entre el
> modelo propuesto y la línea base es de 0,0177 en mAP50, equivalente a una mejora relativa del
> 2,1 %. El número de parámetros sigue el orden inverso: 2 534 372 en YOLO26n frente a
> 3 138 246 en YOLOv8n, un 19 % menos. Los tiempos de entrenamiento fueron de 120,4, 121,9 y
> 132,9 minutos, siendo el modelo propuesto el más costoso de entrenar de los tres.

**(2) Precisión y exhaustividad**

> Las dos métricas que componen la mAP se comportan de forma divergente. YOLO26n registra la
> exhaustividad más alta de los tres modelos, 0,8526, frente a 0,8316 de YOLO11n y 0,8253 de la
> línea base. En precisión, en cambio, ocupa la última posición: 0,7505, por debajo de 0,7647 y
> 0,7586. La Figura 3 muestra la evolución de ambas métricas a lo largo de las 50 épocas, junto
> con las curvas de pérdida de los tres componentes del objetivo de entrenamiento.

**(3) Desagregado por clase**

> La Tabla 3 desagrega el desempeño por clase. En los tres modelos la clase `casco` obtiene
> valores sustancialmente superiores a `chaleco`: 0,9251 frente a 0,7933 en YOLO26n, con una
> diferencia de 0,1318. La misma brecha es de 0,1416 en YOLO11n y de 0,1509 en la línea base.
> La mejora del modelo propuesto respecto a la línea base se distribuye de forma desigual entre
> ambas clases: 0,0272 en `chaleco` y 0,0081 en `casco`. La Figura 2 presenta las matrices de
> confusión normalizadas, donde se observa ⟦describir qué muestran: dónde se concentran las
> confusiones y con qué clase⟧.

**(4) Ejemplos**

> La Figura 4 reúne predicciones del modelo propuesto sobre imágenes del conjunto de prueba,
> seleccionadas para incluir tanto detecciones correctas como fallos. ⟦describir los casos
> elegidos: qué se detecta bien y en qué situaciones falla — oclusión, escala, iluminación⟧.

**Pies**

> Tabla 2. Desempeño de los tres modelos sobre el conjunto de prueba, bajo protocolo de
> entrenamiento idéntico. Se reportan las métricas agregadas, el número de parámetros y el
> tiempo de entrenamiento.
>
> Tabla 3. Precisión media por clase a un umbral de solapamiento de 0,50, y diferencia entre
> ambas clases para cada modelo.
>
> Figura 2. Matrices de confusión normalizadas sobre el conjunto de prueba.
>
> Figura 3. Evolución de las métricas de desempeño y de las componentes de la función de
> pérdida durante las 50 épocas de entrenamiento.
>
> Figura 4. Predicciones del modelo propuesto sobre imágenes del conjunto de prueba, con casos
> de acierto y de error.

**Irrenunciables**

- **Ninguna interpretación.** Ni «mejora porque», ni «lo que indica». Eso es la Sección 4.
- La mejora **en puntos y en porcentaje**, y el dato de parámetros.
- La **divergencia precisión/exhaustividad** reportada como dato, sin valorarla aún.
- La brecha por clase y el reparto desigual de la ganancia.
- Que YOLO26n fue **el más lento de entrenar**: omitirlo sería selectivo.

---

## 4. Discusión  ·  ~1,2 páginas  ·  Rúbrica: discusión y análisis (2,6 pts)

**(a) Comparación con la línea base y explicación**

> La mejora de 0,0177 en mAP50 sobre la línea base se obtiene con un 19 % menos de parámetros,
> una combinación que merece atención: el modelo propuesto no mejora por disponer de mayor
> capacidad, sino con menos. Dado que las tres arquitecturas se entrenaron con el mismo corpus,
> los mismos aumentos, la misma semilla y el mismo conjunto de hiperparámetros, la diferencia
> observada es atribuible a la arquitectura y no al procedimiento. Conviene, no obstante,
> delimitar el alcance de esa atribución: el experimento compara generaciones completas, no
> componentes aislados, de modo que no permite establecer cuál de los cambios arquitectónicos
> introducidos en la nueva generación produce la ganancia. Determinarlo exigiría un estudio de
> ablación que queda fuera del alcance de este trabajo. La magnitud de la mejora, por otra
> parte, es modesta en términos absolutos, y se obtiene sobre una única ejecución por modelo:
> no se dispone de varias repeticiones con semillas distintas que permitan estimar la
> variabilidad del procedimiento y contrastar la diferencia frente a ella.

**(b) Análisis de errores**

> El análisis por clase revela que el error se concentra de forma sistemática en el chaleco, con
> una diferencia cercana a los trece puntos respecto al casco en el modelo propuesto. Esa brecha
> se corresponde con el desbalance medido en el corpus, donde las instancias de casco superan a
> las de chaleco en una razón de 4,84 a 1. Resulta significativo que la mejora del modelo
> propuesto se concentre precisamente en la clase peor representada —0,0272 frente a 0,0081—, lo
> que sugiere que el margen de mejora disponible era mayor donde los datos eran más débiles.
> Dos factores adicionales del dominio contribuyen al error. El primero es el régimen de objeto
> pequeño del casco: su área mediana en las fuentes medidas se sitúa entre el 0,45 % y el 1,2 %
> de la imagen, lo que lo coloca en el rango donde los detectores de una sola etapa pierden
> precisión de localización. El segundo es la oclusión mutua entre trabajadores en planos con
> varias personas, frecuente en imagen de obra.
>
> El resultado que exige una lectura más matizada es el compromiso entre precisión y
> exhaustividad. El modelo propuesto detecta más —exhaustividad de 0,8526, la más alta de los
> tres— pero se equivoca con mayor frecuencia al hacerlo, con la precisión más baja, 0,7505.
> Para la aplicación considerada ese intercambio es favorable, por la asimetría de costes ya
> expuesta: un trabajador sin casco no detectado constituye un riesgo real, mientras que una
> detección espuria se resuelve con una verificación. Conviene, sin embargo, declararlo de forma
> explícita, porque en un despliegue operativo una tasa elevada de falsas alarmas degrada la
> confianza del personal en el sistema y puede llevar a desatenderlo.

**(c) Limitaciones**

> El trabajo presenta varias limitaciones que conviene explicitar. En cuanto a los datos, el
> corpus reúne tres fuentes con paradigmas de anotación heterogéneos, y dos de ellas no han
> pasado revisión por pares; el redimensionado a una resolución cuadrada introduce además
> deformación en imágenes de proporción distinta. El esquema de dos clases positivas, adoptado
> deliberadamente, no modela el incumplimiento: las clases que marcan la ausencia del equipo
> están disponibles de forma desigual entre las fuentes —*PPE Combined Model* las incluye para
> casco y chaleco, *Construction-PPE* solo para el casco y CHV no las contempla—, y su
> aprovechamiento exigiría un planteamiento distinto. En cuanto al experimento, los tres
> modelos se evaluaron en su escala más ligera y en una única ejecución, sin repeticiones que
> permitan estimar la variabilidad. En cuanto a la revisión de literatura, la búsqueda se
> ejecutó sobre una sola base de datos bibliográfica, al no disponerse de acceso institucional
> a Web of Science, lo que puede haber dejado fuera estudios indexados únicamente allí.

**(d) Conclusión y trabajo futuro**

> Los resultados obtenidos indican que la generación más reciente de la familia YOLO aporta una
> mejora consistente en la detección de casco y chaleco de seguridad respecto a las dos
> generaciones precedentes, evaluadas bajo condiciones idénticas, y que lo hace con un modelo
> sensiblemente más ligero. La ganancia se concentra en la clase peor representada en los datos,
> y viene acompañada de un desplazamiento del equilibrio entre precisión y exhaustividad que
> resulta favorable para la aplicación considerada. La brecha de desempeño entre ambas clases
> persiste, sin embargo, en los tres modelos, lo que señala el desbalance de los datos —y no la
> arquitectura— como el factor limitante dominante.
>
> Tres líneas de continuación se desprenden de este trabajo. La primera es la evaluación del
> modo de inferencia sin supresión de no máximos que ofrece la arquitectura empleada, cuyo
> interés es particularmente claro en escenas con oclusión entre trabajadores. La segunda es el
> estudio de la capacidad de generalización entre fuentes, reservando uno de los conjuntos como
> prueba externa en lugar de integrarlo en el entrenamiento; la implementación empleada ya
> contempla esa configuración, aunque exigiría reentrenar los tres modelos. La tercera es el
> aprovechamiento de las clases que marcan la ausencia del equipo, disponibles en parte del
> corpus, para pasar de la detección del equipo a la verificación de su uso efectivo.

**Irrenunciables**

- (a) tiene que **explicar**, no solo comparar. Y delimitar hasta dónde llega la atribución.
- La **ausencia de ablación y de repeticiones** reconocida. Es lo que separa rigor de entusiasmo.
- (b) el compromiso precisión/exhaustividad **declarado**, incluido su riesgo operativo.
- (c) la limitación de las clases negativas **bien formulada**: es exclusión deliberada, no
  inexistencia. Hay 12 965 `NO-Hardhat` y 2 022 `NO-Safety Vest` disponibles sin usar.
- (d) la conclusión **anclada en lo medido**, y el trabajo futuro con las tres líneas de D16.

---

## Declaración sobre el uso de herramientas de inteligencia artificial

> Los autores declaran el uso de herramientas de inteligencia artificial generativa durante la
> realización de este trabajo, en los siguientes términos. ⟦Nombrar la herramienta y el
> periodo⟧ se empleó como apoyo en: la definición de la estructura del artículo y de los
> documentos de trabajo del proyecto; la discusión de decisiones metodológicas, incluidas la
> formulación de los criterios de inclusión y exclusión y la construcción de las cadenas de
> búsqueda; la ejecución de un primer tamizaje automatizado de los registros recuperados, cuyo
> resultado fue posteriormente revisado por los revisores humanos; la medición y el análisis
> comparativo de los conjuntos de datos candidatos; la escritura y depuración del código de
> preparación de datos, entrenamiento y despliegue; la verificación de las cifras reportadas
> contra los archivos de datos originales; y la elaboración de párrafos de referencia que los
> autores leyeron, evaluaron y reescribieron para producir el texto final.
>
> La redacción del artículo es obra de los autores. Las decisiones metodológicas, la
> interpretación de los resultados y las conclusiones son igualmente de su responsabilidad, así
> como la verificación de toda la información reportada.

**Irrenunciables**

- Declarar también el **apoyo técnico**, no solo el de redacción: código, análisis, cribado.
- La mención a los **párrafos de referencia**, para que la declaración refleje lo que de verdad
  ocurrió. Declarar de menos es el único riesgo real en este apartado.
- **Nombrar la herramienta y el periodo** de uso.

---

## Orden sugerido de redacción

1. **2.2 → 2.3 → 2.4 → 2.5 → 2.6** — Métodos completo, sin dependencias
2. **3 Resultados** — todas las cifras están
3. **4 Discusión** — depende de que Resultados esté escrito
4. **2.1 PRISMA** — con huecos hasta el 1 de noviembre
5. **1 Introducción** — el párrafo (b) exige leer los PDF
6. **Declaración de IA**
7. **Resumen** — el último
8. **Figura 1** — cuando cierre el cribado
