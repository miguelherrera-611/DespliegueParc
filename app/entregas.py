from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Pizzería API - Microservicio de Entregas")

# Modelos para Entregas
class EntregaIn(BaseModel):
    pedido_id: str
    direccion: str
    repartidor: str

class Entrega(EntregaIn):
    id: str
    estado: str  # "asignada", "en_camino", "entregada"
    fecha_asignacion: str
    fecha_entrega: str = None

# Almacenamiento en memoria
_entregas_db: Dict[str, Entrega] = {}

@app.get("/health")
def health():
    return {"status": "ok", "servicio": "entregas"}

@app.post("/entregas/", response_model=Entrega, status_code=201)
def crear_entrega(entrega_in: EntregaIn):
    """Asignar una entrega a un repartidor"""
    eid = str(uuid4())
    entrega = Entrega(
        id=eid,
        estado="asignada",
        fecha_asignacion=datetime.now().isoformat(),
        **entrega_in.model_dump()
    )
    _entregas_db[eid] = entrega
    return entrega

@app.get("/entregas/", response_model=List[Entrega])
def listar_entregas():
    """Listar todas las entregas"""
    return list(_entregas_db.values())

@app.get("/entregas/{entrega_id}", response_model=Entrega)
def obtener_entrega(entrega_id: str):
    """Obtener una entrega específica"""
    entrega = _entregas_db.get(entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return entrega

@app.get("/entregas/pedido/{pedido_id}", response_model=List[Entrega])
def obtener_entregas_por_pedido(pedido_id: str):
    """Obtener entregas asociadas a un pedido"""
    entregas = [e for e in _entregas_db.values() if e.pedido_id == pedido_id]
    return entregas

@app.put("/entregas/{entrega_id}/estado", response_model=Entrega)
def actualizar_estado_entrega(entrega_id: str, estado: str):
    """Actualizar el estado de una entrega (asignada, en_camino, entregada)"""
    entrega = _entregas_db.get(entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")

    estados_validos = ["asignada", "en_camino", "entregada"]
    if estado not in estados_validos:
        raise HTTPException(status_code=400, detail=f"Estado inválido. Use: {estados_validos}")

    entrega.estado = estado
    if estado == "entregada":
        entrega.fecha_entrega = datetime.now().isoformat()

    _entregas_db[entrega_id] = entrega
    return entrega

@app.delete("/entregas/{entrega_id}", status_code=204)
def eliminar_entrega(entrega_id: str):
    """Eliminar una entrega"""
    if entrega_id not in _entregas_db:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    del _entregas_db[entrega_id]
    return None

