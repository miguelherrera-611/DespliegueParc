# 🎯 GUÍA DE INICIO RÁPIDO - Pizzería API

## ✅ ¿Qué se ha implementado?

Se ha creado un sistema completo de microservicios para una pizzería con:

### 🏗️ Arquitectura Modular
```
✅ Microservicio de Pedidos (Puerto 8000)
   └── Estructura: Controllers / Models / Repositories

✅ Microservicio de Entregas (Puerto 8001)
   └── Estructura: Controllers / Models / Repositories
```

### 📦 Funcionalidades

**Pedidos:**
- ✅ Crear pedidos de pizza
- ✅ Listar todos los pedidos
- ✅ Consultar pedido específico
- ✅ Actualizar estado (pendiente → preparando → listo)
- ✅ Eliminar pedidos

**Entregas:**
- ✅ Asignar entregas a repartidores
- ✅ Listar todas las entregas
- ✅ Consultar entrega específica
- ✅ Buscar entregas por pedido
- ✅ Actualizar estado (asignada → en_camino → entregada)
- ✅ Eliminar entregas

## 🚀 INICIO RÁPIDO

### Opción 1: Ejecutar TODO (Recomendado)
```bash
run_all.bat
```
Esto inicia ambos microservicios en ventanas separadas.

### Opción 2: Ejecutar servicios por separado

**Terminal 1 - Pedidos:**
```bash
run_pedidos.bat
```

**Terminal 2 - Entregas:**
```bash
run_entregas.bat
```

### Opción 3: Con Docker Compose
```bash
docker-compose up --build
```

## 🌐 URLs de Acceso

Una vez iniciados los servicios:

### Microservicio de Pedidos
- **API**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **Health**: http://localhost:8000/health

### Microservicio de Entregas
- **API**: http://localhost:8001
- **Documentación**: http://localhost:8001/docs
- **Health**: http://localhost:8001/health

## 🧪 Ejecutar Pruebas

```bash
run_tests.bat
```

O manualmente:
```bash
python -m pytest tests/ -v
```

## 📝 Ejemplo de Uso con Postman/cURL

### 1. Crear un Pedido
```bash
curl -X POST http://localhost:8000/pedidos/ ^
  -H "Content-Type: application/json" ^
  -d "{\"cliente\":\"Juan Perez\",\"telefono\":\"3001234567\",\"direccion\":\"Calle 123\",\"pizzas\":[\"Margarita\"],\"cantidad\":1}"
```

### 2. Listar Pedidos
```bash
curl http://localhost:8000/pedidos/
```

### 3. Crear una Entrega
```bash
curl -X POST http://localhost:8001/entregas/ ^
  -H "Content-Type: application/json" ^
  -d "{\"pedido_id\":\"abc-123\",\"direccion\":\"Calle 123\",\"repartidor\":\"Carlos\"}"
```

### 4. Listar Entregas
```bash
curl http://localhost:8001/entregas/
```

## 📚 Documentación Disponible

- **README_NUEVO.md** → Documentación completa del proyecto
- **ARQUITECTURA.md** → Detalles de la arquitectura y estructura
- **GUIA_POSTMAN_NUEVA.md** → Guía completa de endpoints con ejemplos
- **GUIA_POSTMAN.md** → Guía original (legacy)

## 🐳 Despliegue

### Despliegue Local con Docker

**Construir imágenes:**
```bash
docker build -t pizzeria-pedidos -f Dockerfile .
docker build -t pizzeria-entregas -f Dockerfile.entregas .
```

**Ejecutar:**
```bash
docker-compose up
```

### Despliegue en Render

El archivo `render.yaml` está configurado y listo para desplegar:

1. Conecta tu repositorio a Render
2. Render detectará automáticamente el `render.yaml`
3. Los servicios se desplegarán automáticamente

## 📂 Estructura de Archivos Clave

### Nuevos Archivos Modularizados
```
services/
├── pedidos/
│   ├── app.py                      # ← App principal de Pedidos
│   ├── controllers/
│   │   └── pedido_controller.py    # ← Endpoints de Pedidos
│   ├── models/
│   │   └── pedido.py               # ← Modelos de datos
│   └── repositories/
│       └── pedido_repository.py    # ← Lógica de persistencia

└── entregas/
    ├── app.py                      # ← App principal de Entregas
    ├── controllers/
    │   └── entrega_controller.py   # ← Endpoints de Entregas
    ├── models/
    │   └── entrega.py              # ← Modelos de datos
    └── repositories/
        └── entrega_repository.py   # ← Lógica de persistencia
```

### Archivos de Configuración
```
Dockerfile                  # ← Docker para Pedidos
Dockerfile.entregas         # ← Docker para Entregas
docker-compose.yml          # ← Orquestación local
render.yaml                 # ← Configuración de Render
pytest.ini                  # ← Configuración de tests
requirements.txt            # ← Dependencias Python
```

### Tests
```
tests/
├── test_main.py           # ← Tests de Pedidos
└── test_entregas.py       # ← Tests de Entregas
```

## ⚠️ Archivos Legacy (Mantener por compatibilidad)

```
app/
├── main.py                # ← Código antiguo de Pedidos
└── entregas.py            # ← Código antiguo de Entregas
```

Estos archivos se mantienen por si hay referencias externas, pero la nueva arquitectura está en `services/`.

## 🔧 Troubleshooting

### Error: "No module named 'services'"
**Solución:** Ejecuta desde la raíz del proyecto:
```bash
cd C:\Users\maho4\OneDrive\Escritorio\parcial\PracticaManolo
python -m uvicorn services.pedidos.app:app --reload
```

### Error: Puerto en uso
**Solución:** Cambia el puerto:
```bash
python -m uvicorn services.pedidos.app:app --port 8002
```

### Tests no se ejecutan
**Solución:** Instala dependencias:
```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## 🎓 Cumplimiento del Examen

### ✅ Checklist Completo

- [x] **API REST funcionando** - FastAPI con JSON
- [x] **Endpoints probados** - Documentación en /docs
- [x] **Microservicios separados** - Pedidos y Entregas independientes
- [x] **Responsabilidad clara** - Controllers/Models/Repositories
- [x] **Docker** - Dockerfile y Docker Compose
- [x] **Despliegue configurado** - render.yaml listo
- [x] **Pruebas unitarias** - pytest con cobertura completa
- [x] **Código organizado** - Arquitectura modular y limpia

## 🎯 Para el Profesor

### Demostración Rápida

1. **Iniciar servicios:**
   ```bash
   run_all.bat
   ```

2. **Ver documentación interactiva:**
   - Pedidos: http://localhost:8000/docs
   - Entregas: http://localhost:8001/docs

3. **Ejecutar tests:**
   ```bash
   run_tests.bat
   ```

4. **Verificar Docker:**
   ```bash
   docker-compose up
   ```

### Endpoints a Probar

**Pedidos:**
- GET http://localhost:8000/health
- POST http://localhost:8000/pedidos/
- GET http://localhost:8000/pedidos/

**Entregas:**
- GET http://localhost:8001/health
- POST http://localhost:8001/entregas/
- GET http://localhost:8001/entregas/

## 📞 Soporte

Para más detalles, consulta:
- `README_NUEVO.md` - Documentación completa
- `ARQUITECTURA.md` - Detalles técnicos
- `GUIA_POSTMAN_NUEVA.md` - Ejemplos de uso

---

**¡Listo para demostrar! 🚀**

