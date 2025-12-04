# 🍕 GUÍA COMPLETA DE POSTMAN - API Pizzería

## 📋 ÍNDICE
1. [Configuración Inicial](#configuración-inicial)
2. [Microservicio de Pedidos (Puerto 8000)](#microservicio-de-pedidos)
3. [Microservicio de Entregas (Puerto 8001)](#microservicio-de-entregas)
4. [Flujo Completo de Prueba](#flujo-completo-de-prueba)

---

## ⚙️ CONFIGURACIÓN INICIAL

### 1. Iniciar los Servicios

**Opción A - Ambos servicios a la vez:**
```cmd
run_all.bat
```

**Opción B - Por separado:**
```cmd
run_pedidos.bat    # Terminal 1 - Puerto 8000
run_entregas.bat   # Terminal 2 - Puerto 8001
```

### 2. Verificar que están corriendo
- **Pedidos**: http://localhost:8000/docs
- **Entregas**: http://localhost:8001/docs

---

## 🍕 MICROSERVICIO DE PEDIDOS (Puerto 8000)

### 1️⃣ Health Check

**Método:** `GET`  
**URL:** `http://localhost:8000/health`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
{
  "status": "ok",
  "servicio": "pedidos"
}
```

---

### 2️⃣ Crear un Pedido

**Método:** `POST`  
**URL:** `http://localhost:8000/pedidos/`  
**Headers:**
```
Content-Type: application/json
```

**Body (raw - JSON):**
```json
{
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "direccion": "Calle Principal 123",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2
}
```

**Respuesta esperada (201 Created):**
```json
{
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "direccion": "Calle Principal 123",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2,
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "estado": "pendiente",
  "fecha": "2025-12-04T10:30:00.123456"
}
```

**⭐ IMPORTANTE:** Guarda el `id` que te devuelve, lo necesitarás para las siguientes peticiones.

---

### 3️⃣ Listar Todos los Pedidos

**Método:** `GET`  
**URL:** `http://localhost:8000/pedidos/`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
[
  {
    "cliente": "Juan Pérez",
    "telefono": "555-1234",
    "direccion": "Calle Principal 123",
    "pizzas": ["Margarita", "Pepperoni"],
    "cantidad": 2,
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "estado": "pendiente",
    "fecha": "2025-12-04T10:30:00.123456"
  }
]
```

---

### 4️⃣ Obtener un Pedido Específico

**Método:** `GET`  
**URL:** `http://localhost:8000/pedidos/{pedido_id}`  
**Ejemplo:** `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
{
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "direccion": "Calle Principal 123",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2,
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "estado": "pendiente",
  "fecha": "2025-12-04T10:30:00.123456"
}
```

**Si el ID no existe (404):**
```json
{
  "detail": "Pedido no encontrado"
}
```

---

### 5️⃣ Actualizar Estado de un Pedido

**Método:** `PUT`  
**URL:** `http://localhost:8000/pedidos/{pedido_id}/estado?estado=preparando`  
**Ejemplo:** `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890/estado?estado=preparando`

**Headers:** Ninguno necesario  
**Body:** Ninguno

**Estados válidos:**
- `pendiente`
- `preparando`
- `listo`

**Respuesta esperada:**
```json
{
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "direccion": "Calle Principal 123",
  "pizzas": ["Margarita", "Pepperoni"],
  "cantidad": 2,
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "estado": "preparando",
  "fecha": "2025-12-04T10:30:00.123456"
}
```

**Ejemplos de URLs completas:**
- Cambiar a preparando: `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890/estado?estado=preparando`
- Cambiar a listo: `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890/estado?estado=listo`
- Cambiar a pendiente: `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890/estado?estado=pendiente`

**Si el estado es inválido (400):**
```json
{
  "detail": "Estado inválido. Use: ['pendiente', 'preparando', 'listo']"
}
```

---

### 6️⃣ Eliminar un Pedido

**Método:** `DELETE`  
**URL:** `http://localhost:8000/pedidos/{pedido_id}`  
**Ejemplo:** `http://localhost:8000/pedidos/a1b2c3d4-e5f6-7890-abcd-ef1234567890`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada (204 No Content):**
Sin contenido en el body.

**Si el ID no existe (404):**
```json
{
  "detail": "Pedido no encontrado"
}
```

---

## 🚚 MICROSERVICIO DE ENTREGAS (Puerto 8001)

### 1️⃣ Health Check

**Método:** `GET`  
**URL:** `http://localhost:8001/health`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
{
  "status": "ok",
  "servicio": "entregas"
}
```

---

### 2️⃣ Crear una Entrega

**Método:** `POST`  
**URL:** `http://localhost:8001/entregas/`  
**Headers:**
```
Content-Type: application/json
```

**Body (raw - JSON):**
```json
{
  "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "direccion": "Calle Principal 123",
  "repartidor": "Carlos López"
}
```

**Respuesta esperada (201 Created):**
```json
{
  "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "direccion": "Calle Principal 123",
  "repartidor": "Carlos López",
  "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
  "estado": "asignada",
  "fecha_asignacion": "2025-12-04T10:35:00.654321",
  "fecha_entrega": null
}
```

**⭐ IMPORTANTE:** Guarda el `id` de la entrega para las siguientes peticiones.

---

### 3️⃣ Listar Todas las Entregas

**Método:** `GET`  
**URL:** `http://localhost:8001/entregas/`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
[
  {
    "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "direccion": "Calle Principal 123",
    "repartidor": "Carlos López",
    "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
    "estado": "asignada",
    "fecha_asignacion": "2025-12-04T10:35:00.654321",
    "fecha_entrega": null
  }
]
```

---

### 4️⃣ Obtener una Entrega Específica

**Método:** `GET`  
**URL:** `http://localhost:8001/entregas/{entrega_id}`  
**Ejemplo:** `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
{
  "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "direccion": "Calle Principal 123",
  "repartidor": "Carlos López",
  "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
  "estado": "asignada",
  "fecha_asignacion": "2025-12-04T10:35:00.654321",
  "fecha_entrega": null
}
```

**Si el ID no existe (404):**
```json
{
  "detail": "Entrega no encontrada"
}
```

---

### 5️⃣ Obtener Entregas por Pedido

**Método:** `GET`  
**URL:** `http://localhost:8001/entregas/pedido/{pedido_id}`  
**Ejemplo:** `http://localhost:8001/entregas/pedido/a1b2c3d4-e5f6-7890-abcd-ef1234567890`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada:**
```json
[
  {
    "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "direccion": "Calle Principal 123",
    "repartidor": "Carlos López",
    "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
    "estado": "asignada",
    "fecha_asignacion": "2025-12-04T10:35:00.654321",
    "fecha_entrega": null
  }
]
```

---

### 6️⃣ Actualizar Estado de una Entrega

**Método:** `PUT`  
**URL:** `http://localhost:8001/entregas/{entrega_id}/estado?estado=en_camino`  
**Ejemplo:** `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901/estado?estado=en_camino`

**Headers:** Ninguno necesario  
**Body:** Ninguno

**Estados válidos:**
- `asignada`
- `en_camino`
- `entregada`

**Respuesta esperada:**
```json
{
  "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "direccion": "Calle Principal 123",
  "repartidor": "Carlos López",
  "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
  "estado": "en_camino",
  "fecha_asignacion": "2025-12-04T10:35:00.654321",
  "fecha_entrega": null
}
```

**Cuando cambias a "entregada":**
```json
{
  "pedido_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "direccion": "Calle Principal 123",
  "repartidor": "Carlos López",
  "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
  "estado": "entregada",
  "fecha_asignacion": "2025-12-04T10:35:00.654321",
  "fecha_entrega": "2025-12-04T10:45:00.123456"
}
```

**Ejemplos de URLs completas:**
- Cambiar a en_camino: `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901/estado?estado=en_camino`
- Cambiar a entregada: `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901/estado?estado=entregada`
- Cambiar a asignada: `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901/estado?estado=asignada`

**Si el estado es inválido (400):**
```json
{
  "detail": "Estado inválido. Use: ['asignada', 'en_camino', 'entregada']"
}
```

---

### 7️⃣ Eliminar una Entrega

**Método:** `DELETE`  
**URL:** `http://localhost:8001/entregas/{entrega_id}`  
**Ejemplo:** `http://localhost:8001/entregas/b2c3d4e5-f6g7-8901-bcde-fg2345678901`  
**Headers:** Ninguno necesario  
**Body:** Ninguno

**Respuesta esperada (204 No Content):**
Sin contenido en el body.

**Si el ID no existe (404):**
```json
{
  "detail": "Entrega no encontrada"
}
```

---

## 🔄 FLUJO COMPLETO DE PRUEBA

### Paso 1: Verificar que los servicios estén corriendo

```
GET http://localhost:8000/health
GET http://localhost:8001/health
```

### Paso 2: Crear un pedido

```
POST http://localhost:8000/pedidos/
Body:
{
  "cliente": "María García",
  "telefono": "555-9876",
  "direccion": "Avenida Central 456",
  "pizzas": ["Hawaiana", "Cuatro Quesos"],
  "cantidad": 2
}

→ Recibes el pedido con ID: "abc123..."
```

### Paso 3: Listar pedidos para verificar

```
GET http://localhost:8000/pedidos/
```

### Paso 4: Actualizar estado del pedido a "preparando"

```
PUT http://localhost:8000/pedidos/abc123.../estado?estado=preparando
```

### Paso 5: Actualizar estado del pedido a "listo"

```
PUT http://localhost:8000/pedidos/abc123.../estado?estado=listo
```

### Paso 6: Crear una entrega para ese pedido

```
POST http://localhost:8001/entregas/
Body:
{
  "pedido_id": "abc123...",
  "direccion": "Avenida Central 456",
  "repartidor": "Pedro Martínez"
}

→ Recibes la entrega con ID: "xyz789..."
```

### Paso 7: Actualizar estado de entrega a "en_camino"

```
PUT http://localhost:8001/entregas/xyz789.../estado?estado=en_camino
```

### Paso 8: Consultar entregas del pedido

```
GET http://localhost:8001/entregas/pedido/abc123...
```

### Paso 9: Marcar entrega como "entregada"

```
PUT http://localhost:8001/entregas/xyz789.../estado?estado=entregada
```

### Paso 10: Verificar la entrega completa

```
GET http://localhost:8001/entregas/xyz789...
```

---

## 📊 RESUMEN DE ENDPOINTS

### Microservicio de Pedidos (Puerto 8000)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/pedidos/` | Crear pedido |
| GET | `/pedidos/` | Listar todos los pedidos |
| GET | `/pedidos/{id}` | Obtener pedido específico |
| PUT | `/pedidos/{id}/estado?estado={estado}` | Actualizar estado |
| DELETE | `/pedidos/{id}` | Eliminar pedido |

### Microservicio de Entregas (Puerto 8001)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/entregas/` | Crear entrega |
| GET | `/entregas/` | Listar todas las entregas |
| GET | `/entregas/{id}` | Obtener entrega específica |
| GET | `/entregas/pedido/{pedido_id}` | Entregas por pedido |
| PUT | `/entregas/{id}/estado?estado={estado}` | Actualizar estado |
| DELETE | `/entregas/{id}` | Eliminar entrega |

---

## 💡 CONSEJOS PARA POSTMAN

### 1. Crear una Colección
- Crea una colección llamada "Pizzería API"
- Organiza en carpetas: "Pedidos" y "Entregas"

### 2. Usar Variables
- Crea variables de entorno:
  - `pedidos_url` = `http://localhost:8000`
  - `entregas_url` = `http://localhost:8001`
  - `pedido_id` = (guarda el ID del último pedido creado)
  - `entrega_id` = (guarda el ID de la última entrega creada)

### 3. Scripts Automáticos
En la pestaña "Tests" de "Crear Pedido", agrega:
```javascript
var jsonData = pm.response.json();
pm.environment.set("pedido_id", jsonData.id);
```

En la pestaña "Tests" de "Crear Entrega", agrega:
```javascript
var jsonData = pm.response.json();
pm.environment.set("entrega_id", jsonData.id);
```

Así podrás usar `{{pedido_id}}` y `{{entrega_id}}` en las siguientes peticiones.

---

## 🎯 EJEMPLOS ADICIONALES

### Crear Múltiples Pedidos

**Pedido 1 - Familiar:**
```json
{
  "cliente": "Familia Rodríguez",
  "telefono": "555-1111",
  "direccion": "Calle del Sol 789",
  "pizzas": ["Margarita", "Pepperoni", "Vegetariana"],
  "cantidad": 3
}
```

**Pedido 2 - Individual:**
```json
{
  "cliente": "Ana Torres",
  "telefono": "555-2222",
  "direccion": "Avenida Luna 321",
  "pizzas": ["Cuatro Quesos"],
  "cantidad": 1
}
```

**Pedido 3 - Oficina:**
```json
{
  "cliente": "Oficina Tech Corp",
  "telefono": "555-3333",
  "direccion": "Edificio Business Center, Piso 5",
  "pizzas": ["Pepperoni", "Hawaiana", "BBQ", "Vegetariana", "Margarita"],
  "cantidad": 5
}
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: Connection refused
- Verifica que los servicios estén corriendo
- Ejecuta `run_all.bat` o los scripts individuales

### Error: 404 Not Found
- Verifica que el ID sea correcto
- Usa GET para listar y obtener IDs válidos

### Error: 400 Bad Request
- Verifica que el JSON del body esté bien formado
- Asegúrate de usar los estados válidos

### Error: 422 Unprocessable Entity
- Verifica que todos los campos requeridos estén presentes
- Revisa que los tipos de datos sean correctos

---

## ✅ CHECKLIST DE PRUEBA

- [ ] Health check de Pedidos funciona
- [ ] Health check de Entregas funciona
- [ ] Puedo crear un pedido
- [ ] Puedo listar todos los pedidos
- [ ] Puedo obtener un pedido específico
- [ ] Puedo actualizar el estado de un pedido
- [ ] Puedo eliminar un pedido
- [ ] Puedo crear una entrega
- [ ] Puedo listar todas las entregas
- [ ] Puedo obtener una entrega específica
- [ ] Puedo buscar entregas por pedido
- [ ] Puedo actualizar el estado de una entrega
- [ ] Puedo eliminar una entrega
- [ ] El flujo completo funciona correctamente

---

**¡Listo para probar! 🍕🚀**

