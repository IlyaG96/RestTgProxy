from pydantic import BaseModel


class IntegrationLogMessage(BaseModel):
    action: str = ""
    data: dict = dict()
    operation: str = 'create'
    schema: str = 'p2p'
    table: str = 'integrationlog'


def create_message(incoming_data: dict) -> IntegrationLogMessage:
    message: IntegrationLogMessage = IntegrationLogMessage()
    message.action = incoming_data['action']
    message.data = incoming_data
    return message
