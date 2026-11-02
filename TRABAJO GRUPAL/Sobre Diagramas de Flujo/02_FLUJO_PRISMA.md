# 02 · Flujo de la revisión sistemática

Cómo funciona el embudo PRISMA y en qué punto estamos.
**Actualizado: 2026-11-02 (cribado cerrado)**

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

    subgraph ELE["ELEGIBILIDAD · selección documental y recuperación"]
        E1["148 cribados por I1-I7"]:::ok
        E2["Excluidos en selección documental: 51<br/>39 E3 · 12 E4"]:::ok
        E3["97 buscados para recuperación"]:::ok
        E4["No recuperados: 22 (E5)"]:::ok
        E5["75 evaluados<br/>0 excluidos tras la evaluación"]:::ok
    end
    C1 --> E1 --> E3 --> E5
    E1 --> E2
    E3 --> E4

    INC(["ESTUDIOS INCLUIDOS: 75<br/>alimentan la Introduccion"]):::ok
    E5 --> INC

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
| Duplicados eliminados | 0 (sin DOI repetidos; sin WoS no hubo deduplicación) |
| Cribados por título y resumen | 158 |
| Excluidos en cribado | **10** |
| Cribados por criterios I1-I7 (selección documental) | **148** |
| Excluidos en selección documental | **51** (39 E3, 12 E4) |
| Buscados para recuperación | **97** |
| No recuperados (E5) | **22** |
| Evaluados para elegibilidad | **75** |
| Excluidos tras la evaluación | 0 |
| **Estudios incluidos** | **75** |

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
Se planteó con tres revisores (R1, R2, R3); en la práctica fueron asistentes de IA. Se reporta cuántas discrepancias hubo (28).
