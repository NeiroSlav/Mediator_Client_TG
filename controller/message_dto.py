from pydantic import BaseModel
from aiogram import types


# универсальный объект передачи сообщений
class MessageDTO(BaseModel):
    social: str
    chat_id: int
    sender_name: str
    text: str | None
    image: str | None
    meta: dict

    @classmethod  # фабричный метод, создающий объект из сообщения телеграмма
    def parce_tg(cls, message: types.Message):
        chat_id = message.chat.id
        if message.message_thread_id:
            chat_id = message.message_thread_id

        text = ''
        image = None
        meta = {}

        if message.photo:  # если есть фото, берёт его id и подпись
            image = message.photo[-1].file_id
            text = message.caption

        elif message.text:  # или если есть просто текст, берёт его 
            text = message.text

        elif message.animation:  # или если есть анимация, берёт id
            meta['animation'] = message.animation.file_id

        elif message.sticker:  # или если есть стикер, берёт id
            meta['sticker'] = message.sticker.file_id
            
        return cls(
            social = 'tg',
            chat_id = chat_id,
            sender_name = message.from_user.full_name,
            text = text,
            image = image,
            meta = meta,
        )
