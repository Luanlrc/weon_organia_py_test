from fastapi import APIRouter
from app.api.routs_reviews.controllers import review_controller
from app.api.routs_reviews.models import Review
router = APIRouter()

@router.get("/reviews", tags=["Reviews"])
async def list_reviews():
    return review_controller.list_reviews()

@router.get("/reviews/{id}", tags=["Reviews"])
async def get_review_by_id(review_id: int):
    return review_controller.get_review_by_id(review_id)

@router.get("/reviews/report", tags=["Reviews"])
async def get_report(start_date: str, end_date: str):
    return review_controller.get_report(start_date, end_date)

@router.post("/reviews", tags=["Reviews"])
async def create_review(review: Review):
    return review_controller.create_review(review)
