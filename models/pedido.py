from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

pedidos = Table('pedidos', meta, Column('codigoPedido', Integer, primary_key=True), Column('cliente', String(55)),Column('correo', String(50)), Column(
    'cantPlato', Integer), Column('delivery', Boolean), Column('Observacion', String(255)),Column('hora', String(20)),Column('fecha', String(20)),Column('estado', String(50)),Column('total', Integer))

meta.create_all(engine)
