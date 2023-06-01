import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_datepicker import Datepicker, DatepickerSettings

from config import dp, keyboards
from config import bot
from config import roles
from models.characteristics import Characteristics
from models.product import Product
from models.productcharacteristics import Productcharacteristics
from models.selectedproduct import Selectedproduct
from models.selectedproductcharacteristics import Selectedproductcharacteristics
from states.form import StateUsers
from states import form as st
from core.api_requests import ApiRequests as api
from config import const
from config import validate_data as valid


@dp.callback_query_handler(state=StateUsers.order_menu)
async def form_menu_order(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_basket, None) is None:
        message_from_user = ''
        order_list = [data["Order"][int(callback_query.data)]]
        for item in order_list:
            status = ''
            id_status = item["Order"]["orderStatusList"][0]["status"]["id"]
            if id_status == 1: status = "Ожидает оформления"
            if id_status == 2: status = f'Оформлен - ' \
                                f'{datetime.datetime.strptime(item["Order"]["orderStatusList"][0]["date_status"], "%Y-%m-%dT%H:%M:%S.%fZ")}'
            date_time_obj = datetime.datetime.strptime(item["Order"]["order_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
            message_from_user += f'*Номер заказа:* {item["Order"]["id"]}\n\n'
            message_from_user += f'*Дата:* {date_time_obj.date()} {date_time_obj.time().hour}:{date_time_obj.time().minute}\n\n'
            message_from_user += f'*Комментарий:* {item["Order"]["comment"]}\n\n'
            message_from_user += f'*Итоговая сумма*: {item["Order"]["total_price"]} руб.\n\n'
            message_from_user += f'Статус: *{status}*\n\n'
            message_from_user += f'Товары:\n'
            for item2 in item["Products"]:
                message_from_user += f'Наименование товара: *{item2["Product"]["product_name"]}*\n'
                message_from_user += f'Характеристики:\n'
                for item3 in item2["SelectedProductCharacteristics"]:
                    message_from_user += f'*{item3["productCharacteristics"]["characteristc_value"]}*\n'
                message_from_user += f'*Цена:* {item2["Product"]["product_price"]} руб. X {item2["Quantity"]} шт. = ' \
                                     f'{item2["Product"]["product_price"]  * item2["Quantity"]} руб\n\n'
        message_user = await callback_query.message.answer(message_from_user, parse_mode="Markdown",
                                            reply_markup=keyboards.generate_keyboard(["Отменить заказ", "Назад", "Отмена"]))
        await state.update_data({"id_order_menu": message_user.message_id})
        await state.update_data({"selected_order": order_list})
        await StateUsers.selected_order_menu.set()

@dp.callback_query_handler(state=StateUsers.selected_order_menu)
async def form_selected_menu_order(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback_query.data == "Назад":
        await bot.delete_message(callback_query.message.chat.id, data["id_order_menu"])
        await StateUsers.order_menu.set()
    if callback_query.data == "Отмена":
        await callback_query.message.answer("Выход из меню")
        await StateUsers.main_menu.set()
    if callback_query.data == "Отменить заказ":
        for item in data["selected_order"]:
            status = ''
            id_status = item["Order"]["orderStatusList"][0]["status"]["id"]
            id_order = item["Order"]["id"]
            if id_status != 1:
                await callback_query.message.answer("Уже невозможно отменить заказ")
                await StateUsers.main_menu.set()
                return
            await callback_query.message.answer(await api.delete(const.order+f'/{item["Order"]["id"]}',
                                                                 callback_query.from_user.id))
            await StateUsers.main_menu.set()







