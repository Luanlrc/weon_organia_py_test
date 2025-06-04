from datetime import date, datetime

from pydantic import BaseModel
from sqlalchemy import Column, Date, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ReviewDB(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    avaliation_date = Column(Date, nullable=False)
    avaliation = Column(String, nullable=False)
    avaliation_type = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Review(BaseModel):
    client_name: str
    avaliation_date: date
    avaliation: str


class ReviewResponse(BaseModel):
    id: int
    client_name: str
    avaliation_date: date
    avaliation: str
    avaliation_type: str
    created_at: datetime

    model_config = {"from_attributes": True}
