from aiogram.filters import BaseFilter
from aiogram import types


# класс фильтрации личных сообщений
class MyAbonChatFilter(BaseFilter):

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == 'private'
