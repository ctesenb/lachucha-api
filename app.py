from fastapi import FastAPI
from routes.pedido import pedido
from routes.detallepedido import detallepedido
from routes.plato import plato
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(pedido)
app.include_router(detallepedido)
app.include_router(plato)

origins = [
    "https://lachucha-api.herokuapp.com/",
    "http://localhost:3000/",
    "http://localhost:8000/",
    "http://localhost:5000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)