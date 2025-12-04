from typing import Dict, List, Optional
from services.entregas.models.entrega import Entrega
from services import db


class EntregaRepository:
    """Repositorio para gestionar entregas en SQLite"""

    def __init__(self):
        self.conn = db.get_connection()

    def crear(self, entrega: Entrega) -> Entrega:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO entregas (id, pedido_id, direccion, repartidor, estado, fecha_asignacion, fecha_entrega) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                entrega.id,
                entrega.pedido_id,
                entrega.direccion,
                entrega.repartidor,
                entrega.estado,
                entrega.fecha_asignacion,
                entrega.fecha_entrega,
            ),
        )
        self.conn.commit()
        return entrega

    def obtener_por_id(self, entrega_id: str) -> Optional[Entrega]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM entregas WHERE id = ?", (entrega_id,))
        row = cur.fetchone()
        if not row:
            return None
        data = dict(row)
        return Entrega(**data)

    def listar_todos(self) -> List[Entrega]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM entregas")
        rows = cur.fetchall()
        return [Entrega(**dict(row)) for row in rows]

    def obtener_por_pedido(self, pedido_id: str) -> List[Entrega]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM entregas WHERE pedido_id = ?", (pedido_id,))
        rows = cur.fetchall()
        return [Entrega(**dict(row)) for row in rows]

    def actualizar(self, entrega_id: str, entrega: Entrega) -> Optional[Entrega]:
        if not self.existe(entrega_id):
            return None
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE entregas SET pedido_id=?, direccion=?, repartidor=?, estado=?, fecha_asignacion=?, fecha_entrega=? WHERE id=?",
            (
                entrega.pedido_id,
                entrega.direccion,
                entrega.repartidor,
                entrega.estado,
                entrega.fecha_asignacion,
                entrega.fecha_entrega,
                entrega_id,
            ),
        )
        self.conn.commit()
        return entrega

    def eliminar(self, entrega_id: str) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM entregas WHERE id = ?", (entrega_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def existe(self, entrega_id: str) -> bool:
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM entregas WHERE id = ?", (entrega_id,))
        return cur.fetchone() is not None
