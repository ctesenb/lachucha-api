from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

platos = Table('platos', meta, Column('codigoPlato', Integer, primary_key=True), Column('descripcionPlato', String(255)), Column('disponible', Boolean), Column('nombrePlato', String(255)), Column('precio', Integer))

meta.create_all(engine)