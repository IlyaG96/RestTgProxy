from typing import Dict

from pydantic import BaseModel


class TelegramMessage(BaseModel):
    action: str
    chat_id: str
    data: Dict | 'FirstMessageData'


class FirstMessageData(BaseModel):
    tg_nickmname: str
    tg_username: str
    mobile_phone: str
    chat_type: str
