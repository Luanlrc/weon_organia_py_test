from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from datetime import date

Base = declarative_base()

class ReviewDB(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    avaliation_date = Column(Date, nullable=False)
    avaliation = Column(String, nullable=False)
    avaliation_type = Column(String, nullable=False)

class Review(BaseModel):
    client_name: str
    avaliation_date: date
    avaliation: str
    avaliation_type: str

class ReviewResponse(Review):
    id: int

    model_config = {
        "from_attributes": True
    }
