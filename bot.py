import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Загружаем токены из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация бота
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Ответ на /start
@dp.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer(
        f"<b>Привет. Я Люкс 2.0 — ИИ, помогающий видеть суть сквозь шум.</b>\n"
        f"Задай мне вопрос, и я постараюсь помочь тебе понять больше."
    )

# Ответ на обычные сообщения
@dp.message()
async def handle_message(message: Message):
    await message.answer("Я пока ещё не подключён к OpenAI, но я слушаю. Продолжай.")

# Запуск
if __name__ == "__main__":
    dp.run_polling(bot)
