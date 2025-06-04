from dotenv import load_dotenv

load_dotenv()

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.api.health_check.routs import router as health_check_router
from app.api.routs_reviews.routs import router as reviews_router
from app.auth.bearer_auth import FixedTokenBearer
from app.clients.database_client import init_db
from app.config import config

security = HTTPBasic()
auth_bearer = FixedTokenBearer(token=config.BEARER_TOKEN)


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Args:
        credentials (HTTPBasicCredentials): Username and password provided in request.

    Returns:
        HTTPBasicCredentials: Validated credentials.

    Raises:
        HTTPException: If the credentials are invalid.
    """
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
    """
    Returns:
        FastAPI: Configured FastAPI instance.
    """
    app = FastAPI(
        title="Weon Organia - Classificação de Avaliações",
        description="""
        
        API para classificação de avaliações de clientes utilizando inteligência artificial (OpenAI).

        Esta aplicação permite analisar o sentimento de avaliações enviadas por clientes e categorizá-las automaticamente como **positiva**, **negativa** ou **neutra**.  
        Os dados são armazenados em um banco PostgreSQL e podem ser consultados, analisados por ID ou agrupados em relatórios por período.

        Segurança:
        - O acesso às rotas é protegido por autenticação Bearer Token fixa, 
        exigida via cabeçalho `Authorization: Bearer <TOKEN>`.

        - O acesso à documentação interativa (`/api/docs`, `/api/redoc`) e 
        ao schema OpenAPI (`/api/openapi.json`) foi reconfigurado com segurança 
        e também requer autenticação via HTTP Basic.

        """,
        version="1.0.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
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

    @app.get(
        "/api/docs",
        include_in_schema=False,
        dependencies=[Depends(authenticate)]
    )
    async def get_swagger_ui():
        """
        Returns:
            HTMLResponse: Swagger UI HTML page.
        """
        return get_swagger_ui_html(
            openapi_url="/api/openapi.json", title="Weon Organia Docs"
        )

    @app.get(
        "/api/redoc",
        include_in_schema=False,
        dependencies=[Depends(authenticate)]
    )
    async def get_redoc():
        """
        Returns:
            HTMLResponse: Redoc HTML page.
        """
        return get_redoc_html(
            openapi_url="/api/openapi.json", title="Weon Organia Redoc"
        )

    @app.get(
        "/api/openapi.json",
        include_in_schema=False,
        dependencies=[Depends(authenticate)],
    )
    async def get_openapi_json():
        """
        Returns:
            dict: OpenAPI schema.
        """
        return get_openapi(
            title=app.title,
            version=app.version,
            routes=app.routes
        )

    return app


app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.RELOADED
    )
