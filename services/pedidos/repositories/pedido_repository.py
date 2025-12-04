from typing import Dict, List, Optional
from services.pedidos.models.pedido import Pedido
from services import db
import json


class PedidoRepository:
    """Repositorio para gestionar pedidos en SQLite"""

    def __init__(self):
        self.conn = db.get_connection()

    def crear(self, pedido: Pedido) -> Pedido:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO pedidos (id, cliente, telefono, direccion, pizzas, cantidad, estado, fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                pedido.id,
                pedido.cliente,
                pedido.telefono,
                pedido.direccion,
                json.dumps(pedido.pizzas, ensure_ascii=False),
                pedido.cantidad,
                pedido.estado,
                pedido.fecha,
            ),
        )
        self.conn.commit()
        return pedido

    def obtener_por_id(self, pedido_id: str) -> Optional[Pedido]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
        row = cur.fetchone()
        if not row:
            return None
        data = dict(row)
        data['pizzas'] = json.loads(data['pizzas'])
        return Pedido(**data)

    def listar_todos(self) -> List[Pedido]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pedidos")
        rows = cur.fetchall()
        result: List[Pedido] = []
        for row in rows:
            data = dict(row)
            data['pizzas'] = json.loads(data['pizzas'])
            result.append(Pedido(**data))
        return result

    def actualizar(self, pedido_id: str, pedido: Pedido) -> Optional[Pedido]:
        if not self.existe(pedido_id):
            return None
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE pedidos SET cliente=?, telefono=?, direccion=?, pizzas=?, cantidad=?, estado=?, fecha=? WHERE id=?",
            (
                pedido.cliente,
                pedido.telefono,
                pedido.direccion,
                json.dumps(pedido.pizzas, ensure_ascii=False),
                pedido.cantidad,
                pedido.estado,
                pedido.fecha,
                pedido_id,
            ),
        )
        self.conn.commit()
        return pedido

    def eliminar(self, pedido_id: str) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def existe(self, pedido_id: str) -> bool:
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM pedidos WHERE id = ?", (pedido_id,))
        return cur.fetchone() is not None
