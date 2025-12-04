from pydantic import BaseModel
from typing import Optional


class EntregaIn(BaseModel):
    """Modelo de entrada para crear una entrega"""
    pedido_id: str
    direccion: str
    repartidor: str


class Entrega(EntregaIn):
    """Modelo completo de una entrega"""
    id: str
    estado: str  # "asignada", "en_camino", "entregada"
    fecha_asignacion: str
    fecha_entrega: Optional[str] = None

