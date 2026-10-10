# Sobre Diagramas de Flujo

Carpeta **de uso interno** del equipo. No forma parte del artículo.
Su propósito es visualizar el proceso para entender y dar seguimiento a lo que se ejecuta.

| Archivo | Responde a la pregunta |
|---|---|
| [01_MAPA_GENERAL.md](01_MAPA_GENERAL.md) | ¿Cuáles son los frentes y cómo confluyen en el artículo? |
| [02_FLUJO_PRISMA.md](02_FLUJO_PRISMA.md) | ¿Cómo funciona la revisión sistemática y dónde estamos? |
| [03_PIPELINE_EXPERIMENTO.md](03_PIPELINE_EXPERIMENTO.md) | ¿Cómo se va del dato crudo al resultado? |
| [04_DEPENDENCIAS.md](04_DEPENDENCIAS.md) | ¿Qué espera a qué, y qué urge? |

## Cómo verlos

Los diagramas están escritos en **Mermaid** dentro de markdown. En VS Code se ven
renderizados con la vista previa — ya tienes instalada la extensión `bierner.markdown-mermaid`:

> Abre el archivo y pulsa **Ctrl+Shift+V**

Al ser texto, se editan como código y se versionan en git. Si un diagrama deja de reflejar
la realidad, se corrige la línea correspondiente, no hay que rehacer una imagen.

## Código de colores

| | |
|---|---|
| 🟩 verde | completado |
| 🟨 amarillo | pendiente |
| 🟥 rojo | bloqueado por algo externo al equipo |
| 🟦 azul | hito o entregable |
| ⬜ gris | descartado, o fuera del flujo principal |

## Relación con los demás documentos

| Documento | Para qué |
|---|---|
| `GUIA_INVESTIGADOR.md` | El **detalle**: decisiones, estado, bitácora, glosario |
| Esta carpeta | La **vista rápida**: el mismo estado, en diagramas |
| `metodologia Prisma/LEEME.md` | El estado específico de la revisión sistemática |

> Estos diagramas se actualizan cuando cambia el estado del proyecto.
> Si alguno no coincide con la realidad, avisar para corregirlo.
