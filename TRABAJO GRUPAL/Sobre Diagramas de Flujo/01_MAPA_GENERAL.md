# 01 · Mapa general del proyecto

Los cuatro frentes de trabajo y cómo confluyen en el artículo.
**Actualizado: 2026-10-09**

```mermaid
flowchart TB
    subgraph BIB["A · Bibliografía y revisión sistemática"]
        direction TB
        B1["Protocolo PRISMA<br/>pregunta + criterios"]:::ok
        B2["Busqueda Scopus<br/>158 registros"]:::ok
        B3["Cribado titulo/resumen<br/>10 excluidos, 148 pasan"]:::ok
        B4["Busqueda WoS"]:::blocked
        B5["Cribado texto completo<br/>148 papers"]:::todo
        B6["Estudios incluidos<br/>+ diagrama de flujo"]:::todo
        B1 --> B2 --> B3 --> B5 --> B6
        B4 -.-> B5
    end

    subgraph DAT["B · Datos"]
        direction TB
        D1["4 datasets descargados<br/>y medidos"]:::ok
        D2["Esquema de 2 clases<br/>casco + chaleco"]:::ok
        D3["Dataset unificado<br/>20 944 imagenes"]:::ok
        D1 --> D2 --> D3
    end

    subgraph EXP["C · Experimento"]
        direction TB
        E1["Linea base: 3 modelos"]:::ok
        E2["Notebook de entrenamiento"]:::ok
        E3["Entrenamiento en Kaggle<br/>50 epocas x 3 modelos"]:::ok
        E4["RESULTADOS<br/>YOLO26n mAP50 0.859"]:::ok
        E1 --> E2 --> E3 --> E4
    end

    subgraph RED["D · Redaccion · 100% humana"]
        direction TB
        R1["Esqueleto del articulo"]:::ok
        R2["Introduccion"]:::todo
        R3["Metodos"]:::todo
        R4["Resultados"]:::todo
        R5["Discusion"]:::todo
        R1 --> R2 & R3 & R4 & R5
    end

    PAPER(["Articulo final<br/>6-8 paginas"]):::meta

    B6 --> R2
    D3 --> E2
    D3 --> R3
    E4 --> R4 --> R5
    R2 & R3 & R4 & R5 --> PAPER

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef todo fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef blocked fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef meta fill:#cfe2ff,stroke:#0d6efd,color:#084298
```

| | |
|---|---|
| 🟩 verde | completado |
| 🟨 amarillo | pendiente |
| 🟥 rojo | bloqueado por algo externo |

## Lectura rápida

- **Los datos están resueltos.** El frente B está completo y alimenta tanto al experimento como a la sección de Métodos.
- **El experimento está resuelto**: YOLO26n alcanza mAP50 0,8592 y supera a la línea base.
- **La bibliografía va a medias**: el protocolo y Scopus están hechos; falta WoS y el cribado de texto completo.
- **La redacción solo tiene el esqueleto**, y depende de que lleguen resultados.
