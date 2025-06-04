from app.handlers.llm_handler import call_openai_model
from app.openai_config import openai_settings


class SentimentAgent:
    """
    Sentiment analysis agent based on natural language processing.

    This class uses the OpenAI API to classify customer reviews as
    'positive', 'negative', or 'neutral'.
    """

    def __init__(self):
        """
        Initializes the sentiment agent with OpenAI model settings,
        including model name, temperature, and max tokens.
        """
        self.model = openai_settings.model
        self.temperature = openai_settings.temperature
        self.max_tokens = openai_settings.max_tokens

    def classify(self, customer_text: str) -> str:
        """
        Args:
            customer_text (str): The customer's review text.

        Returns:
            str: Sentiment classification (""positiva"", ""neutra"", ""negativa"").
        """
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
