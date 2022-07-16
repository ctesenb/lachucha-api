from pydantic import BaseModel
from typing import Optional

class Plato(BaseModel):
    codigoPlato: Optional[int]
    descripcionPlato: str
    disponible: bool
    nombrePlato: str
    precio: int