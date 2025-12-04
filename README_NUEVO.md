# 🍕 API REST - Pizzería con Microservicios

Sistema de gestión de pedidos y entregas para una pizzería pequeña, implementado con arquitectura de microservicios.

## 📋 Descripción

Este proyecto implementa un API REST para gestionar pedidos y entregas de una pizzería, dividido en dos microservicios independientes:

- **Microservicio de Pedidos**: Gestiona la creación y seguimiento de pedidos
- **Microservicio de Entregas**: Gestiona la asignación y seguimiento de entregas a domicilio

## 🏗️ Arquitectura

```
PracticaManolo/
├── services/
│   ├── pedidos/                    # Microservicio de Pedidos
│   │   ├── controllers/            # Controladores (endpoints)
│   │   │   └── pedido_controller.py
│   │   ├── models/                 # Modelos de datos
│   │   │   └── pedido.py
│   │   ├── repositories/           # Capa de datos
│   │   │   └── pedido_repository.py
│   │   └── app.py                  # Aplicación FastAPI
│   └── entregas/                   # Microservicio de Entregas
│       ├── controllers/
│       │   └── entrega_controller.py
│       ├── models/
│       │   └── entrega.py
│       ├── repositories/
│       │   └── entrega_repository.py
│       └── app.py
├── tests/                          # Pruebas unitarias
├── Dockerfile                      # Docker para Pedidos
├── Dockerfile.entregas             # Docker para Entregas
├── docker-compose.yml              # Orquestación local
└── render.yaml                     # Configuración de despliegue
```

## 🚀 Tecnologías

- **Framework**: FastAPI (Python)
- **Containerización**: Docker
- **Orquestación**: Docker Compose
- **Testing**: Pytest
- **Despliegue**: Render (Cloud)

## 📦 Instalación

### Prerrequisitos
- Python 3.11+
- Docker y Docker Compose

### Instalación Local

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd PracticaManolo
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar con Docker Compose:
```bash
docker-compose up --build
```

Los servicios estarán disponibles en:
- **Pedidos**: http://localhost:8000
- **Entregas**: http://localhost:8001

## 🔗 Endpoints API

### Microservicio de Pedidos (Puerto 8000)

#### Health Check
```
GET /health
```

#### Crear Pedido
```
POST /pedidos/
Body: {
  "cliente": "Juan Pérez",
  "telefono": "3001234567",
  "direccion": "Calle 123 #45-67",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2
}
```

#### Listar Pedidos
```
GET /pedidos/
```

#### Obtener Pedido
```
GET /pedidos/{pedido_id}
```

#### Actualizar Estado de Pedido
```
PUT /pedidos/{pedido_id}/estado?estado=preparando
Estados válidos: pendiente, preparando, listo
```

#### Eliminar Pedido
```
DELETE /pedidos/{pedido_id}
```

### Microservicio de Entregas (Puerto 8001)

#### Health Check
```
GET /health
```

#### Crear Entrega
```
POST /entregas/
Body: {
  "pedido_id": "abc-123",
  "direccion": "Calle 123 #45-67",
  "repartidor": "Carlos Ramírez"
}
```

#### Listar Entregas
```
GET /entregas/
```

#### Obtener Entrega
```
GET /entregas/{entrega_id}
```

#### Obtener Entregas por Pedido
```
GET /entregas/pedido/{pedido_id}
```

#### Actualizar Estado de Entrega
```
PUT /entregas/{entrega_id}/estado?estado=en_camino
Estados válidos: asignada, en_camino, entregada
```

#### Eliminar Entrega
```
DELETE /entregas/{entrega_id}
```

## 🧪 Pruebas

Ejecutar todas las pruebas:
```bash
pytest tests/ -v
```

Ejecutar pruebas específicas:
```bash
pytest tests/test_main.py -v       # Pruebas de Pedidos
pytest tests/test_entregas.py -v   # Pruebas de Entregas
```

En Windows:
```bash
.\run_tests.bat
```

## 🐳 Docker

### Construcción de imágenes
```bash
docker build -t pizzeria-pedidos -f Dockerfile .
docker build -t pizzeria-entregas -f Dockerfile.entregas .
```

### Ejecución individual
```bash
docker run -p 8000:8000 pizzeria-pedidos
docker run -p 8001:8001 pizzeria-entregas
```

## ☁️ Despliegue en la Nube

El proyecto está configurado para desplegarse en Render utilizando el archivo `render.yaml`.

### URLs de Producción
- **Pedidos**: [URL del servicio desplegado]
- **Entregas**: [URL del servicio desplegado]

### Pasos para Desplegar
1. Conectar repositorio a Render
2. Render detectará automáticamente el `render.yaml`
3. Los servicios se desplegarán automáticamente

## 📚 Documentación Interactiva

FastAPI genera documentación automática:

- **Pedidos**: http://localhost:8000/docs
- **Entregas**: http://localhost:8001/docs

## 👨‍💻 Desarrollo

### Estructura de Capas

Cada microservicio sigue una arquitectura de 3 capas:

1. **Controllers**: Definen los endpoints y validan requests
2. **Models**: Definen la estructura de datos (Pydantic)
3. **Repositories**: Gestionan la persistencia de datos

### Añadir Nuevas Funcionalidades

1. Crear el modelo en `models/`
2. Crear el repositorio en `repositories/`
3. Crear el controlador en `controllers/`
4. Registrar el router en `app.py`
5. Crear tests en `tests/`

## 🔐 Seguridad

- Variables de entorno para configuración sensible
- Validación de datos con Pydantic
- Manejo de errores HTTP apropiados

## 📄 Licencia

Este proyecto es de uso académico.

## 👤 Autor

Proyecto desarrollado para el examen final de Ingeniería de Software.
Profesor: Arle Morales Ortiz

