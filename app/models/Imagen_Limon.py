from app.database import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, LargeBinary, Numeric


class Imagen_Limon(Base):
    __tablename__ = "imagen_limon"

    id_limon = Column(
        BigInteger,
        ForeignKey("limones.id_limones"),
        primary_key=True,
        index=True,
        autoincrement=True,
    )
    imagen = Column(LargeBinary)
    rgb = Column(Numeric(5, 2), default=0)
    umbral = Column(Numeric(5, 2), default=0)
    hsv = Column(Numeric(5, 2), default=0)
    numero_pixeles = Column(Integer)
