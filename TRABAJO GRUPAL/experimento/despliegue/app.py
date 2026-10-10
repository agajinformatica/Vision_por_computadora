"""
API y demo de inferencia para detección de casco y chaleco de seguridad.

Expone:
    GET  /salud      estado del servicio y del modelo
    POST /detectar   recibe una imagen, devuelve las detecciones en JSON
    GET  /           interfaz web de demostración
"""
import io
import os
import time
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import HTMLResponse

PESOS = Path(os.getenv("PESOS", "/app/pesos/best.pt"))
UMBRAL = float(os.getenv("UMBRAL", "0.25"))
CLASES = {0: "casco", 1: "chaleco"}

app = FastAPI(title="Detección de EPP · YOLO26", version="0.2.0")
_modelo = None


def modelo():
    """Carga diferida: el contenedor arranca aunque aún no haya pesos."""
    global _modelo
    if _modelo is None:
        if not PESOS.exists():
            raise HTTPException(503, f"No hay pesos en {PESOS}. Entrena primero.")
        from ultralytics import YOLO
        _modelo = YOLO(str(PESOS))
    return _modelo


@app.get("/salud")
def salud():
    return {
        "estado": "activo",
        "pesos_presentes": PESOS.exists(),
        "ruta_pesos": str(PESOS),
        "modelo_cargado": _modelo is not None,
        "umbral": UMBRAL,
        "clases": CLASES,
    }


@app.post("/detectar")
async def detectar(imagen: UploadFile = File(...), conf: float = Form(None)):
    if not (imagen.content_type or "").startswith("image/"):
        raise HTTPException(400, "El archivo debe ser una imagen.")
    datos = await imagen.read()
    if not datos:
        raise HTTPException(400, "La imagen está vacía.")

    from PIL import Image
    try:
        img = Image.open(io.BytesIO(datos)).convert("RGB")
    except Exception:
        raise HTTPException(400, "No se pudo decodificar la imagen.")

    umbral = UMBRAL if conf is None else max(0.01, min(0.95, float(conf)))

    t0 = time.perf_counter()
    res = modelo().predict(img, conf=umbral, verbose=False)[0]
    ms = (time.perf_counter() - t0) * 1000

    det = []
    for c in res.boxes:
        x1, y1, x2, y2 = (round(float(v), 1) for v in c.xyxy[0])
        det.append({
            "clase": CLASES.get(int(c.cls), str(int(c.cls))),
            "confianza": round(float(c.conf), 3),
            "caja": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        })
    det.sort(key=lambda d: -d["confianza"])

    return {
        "archivo": imagen.filename,
        "dimensiones": {"ancho": img.width, "alto": img.height},
        "umbral": round(umbral, 2),
        "ms_inferencia": round(ms, 1),
        "total": len(det),
        "por_clase": {v: sum(1 for d in det if d["clase"] == v) for v in CLASES.values()},
        "detecciones": det,
    }


