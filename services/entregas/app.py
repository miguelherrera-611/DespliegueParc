from fastapi import FastAPI
from services.entregas.controllers.entrega_controller import router as entrega_router

app = FastAPI(
    title="Pizzería API - Microservicio de Entregas",
    description="API REST para gestionar entregas de pedidos de pizzería",
    version="1.0.0"
)


@app.get("/health")
def health():
    """Endpoint de salud del servicio"""
    return {"status": "ok", "servicio": "entregas"}


# Registrar rutas
app.include_router(entrega_router)

