# 🍕 API REST - Gestión de Pizzería

Sistema de microservicios para gestionar pedidos y entregas de una pizzería pequeña a domicilio.

## 📋 Descripción

Este proyecto implementa una arquitectura de microservicios con dos servicios principales:

1. **Microservicio de Pedidos**: Gestiona la creación y seguimiento de pedidos de pizzas
2. **Microservicio de Entregas**: Gestiona la asignación y seguimiento de entregas a domicilio

## 🏗️ Arquitectura

```
├── Microservicio de Pedidos (Puerto 8000)
│   └── Endpoints: /pedidos/*
│
└── Microservicio de Entregas (Puerto 8001)
    └── Endpoints: /entregas/*
```

## 🚀 Tecnologías

- **Framework**: FastAPI (Python)
- **Containerización**: Docker
- **Despliegue**: Render
- **Testing**: Pytest

## 📡 Endpoints

### Microservicio de Pedidos (Puerto 8000)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Verificar estado del servicio |
| POST | `/pedidos/` | Crear un nuevo pedido |
| GET | `/pedidos/` | Listar todos los pedidos |
| GET | `/pedidos/{id}` | Obtener un pedido específico |
| PUT | `/pedidos/{id}/estado` | Actualizar estado del pedido |
| DELETE | `/pedidos/{id}` | Eliminar un pedido |

**Estados de pedido**: `pendiente`, `preparando`, `listo`

**Ejemplo de creación de pedido**:
```json
POST /pedidos/
{
  "cliente": "Juan Pérez",
  "telefono": "3001234567",
  "direccion": "Calle 123 #45-67",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2
}
```

### Microservicio de Entregas (Puerto 8001)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Verificar estado del servicio |
| POST | `/entregas/` | Crear una nueva entrega |
| GET | `/entregas/` | Listar todas las entregas |
| GET | `/entregas/{id}` | Obtener una entrega específica |
| GET | `/entregas/pedido/{pedido_id}` | Obtener entregas de un pedido |
| PUT | `/entregas/{id}/estado` | Actualizar estado de la entrega |
| DELETE | `/entregas/{id}` | Eliminar una entrega |

**Estados de entrega**: `asignada`, `en_camino`, `entregada`

**Ejemplo de creación de entrega**:
```json
POST /entregas/
{
  "pedido_id": "uuid-del-pedido",
  "direccion": "Calle 123 #45-67",
  "repartidor": "Carlos Ramos"
}
```

## 🐳 Ejecución Local con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
# Construir y ejecutar ambos servicios
docker-compose up --build

# Servicios disponibles en:
# - Pedidos: http://localhost:8000
# - Entregas: http://localhost:8001
```

### Opción 2: Docker Individual

```bash
# Servicio de Pedidos
docker build -t pizzeria-pedidos .
docker run -p 8000:8000 pizzeria-pedidos

# Servicio de Entregas
docker build -t pizzeria-entregas -f Dockerfile.entregas .
docker run -p 8001:8001 pizzeria-entregas
```

## 🧪 Pruebas Unitarias

Ejecutar las pruebas automáticas:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas
pytest

# Ejecutar con reporte detallado
pytest -v

# Ejecutar pruebas de un servicio específico
pytest tests/test_main.py        # Pedidos
pytest tests/test_entregas.py    # Entregas
```

## 📝 Documentación Interactiva

Una vez que los servicios estén ejecutándose, accede a la documentación Swagger:

- Pedidos: http://localhost:8000/docs
- Entregas: http://localhost:8001/docs

## ☁️ Despliegue en Render

El proyecto está configurado para desplegarse automáticamente en Render usando `render.yaml`.

Ambos servicios se despliegan independientemente:
- `pizzeria-pedidos`
- `pizzeria-entregas`

## 👨‍💻 Desarrollo

```bash
# Clonar el repositorio
git clone <url-repositorio>

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servicio de pedidos en modo desarrollo
uvicorn app.main:app --reload --port 8000

# Ejecutar servicio de entregas en modo desarrollo
uvicorn app.entregas:app --reload --port 8001
```

## 📦 Estructura del Proyecto

```
PracticaManolo/
├── app/
│   ├── __init__.py
│   ├── main.py          # Microservicio de Pedidos
│   └── entregas.py      # Microservicio de Entregas
├── tests/
│   ├── test_main.py     # Tests de Pedidos
│   └── test_entregas.py # Tests de Entregas
├── Dockerfile           # Imagen para Pedidos
├── Dockerfile.entregas  # Imagen para Entregas
├── docker-compose.yml   # Orquestación local
├── render.yaml          # Configuración de despliegue
├── requirements.txt
└── README.md
```

## 🎯 Funcionalidades Principales

- ✅ API REST completa con operaciones CRUD
- ✅ Arquitectura de microservicios separada por responsabilidad
- ✅ Dockerización de ambos servicios
- ✅ Pruebas unitarias automáticas
- ✅ Despliegue en la nube con Render
- ✅ Documentación automática con Swagger/OpenAPI
- ✅ Validación de datos con Pydantic
- ✅ Gestión de estados de pedidos y entregas

## 📄 Licencia

Proyecto académico - Examen Final API REST con Microservicios y DevOps
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