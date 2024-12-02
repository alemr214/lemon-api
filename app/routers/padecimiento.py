from fastapi import APIRouter

router = APIRouter(
    prefix="/padecimiento",
    tags=["padecimiento"],
)


@router.get("/")
async def read_padecimiento():
    return [{"padecimiento": "padecimiento"}]
