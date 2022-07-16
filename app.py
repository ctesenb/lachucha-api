from fastapi import FastAPI
from routes.pedido import pedido
from routes.detallepedido import detallepedido
from routes.plato import plato

app = FastAPI()

app.include_router(pedido)
app.include_router(detallepedido)
app.include_router(plato)
