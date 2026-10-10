#!/usr/bin/env python3
"""
Unificación de los tres conjuntos de datos a un esquema de dos clases positivas.

    0 = casco      1 = chaleco

Fuentes y mapeo (decidido el 2026-10-09, ver GUIA_INVESTIGADOR.md D10):

  Roboflow PPE Combined v8   Hardhat(3) -> casco      Safety Vest(13) -> chaleco
  Construction-PPE           helmet(0)  -> casco      vest(2)         -> chaleco
  CHV                        casco en 4 colores(2-5) -> casco   vest(1) -> chaleco

Se conservan las particiones originales de cada fuente: no se re-particiona, para
no mezclar imágenes que los autores separaron deliberadamente.

Las imágenes sin ninguna clase relevante se descartan. Las etiquetas vacías
resultantes se conservan como negativos, que reducen falsos positivos.

Uso:
    python3 01_preparar_dataset.py                 # fusiona los tres
    python3 01_preparar_dataset.py --chv-externo   # CHV queda fuera del
                                                   # entrenamiento, como test externo
"""
import argparse, csv, json, shutil, sys
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path(__file__).resolve().parent.parent / "dataset"
SALIDA = Path(__file__).resolve().parent / "dataset_unificado"
CLASES = ["casco", "chaleco"]

FUENTES = {
    "roboflow": {
        "raiz": BASE / "Personal Protective Equipment - Combined Model.v8i.yolo26",
        "mapeo": {3: 0, 13: 1},
        "splits": {"train": "train", "val": "valid", "test": "test"},
        "layout": "yolo_split",          # <raiz>/<split>/{images,labels}
    },
    "construction-ppe": {
        "raiz": BASE / "Construction-PPE",
        "mapeo": {0: 0, 2: 1},
        "splits": {"train": "train", "val": "val", "test": "test"},
        "layout": "yolo_plano",          # <raiz>/{images,labels}/<split>
    },
    "chv": {
        "raiz": BASE / "CHV" / "CHV_dataset",
        "mapeo": {2: 0, 3: 0, 4: 0, 5: 0, 1: 1},
        "splits": {"train": "train", "val": "valid", "test": "test"},
        "layout": "chv",                 # listas en "data split/<x>.txt"
    },
}


def pares(cfg, split_dir):
    """Devuelve [(ruta_imagen, ruta_etiqueta)] de una partición."""
    raiz, layout = cfg["raiz"], cfg["layout"]
    if layout == "yolo_split":
        img_d, lbl_d = raiz / split_dir / "images", raiz / split_dir / "labels"
    elif layout == "yolo_plano":
        img_d, lbl_d = raiz / "images" / split_dir, raiz / "labels" / split_dir
    else:  # chv
        lista = raiz / "data split" / f"{split_dir}.txt"
        if not lista.exists():
            return []
        out = []
        for linea in lista.read_text(encoding="utf-8", errors="ignore").splitlines():
            linea = linea.strip()
            if not linea:
                continue
            img = raiz / Path(linea).name if (raiz / Path(linea).name).exists() \
                  else raiz / "images" / Path(linea).name
            lbl = raiz / "annotations" / (Path(linea).stem + ".txt")
            if img.exists() and lbl.exists():
                out.append((img, lbl))
        return out
    if not img_d.is_dir() or not lbl_d.is_dir():
        return []
    out = []
    for img in sorted(img_d.iterdir()):
        if img.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        lbl = lbl_d / (img.stem + ".txt")
        if lbl.exists():
            out.append((img, lbl))
    return out


