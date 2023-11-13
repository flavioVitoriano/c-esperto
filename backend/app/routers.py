from fastapi import APIRouter, UploadFile, Depends
from typing import List
from sqlmodel import Session
from app.models import ChatModel
from app.database import get_session
from langchain.vectorstores.qdrant import Qdrant
from tempfile import TemporaryDirectory
from fastapi.responses import HTMLResponse


chat_router = APIRouter()


@chat_router.post("/")
def create_chat(files: List[UploadFile], session: Session = Depends(get_session)):
    with TemporaryDirectory() as tmpdir:
        # save files as temporary files
        # for file in files:
        return [file.filename for file in files]


@chat_router.get("/by_uuid/{uuid}")
def get_by_uuid():
    pass


@chat_router.get("/test_upload")
async def main():
    content = """
<body>
<form action="/chat/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
