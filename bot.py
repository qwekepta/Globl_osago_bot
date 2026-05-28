import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден в переменных окружения")

ADMIN_IDS = [1259255945]

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Связаться с агентом")],
        [KeyboardButton(text="❓ Частые вопросы")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("🚗 Добро пожаловать! Бот работает.", reply_markup=main_kb)

@dp.message(F.text == "📞 Связаться с агентом")
async def contact(message: types.Message):
    await message.answer("Свяжем вас с агентом. Напишите свой номер телефона.")

@dp.message(F.text == "❓ Частые вопросы")
async def faq(message: types.Message):
    await message.answer("Здесь будут ответы на частые вопросы.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())