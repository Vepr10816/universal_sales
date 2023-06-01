import logging
from aiogram import Dispatcher
from config.roles import admins
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards


async def on_startup_notify(dp: Dispatcher):
    """
    Отправка сообщения о запуске бота администраторам.
    @param dp: объект бота.
    """
    for admin in admins:
        try:
            await api.auth(const.auth + '?tgID=' + str(admin)+'&idRole=1')
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text, reply_markup=keyboards.button_case_admin)
        except Exception as err:
            logging.exception(err)