PAGINA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Detección de EPP · YOLO26</title>
<style>
  :root {
    --fondo:      #F5F7F7;
    --panel:      #FFFFFF;
    --panel-alt:  #EDF1F1;
    --tinta:      #15201F;
    --tinta-sv:   #536462;
    --tinta-db:   #8396938;
    --linea:      #D8E2E0;
    --acento:     #0F6B62;
    --acento-sv:  #DDEFEC;
    --casco:      #E89B1C;
    --chaleco:    #12A99B;
    --alerta:     #B2453A;
    --alerta-sv:  #F8E7E4;
    --sans: "Segoe UI", Roboto, -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    --mono: ui-monospace, "SF Mono", "Cascadia Mono", Menlo, Consolas, monospace;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: var(--fondo); color: var(--tinta);
    font-family: var(--sans); font-size: 16px; line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  .barra {
    background: var(--panel); border-bottom: 1px solid var(--linea);
    padding: .85rem clamp(1rem, 4vw, 2.5rem);
    display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;
  }
  .marca { display: flex; align-items: baseline; gap: .6rem; margin-right: auto; }
  .marca b { font-size: 1.05rem; font-weight: 650; letter-spacing: -.01em; }
  .marca span { font-family: var(--mono); font-size: .72rem; color: var(--tinta-sv); }
  .estado {
    display: inline-flex; align-items: center; gap: .45rem;
    font-size: .8rem; font-weight: 600;
    padding: .3rem .7rem; border-radius: 999px;
    background: var(--panel-alt); color: var(--tinta-sv);
  }
  .punto { width: .5rem; height: .5rem; border-radius: 50%; background: var(--tinta-sv); }
  .estado.ok    { background: var(--acento-sv); color: var(--acento); }
  .estado.ok    .punto { background: var(--acento); }
  .estado.falta { background: var(--alerta-sv); color: var(--alerta); }
  .estado.falta .punto { background: var(--alerta); }

  main {
    max-width: 1180px; margin: 0 auto;
    padding: clamp(1.2rem, 4vw, 2.5rem) clamp(1rem, 4vw, 2.5rem) 4rem;
    display: grid; gap: 1.5rem;
    grid-template-columns: minmax(0, 1fr);
  }
  @media (min-width: 900px) { main { grid-template-columns: minmax(0, 1fr) 320px; } }

  .lienzo-panel {
    background: var(--panel); border: 1px solid var(--linea);
    border-radius: 12px; overflow: hidden;
    display: flex; flex-direction: column; min-height: 420px;
  }

  #zona {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: .9rem; padding: 3rem 1.5rem; text-align: center;
    border: 2px dashed var(--linea); margin: .9rem; border-radius: 9px;
    transition: border-color .15s, background .15s; cursor: pointer;
  }
  #zona:hover, #zona.sobre { border-color: var(--acento); background: var(--acento-sv); }
  #zona h2 { margin: 0; font-size: 1.15rem; font-weight: 600; }
  #zona p  { margin: 0; color: var(--tinta-sv); font-size: .92rem; }
  .icono { width: 44px; height: 44px; color: var(--acento); }

  .boton {
    font: inherit; font-weight: 600; font-size: .92rem;
    border: none; border-radius: 8px; padding: .62rem 1.15rem;
    background: var(--acento); color: #fff; cursor: pointer;
  }
  .boton:hover { filter: brightness(1.08); }
  .boton.sec { background: var(--panel-alt); color: var(--tinta); border: 1px solid var(--linea); }
  .boton:disabled { opacity: .5; cursor: not-allowed; }
  :focus-visible { outline: 2px solid var(--acento); outline-offset: 2px; }

  #vista { display: none; flex-direction: column; flex: 1; }
  .lienzo-caja { position: relative; background: var(--panel-alt); display: grid; place-items: center; padding: .9rem; }
  canvas { max-width: 100%; height: auto; border-radius: 7px; display: block; }
  .pie {
    border-top: 1px solid var(--linea); padding: .7rem 1rem;
    display: flex; gap: .7rem; align-items: center; flex-wrap: wrap;
    font-size: .85rem; color: var(--tinta-sv);
  }
  .pie .sep { margin-left: auto; }

  aside { display: flex; flex-direction: column; gap: 1rem; }
  .tarjeta {
    background: var(--panel); border: 1px solid var(--linea);
    border-radius: 12px; padding: 1.1rem 1.2rem;
    display: flex; flex-direction: column; gap: .75rem;
  }
  .tarjeta h3 {
    margin: 0; font-size: .74rem; font-weight: 700;
    letter-spacing: .1em; text-transform: uppercase; color: var(--tinta-sv);
  }

  .marcadores { display: grid; grid-template-columns: 1fr 1fr; gap: .7rem; }
  .marcador { border-radius: 9px; padding: .7rem .85rem; border: 1px solid var(--linea); }
  .marcador .n { font-size: 1.85rem; font-weight: 680; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .marcador .t { font-size: .82rem; font-weight: 600; }
  .marcador.c { background: #FDF3E2; border-color: var(--casco); }
  .marcador.c .n, .marcador.c .t { color: #9A6306; }
  .marcador.v { background: #E2F6F3; border-color: var(--chaleco); }
  .marcador.v .n, .marcador.v .t { color: #0A6E66; }

  .deslizador { display: flex; flex-direction: column; gap: .35rem; }
  .deslizador .fila { display: flex; justify-content: space-between; font-size: .85rem; }
  .deslizador b { font-family: var(--mono); color: var(--acento); }
  input[type=range] { width: 100%; accent-color: var(--acento); }

  ul.lista { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: .3rem; max-height: 230px; overflow-y: auto; }
  ul.lista li {
    display: flex; align-items: center; gap: .55rem;
    font-size: .86rem; padding: .35rem .5rem; border-radius: 6px; background: var(--panel-alt);
  }
  .chip { width: .62rem; height: .62rem; border-radius: 3px; flex: none; }
  .chip.c { background: var(--casco); }
  .chip.v { background: var(--chaleco); }
  ul.lista .pct { margin-left: auto; font-family: var(--mono); font-size: .8rem; color: var(--tinta-sv); }

  dl.datos { margin: 0; display: grid; grid-template-columns: auto 1fr; gap: .35rem .9rem; font-size: .85rem; }
  dl.datos dt { color: var(--tinta-sv); }
  dl.datos dd { margin: 0; font-family: var(--mono); font-size: .82rem; text-align: right; }

  .aviso {
    border-left: 3px solid var(--alerta); background: var(--alerta-sv);
    padding: .8rem 1rem; border-radius: 0 8px 8px 0; font-size: .88rem; color: #7E2F27;
  }
  .oculto { display: none !important; }
  .cargando { display: flex; align-items: center; gap: .6rem; font-size: .9rem; color: var(--tinta-sv); }
  .giro {
    width: 1rem; height: 1rem; border: 2px solid var(--linea);
    border-top-color: var(--acento); border-radius: 50%;
    animation: gira .7s linear infinite;
  }
  @keyframes gira { to { transform: rotate(360deg); } }
  @media (prefers-reduced-motion: reduce) { .giro { animation: none; } }
</style>
</head>
<body>

<div class="barra">
  <div class="marca">
    <b>Detección de EPP</b>
    <span>casco y chaleco · YOLO26</span>
  </div>
  <span id="estado" class="estado"><span class="punto"></span><span id="estadoTxt">comprobando…</span></span>
</div>

<main>
  <section class="lienzo-panel">
    <div id="zona" tabindex="0" role="button" aria-label="Seleccionar imagen">
      <svg class="icono" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"
           stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>
      </svg>
      <h2>Arrastra una imagen de obra</h2>
      <p>o pulsa para elegir un archivo &middot; JPG o PNG</p>
    </div>

    <div id="vista">
      <div class="lienzo-caja"><canvas id="lienzo"></canvas></div>
      <div class="pie">
        <span id="nombre"></span>
        <span id="tiempo"></span>
        <button class="boton sec sep" id="otra">Probar otra imagen</button>
      </div>
    </div>
    <input type="file" id="archivo" accept="image/*" class="oculto">
  </section>

  <aside>
    <div class="tarjeta" id="panelResumen">
      <h3>Resultado</h3>
      <div class="marcadores">
        <div class="marcador c"><div class="n" id="nCasco">—</div><div class="t">Cascos</div></div>
        <div class="marcador v"><div class="n" id="nChaleco">—</div><div class="t">Chalecos</div></div>
      </div>
      <div class="deslizador">
        <div class="fila"><label for="umbral">Umbral de confianza</label><b id="umbralTxt">0.25</b></div>
        <input type="range" id="umbral" min="5" max="90" value="25" step="5">
      </div>
    </div>

    <div class="tarjeta oculto" id="panelLista">
      <h3>Detecciones</h3>
      <ul class="lista" id="lista"></ul>
    </div>

    <div class="tarjeta">
      <h3>Modelo</h3>
      <dl class="datos">
        <dt>Arquitectura</dt><dd>YOLO26n</dd>
        <dt>Clases</dt><dd>2</dd>
        <dt>Entrenamiento</dt><dd>20 944 img</dd>
        <dt>Resolución</dt><dd>640 px</dd>
      </dl>
    </div>
  </aside>
</main>

<script>
(function () {
  const $ = (id) => document.getElementById(id);
  const zona = $('zona'), archivo = $('archivo'), vista = $('vista');
  const lienzo = $('lienzo'), ctx = lienzo.getContext('2d');
  const COLOR = { casco: '#E89B1C', chaleco: '#12A99B' };
  let imagenActual = null, bytesActual = null;

  // ---- estado del servicio ----
  fetch('/salud').then(r => r.json()).then(s => {
    const e = $('estado'), t = $('estadoTxt');
    if (s.pesos_presentes) { e.className = 'estado ok'; t.textContent = 'modelo cargado'; }
    else {
      e.className = 'estado falta'; t.textContent = 'sin modelo entrenado';
      const aviso = document.createElement('div');
      aviso.className = 'aviso';
      aviso.textContent = 'El servicio está activo pero todavía no hay un modelo entrenado. '
                        + 'Las detecciones estarán disponibles cuando se carguen los pesos.';
      $('panelResumen').after(aviso);
    }
    if (typeof s.umbral === 'number') {
      $('umbral').value = Math.round(s.umbral * 100);
      $('umbralTxt').textContent = s.umbral.toFixed(2);
    }
  }).catch(() => {
    $('estado').className = 'estado falta';
    $('estadoTxt').textContent = 'servicio no disponible';
  });

  // ---- selección de archivo ----
  zona.addEventListener('click', () => archivo.click());
  zona.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); archivo.click(); }
  });
  ['dragenter', 'dragover'].forEach(ev =>
    zona.addEventListener(ev, e => { e.preventDefault(); zona.classList.add('sobre'); }));
  ['dragleave', 'drop'].forEach(ev =>
    zona.addEventListener(ev, e => { e.preventDefault(); zona.classList.remove('sobre'); }));
  zona.addEventListener('drop', e => {
    const f = e.dataTransfer.files[0];
    if (f) procesar(f);
  });
  archivo.addEventListener('change', () => { if (archivo.files[0]) procesar(archivo.files[0]); });
  $('otra').addEventListener('click', () => {
    vista.style.display = 'none'; zona.style.display = 'flex';
    archivo.value = ''; imagenActual = null; bytesActual = null;
    $('nCasco').textContent = '—'; $('nChaleco').textContent = '—';
    $('panelLista').classList.add('oculto');
  });

  // ---- umbral ----
  const umbral = $('umbral');
  umbral.addEventListener('input', () => {
    $('umbralTxt').textContent = (umbral.value / 100).toFixed(2);
  });
  umbral.addEventListener('change', () => { if (bytesActual) enviar(bytesActual); });

  function procesar(f) {
    bytesActual = f;
    const lector = new FileReader();
    lector.onload = (ev) => {
      const img = new Image();
      img.onload = () => {
        imagenActual = img;
        zona.style.display = 'none';
        vista.style.display = 'flex';
        $('nombre').textContent = f.name;
        dibujar([]);
        enviar(f);
      };
      img.src = ev.target.result;
    };
    lector.readAsDataURL(f);
  }

  function enviar(f) {
    $('tiempo').innerHTML = '<span class="cargando"><span class="giro"></span>analizando…</span>';
    const datos = new FormData();
    datos.append('imagen', f);
    datos.append('conf', umbral.value / 100);
    fetch('/detectar', { method: 'POST', body: datos })
      .then(async r => {
        if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || 'Error ' + r.status);
        return r.json();
      })
      .then(pintarResultado)
      .catch(err => {
        $('tiempo').textContent = '';
        const a = document.createElement('div');
        a.className = 'aviso'; a.textContent = err.message;
        $('panelResumen').after(a);
        setTimeout(() => a.remove(), 6000);
      });
  }

  function pintarResultado(d) {
    dibujar(d.detecciones);
    $('nCasco').textContent   = d.por_clase.casco ?? 0;
    $('nChaleco').textContent = d.por_clase.chaleco ?? 0;
    $('tiempo').textContent = `${d.dimensiones.ancho}×${d.dimensiones.alto} px · ${d.ms_inferencia} ms`;

    const lista = $('lista');
    lista.innerHTML = '';
    if (d.detecciones.length) {
      $('panelLista').classList.remove('oculto');
      d.detecciones.forEach((det, i) => {
        const li = document.createElement('li');
        li.innerHTML = `<span class="chip ${det.clase === 'casco' ? 'c' : 'v'}"></span>`
                     + `<span>${i + 1}. ${det.clase}</span>`
                     + `<span class="pct">${(det.confianza * 100).toFixed(0)}%</span>`;
        lista.appendChild(li);
      });
    } else {
      $('panelLista').classList.add('oculto');
    }
  }

  function dibujar(dets) {
    if (!imagenActual) return;
    const maxAncho = 900;
    const esc = Math.min(1, maxAncho / imagenActual.width);
    lienzo.width  = imagenActual.width  * esc;
    lienzo.height = imagenActual.height * esc;
    ctx.drawImage(imagenActual, 0, 0, lienzo.width, lienzo.height);

    const grosor = Math.max(2, Math.round(lienzo.width / 320));
    const tam    = Math.max(12, Math.round(lienzo.width / 52));
    ctx.lineWidth = grosor;
    ctx.font = `600 ${tam}px system-ui, sans-serif`;
    ctx.textBaseline = 'alphabetic';

    dets.forEach(det => {
      const c = COLOR[det.clase] || '#888';
      const x = det.caja.x1 * esc, y = det.caja.y1 * esc;
      const w = (det.caja.x2 - det.caja.x1) * esc, h = (det.caja.y2 - det.caja.y1) * esc;

      ctx.strokeStyle = c;
      ctx.strokeRect(x, y, w, h);

      const txt = `${det.clase} ${(det.confianza * 100).toFixed(0)}%`;
      const anchoTxt = ctx.measureText(txt).width + tam * 0.7;
      const altoTxt = tam * 1.5;
      const yEtiq = y - altoTxt < 0 ? y + h : y - altoTxt;

      ctx.fillStyle = c;
      ctx.fillRect(x - grosor / 2, yEtiq, anchoTxt, altoTxt);
      ctx.fillStyle = '#fff';
      ctx.fillText(txt, x + tam * 0.35 - grosor / 2, yEtiq + altoTxt * 0.72);
    });
  }
})();
</script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def inicio():
    return PAGINA
