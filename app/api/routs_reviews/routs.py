from typing import List

from fastapi import APIRouter, Depends

from app.api.routs_reviews.controllers import review_controller
from app.api.routs_reviews.models import Review, ReviewResponse
from app.auth.bearer_auth import auth_bearer

router = APIRouter()


@router.get(
    "/reviews",
    tags=["Reviews"],
    response_model=List[ReviewResponse],
    dependencies=[Depends(auth_bearer)],
    description="Retorna todas as avaliações cadastradas.",
    include_in_schema=True,
)
async def list_reviews():
    """
    Returns:
        List[ReviewResponse]: List of all reviews.
    """
    return review_controller.list_reviews()


@router.get(
    "/reviews/report",
    tags=["Reviews"],
    response_model=List[dict],
    dependencies=[Depends(auth_bearer)],
    description="Retorna um relatório de avaliações no período informado, com contagem por tipo (positiva, negativa ou neutra). Formato YYYY-MM-DD.",
    include_in_schema=True,
)
async def get_report(start_date: str, end_date: str):
    """
    Args:
        start_date (str): Start date filter YYYY-MM-DD..
        end_date (str): End date filter YYYY-MM-DD..

    Returns:
        List[dict]: Aggregated sentiment counts.
    """
    return review_controller.get_report(start_date, end_date)


@router.get(
    "/reviews/{review_id}",
    tags=["Reviews"],
    response_model=ReviewResponse,
    dependencies=[Depends(auth_bearer)],
    description="Busca uma avaliação específica pelo ID.",
    include_in_schema=True,
)
async def get_review_by_id(review_id: int):
    """
    Args:
        review_id (int): Review identifier.

    Returns:
        ReviewResponse: Review details.
    """
    return review_controller.get_review_by_id(review_id)


@router.post(
    "/reviews",
    tags=["Reviews"],
    response_model=ReviewResponse,
    dependencies=[Depends(auth_bearer)],
    description="Cria uma nova avaliação e classifica automaticamente com IA como positiva, negativa ou neutra.",
    include_in_schema=True,
)
async def create_review(review: Review):
    """
    Args:
        review (Review): Review data.

    Returns:
        ReviewResponse: Stored and classified review.
    """
    return review_controller.create_review(review)


@router.post(
    "/test/agent",
    tags=["Reviews"],
    dependencies=[Depends(auth_bearer)],
    description="Testa diretamente a classificação de sentimento de um texto usando o agente de IA.",
    include_in_schema=False,
)
async def create_review(text: str):
    """
    Args:
        text (str): Text to classify.

    Returns:
        str: Sentiment classification.
    """
    return review_controller.test_agent(text)
