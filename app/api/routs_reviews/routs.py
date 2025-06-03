from fastapi import APIRouter

router = APIRouter()

@router.get("/reviews", tags=["Reviews"])
async def list_reviews():
    return {"message": "Listar todas as avaliações (placeholder)"}

@router.get("/reviews/{id}", tags=["Reviews"])
async def get_review(review_id: int):
    return {"message": f"Buscar avaliação com ID {review_id} (placeholder)"}

@router.get("/reviews/report/", tags=["Reviews"])
async def get_report(start_date: str, end_date: str):
    return {"message": f"Relatório de {start_date} a {end_date} (placeholder)"}

@router.post("/reviews", tags=["Reviews"])
async def create_review():
    return {"message": "Criar nova avaliação (placeholder)"}
