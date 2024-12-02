from pydantic import BaseModel, Field


class padecimientoBase(BaseModel):
    nombre_pad: str = Field(max_length=30)
    concepto: str = Field(max_length=100)
    tipo: str = Field(max_length=30)
    area: float = Field(max_digits=5, decimal_places=2)
