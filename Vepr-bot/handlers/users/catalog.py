import datetime
import pathlib

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram_datepicker import Datepicker, DatepickerSettings

import app
from config import dp, keyboards
from config import bot
from config import roles
from models.characteristics import Characteristics
from models.currency import Currency
from models.mycompany import Mycompany
from models.product import Product
from models.productcharacteristics import Productcharacteristics
from models.selectedproduct import Selectedproduct
from models.selectedproductcharacteristics import Selectedproductcharacteristics
from states.form import StateUsers
from states import form as st
from core.api_requests import ApiRequests as api
from config import const
from config import validate_data as valid
from app import dir_path


@dp.message_handler(state=StateUsers.main_menu)
async def form_main_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == "/start":
        await state.update_data({"Basket": []})
        await message.answer("Приветствую в нашем магазине, вот инструкция пользования нашем магазином.",
                             reply_markup=keyboards.button_case_users)
        await api.auth(const.auth + '?tgID=' + f'{message.from_user.id}' + '&idRole=2')
    if message.text == "/Каталог":
        await st.get_categories(message, state, StateUsers.menu_all_categories)
    if message.text == "/keyboard":
        await message.answer('Клавиатура возвращена', reply_markup=keyboards.button_case_users)
    if message.text == "/help":
        message_from_user = 'Активирование бота со стороны клиента осуществляется при отправке команды «/start».' \
                            'При нажатии на одну из кнопок клавиатура происходит переход бота в машинное состояние, ' \
                            'ожидающее определенное' \
                            'действие от пользователя. Необходимо следовать указаниям бота, иначе он просто не будет ' \
                            'отвечать на' \
                            'непредусмотренные действия.'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'bot_states.png'))),
                             caption=message_from_user)
        message_from_user = 'Для простого понимания, машинное состояние представляет из себя меню, где кнопки' \
                            'отвечают за переход в следующее меню. Кнопка «Отмена» является выходом из меню (' \
                            'машинного состояния),' \
                            'а кнопка «Назад» является переходом в прошлое меню.'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'bot_states_buttons.png'))),
                             caption=message_from_user)
        message_from_user = '«/Магазин» - вывод подробной информации о магазине\n' \
                            '«/Каталог» - просмотр каталога, заполненный продавцом, добавление товара в корзину' \
                            'соответствующей кнопкой. \n«/Корзина» - просмотр корзины, изменение количества товара и ' \
                            'удаление товаров из' \
                            'корзины, формирование заказа. \nИзменение количества товара осуществляется по кнопкам ' \
                            '«+» и «-».\n'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'edit_basket.png'))),
                             caption=message_from_user)
        message_from_user = '«Мои_Заказы» - просмотр сформированных заказов и их статусов. Заказ также можно' \
                            'отменить по соответствующей кнопке, но удалить можно только тот заказ, который не ' \
                            'оформлен продавцом.'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'order.png'))),
                             caption=message_from_user)
    if message.from_user.id * -1 in roles.admins and message.text == "/Режим_Администратора":
        roles.admins = [message.from_user.id if x == message.from_user.id * -1 else x for x in roles.admins]
        await message.answer(text="Режим администратора активирован", reply_markup=keyboards.button_case_admin)
        await state.finish()
    if message.text == "/Корзина":
        await st.get_basket(data, state, message)
    if message.text == "/Мои_Заказы":
        order = await api.get(const.order, None, message.from_user.id)
        if isinstance(order, str):
            await message.answer(order)
            return
        for item in order:
            status = ''
            id_status = item["Order"]["orderStatusList"][0]["status"]["id"]
            if id_status == 1: status = "Ожидает оформления"
            if id_status == 2: status = f'Оформлен - ' \
                                        f'{datetime.datetime.strptime(item["Order"]["orderStatusList"][0]["date_status"], "%Y-%m-%dT%H:%M:%S.%fZ")}'
            await state.update_data({"Order": order})
            date_time_obj = datetime.datetime.strptime(item["Order"]["order_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
            await message.answer(
                f'Дата: {date_time_obj.date()} {date_time_obj.time().hour}:{date_time_obj.time().minute}'
                f'\nСумма: {item["Order"]["total_price"]} руб.'
                f'\nСтатус: *{status}*',
                parse_mode="Markdown",
                reply_markup=keyboards.generate_keyboard_with_id(["Просмотр", "Отмена"], [order.index(item)]))
            await StateUsers.order_menu.set()
    if message.text == "/Магазин":
        data = await st.update_data({"Company": await api.get(const.company, Mycompany(), message.from_user.id)}, state)
        await StateUsers.menu_shop.set()
        if isinstance(data["Company"], str):
            await message.answer("Скоро открытие, увидимся позже)")
            message_id = message
            await StateUsers.main_menu.set()
        elif data["Company"].url_logo == ' ' and data["Company"].logo_name == ' ':
            message_id = await message.answer(f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                              parse_mode="Markdown",
                                              reply_markup=keyboards.generate_keyboard(
                                                  ["Реквизиты", "Адреса", "Отмена"]))
        else:
            if data["Company"].url_logo != ' ':
                message_id = await bot.send_photo(message.chat.id, data["Company"].url_logo,
                                                  f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                                  parse_mode="Markdown",
                                                  reply_markup=keyboards.generate_keyboard(
                                                      ["Реквизиты", "Адреса", "Отмена"]))
            elif data["Company"].logo_name != ' ':
                main_dir = str(pathlib.Path(app.dir_path).parents[0])
                message_id = await bot.send_photo(message.chat.id, InputFile(str(pathlib.Path(
                                                  main_dir, 'images', 'logo', data["Company"].logo_name))),
                                                  f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                                  parse_mode="Markdown",
                                                  reply_markup=keyboards.generate_keyboard(
                                                      ["Реквизиты", "Адреса", "Отмена"]))
        await state.update_data({"id_company_menu": message_id["message_id"]})


@dp.callback_query_handler(state=StateUsers.menu_all_categories)
async def form_menu_categories(callback_query: types.CallbackQuery, state: FSMContext):
    await st.get_subcategories(callback_query, state, StateUsers)


@dp.callback_query_handler(state=StateUsers.menu_all_subcategories)
async def form_menu_subcategories(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_all_categories,
                                       data["id_category_menu"]) is None:
        await state.update_data({"id_subcategory": callback_query.data})
        list_product = await api.get_list(const.products + f'/{callback_query.data}',
                                          Product, callback_query.from_user.id)
        buttons_text = []
        if not isinstance(list_product, str):
            for item in list_product:
                buttons_text.append(f'{item.product_name} - {item.product_price} {item.currency["currency_name"]}')
        await keyboards.generate_big_keyboard_from_user(list_product, bot, callback_query,
                                                        StateUsers.menu_all_product,
                                                        f'Товары',
                                                        buttons_text,
                                                        state, "id_product_menu")


@dp.callback_query_handler(state=StateUsers.menu_all_product)
async def form_menu_product(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_all_subcategories,
                                       data["id_subcategory_menu"]) is None:
        if callback_query.data == "Просмотр всего каталога":
            list_product = await api.get_list(const.products + f'/{data["id_subcategory"]}',
                                              Product, callback_query.from_user.id)
            for product in list_product:
                message_from_user = await st.get_product(product, callback_query, data, None)
                await callback_query.message.answer(message_from_user,
                                                    parse_mode="Markdown",
                                                    reply_markup=keyboards.generate_keyboard_from_user(product.id))
        else:
            try:
                product = await api.get(const.product + f'/{callback_query.data}', Product(), callback_query.from_user.id)
                message_from_user = await st.get_product(product, callback_query, data, None)
                keyboard = InlineKeyboardMarkup()
                keyboard.row_width = 1
                await callback_query.message.answer(message_from_user,
                                                    parse_mode="Markdown",
                                                    reply_markup=keyboards.generate_keyboard_from_user(product.id))
            except Exception as err:
                await callback_query.message.answer("Ошибка. повторите попытку")
                print(err)
                StateUsers.main_menu.set()
                return
        await StateUsers.menu_selected_product.set()


@dp.callback_query_handler(state=StateUsers.menu_selected_product)
async def form_selected_product(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_all_product,
                                       data["id_product_menu"]) is None:
        data = await st.update_data(
            {'Product': await api.get(const.product + f'/{callback_query.data}',
                                      Product(), callback_query.from_user.id)}, state)
        selectable_characteristics_list = await api.get_list(
            const.selectable_characteristics + f'?idSubcategory={int(data["id_subcategory"])}&idProduct={int(callback_query.data)}',
            Productcharacteristics, callback_query.from_user.id)
        await state.update_data({"selectable_characterisrics": []})
        if isinstance(selectable_characteristics_list, str) == False:
            selectable_characterisrics = [{"null": None}]
            button_text = []
            button_data = []
            for i in range(len(selectable_characteristics_list)):
                item = selectable_characteristics_list[i]
                button_text.append(item.characteristc_value)
                button_data.append(item.id)
                if item == selectable_characteristics_list[-1]:
                    button_text.append("Отмена")
                if item == selectable_characteristics_list[-1] or \
                        item.characteristics["id"] != selectable_characteristics_list[i + 1].characteristics["id"]:
                    message_text = f'Выберете {item.characteristics["characteristic_name"]:}'
                    selectable_characterisrics.append(
                        {
                            "message_text": message_text,
                            "button_text": button_text,
                            "button_data": button_data,
                        }
                    )
                    button_text = []
                    button_data = []
            selectable_characterisrics.pop(0)
            data = await st.update_data({"selectable_characterisrics": selectable_characterisrics}, state)
        await state.update_data(data)

        await callback_query.message.answer("Введите желаемое колличество:")
        await StateUsers.add_quantity.set()


@dp.message_handler(state=StateUsers.add_quantity)
async def form_get_product_quantity(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if await valid.check_int(message, StateUsers.add_quantity, message.text) is not None:
        sl = Selectedproduct()
        sl.product = data["Product"].id
        sl.product_quantity = int(message.text)
        data["Basket"].append(
            {
                "Product": data["Product"],
                "Selectedproduct": sl,
                "Price": data["Product"].product_price * int(message.text),
                "Selectedproductcharacteristics": []
            }
        )
        await state.update_data(data)
        if data["selectable_characterisrics"] == []:
            # data["Basket"][-1]["Selectedproductcharacteristics"].append(None)
            await message.answer("Успешное добавление товара в корзину")
            await StateUsers.main_menu.set()
            print(data["Basket"])
        else:
            await form_add_basket(state, message)


async def form_add_basket(state: FSMContext, msg):
    data = await state.get_data()
    if len(data["selectable_characterisrics"]) == 0:
        await bot.send_message(msg.from_user.id, "Успешное добавление товара в корзину")
        await StateUsers.main_menu.set()
        print(data["Basket"])
        return
    for item in data["selectable_characterisrics"]:
        await bot.send_message(msg.from_user.id, item["message_text"],
                               reply_markup=keyboards.generate_keyboard_with_id(
                                   item["button_text"],
                                   item["button_data"]))
        data["selectable_characterisrics"].remove(item)
        await StateUsers.set_characteristics.set()
        break
    await state.update_data(data)


@dp.callback_query_handler(state=StateUsers.set_characteristics)
async def form_set_characteristics(callback_query: types.CallbackQuery, state: FSMContext):
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.main_menu,
                                       None) is None:
        data = await state.get_data()
        spc = Selectedproductcharacteristics()
        spc.productcharacteristics = int(callback_query.data)
        data["Basket"][-1]["Selectedproductcharacteristics"].append(spc)
        await state.update_data(data)
        await form_add_basket(state, callback_query)
