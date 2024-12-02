from pydantic import BaseModel, Field


class limonesBase(BaseModel):
    color_cascara: str = Field(max_length=7)
    textura_cacara: str = Field(max_length=30)
    diametro: float = Field(max_digits=4, decimal_places=2)
    forma: str = Field(max_length=20)
    brillo: float = Field(max_digits=5, decimal_places=2)
    uniformidad: float = Field(max_digits=5, decimal_places=2)
    peso: float = Field(max_digits=5, decimal_places=2)
    porosidad: str = Field(max_length=30)
    nivel_madurez: str = Field(max_length=30)
    certificacion: int = Field(gt=0)
    id_pad: int = Field(gt=0)
