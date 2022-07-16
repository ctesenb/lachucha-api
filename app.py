from fastapi import FastAPI
from routes.pedido import pedido
from routes.detallepedido import detallepedido
from routes.plato import plato
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=['*']
    )
app.include_router(pedido)
app.include_router(detallepedido)
app.include_router(plato)
