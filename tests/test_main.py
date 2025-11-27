from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_crud_flow():
    # Crear
    r = client.post("/notes/", json={"title": "Test", "content": "Contenido"})
    assert r.status_code == 201
    note = r.json()
    assert "id" in note
    nid = note["id"]
    assert note["title"] == "Test"

    # Obtener
    r = client.get(f"/notes/{nid}")
    assert r.status_code == 200
    assert r.json()["id"] == nid

    # Listar
    r = client.get("/notes/")
    assert r.status_code == 200
    assert any(n["id"] == nid for n in r.json())

    # Actualizar
    r = client.put(f"/notes/{nid}", json={"title": "Updated", "content": "Nuevo"})
    assert r.status_code == 200
    assert r.json()["title"] == "Updated"

    # Borrar
    r = client.delete(f"/notes/{nid}")
    assert r.status_code == 204

    # Ver que ya no existe
    r = client.get(f"/notes/{nid}")
    assert r.status_code == 404