import os
import secrets

from pydantic import BaseSettings
from typing import Union, Literal


class Settings(BaseSettings):
    PROJECT_NAME: str = (
        f"C-Esperto - Study Assistant - {os.getenv('ENV', 'dev').capitalize()}"
    )
    DESCRIPTION: str = "A Study assistant"
    ENV: Union[Literal["dev"], Literal["prod"]] = "dev"
    VERSION: str = "0.1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = "sqlite:///database.db"
    QDRANT_PERSIST_DIRECTORY: str = "/tmp/c_esperto"


settings = Settings()
