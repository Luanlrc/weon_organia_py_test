from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.config import config
from app.api.routs_reviews.routs import router as reviews_router
from app.api.health_check.routs import router as health_check_router
from app.clients.database_client import init_db
from app.auth.bearer_auth import FixedTokenBearer

import uvicorn

security = HTTPBasic()
auth_bearer = FixedTokenBearer(token=config.BEARER_TOKEN)

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != config.USER or credentials.password != config.PASSWORD:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return credentials

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
    "http://0.0.0.0:8000",
]

def create_application():
    app = FastAPI(
        title="Weon Organia - Classificação de Avaliações",
        description="""
        API para classificação de avaliações de clientes usando IA (OpenAI).
        """,
        version="1.0.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_db()

    app.include_router(reviews_router)
    app.include_router(health_check_router)

    @app.get("/api/docs", include_in_schema=False, dependencies=[Depends(authenticate)])
    async def get_swagger_ui():
        return get_swagger_ui_html(openapi_url="/api/openapi.json", title="Weon Organia Docs")

    @app.get("/api/redoc", include_in_schema=False, dependencies=[Depends(authenticate)])
    async def get_redoc():
        return get_redoc_html(openapi_url="/api/openapi.json", title="Weon Organia Redoc")

    @app.get("/api/openapi.json", include_in_schema=False, dependencies=[Depends(authenticate)])
    async def get_openapi_json():
        return get_openapi(title=app.title, version=app.version, routes=app.routes)

    return app

app = create_application()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=config.HOST, port=config.PORT, reload=config.RELOADED)
