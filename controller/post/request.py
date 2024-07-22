import httpx
import json
from controller.message_dto import MessageDTO
from const import SERVER_PORT


# отправка сообщения на сервер
async def send_to_server(message: MessageDTO):
    await _send_post_request(
        f'http://127.0.0.1:{SERVER_PORT}/', 
        message.model_dump_json()
    )


# отправляет post-запросс по url с указаными данными 
async def _send_post_request(url: str, data: json):
    async with httpx.AsyncClient() as client:
        try:
            return await client.post(url, data=data)
        except Exception as e:
            return False
