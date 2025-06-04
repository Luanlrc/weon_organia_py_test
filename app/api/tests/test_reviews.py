import pytest
from httpx import AsyncClient
import asyncio

BASE_URL = "http://weon_api:8000"

async def wait_for_api(url=f"{BASE_URL}/health_check", retries=10, delay=1):
    for _ in range(retries):
        try:
            async with AsyncClient() as ac:
                response = await ac.get(url)
                if response.status_code == 200:
                    return
        except:
            pass
        await asyncio.sleep(delay)
    raise RuntimeError("API não respondeu a tempo.")

@pytest.mark.asyncio
async def test_create_review():
    await wait_for_api()
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.post("/reviews", json={
            "client_name": "Teste Review",
            "avaliation_date": "2025-06-04",
            "avaliation": "Gostei bastante do atendimento."
        })
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["avaliation_type"] in ["positiva", "neutra", "negativa"]

@pytest.mark.asyncio
async def test_list_reviews():
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.get("/reviews")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_review_by_id():
    async with AsyncClient(base_url=BASE_URL) as ac:
        post = await ac.post("/reviews", json={
            "client_name": "Teste Individual",
            "avaliation_date": "2025-06-04",
            "avaliation": "Achei o serviço bom, mas poderia ser mais rápido."
        })
        assert post.status_code == 200
        review_id = post.json()["id"]

        get = await ac.get(f"/reviews/{review_id}")
        assert get.status_code == 200
        assert get.json()["id"] == review_id

@pytest.mark.asyncio
async def test_report():
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.get("/reviews/report", params={
            "start_date": "2025-06-01",
            "end_date": "2025-06-30"
        })
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        for item in response.json():
            assert "avaliation_type" in item
            assert "total" in item
