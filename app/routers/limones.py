from fastapi import APIRouter

router = APIRouter(
    prefix="/limones",
    tags=["limones"],
)


@router.get("/")
async def read_limones():
    return [{"limones": "limones"}]
