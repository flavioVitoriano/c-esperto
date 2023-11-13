from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import chat_router
from pydantic import BaseSettings
from app.config import settings


def create_app(settings: BaseSettings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
    )

    @app.get("ping")
    def pong():
        return "pong!"

    @app.on_event("startup")
    def on_starup():
        create_db_and_tables()

    # routers
    app.include_router(chat_router, prefix="/chat")

    return app


app = create_app(settings)
