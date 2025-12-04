from fastapi import FastAPI
from services.pedidos.controllers.pedido_controller import router as pedido_router

app = FastAPI(
    title="Pizzería API - Microservicio de Pedidos",
    description="API REST para gestionar pedidos de una pizzería",
    version="1.0.0"
)


@app.get("/health")
def health():
    """Endpoint de salud del servicio"""
    return {"status": "ok", "servicio": "pedidos"}


# Registrar rutas
app.include_router(pedido_router)

