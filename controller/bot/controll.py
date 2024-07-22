from controller.bot.init import bot
from controller.message_dto import MessageDTO


# отправка сообщения ботом
async def send_personal_message(message_dto: MessageDTO):

    if message_dto.image:  # если есть изображение из тг
        await bot.send_photo(
            chat_id=message_dto.chat_id, 
            caption=message_dto.text,
            photo=message_dto.image,
        )
    elif message_dto.text:  # если есть текст
        await bot.send_message(
            chat_id=message_dto.chat_id, 
            text=message_dto.text,
        )
    elif message_dto.meta.get('animation'):  # если есть гифка
        await bot.send_animation(
            chat_id=message_dto.chat_id,
            animation=message_dto.meta['animation']
        )
    elif message_dto.meta.get('sticker'):  # если есть стикер
        await bot.send_sticker(
            chat_id=message_dto.chat_id,
            sticker=message_dto.meta['sticker']
        )
