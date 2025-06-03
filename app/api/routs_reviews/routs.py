from fastapi import APIRouter

router = APIRouter()

@router.get("/teste")
async def teste():
    return "teste"