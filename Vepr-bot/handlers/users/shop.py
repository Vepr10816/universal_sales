from aiogram import types
from config import dp
from config import bot
from models.addresses import Addresses
from models.requisites import Requisites
from states.form import StateMyCompany, StateUsers
from aiogram.dispatcher import FSMContext
from models.mycompany import Mycompany
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st


@dp.callback_query_handler(state=StateUsers.menu_shop)
async def form_select_action1(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_shop, data["id_company_menu"]) is None:
        if "Реквизиты" in callback_query.data:
            list_requisites = await api.get_list(const.requisites + f'/1', Requisites,
                                                callback_query.from_user.id)
            if isinstance(list_requisites, str):
                await callback_query.message.answer("Пока не заполнено)")
            else:
                message_from_user = 'Реквизиты:\n\n'
                for item in list_requisites:
                    message_from_user += f'*{item.requisites_name}*: {item.requisites_value}\n\n'
                await callback_query.message.answer(message_from_user, parse_mode="Markdown",
                                                    reply_markup=keyboards.generate_keyboard(["Назад", "Отмена"]))
        elif "Адреса" in callback_query.data:
            list_addresses = await api.get_list(const.addresses + f'/1',
                                                Addresses, callback_query.from_user.id)
            if isinstance(list_addresses, str):
                await callback_query.message.answer("Пока не заполнено)")
            else:
                message_from_user = 'Адреса:\n\n'
                for item in list_addresses:
                    message_from_user += f'{item.address_name}\n\n'
                await callback_query.message.answer(message_from_user, parse_mode="Markdown",
                                                    reply_markup=keyboards.generate_keyboard(["Назад", "Отмена"]))
