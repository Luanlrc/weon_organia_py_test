from app.api.health_check.models import HealthCheckResponse
from fastapi import APIRouter
from fastapi import Depends
from app.auth.bearer_auth import auth_bearer

router = APIRouter()

@router.get(
    "/health_check",
    tags=["Fastapi"],
    summary="Verifica a saúde da API",
    response_description="Retorna sucesso se a API estiver funcionando",
    dependencies=[Depends(auth_bearer)],
    response_model=HealthCheckResponse,
    include_in_schema=False
)
async def health_check():
    return {"status": "success"}
