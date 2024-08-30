from controller.bot.init import dp, bot
from aiogram import types
from controller.message_dto import MessageDTO
from controller.post.request import send_to_server
from controller.bot.filters import MyAbonChatFilter
from const import UNSUPPORTED_CONTENT_TEXT


# хендлер сообщения в личку бота
@dp.message(MyAbonChatFilter())
async def get_personal_message(message: types.Message):
    
    try:
        message_dto = await MessageDTO.parce_tg(message)
        await send_to_server(message_dto)
    except TypeError:
        await message.reply(UNSUPPORTED_CONTENT_TEXT)
