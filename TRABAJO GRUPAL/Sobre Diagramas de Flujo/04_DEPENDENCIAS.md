# 04 · Dependencias, bloqueos y ruta crítica

Qué espera a qué. **Actualizado: 2026-10-09**

```mermaid
flowchart LR
    subgraph EXT["Fuera de nuestro control"]
        X1["Consulta al docente<br/>congresos · ESCI · fechas"]:::blocked
        X2["Acceso WoS<br/>biblioteca UNMSM"]:::blocked
    end

    subgraph NADA["No dependen de nada"]
        Y1["Linea base<br/>3 modelos definidos"]:::ok
        Y2["Notebook listo<br/>+ dataset empaquetado"]:::ok
        Y3["Entrenar en Kaggle"]:::ok
        Y4["PRIMER RESULTADO<br/>mAP50 0.859"]:::ok
        Y1 --> Y2 --> Y3 --> Y4
    end

    subgraph DEP["Dependen de algo"]
        Z1["Cadena definitiva<br/>en las bases correctas"]:::todo
        Z2["Cribado texto completo<br/>148 papers"]:::todo
        Z3["Diagrama de flujo<br/>con numeros reales"]:::todo
        Z4["Introduccion"]:::todo
    end

    X1 --> Z1 --> Z2 --> Z3
    X2 --> Z1
    Z2 --> Z4

    PARCIAL(["EXAMEN PARCIAL<br/>semana 10 · 20% de la nota"]):::meta
    Y4 ==> PARCIAL
    Z4 -.-> PARCIAL

    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef todo fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef blocked fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef crit fill:#ff8787,stroke:#c92a2a,color:#fff
    classDef meta fill:#cfe2ff,stroke:#0d6efd,color:#084298
```

## La ruta crítica

**El prototipo no depende de nada.** Ni del docente, ni de WoS, ni del cribado.
Se puede ejecutar hoy, y es lo único que la rúbrica no perdona en el parcial.

```mermaid
flowchart LR
    A["Linea base"]:::ok --> B["Notebook"]:::ok --> C["Entrenar en Kaggle"]:::ok --> D["Primer resultado"]:::ok
    D --> E["6 puntos del parcial"]:::meta

    classDef crit fill:#ff8787,stroke:#c92a2a,color:#fff
    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef meta fill:#cfe2ff,stroke:#0d6efd,color:#084298
```

## La aritmética que lo justifica

| Escenario | Nota del parcial |
|---|---|
| Sin prototipo, todo lo demás excelente | **14 / 20** — aprueba raspando |
| Prototipo aceptable | 17,6 / 20 |
| Prototipo excelente | 20 / 20 |

Sin prototipo el techo es 14, y solo bordando los otros tres criterios.
Cualquier tropiezo adicional y se desaprueba.

## Pendientes, por urgencia

| # | Pendiente | Bloqueado por | Coste de resolverlo |
|---|---|---|---|
| **P1-P3** | Congresos · ESCI · fechas | consulta al docente | un mensaje |
| P4 | Acceso a WoS | biblioteca UNMSM | una gestión |
| P7 | Asignación de revisores | decisión del equipo | 5 minutos |

Las dos primeras son baratísimas y desbloquean mucho. Conviene resolverlas ya.
