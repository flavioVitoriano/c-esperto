from app.config import settings
import uvicorn


if __name__ == "__main__":
    reload = settings.ENV == "dev"
    uvicorn.run("app:app", port=8888, reload=reload)
