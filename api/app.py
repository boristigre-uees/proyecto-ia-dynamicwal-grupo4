from fastapi import FastAPI
from api.routes.pricing import router as pricing_router

app = FastAPI(
    title="DynamicWal API",
    description="API para optimización de precios dinámica",
    version="1.0"
)

app.include_router(pricing_router)

@app.get("/")
def root():
    return {"message": "DynamicWal API - Optimización de Precios Dinámica"}