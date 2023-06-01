from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton

import core.api_requests
from config import dp, keyboards, roles
from models.financedata import FinanceData
from core.api_requests import ApiRequests as api
from config import const
from config import bot
from states.form import StateUsers
import states.form as st


@dp.message_handler(commands=['Режим_Покупателя'])
async def command_switch_mode(message: types.Message, state: FSMContext):
    if not await st.check_role(message.from_user.id, message, state):
        return
    """keyboard = keyboards.button_case_users
    keyboard = keyboard.add(KeyboardButton('/Мои_Заказы'))"""
    await message.answer("Режим пользователя активирован",
                         reply_markup=keyboards.button_case_admin_switch_mode)
    roles.admins = [message.from_user.id * -1 if x == message.from_user.id else x for x in roles.admins]
    await state.update_data({"Basket": []})
    await StateUsers.main_menu.set()
