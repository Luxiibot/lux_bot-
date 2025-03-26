import os
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

# Загружаем токен из .env файла
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота с использованием DefaultBotProperties
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(bot)

# Командный обработчик для /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой бот.")

# Командный обработчик для /help
@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    await message.answer("Напиши /start чтобы начать.")

# Стартуем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
