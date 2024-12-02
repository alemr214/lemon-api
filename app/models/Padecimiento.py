from database import Base
from sqlalchemy import BigInteger, Column, Numeric, String


class Padecimiento(Base):
    __tablename__ = "padecimiento"

    id_pad = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre_pad = Column(String(30))
    concepto = Column(String(100))
    tipo = Column(String(30))
    area = Column(Numeric(5, 2))
