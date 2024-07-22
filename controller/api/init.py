from fastapi import FastAPI
from const import CLIENT_PORT
import asyncio


# инициализация api
app = FastAPI()


# процесс запуска сервера
async def run_server():
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=CLIENT_PORT)
    server = uvicorn.Server(config)
    await server.serve()


# запуск сервера
def start_fastapi():
    loop = asyncio.get_event_loop()
    loop.create_task(run_server())
