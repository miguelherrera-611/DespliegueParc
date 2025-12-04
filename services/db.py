import os
import sqlite3
from typing import Tuple


def _get_db_path() -> str:
    # project root is one level above services/
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, 'db.sqlite')


def get_connection() -> sqlite3.Connection:
    db_path = _get_db_path()
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    _ensure_tables(conn)
    return conn


def _ensure_tables(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id TEXT PRIMARY KEY,
        cliente TEXT,
        telefono TEXT,
        direccion TEXT,
        pizzas TEXT,
        cantidad INTEGER,
        estado TEXT,
        fecha TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS entregas (
        id TEXT PRIMARY KEY,
        pedido_id TEXT,
        direccion TEXT,
        repartidor TEXT,
        estado TEXT,
        fecha_asignacion TEXT,
        fecha_entrega TEXT
    )
    ''')
    conn.commit()

