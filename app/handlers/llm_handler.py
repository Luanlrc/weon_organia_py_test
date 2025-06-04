import os

import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_openai_model(
    prompt: str, model: str, temperature: float = 0, max_tokens: int = 3000
) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Erro ao chamar modelo OpenAI: {e}")
