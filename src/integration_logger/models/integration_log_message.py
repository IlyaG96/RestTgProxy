from pydantic import BaseModel
from telethon import events
from ..models.telegram_message import TelegramMessage, FirstMessageData

from ..constants import ActionTypes


class IntegrationLogMessage(BaseModel):
    action: str = ""
    data: dict = dict()
    operation: str = 'create'
    schema: str = 'p2p'
    table: str = 'integrationlog'  #TODO from app_config


def create_first_message(incoming_data: events.NewMessage) -> IntegrationLogMessage:
    message: IntegrationLogMessage = IntegrationLogMessage()
    message.action = ActionTypes.first_action
    message.data = TelegramMessage(
        data=FirstMessageData(
            tg_nickmname=incoming_data.chat.username,
            tg_username=incoming_data.chat.first_name,
            mobile_phone=str(88888888888),
            chat_type="chat"
        ).model_dump(),
        action=ActionTypes.first_action,
        chat_id=str(incoming_data.chat_id)

    ).model_dump()
    return message
