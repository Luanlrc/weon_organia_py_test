from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.routs_reviews.models import Base
from app.config import config

engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Calls SQLAlchemy metadata to create all tables.
    """
    Base.metadata.create_all(bind=engine)
