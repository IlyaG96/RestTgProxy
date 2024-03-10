from abc import ABC, abstractmethod
from typing import Any
from telethon import TelegramClient
from telegram_bot.application import ConcreteTelegramBot


class TelegramServiceInterface(ABC):
    @abstractmethod
    def send(self, message: Any):
        """Отправляет сообщение тому человеку, с которым открыт диалог"""
        raise NotImplementedError

    @abstractmethod
    def send_multiple_messages(self):
        """Метод для спам-рассылок"""
        raise NotImplementedError


class ConcreteTelegramService(TelegramServiceInterface, ABC):

    def __init__(self, bot: ConcreteTelegramBot):
        self._service = bot

    async def send(self, message: Any):
        return await self.__send(message)

    def send_multiple_messages(self):
        pass

    def _get_bot(self):
        return self._service.bot

    async def __send(self, message: Any):
        bot: TelegramClient = self._get_bot()
        if not self.__validate_message(message):
            raise BaseException
        async with bot:
            entity = await bot.get_entity("")  #todo fixme
        await bot.send_message(
            entity=entity.id,
            message=str(message)
        )

    def __validate_message(self, message: Any):
        return True

    def __parse_message(self):
        pass


