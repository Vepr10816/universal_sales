from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import quote_html

from config import dp
from config import bot
from states.form import StateCategory
from aiogram.dispatcher import FSMContext
from models.category import Category
from models.mycompany import Mycompany
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st
from states.form import StateOrder
import datetime


@dp.message_handler(commands=['Заказы'])
async def command_order(message: types.Message, state: FSMContext, message_id=None):
    if not await st.check_role(message.from_user.id, message, state):
        return
    await message.answer("Выберете статсус заказов:",
                         reply_markup=keyboards.generate_keyboard([
                             "Неоформленные", "Оформленные", "Отмена"
                         ]))
    await StateOrder.get_status_order.set()


@dp.callback_query_handler(state=StateOrder.get_status_order)
async def form_order_status(callback_query: types.CallbackQuery, state: FSMContext):
    if await keyboards.run_action(callback_query, state, bot, StateOrder.get_status_order,
                                  None) is None:
        url = const.orders
        if callback_query.data == "Неоформленные":
            url += '/1'
            await StateOrder.order_menu.set()
        if callback_query.data == "Оформленные":
            url += '/2'
            await StateOrder.finished_order.set()
        api_answer = await api.get(url, None, callback_query.from_user.id)
        if isinstance(api_answer, str):
            await callback_query.message.answer(api_answer)
            await state.finish()
        else:
            for item in api_answer:
                status = ''
                id_status = item["Order"]["orderStatusList"][0]["status"]["id"]
                if id_status == 1: status = "Ожидает оформления"
                if id_status == 2: status = f'Оформлен - ' \
                                f'{datetime.datetime.strptime(item["Order"]["orderStatusList"][0]["date_status"], "%Y-%m-%dT%H:%M:%S.%fZ")}'
                await state.update_data({"Order": api_answer})
                date_time_obj = datetime.datetime.strptime(item["Order"]["order_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
                user_id = int(item["Order"]["user"]["tg_id"])
                chat_id = await bot.get_chat(user_id)
                user_name = quote_html(chat_id.username)
                await callback_query.message.answer(
                    f'Дата: {date_time_obj.date()} {date_time_obj.time().hour}:{date_time_obj.time().minute}'
                    f'\nСумма: {item["Order"]["total_price"]} руб.'
                    f'\nСтатус: <b>{status}</b>'
                    f'\nЗаказчик: '
                    f'<a href="tg://user?id={user_id}">@{user_name}</a>',
                    parse_mode="HTML",
                    reply_markup=keyboards.generate_keyboard_with_id(["Просмотр", "Отмена"], [api_answer.index(item)]))


@dp.callback_query_handler(state={StateOrder.order_menu, StateOrder.finished_order})
async def form_menu_order(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateOrder.get_status_order, None) is None:
        message_from_user = ''
        order_list = [data["Order"][int(callback_query.data)]]
        for item in order_list:
            status = ''
            id_status = item["Order"]["orderStatusList"][0]["status"]["id"]
            if id_status == 1: status = "Ожидает оформления"
            if id_status == 2: status = f'Оформлен - {item["Order"]["orderStatusList"][0]["date_status"]}'
            date_time_obj = datetime.datetime.strptime(item["Order"]["order_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
            message_from_user += f'<b>Номер заказа:</b> {item["Order"]["id"]}\n\n'
            message_from_user += f'<b>Дата:</b> {date_time_obj.date()} {date_time_obj.time().hour}:{date_time_obj.time().minute}\n\n'
            message_from_user += f'<b>Комментарий:</b> {item["Order"]["comment"]}\n\n'
            message_from_user += f'<b>Итоговая сумма</b>: {item["Order"]["total_price"]} руб.\n\n'
            message_from_user += f'Статус: <b>{status}</b>\n\n'
            message_from_user += f'Товары:\n'
            for item2 in item["Products"]:
                message_from_user += f'Наименование товара: <b>{item2["Product"]["product_name"]}</b>\n'
                message_from_user += f'Характеристики:\n'
                for item3 in item2["SelectedProductCharacteristics"]:
                    message_from_user += f'<b>{item3["productCharacteristics"]["characteristc_value"]}</b>\n'
                message_from_user += f'<b>Цена:</b> {item2["Product"]["product_price"]} руб. X {item2["Quantity"]} шт. = ' \
                                     f'{item2["Product"]["product_price"] * item2["Quantity"]} руб\n\n'
            user_id = int(item["Order"]["user"]["tg_id"])
            chat_id = await bot.get_chat(user_id)
            user_name = quote_html(chat_id.username)
            message_from_user += f'Заказчик: <a href="tg://user?id={user_id}">@{user_name}</a>'
        if await state.get_state() != 'StateOrder:finished_order':
            keyboard = keyboards.generate_keyboard(["Оформить заказ", "Отменить заказ", "Назад", "Отмена"])
            await StateOrder.selected_order_menu.set()
        else:
            keyboard = keyboards.generate_keyboard(["Назад"])
            await StateOrder.selected_finished_order_menu.set()
        message_user = await callback_query.message.answer(message_from_user, parse_mode="HTML",
                                                           reply_markup=keyboard)
        await state.update_data({"id_order_menu": message_user.message_id})
        await state.update_data({"selected_order": order_list})


@dp.callback_query_handler(state={StateOrder.selected_order_menu, StateOrder.selected_finished_order_menu})
async def form_selected_menu_order(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback_query.data == "Назад":
        await bot.delete_message(callback_query.message.chat.id, data["id_order_menu"])
        if await state.get_state() != 'StateOrder:selected_finished_order_menu':
            await StateOrder.order_menu.set()
        else:
            await StateOrder.finished_order.set()
    if callback_query.data == "Отмена":
        await callback_query.message.answer("Выход из меню")
        await state.finish()
    if callback_query.data == "Отменить заказ":
        for item in data["selected_order"]:
            await callback_query.message.answer(await api.delete(const.order+f'/{item["Order"]["id"]}',
                                                                 callback_query.from_user.id))
            user_id = int(item["Order"]["user"]["tg_id"])
            chat_id = await bot.get_chat(user_id)
            await bot.send_message(chat_id=chat_id.id,
                                   text=f'Ваш заказ №{item["Order"]["id"]}\n *был отменен продавцом*',
                                   parse_mode="Markdown",)
            await state.finish()
    if callback_query.data == "Оформить заказ":
        for item in data["selected_order"]:
            await callback_query.message.answer(await api.post(const.status+f'/{item["Order"]["id"]}',None,
                                                               callback_query.from_user.id))
            user_id = int(item["Order"]["user"]["tg_id"])
            chat_id = await bot.get_chat(user_id)
            await bot.send_message(chat_id=chat_id.id,
                                   text=f'Ваш заказ №{item["Order"]["id"]}\n *был оформлен продавцом*',
                                   parse_mode="Markdown")
            await state.finish()

