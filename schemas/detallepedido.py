from pydantic import BaseModel
from typing import Optional

class DetallePedido(BaseModel):
    codigoDetallePedido: Optional[int]
    codigoPedido: int
    nombrePlato: str
    cantidad: int
    precio: int