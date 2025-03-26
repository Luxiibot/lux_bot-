import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "<b>Привет. Я Люкс 2.0 — ИИ, помогающий видеть суть сквозь шум.</b>\n"
        "Задай мне вопрос, и я постараюсь помочь тебе понять больше."
    )

@dp.message()
async def handle_message(message: Message):
    await message.answer("Я пока ещё не подключён к OpenAI, но я слушаю. Продолжай.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
