import os
import pathlib

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_command
from aiogram import executor
from handlers import dp

dir_path = pathlib.Path.cwd()


async def on_startup(dp):
    """
        Запуск бота и постановка его конфигураций.
        @param dp: диспетчер созданный в файле initialize.py
    """
    await on_startup_notify(dp)
    await set_default_command(dp)
    print('Бот запущен')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
