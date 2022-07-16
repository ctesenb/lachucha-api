from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

detallepedidos = Table('detallepedidos', meta, Column('codigoDetallePedido', Integer, primary_key=True), Column(
    'codigoPedido', Integer), Column('nombrePlato', String(255)), Column('cantidad', Integer), Column('precio', Integer))

meta.create_all(engine)
