from fastapi import FastAPI
from routers import imagen_limon, certificacion, limones, padecimiento
from models import Certificacion, Limones, Padecimiento, Imagen_Limon
from database import engine


app = FastAPI(
    title="API de Limones",
    description="API de Limones",
    version="0.0.1",
    docs_url="/",
)

Certificacion.Base.metadata.create_all(bind=engine)
Limones.Base.metadata.create_all(bind=engine)
Padecimiento.Base.metadata.create_all(bind=engine)
Imagen_Limon.Base.metadata.create_all(bind=engine)

app.include_router(imagen_limon.router)
app.include_router(certificacion.router)
app.include_router(limones.router)
app.include_router(padecimiento.router)
