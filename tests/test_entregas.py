from fastapi.testclient import TestClient
from services.entregas.app import app

client = TestClient(app)


def test_health():
    """Verificar que el endpoint de salud funciona"""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    assert r.json()["servicio"] == "entregas"


def test_crear_entrega():
    """Verificar la creación de una entrega"""
    r = client.post("/entregas/", json={
        "pedido_id": "pedido-123",
        "direccion": "Calle 123 #45-67",
        "repartidor": "Carlos Ramírez"
    })
    assert r.status_code == 201
    entrega = r.json()
    assert "id" in entrega
    assert entrega["pedido_id"] == "pedido-123"
    assert entrega["estado"] == "asignada"
    assert "fecha_asignacion" in entrega


def test_listar_entregas():
    """Verificar que se pueden listar las entregas"""
    r = client.get("/entregas/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_entrega_no_encontrada():
    """Verificar manejo de entrega inexistente"""
    r = client.get("/entregas/id-inexistente")
    assert r.status_code == 404


def test_estado_invalido():
    """Verificar que no se aceptan estados inválidos"""
    # Crear una entrega primero
    r = client.post("/entregas/", json={
        "pedido_id": "pedido-456",
        "direccion": "Avenida 68 #23-45",
        "repartidor": "Luis Gómez"
    })
    eid = r.json()["id"]

    # Intentar actualizar con estado inválido
    r = client.put(f"/entregas/{eid}/estado?estado=invalido")
    assert r.status_code == 400


def test_crud_entrega_completo():
    """Prueba completa del flujo CRUD de entregas"""
    # Crear
    r = client.post("/entregas/", json={
        "pedido_id": "pedido-789",
        "direccion": "Carrera 7 #10-20",
        "repartidor": "Ana Martínez"
    })
    assert r.status_code == 201
    entrega = r.json()
    assert "id" in entrega
    eid = entrega["id"]
    assert entrega["repartidor"] == "Ana Martínez"

    # Obtener
    r = client.get(f"/entregas/{eid}")
    assert r.status_code == 200
    assert r.json()["id"] == eid

    # Listar
    r = client.get("/entregas/")
    assert r.status_code == 200
    assert any(e["id"] == eid for e in r.json())

    # Actualizar estado a "en_camino"
    r = client.put(f"/entregas/{eid}/estado?estado=en_camino")
    assert r.status_code == 200
    assert r.json()["estado"] == "en_camino"

    # Actualizar estado a "entregada"
    r = client.put(f"/entregas/{eid}/estado?estado=entregada")
    assert r.status_code == 200
    assert r.json()["estado"] == "entregada"
    assert r.json()["fecha_entrega"] is not None

    # Borrar
    r = client.delete(f"/entregas/{eid}")
    assert r.status_code == 204

    # Verificar que no existe
    r = client.get(f"/entregas/{eid}")
    assert r.status_code == 404


def test_obtener_entregas_por_pedido():
    """Verificar que se pueden obtener entregas de un pedido específico"""
    pedido_id = "pedido-test-123"

    # Crear varias entregas para el mismo pedido
    r1 = client.post("/entregas/", json={
        "pedido_id": pedido_id,
        "direccion": "Dirección 1",
        "repartidor": "Repartidor 1"
    })
    r2 = client.post("/entregas/", json={
        "pedido_id": pedido_id,
        "direccion": "Dirección 1",
        "repartidor": "Repartidor 2"
    })

    assert r1.status_code == 201
    assert r2.status_code == 201

    # Obtener entregas del pedido
    r = client.get(f"/entregas/pedido/{pedido_id}")
    assert r.status_code == 200
    entregas = r.json()
    assert len(entregas) >= 2
    assert all(e["pedido_id"] == pedido_id for e in entregas)

