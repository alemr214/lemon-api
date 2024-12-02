from fastapi import APIRouter

router = APIRouter(
    prefix="/imagen_limon",
    tags=["imagen_limon"],
)


@router.get("/")
async def read_certificacion():
    return [{"imagen limon": "imagen_limon"}]
