import asyncio
from controller import start_bot
from controller import start_fastapi


async def main():
    start_fastapi()
    await start_bot()


if __name__ == "__main__":
    asyncio.run(main())
