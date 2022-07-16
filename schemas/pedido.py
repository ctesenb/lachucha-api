from pydantic import BaseModel
from typing import Optional

class Pedido(BaseModel):
    codigoPedido: Optional[int]
    cliente: str
    correo: str
    cantPlato: int
    delivery: bool
    Observacion: str
    hora: str
    fecha: str
    estado: str
    total: int