from typing import ClassVar, Dict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOADED: bool = True

config = Settings()
