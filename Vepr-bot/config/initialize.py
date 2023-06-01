from aiogram import Bot, Dispatcher, types

from .const import BOT_TOKEN

from aiogram_dialog import DialogRegistry

from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Инициализация токена бота, создание диспетчера.

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())

registry = DialogRegistry(dp)
