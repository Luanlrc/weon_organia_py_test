from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API Weon Organia está online"}