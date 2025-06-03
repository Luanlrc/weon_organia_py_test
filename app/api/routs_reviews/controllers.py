from sqlalchemy.orm import Session
from app.clients.database_client import SessionLocal
from app.api.routs_reviews.models import Review, ReviewDB, ReviewResponse

class ReviewController:
    def list_reviews(self):
        with SessionLocal() as db:
            reviews = db.query(ReviewDB).all()
            response_list = []
            for r in reviews:
                response = ReviewResponse.model_validate(r)
                response_list.append(response)

            return response_list

    def get_review_by_id(self, review_id: int):
        with SessionLocal() as db:
            review = db.query(ReviewDB).filter(ReviewDB.id == review_id).first()
            if review:
                return ReviewResponse.model_validate(review)
            return {"error": "Review not found"}

    def create_review(self, review: Review):
        with SessionLocal() as db:
            db_review = ReviewDB(
                client_name=review.client_name,
                avaliation_date=review.avaliation_date,
                avaliation=review.avaliation,
                avaliation_type=review.avaliation_type
            )
            db.add(db_review)
            db.commit()
            db.refresh(db_review)
            return ReviewResponse.model_validate(db_review)

    def get_report(self, start_date: str, end_date: str):
        return {"message": "em construção"}

review_controller = ReviewController()
