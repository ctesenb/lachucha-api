from fastapi import APIRouter, Response, status
from config.db import conn
from models.detallepedido import detallepedidos
from schemas.detallepedido import DetallePedido
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)     # Cifrado de contraseña para el usuario https://www.youtube.com/watch?v=6eVj33l5e9M

detallepedido = APIRouter()

@detallepedido.get("/detallepedidos", response_model=list[DetallePedido], tags=["DetallePedidos"])
def get_detallepedidos():
    return conn.execute(detallepedidos.select()).fetchall()

@detallepedido.post("/detallepedidos", response_model=DetallePedido, tags=["DetallePedidos"])
def create_detallepedido(detallepedido: DetallePedido):
    new_post = {'codigoPedido': detallepedido.codigoPedido, 'nombrePlato': detallepedido.nombrePlato, 'cantidad': detallepedido.cantidad, 'precio': detallepedido.precio}
    result = conn.execute(detallepedidos.insert().values(new_post))
    print(result.lastrowid)
    return conn.execute(detallepedidos.select().where(detallepedidos.c.codigoDetallePedido == result.lastrowid)).first()

@detallepedido.get("/detallepedidos/{codigoDetallePedido}", response_model=DetallePedido, tags=["DetallePedidos"])
def get_detallepedido(codigoDetallePedido: int):
    return conn.execute(detallepedidos.select().where(detallepedidos.c.codigoDetallePedido == codigoDetallePedido)).first()

@detallepedido.delete("/detallepedidos/{codigoDetallePedido}", status_code=status.HTTP_204_NO_CONTENT, tags=["DetallePedidos"])
def delete_detallepedido(codigoDetallePedido: int):
    conn.execute(detallepedidos.delete().where(detallepedidos.c.codigoDetallePedido == codigoDetallePedido))
    return Response(status_code=HTTP_204_NO_CONTENT)

@detallepedido.put("/detallepedidos/{codigoDetallePedido}", response_model=DetallePedido, tags=["DetallePedidos"])
def update_detallepedido(codigoDetallePedido: int, detallepedido: DetallePedido):
    conn.execute(detallepedidos.update().values(nombrePlato=detallepedido.nombrePlato, cantidad=detallepedido.cantidad).where(detallepedidos.c.codigoDetallePedido == codigoDetallePedido))
    return conn.execute(detallepedidos.select().where(detallepedidos.c.codigoDetallePedido == codigoDetallePedido)).first()