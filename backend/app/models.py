from sqlmodel import SQLModel, Field
import uuid as uuid
from typing import Optional


class ChatModel(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    public_id: uuid.UUID = Field(default_factory=uuid.uuid4)
