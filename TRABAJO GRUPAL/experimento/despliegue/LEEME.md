# Servicio de inferencia — despliegue

API que sirve el detector de casco y chaleco. Pensada para la **demo en vivo de la
defensa oral**, que vale 6 de los 20 puntos del examen final.

## Estado

| | |
|---|---|
| Servidor | Contabo VPS · `213.136.69.236` · Rocky Linux 9.8 |
| Ruta | `/opt/epp-yolo26` |
| Puerto | **8090** |
| Imagen | `epp-yolo26-epp-yolo26:latest` |
| Desplegado | 2026-10-09 ✅ |
| Interfaz | v0.2 — visualización de cajas sobre la imagen |
| Modelo | ⬜ pendiente de entrenamiento |

## Endpoints

| Ruta | Qué hace |
|---|---|
| `GET /` | Interfaz de demostración: arrastrar imagen, ver detecciones dibujadas |
| `GET /salud` | Estado del servicio y si hay pesos cargados |
| `GET /docs` | Documentación interactiva de la API |
| `POST /detectar` | Recibe una imagen y un umbral opcional, devuelve detecciones en JSON |

Prueba: http://213.136.69.236:8090/salud

## La interfaz

Pensada para la **defensa oral**, donde se proyecta en aula:

- Las detecciones se dibujan sobre la imagen en un canvas, no se devuelven solo como JSON
- Ámbar para `casco`, verde azulado para `chaleco`: cálido contra frío, distinguibles sobre
  fotografías de obra, que suelen ser de tonos terrosos
- Fondo claro, porque los proyectores lavan los fondos oscuros
- **Umbral ajustable en vivo**: bajarlo hace aparecer falsos positivos y subirlo los elimina.
  Buen recurso si en la defensa preguntan por el compromiso precisión-exhaustividad
- Si no hay pesos, la barra superior lo indica y la página sigue siendo navegable

## Decisiones de diseño

- **Torch en variante CPU** (`/whl/cpu`): ~200 MB en lugar de ~2,5 GB. El servidor no
  tiene GPU, así que arrastrar CUDA sería desperdicio.
- **Carga diferida del modelo**: el contenedor arranca aunque no haya pesos. Permitió
  desplegar y validar antes de entrenar.
- **Red Docker propia** (`epp-yolo26_epp`): aislada de los 12 contenedores del stack
  de trabajo que ya corría en el servidor. No se tocó ninguno.

## Cuando haya modelo entrenado

```bash
# 1. Copiar los pesos desde donde los produjo Kaggle
scp best.pt root@213.136.69.236:/opt/epp-yolo26/pesos/

# 2. Reiniciar para que los tome
ssh root@213.136.69.236 "cd /opt/epp-yolo26 && docker compose restart"

# 3. Verificar
ssh root@213.136.69.236 "curl -s localhost:8090/salud"
```

Debe pasar a `"pesos_presentes": true`.

## Operación

```bash
cd /opt/epp-yolo26
docker compose logs -f        # ver registros
docker compose restart        # reiniciar
docker compose down           # detener y eliminar
docker compose up -d --build  # reconstruir tras cambios
```

## Nota de seguridad

El puerto 8090 está **expuesto a internet**, igual que el resto del stack del servidor.
Para un servicio de inferencia sin datos sensibles el riesgo es bajo, pero cualquiera
podría consumir CPU enviando imágenes.

Si se prefiere cerrarlo, cambiar en `docker-compose.yml`:

```yaml
ports:
  - "127.0.0.1:8090:8090"
```

y acceder por túnel SSH: `ssh -L 8090:localhost:8090 root@213.136.69.236`.
