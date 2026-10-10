# 03 · Pipeline del experimento

Del dato crudo al resultado. **Actualizado: 2026-10-09**

```mermaid
flowchart TB
    subgraph CRUDO["Datos crudos · 6,1 GB"]
        A1["Roboflow Combined v8<br/>44 002 img · 14 clases"]:::ok
        A2["Construction-PPE<br/>1 416 img · 11 clases"]:::ok
        A3["CHV<br/>1 330 img · 6 clases"]:::ok
        A4["Pictor-v3<br/>DESCARTADO<br/>solo 42 chalecos"]:::out
    end

    SCRIPT["01_preparar_dataset.py<br/>remapeo a 2 clases + filtrado"]:::ok
    A1 & A2 & A3 --> SCRIPT

    UNIF["dataset_unificado<br/>20 944 img · casco + chaleco<br/>train 14 729 · val 4 044 · test 2 171"]:::ok
    SCRIPT --> UNIF
    SCRIPT -.->|"descartadas"| DESC["25 804 img<br/>sin clase relevante"]:::out

    subgraph ENTR["Entrenamiento · Kaggle GPU"]
        B1["YOLOv8n<br/>linea base simple"]:::todo
        B2["YOLO11n<br/>comparador directo"]:::todo
        B3["YOLO26n<br/>modelo propuesto"]:::todo
    end
    UNIF --> B1 & B2 & B3

    EVAL["Evaluacion sobre test<br/>mAP50 · mAP50-95 · recall<br/>desagregado por clase"]:::todo
    B1 & B2 & B3 --> EVAL

    FIG["Tablas y figuras<br/>del articulo"]:::todo
    EVAL --> FIG

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef todo fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef out fill:#e9ecef,stroke:#adb5bd,color:#495057
```

## Dónde corre cada cosa

```mermaid
flowchart LR
    L["Portatil<br/>i5 sin GPU"]:::no -->|"prepara y verifica<br/>datos"| K
    V["VPS Contabo<br/>12 nucleos, sin GPU"]:::half -->|"aloja el dataset"| K
    K["Kaggle<br/>GPU T4 o P100"]:::ok -->|"pesos best.pt"| V
    V -->|"sirve la demo<br/>en la defensa"| DEMO(["Demo en vivo"]):::meta

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef half fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef no fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef meta fill:#cfe2ff,stroke:#0d6efd,color:#084298
```

**Ninguna máquina local tiene GPU**, así que el entrenamiento va a Kaggle. El VPS no entrena,
pero resuelve el alojamiento del dataset y, más adelante, la demo para la defensa oral.

## El desbalance que arrastra el experimento

| Partición | Imágenes |  Casco | Chaleco |   Razón |
| ---------- | --------: | -----: | ------: | -------: |
| train      |    14 729 | 33 099 |   7 164 | 4,62 : 1 |
| val        |     4 044 |  9 512 |   1 629 | 5,84 : 1 |
| test       |     2 171 |  5 089 |   1 057 | 4,81 : 1 |

Hay casi **cinco cascos por cada chaleco**. Es esperable que las métricas de chaleco salgan
peores, y eso hay que reportarlo en Discusión, no ocultarlo.
