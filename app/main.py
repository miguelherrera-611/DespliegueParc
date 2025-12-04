from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Pizzería API - Microservicio de Pedidos")

# Modelos para Pedidos
class PedidoIn(BaseModel):
    cliente: str
    telefono: str
    direccion: str
    pizzas: List[str]  # Lista de tipos de pizza
    cantidad: int

class Pedido(PedidoIn):
    id: str
    estado: str  # "pendiente", "preparando", "listo"
    fecha: str

# Almacenamiento en memoria
_pedidos_db: Dict[str, Pedido] = {}

@app.get("/health")
def health():
    return {"status": "ok", "servicio": "pedidos"}

@app.post("/pedidos/", response_model=Pedido, status_code=201)
def crear_pedido(pedido_in: PedidoIn):
    """Crear un nuevo pedido de pizza"""
    pid = str(uuid4())
    pedido = Pedido(
        id=pid,
        estado="pendiente",
        fecha=datetime.now().isoformat(),
        **pedido_in.model_dump()
    )
    _pedidos_db[pid] = pedido
    return pedido

@app.get("/pedidos/", response_model=List[Pedido])
def listar_pedidos():
    """Listar todos los pedidos"""
    return list(_pedidos_db.values())

@app.get("/pedidos/{pedido_id}", response_model=Pedido)
def obtener_pedido(pedido_id: str):
    """Obtener un pedido específico"""
    pedido = _pedidos_db.get(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@app.put("/pedidos/{pedido_id}/estado", response_model=Pedido)
def actualizar_estado_pedido(pedido_id: str, estado: str):
    """Actualizar el estado de un pedido (pendiente, preparando, listo)"""
    pedido = _pedidos_db.get(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    estados_validos = ["pendiente", "preparando", "listo"]
    if estado not in estados_validos:
        raise HTTPException(status_code=400, detail=f"Estado inválido. Use: {estados_validos}")

    pedido.estado = estado
    _pedidos_db[pedido_id] = pedido
    return pedido

@app.delete("/pedidos/{pedido_id}", status_code=204)
def eliminar_pedido(pedido_id: str):
    """Eliminar un pedido"""
    if pedido_id not in _pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    del _pedidos_db[pedido_id]
    return None