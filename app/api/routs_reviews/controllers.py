from app.api.routs_reviews.models import Review, ReviewDB, ReviewResponse
from app.agents.sentiment_agent import SentimentAgent
from app.clients.database_client import SessionLocal
from app.sql.config import load_sql
from sqlalchemy import text

agent = SentimentAgent()

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
            sentiment = agent.classify(review.avaliation)

            db_review = ReviewDB(
                client_name=review.client_name,
                avaliation_date=review.avaliation_date,
                avaliation=review.avaliation,
                avaliation_type=sentiment
            )
            db.add(db_review)
            db.commit()
            db.refresh(db_review)
            return ReviewResponse.model_validate(db_review)

    def get_report(self, start_date: str, end_date: str):
        query = load_sql("report_reviews.sql")
        with SessionLocal() as db:
            result = db.execute(
                text(query),
                {"start_date": start_date, "end_date": end_date}
            ).fetchall()
            return [
                {"avaliation_type": row[0], "total": row[1]}
                for row in result
            ]

    def test_agent(self, text):
        sentiment = agent.classify(text)
        return sentiment

review_controller = ReviewController()
