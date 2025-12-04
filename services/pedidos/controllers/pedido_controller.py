from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from datetime import datetime

from services.pedidos.models.pedido import Pedido, PedidoIn
from services.pedidos.repositories.pedido_repository import PedidoRepository


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
repository = PedidoRepository()


@router.post("/", response_model=Pedido, status_code=201)
def crear_pedido(pedido_in: PedidoIn):
    """Crear un nuevo pedido de pizza"""
    pedido = Pedido(
        id=str(uuid4()),
        estado="pendiente",
        fecha=datetime.now().isoformat(),
        **pedido_in.model_dump()
    )
    return repository.crear(pedido)


@router.get("/", response_model=List[Pedido])
def listar_pedidos():
    """Listar todos los pedidos"""
    return repository.listar_todos()


@router.get("/{pedido_id}", response_model=Pedido)
def obtener_pedido(pedido_id: str):
    """Obtener un pedido específico"""
    pedido = repository.obtener_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.put("/{pedido_id}/estado", response_model=Pedido)
def actualizar_estado_pedido(pedido_id: str, estado: str):
    """Actualizar el estado de un pedido (pendiente, preparando, listo)"""
    pedido = repository.obtener_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    estados_validos = ["pendiente", "preparando", "listo"]
    if estado not in estados_validos:
        raise HTTPException(
            status_code=400,
            detail=f"Estado inválido. Use: {estados_validos}"
        )

    pedido.estado = estado
    repository.actualizar(pedido_id, pedido)
    return pedido


@router.delete("/{pedido_id}", status_code=204)
def eliminar_pedido(pedido_id: str):
    """Eliminar un pedido"""
    if not repository.eliminar(pedido_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return None

