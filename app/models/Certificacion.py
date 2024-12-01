from app.database import Base
from sqlalchemy import BigInteger, Column, String, Integer


class Certificacion(Base):
    no_etiquetado = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre_certificado = Column(String(50))
    nivel_calidad = Column(Integer)
