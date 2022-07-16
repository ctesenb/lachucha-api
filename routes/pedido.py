from fastapi import APIRouter, Response, status
from config.db import conn
from models.pedido import pedidos
from schemas.pedido import Pedido
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)     # Cifrado de contraseña para el usuario https://www.youtube.com/watch?v=6eVj33l5e9M

pedido = APIRouter()

@pedido.get("/pedidos", response_model=list[Pedido], tags=["Pedidos"])
def get_pedidos():
    return conn.execute(pedidos.select()).fetchall()

@pedido.post("/pedidos", response_model=Pedido, tags=["Pedidos"])
def create_pedido(pedido: Pedido):
    new_post = {'cliente': pedido.cliente, 'correo': pedido.correo, 'cantPlato': pedido.cantPlato, 'delivery': pedido.delivery, 'Observacion': pedido.Observacion, 'hora': pedido.hora, 'fecha': pedido.fecha, 'estado': pedido.estado, 'total': pedido.total}
    result = conn.execute(pedidos.insert().values(new_post))
    print(result.lastrowid)
    return conn.execute(pedidos.select().where(pedidos.c.codigoPedido == result.lastrowid)).first()

@pedido.get("/pedidos/{codigoPedido}", response_model=Pedido, tags=["Pedidos"])
def get_pedido(codigoPedido: int):
    return conn.execute(pedidos.select().where(pedidos.c.codigoPedido == codigoPedido)).first()

@pedido.delete("/pedidos/{codigoPedido}", status_code=status.HTTP_204_NO_CONTENT, tags=["Pedidos"])
def delete_pedido(codigoPedido: int):
    conn.execute(pedidos.delete().where(pedidos.c.codigoPedido == codigoPedido))
    return Response(status_code=HTTP_204_NO_CONTENT)

@pedido.put("/pedidos/{codigoPedido}", response_model=Pedido, tags=["Pedidos"])
def update_pedido(codigoPedido: int, pedido: Pedido):
    conn.execute(pedidos.update().values(cantPlato=pedido.cantPlato, descuento=pedido.descuento, Observacion=pedido.Observacion, total=pedido.total, delivery=pedido.delivery).where(pedidos.c.codigoPedido == codigoPedido))
    return conn.execute(pedidos.select().where(pedidos.c.codigoPedido == codigoPedido)).first()

@pedido.put("/pedidos/{codigoPedido}/", response_model=Pedido, tags=["Pedidos"])
def update_pedidoestado(codigoPedido: int, pedido: Pedido):
    conn.execute(pedidos.update().values(estado=pedido.estado).where(pedidos.c.codigoPedido == codigoPedido))
    return conn.execute(pedidos.select().where(pedidos.c.codigoPedido == codigoPedido)).first()
