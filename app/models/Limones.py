from database import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Numeric, String


class Limones(Base):
    __tablename__ = "limones"

    id_limones = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    color_cascara = Column(String(7))
    textura_cascara = Column(String(30))
    diametro = Column(Numeric(4, 2))
    forma = Column(String(20))
    brillo = Column(Numeric(5, 2))
    uniformidad = Column(Numeric(5, 2))
    peso = Column(Numeric(5, 2))
    porosidad = Column(String(30))
    nivel_madurez = Column(String(30))
    certificacion = Column(BigInteger, ForeignKey("certificacion.no_etiquetado"))
    id_pad = Column(BigInteger, ForeignKey("padecimiento.id_pad"))
