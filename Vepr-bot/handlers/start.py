from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto
from aiogram_datepicker import Datepicker, DatepickerSettings

from config import dp, keyboards
from config import bot
from config import roles
from states.form import StateUsers
from core.api_requests import ApiRequests as api
from config import const
from aiogram.utils.markdown import quote_html


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    if message.from_user.id in roles.admins:
        await api.auth(const.auth + '?tgID=' + str(message.from_user.id) + '&idRole=1')
        await state.update_data({"Basket": []})
        await message.answer("Бот запущен")
    else:
        await state.update_data({"Basket": []})
        await message.answer("Приветствую в нашем магазине, Инструкия по команде /help.",
                             reply_markup=keyboards.button_case_users)
        await api.auth(const.auth + '?tgID=' + f'{message.from_user.id}' + '&idRole=2')
        await StateUsers.main_menu.set()

