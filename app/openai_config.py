from pydantic import BaseModel

from app.config import config


class OpenAISettings(BaseModel):
    model: str = "gpt-4o"
    temperature: float = 0
    max_tokens: int = 3000
    api_key: str = config.OPENAI_API_KEY


openai_settings = OpenAISettings()
