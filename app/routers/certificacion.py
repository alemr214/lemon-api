from fastapi import APIRouter
from schemas.certificacion import certificacionBase

router = APIRouter(
    prefix="/certificacion",
    tags=["certificacion"],
)


@router.get("/")
async def read_certificacion():
    return [{"certificacion": "certificacion"}]
