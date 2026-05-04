import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Бип! Привет, юнга! Я — Termix, кибер-пиратский кот!\n"
        "Готов учиться программированию?\n\n"
        "/courses — посмотреть курсы\n"
        "/subscribe — подписка\n"
        "/termix — спросить меня"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())