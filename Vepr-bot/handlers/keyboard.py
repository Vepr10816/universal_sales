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


@dp.message_handler(commands=['keyboard'])
async def command_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if "Basket" not in data:
        await state.update_data({"Basket": []})
    if message.from_user.id in roles.admins:
        await message.answer("Клавиатура возвращена", reply_markup=keyboards.button_case_admin)
    else:
        await message.answer("Клавиатура возвращена",
                             reply_markup=keyboards.button_case_users)
        await api.auth(const.auth + '?tgID=' + f'{message.from_user.id}' + '&idRole=2')
        await StateUsers.main_menu.set()
