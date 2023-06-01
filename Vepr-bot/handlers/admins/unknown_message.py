from aiogram import types
from config import dp


@dp.message_handler(state=None)
async def echo_message(message: types.Message):
    await message.answer(message.text)
