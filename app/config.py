from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # API
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = os.getenv("PORT", 8000)
    RELOADED: bool = os.getenv("RELOADED", True)
    USER: str = os.getenv("USER")
    PASSWORD: str = os.getenv("PASSWORD")
    BEARER_TOKEN: str = os.getenv("BEARER_TOKEN")

    # DATABASE
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # OPENAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

config = Settings()
