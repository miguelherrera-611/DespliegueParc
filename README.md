```markdown
# Notes Microservice (FastAPI) - Ejemplo

Descripción
Este proyecto es un microservicio de ejemplo en FastAPI que implementa operaciones CRUD simples para "notas". Usa almacenamiento en memoria (solo para demo).

Requisitos
- Python 3.11 (recomendado)
- Docker (opcional, para ejecutar en contenedor)
- Git (opcional)

Instalación local (PowerShell)
1. Abrir PowerShell en la raíz del proyecto
2. Activar el entorno virtual (.venv creado por PyCharm) o crear uno si no existe:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Actualizar pip e instalar dependencias:
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install -r requirements.txt

Ejecutar tests
python -m pytest -q

Levantar la aplicación localmente
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
- Documentación interactiva: http://localhost:8000/docs

Docker (construir y ejecutar)
docker build -t notes-microservice:local .
docker run --rm -p 8000:8000 notes-microservice:local

Despliegue en Render
- Si usas Render, el archivo render.yaml está presente para configuración básica.
```