def remapear(lbl_path, mapeo):
    """Traduce las clases; devuelve las líneas conservadas y cuántas se descartaron."""
    conservadas, descartadas, malformadas = [], 0, 0
    for linea in lbl_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        campos = linea.split()
        if len(campos) < 5:
            if campos:
                malformadas += 1
            continue
        try:
            c = int(float(campos[0]))
            coords = [float(x) for x in campos[1:5]]
        except ValueError:
            malformadas += 1
            continue
        if not all(0.0 <= v <= 1.0 for v in coords):
            malformadas += 1
            continue
        if c in mapeo:
            conservadas.append(f"{mapeo[c]} " + " ".join(f"{v:.6f}" for v in coords))
        else:
            descartadas += 1
    return conservadas, descartadas, malformadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chv-externo", action="store_true",
                    help="excluye CHV del entrenamiento; queda solo como test externo")
    ap.add_argument("--enlaces", action="store_true",
                    help="crea enlaces simbólicos en vez de copiar (ahorra ~5 GB)")
    args = ap.parse_args()

    if SALIDA.exists():
        print(f"La carpeta {SALIDA} ya existe. Bórrala para regenerar.", file=sys.stderr)
        return 1

    destinos = ["train", "val", "test"] + (["test_chv_externo"] if args.chv_externo else [])
    for d in destinos:
        (SALIDA / d / "images").mkdir(parents=True)
        (SALIDA / d / "labels").mkdir(parents=True)

    stats = defaultdict(lambda: {"img": 0, "vacias": 0, "cajas": Counter(),
                                 "descartadas": 0, "malformadas": 0, "sin_relevante": 0})
    manifiesto = []

    for nombre, cfg in FUENTES.items():
        if not cfg["raiz"].exists():
            print(f"  AVISO: no se encuentra {cfg['raiz']} — se omite {nombre}")
            continue
        for destino, origen in cfg["splits"].items():
            if nombre == "chv" and args.chv_externo:
                destino_real = "test_chv_externo"
                if origen != "test":
                    continue
            else:
                destino_real = destino

            for img, lbl in pares(cfg, origen):
                lineas, desc, mal = remapear(lbl, cfg["mapeo"])
                k = f"{nombre}/{destino_real}"
                stats[k]["descartadas"] += desc
                stats[k]["malformadas"] += mal
                if not lineas:
                    stats[k]["sin_relevante"] += 1
                    continue
                base = f"{nombre}__{img.stem}"
                dst_i = SALIDA / destino_real / "images" / f"{base}{img.suffix.lower()}"
                dst_l = SALIDA / destino_real / "labels" / f"{base}.txt"
                if args.enlaces:
                    dst_i.symlink_to(img.resolve())
                else:
                    shutil.copy2(img, dst_i)
                dst_l.write_text("\n".join(lineas) + "\n", encoding="utf-8")
                stats[k]["img"] += 1
                for l in lineas:
                    stats[k]["cajas"][int(l[0])] += 1
                manifiesto.append({"destino": destino_real, "fuente": nombre,
                                   "archivo": dst_i.name, "origen": str(img.relative_to(BASE))})

    # ---- data.yaml para YOLO26 ----
    y = [f"path: {SALIDA.resolve()}", "train: train/images", "val: val/images",
         "test: test/images", "", "nc: 2", "names:", "  0: casco", "  1: chaleco"]
    if args.chv_externo:
        y.append("")
        y.append("# Evaluación externa: test_chv_externo/images")
    (SALIDA / "data.yaml").write_text("\n".join(y) + "\n", encoding="utf-8")

    with open(SALIDA / "manifiesto.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["destino", "fuente", "archivo", "origen"])
        w.writeheader(); w.writerows(manifiesto)

    # ---- informe ----
    print(f"\n{'fuente / partición':<34}{'imgs':>7}{'casco':>9}{'chaleco':>9}"
          f"{'descart.':>10}{'sin rel.':>10}")
    print("-" * 79)
    tot = Counter(); tot_img = 0
    por_split = defaultdict(lambda: Counter())
    for k in sorted(stats):
        s = stats[k]
        print(f"{k:<34}{s['img']:>7}{s['cajas'][0]:>9}{s['cajas'][1]:>9}"
              f"{s['descartadas']:>10}{s['sin_relevante']:>10}")
        tot += s["cajas"]; tot_img += s["img"]
        por_split[k.split("/")[1]] += s["cajas"]
        por_split[k.split("/")[1]]["img"] += s["img"]
    print("-" * 79)
    print(f"{'TOTAL':<34}{tot_img:>7}{tot[0]:>9}{tot[1]:>9}")
    mal = sum(s["malformadas"] for s in stats.values())
    if mal:
        print(f"\n  Líneas malformadas descartadas: {mal}")
    print(f"\n{'partición':<22}{'imgs':>8}{'casco':>9}{'chaleco':>9}{'razón':>9}")
    for sp in ("train", "val", "test", "test_chv_externo"):
        if sp in por_split:
            c = por_split[sp]
            r = c[0] / c[1] if c[1] else 0
            print(f"{sp:<22}{c['img']:>8}{c[0]:>9}{c[1]:>9}{r:>8.2f}:1")
    json.dump({k: {"img": v["img"], "casco": v["cajas"][0], "chaleco": v["cajas"][1],
                   "descartadas": v["descartadas"], "sin_relevante": v["sin_relevante"],
                   "malformadas": v["malformadas"]} for k, v in stats.items()},
              open(SALIDA / "estadisticas.json", "w"), indent=2, ensure_ascii=False)
    print(f"\nGenerado en: {SALIDA}")
    print("  data.yaml  manifiesto.csv  estadisticas.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
