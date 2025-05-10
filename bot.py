"""Телеграм бота на основе модуля aiogram"""
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from logic import kv_ur


load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    """Функция приветствия"""
    await message.answer(
        "Пришлите три числа a b c через пробел, например: 1 -5 6"
    )


@dp.message()
async def numbers(message: Message):
    """Разбираем ввод и отвечаем результатом kv_ur"""
    parts = message.text.split()
    if len(parts) != 3:
        return await message.answer("Нужно ровно три числа")

    try:
        a, b, c = map(float, parts)
    except ValueError:
        return await message.answer("Все три значения должны быть числами.")

    await message.answer("\n".join(map(str, kv_ur(a, b, c))))


async def main():
    """Функция запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
