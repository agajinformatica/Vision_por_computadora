#!/usr/bin/env bash
# Empaqueta el dataset unificado para subirlo como Kaggle Dataset.
#
# El dataset_unificado usa enlaces simbólicos para no duplicar los 6 GB de datos
# crudos. `zip` sin la opción -y sigue los enlaces y almacena el contenido real,
# que es lo que necesitamos para subirlo.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORIGEN="$DIR/dataset_unificado"
SALIDA="$DIR/epp-casco-chaleco-yolo26.zip"

[ -d "$ORIGEN" ] || { echo "No existe $ORIGEN. Ejecuta antes 01_preparar_dataset.py" >&2; exit 1; }
[ -f "$SALIDA" ] && { echo "Ya existe $SALIDA. Bórralo para regenerar." >&2; exit 1; }

cd "$ORIGEN"
echo "Empaquetando $(find train val test -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' | wc -l) imágenes..."
zip -r -q -1 "$SALIDA" \
    train val test data.yaml estadisticas.json manifiesto.csv \
    -x '*.DS_Store'

echo
echo "Generado: $SALIDA"
du -h "$SALIDA" | awk '{print "  tamaño: "$1}'
unzip -l "$SALIDA" | tail -1 | awk '{print "  entradas: "$2}'
