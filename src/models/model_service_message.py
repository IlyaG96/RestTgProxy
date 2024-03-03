from typing import Dict

from pydantic import BaseModel


class ModelServiceMessage(BaseModel):
    action: str
    chat_id: str
    data: Dict
    error: bool
    comment: str