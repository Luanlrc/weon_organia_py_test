from app.handlers.llm_handler import call_openai_model
from app.openai_config import openai_settings


class SentimentAgent:
    """
    Agente de análise de sentimento baseado em linguagem natural.
    Recebe uma avaliação de cliente e retorna: positiva, negativa ou neutra.
    """

    def __init__(self):
        self.model = openai_settings.model
        self.temperature = openai_settings.temperature
        self.max_tokens = openai_settings.max_tokens

    def classify(self, customer_text: str) -> str:
        prompt = f"""
        Você é um classificador de sentimentos especializado em avaliações de clientes.

        Sua tarefa é classificar a avaliação abaixo como uma das seguintes opções:
        - positiva
        - negativa
        - neutra

        Regras de classificação:
        1. Se o texto for majoritariamente elogioso, com tom de 
        satisfação e sem críticas relevantes, classifique como `positiva`.

        2. Se houver críticas claras, frustração ou tom negativo
        predominante, classifique como `negativa`.

        3. Se o texto tiver pontos positivos e negativos misturados,
        ou se for ambíguo, classifique como `neutra`.

        Importante:
        - Não explique a resposta.
        - Responda apenas com: positiva, negativa ou neutra (em minúsculas).

        Avaliação:
        "{customer_text}"
        """

        response = call_openai_model(
            prompt=prompt,
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        return response.lower().strip()
