from pydantic import BaseModel, Field


class certificacionBase(BaseModel):
    nombre_certificado: str = Field(max_length=50)
    nivel_calidad: int
