from aiogram import types
from aiogram.dispatcher import FSMContext

import core.api_requests
from config import dp, roles, keyboards
from models.financedata import FinanceData
from core.api_requests import ApiRequests as api
from config import const
from states.form import StateUsers


"""@dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    if message.from_user.id in roles.admins:
        await state.update_data({"Basket": []})
        await message.answer("Тут типо инструкция пользования ботом")
    else:
        await state.update_data({"Basket": []})
        await message.answer("Приветствую в нашем магазине, вот инструкция пользования нашем магазином.",
                             reply_markup=keyboards.button_case_users)
        await StateUsers.main_menu.set()"""
