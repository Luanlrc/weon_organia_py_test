from fastapi import FastAPI
from app.api.routs_reviews.routs import router as reviews_router
from app.api.health_check.routs import router as health_check_router
from app.api.default_routs import router as default_router
from app.config import config
import uvicorn

def create_application():
    app = FastAPI(title="Weon Organia - Classificação de Avaliações")

    routers = [reviews_router, health_check_router, default_router]
    default_responses = {
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not found"},
        500: {"description": "Internal server error"}
    }

    for router in routers:
        app.include_router(router, responses=default_responses)

    return app

app = create_application()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=config.HOST, port=config.PORT, reload=config.RELOADED)
