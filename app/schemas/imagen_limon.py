from pydantic import BaseModel, Field


class imagen_limonBase(BaseModel):
    imagen: bytes = Field()
    rgb: float = Field(max_digits=5, decimal_places=2, default=0)
    umbral: float = Field(max_digits=5, decimal_places=2, default=0)
    hsv: float = Field(max_digits=5, decimal_places=2, default=0)
    numero_pixeles: int = Field(gt=0)
