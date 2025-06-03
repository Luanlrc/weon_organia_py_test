from app.api.health_check.models import HealthCheckResponse
from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/health_check",
    tags=["Fastapi"],
    summary="Verifica a saúde da API",
    response_description="Retorna sucesso se a API estiver funcionando",
    response_model=HealthCheckResponse,
)
async def health_check():
    return {"status": "success"}
