from dotenv import load_dotenv
load_dotenv()

import pytest
from httpx import AsyncClient, ConnectError
import asyncio
import os
headers = {"Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"}

BASE_URL = "http://weon_api:8000"

async def wait_for_api(url=f"{BASE_URL}/health_check", retries=10, delay=1):
    for _ in range(retries):
        try:
            async with AsyncClient() as ac:
                response = await ac.get(url, headers = headers)
                if response.status_code == 200:
                    return True
        except ConnectError:
            pass
        await asyncio.sleep(delay)
    raise RuntimeError("API não respondeu dentro do tempo esperado.")

@pytest.mark.asyncio
async def test_agent_classification():
    await wait_for_api()

    async with AsyncClient(base_url=f"{BASE_URL}") as ac:
        response = await ac.post(
            "/test/agent",
            params={
                "text": "O atendimento foi bom, mas incompleto."
            },
            headers=headers
        )
        assert response.status_code == 200
        assert response.text.strip('"') in ["positiva", "neutra", "negativa"]
