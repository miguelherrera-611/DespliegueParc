from pydantic import BaseModel
from typing import List


class PedidoIn(BaseModel):
    """Modelo de entrada para crear un pedido"""
    cliente: str
    telefono: str
    direccion: str
    pizzas: List[str]  # Lista de tipos de pizza
    cantidad: int


class Pedido(PedidoIn):
    """Modelo completo de un pedido"""
    id: str
    estado: str  # "pendiente", "preparando", "listo"
    fecha: str

