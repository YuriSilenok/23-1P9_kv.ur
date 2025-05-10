"""Модули для работы с aiogram"""
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from logic import kv_ur

TOKEN = ""


async def start(message: Message):
    """Функция приветствия"""
    await message.answer(
        "Пришлите три числа a b c через пробел, например: 1 -5 6")


async def numbers(message: Message):
    """Функция работы самой функции"""
    parts = message.text.replace(",", " ").split()
    if len(parts) != 3:
        return await message.answer("Нужно ровно три числа")
    try:
        a, b, c = map(float, parts)
    except ValueError:
        return await message.answer("Все три значения должны быть числами.")
    await message.answer("\n".join(map(str, kv_ur(a, b, c))))

# ─── инициализация ───
bot = Bot(TOKEN)
dp = Dispatcher()
dp.message(CommandStart())(start)
dp.message()(numbers)


async def main():
    """Функция старта бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
