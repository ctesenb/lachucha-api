from fastapi import APIRouter, Response, status
from config.db import conn
from models.plato import platos
from schemas.plato import Plato
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)     # Cifrado de contraseña para el usuario https://www.youtube.com/watch?v=6eVj33l5e9M

plato = APIRouter()

@plato.get("/platos", response_model=list[Plato], tags=["Platos"])
def get_platos():
    return conn.execute(platos.select()).fetchall()

@plato.post("/platos", response_model=Plato, tags=["Platos"])
def create_plato(plato: Plato):
    new_post = {'descripcionPlato': plato.descripcionPlato, 'disponible': plato.disponible, 'nombrePlato': plato.nombrePlato, 'precio': plato.precio}
    result = conn.execute(platos.insert().values(new_post))
    print(result.lastrowid)
    return conn.execute(platos.select().where(platos.c.codigoPlato == result.lastrowid)).first()

@plato.get("/platos/{codigoPlato}", response_model=Plato, tags=["Platos"])
def get_plato(codigoPlato: int):
    return conn.execute(platos.select().where(platos.c.codigoPlato == codigoPlato)).first()

@plato.delete("/platos/{codigoPlato}", status_code=status.HTTP_204_NO_CONTENT, tags=["Platos"])
def delete_plato(codigoPlato: int):
    conn.execute(platos.delete().where(platos.c.codigoPlato == codigoPlato))
    return Response(status_code=HTTP_204_NO_CONTENT)

@plato.put("/platos/{codigoPlato}", response_model=Plato, tags=["Platos"])
def update_plato(codigoPlato: int, plato: Plato):
    conn.execute(platos.update().values(disponible=plato.disponible, precio=plato.precio).where(platos.c.codigoPlato == codigoPlato))
    return conn.execute(platos.select().where(platos.c.codigoPlato == codigoPlato)).first()