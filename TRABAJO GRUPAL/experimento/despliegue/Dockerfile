# Servicio de inferencia EPP · YOLO26
# Imagen ligera: solo inferencia en CPU, sin CUDA.
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# torch en su variante CPU: ~200 MB en vez de ~2,5 GB
RUN pip install --no-cache-dir \
        torch torchvision --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir \
        ultralytics fastapi "uvicorn[standard]" python-multipart

COPY app.py .

EXPOSE 8090
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8090"]
