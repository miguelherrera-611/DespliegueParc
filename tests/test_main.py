from fastapi.testclient import TestClient
from services.pedidos.app import app

client = TestClient(app)


def test_health():
    """Verificar que el endpoint de salud funciona"""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    assert r.json()["servicio"] == "pedidos"


def test_crear_pedido():
    """Verificar la creación de un pedido"""
    r = client.post("/pedidos/", json={
        "cliente": "Juan Pérez",
        "telefono": "3001234567",
        "direccion": "Calle 123 #45-67",
        "pizzas": ["Margarita", "Pepperoni"],
        "cantidad": 2
    })
    assert r.status_code == 201
    pedido = r.json()
    assert "id" in pedido
    assert pedido["cliente"] == "Juan Pérez"
    assert pedido["estado"] == "pendiente"
    assert "fecha" in pedido


def test_listar_pedidos():
    """Verificar que se pueden listar los pedidos"""
    r = client.get("/pedidos/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_pedido_no_encontrado():
    """Verificar manejo de pedido inexistente"""
    r = client.get("/pedidos/id-inexistente")
    assert r.status_code == 404


def test_estado_invalido():
    """Verificar que no se aceptan estados inválidos"""
    # Crear un pedido primero
    r = client.post("/pedidos/", json={
        "cliente": "Pedro García",
        "telefono": "3201112233",
        "direccion": "Avenida 68 #23-45",
        "pizzas": ["Vegetariana"],
        "cantidad": 1
    })
    pid = r.json()["id"]

    # Intentar actualizar con estado inválido
    r = client.put(f"/pedidos/{pid}/estado?estado=invalido")
    assert r.status_code == 400


def test_crud_pedido_completo():
    """Prueba completa del flujo CRUD de pedidos"""
    # Crear
    r = client.post("/pedidos/", json={
        "cliente": "María López",
        "telefono": "3109876543",
        "direccion": "Carrera 7 #10-20",
        "pizzas": ["Hawaiana", "Napolitana"],
        "cantidad": 2
    })
    assert r.status_code == 201
    pedido = r.json()
    assert "id" in pedido
    pid = pedido["id"]
    assert pedido["cliente"] == "María López"

    # Obtener
    r = client.get(f"/pedidos/{pid}")
    assert r.status_code == 200
    assert r.json()["id"] == pid

    # Listar
    r = client.get("/pedidos/")
    assert r.status_code == 200
    assert any(p["id"] == pid for p in r.json())

    # Actualizar estado
    r = client.put(f"/pedidos/{pid}/estado?estado=preparando")
    assert r.status_code == 200
    assert r.json()["estado"] == "preparando"

    # Borrar
    r = client.delete(f"/pedidos/{pid}")
    assert r.status_code == 204

    # Verificar que no existe
    r = client.get(f"/pedidos/{pid}")
    assert r.status_code == 404

