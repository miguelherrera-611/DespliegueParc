from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from datetime import datetime

from services.entregas.models.entrega import Entrega, EntregaIn
from services.entregas.repositories.entrega_repository import EntregaRepository


router = APIRouter(prefix="/entregas", tags=["Entregas"])
repository = EntregaRepository()


@router.post("/", response_model=Entrega, status_code=201)
def crear_entrega(entrega_in: EntregaIn):
    """Asignar una entrega a un repartidor"""
    entrega = Entrega(
        id=str(uuid4()),
        estado="asignada",
        fecha_asignacion=datetime.now().isoformat(),
        **entrega_in.model_dump()
    )
    return repository.crear(entrega)


@router.get("/", response_model=List[Entrega])
def listar_entregas():
    """Listar todas las entregas"""
    return repository.listar_todos()


@router.get("/{entrega_id}", response_model=Entrega)
def obtener_entrega(entrega_id: str):
    """Obtener una entrega específica"""
    entrega = repository.obtener_por_id(entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return entrega


@router.get("/pedido/{pedido_id}", response_model=List[Entrega])
def obtener_entregas_por_pedido(pedido_id: str):
    """Obtener entregas asociadas a un pedido"""
    return repository.obtener_por_pedido(pedido_id)


@router.put("/{entrega_id}/estado", response_model=Entrega)
def actualizar_estado_entrega(entrega_id: str, estado: str):
    """Actualizar el estado de una entrega (asignada, en_camino, entregada)"""
    entrega = repository.obtener_por_id(entrega_id)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")

    estados_validos = ["asignada", "en_camino", "entregada"]
    if estado not in estados_validos:
        raise HTTPException(
            status_code=400,
            detail=f"Estado inválido. Use: {estados_validos}"
        )

    entrega.estado = estado
    if estado == "entregada":
        entrega.fecha_entrega = datetime.now().isoformat()

    repository.actualizar(entrega_id, entrega)
    return entrega


@router.delete("/{entrega_id}", status_code=204)
def eliminar_entrega(entrega_id: str):
    """Eliminar una entrega"""
    if not repository.eliminar(entrega_id):
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return None

