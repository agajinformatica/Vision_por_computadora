# 02 · Flujo de la revisión sistemática

Cómo funciona el embudo PRISMA y en qué punto estamos.
**Actualizado: 2026-10-09**

```mermaid
flowchart TB
    subgraph ID["IDENTIFICACION"]
        I1["Scopus<br/>158 registros"]:::ok
        I2["Web of Science<br/>sin acceso institucional"]:::blocked
        I3["Otros metodos<br/>9 referencias"]:::ok
    end

    DUP{"Eliminar<br/>duplicados"}:::todo
    I1 --> DUP
    I2 -.-> DUP
    I3 --> DUP

    subgraph CRIB["CRIBADO · titulo y resumen"]
        C1["Leer solo la ficha<br/>Regla: ante la duda, pasa"]:::ok
        C2["Excluidos: 10<br/>7 por E3 · 3 por E1"]:::ok
    end
    DUP --> C1 --> C2

    subgraph ELE["ELEGIBILIDAD · texto completo"]
        E1["148 textos a evaluar<br/>79 alta confianza<br/>69 a verificar"]:::todo
        E2["Excluidos con motivo<br/>codigos E1 a E6"]:::todo
    end
    C1 --> E1 --> E2

    INC(["ESTUDIOS INCLUIDOS<br/>alimentan la Introduccion"]):::meta
    E1 --> INC

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef todo fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef blocked fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef meta fill:#cfe2ff,stroke:#0d6efd,color:#084298
```

## Por qué dos etapas de lectura

```mermaid
flowchart LR
    A["Cribado<br/>titulo y resumen"] -->|"rapido y permisivo<br/>ante la duda, PASA"| B["Elegibilidad<br/>texto completo"]
    B -->|"lento y estricto<br/>cada exclusion con MOTIVO"| C["Incluido"]

    classDef n fill:#e9ecef,stroke:#6c757d,color:#212529
    class A,B,C n
```

Descartar en la primera etapa un estudio válido es un error **irreversible**; leer de más un
texto completo solo cuesta tiempo. Por eso la primera es permisiva y la segunda, estricta.

## Estado del embudo

| Casilla | Valor |
|---|---|
| Identificados en bases de datos | **158** · Scopus |
| Identificados por otros métodos | 9 |
| Duplicados eliminados | — *(al sumar WoS)* |
| Cribados por título y resumen | 158 |
| Excluidos en cribado | **10** |
| Buscados para recuperación | **148** |
| Evaluados en texto completo | — |
| Excluidos en texto completo, con motivo | — |
| **Estudios incluidos** | — |

## Quién hace qué

```mermaid
flowchart LR
    R1["Revisor 1"] --> D{"¿Coinciden?"}
    R2["Revisor 2"] --> D
    D -->|si| OK["Decision firme"]:::ok
    D -->|no| R3["Revisor 3<br/>dirime"] --> OK

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
```

PRISMA exige **dos revisores independientes** y un tercero que resuelva discrepancias.
El equipo son tres personas, así que encaja exacto. Se reporta cuántas discrepancias hubo.
