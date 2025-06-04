from dotenv import load_dotenv

load_dotenv()

import asyncio
import os

import pytest
from httpx import AsyncClient

headers = {"Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"}
BASE_URL = "http://weon_api:8000"


async def wait_for_api(retries=30, delay=1):
    for attempt in range(1, retries + 1):
        try:
            async with AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/health_check", headers=headers)
                if response.status_code == 200:
                    print(f"API respondeu OK na tentativa {attempt}")
                    return
        except Exception as e:
            print(f"⏳ Tentativa {attempt}: {e}")
        await asyncio.sleep(delay)
    raise RuntimeError("❌ API não respondeu a tempo.")


@pytest.mark.asyncio
async def test_create_review():
    await wait_for_api()
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.post(
            "/reviews",
            json={
                "client_name": "Teste Review",
                "avaliation_date": "2025-06-04",
                "avaliation": "Gostei bastante do atendimento.",
            },
            headers=headers,
        )
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["avaliation_type"] in ["positiva", "neutra", "negativa"]


@pytest.mark.asyncio
async def test_list_reviews():
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.get("/reviews", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_review_by_id():
    async with AsyncClient(base_url=BASE_URL) as ac:
        post = await ac.post(
            "/reviews",
            json={
                "client_name": "Teste Individual",
                "avaliation_date": "2025-06-04",
                "avaliation": "Achei o serviço bom, mas poderia ser mais rápido.",
            },
            headers=headers,
        )
        assert post.status_code == 200
        review_id = post.json()["id"]

        get = await ac.get(f"/reviews/{review_id}", headers=headers)
        assert get.status_code == 200
        assert get.json()["id"] == review_id


@pytest.mark.asyncio
async def test_report():
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.get(
            "/reviews/report",
            params={"start_date": "2025-06-01", "end_date": "2025-06-30"},
            headers=headers,
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        for item in response.json():
            assert "avaliation_type" in item
            assert "total" in item
