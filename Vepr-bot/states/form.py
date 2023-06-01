import pathlib

from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, roles
from models.category import Category
from models.characteristics import Characteristics
from models.mycompany import Mycompany
from models.subcategory import Subcategory
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st
from aiogram_datepicker import DatepickerSettings, DatepickerCustomAction
from datetime import datetime, date
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InputFile
from aiogram.types import InlineKeyboardButton
from aiogram import types


async def update_data(data, state):
    await state.update_data(data)
    data = await state.get_data()
    return data


async def check_role(user_id, message, state):
    if user_id not in roles.admins:
        await message.answer("Введите команду /start для начала работы бота")
        await state.finish()
        return False
    else:
        return True


async def get_categories(message, state, form_state):
    data = await st.update_data({"Company": await api.get(const.company, Mycompany(), message.from_user.id)}, state)
    buttons_text = []
    if message.from_user.id in roles.admins:
        data = await st.update_data({"Category": await api.get_list(const.categories + f'/1', Category,
                                                                    message.from_user.id)}, state)
        if isinstance(data["Category"], str):
            await message.answer("Для начала необходимо заполнить Категории")
            await state.finish()
        else:
            for item in data["Category"]:
                buttons_text.append(f'{item.category_name}')
    if message.from_user.id not in roles.admins:
        data = await st.update_data({"Category": await api.get_list(f'/allCategoryFromUser/1', Category,
                                                                    message.from_user.id)}, state)
        if isinstance(data["Category"], str):
            await message.answer("Скоро открытие!\nЗаходите позже")
            await StateUsers.main_menu.set()
        else:
            for item in data["Category"]:
                buttons_text.append(f'{item.category_name}')
    await keyboards.generate_big_keyboard_without_help_buttons(data["Category"], bot, message,
                                                               form_state,
                                                               'Выберете категорию', buttons_text,
                                                               state, "id_category_menu")


async def get_subcategories(callback_query, state, form_state):
    data = await state.get_data()
    if callback_query.from_user.id in roles.admins:
        check = await keyboards.run_action(callback_query, state, bot, form_state, data["id_category_menu"])
    else:
        check = await keyboards.run_action_user(callback_query, state, bot, form_state, data["id_category_menu"])
    if check is None:
        data = await st.update_data({'Category': await api.get(const.category + f'/{callback_query.data}',
                                                               Category(), callback_query.from_user.id)}, state)
        list_subcategory = await api.get_list(const.subcategories + f'/{data["Category"].id}',
                                              Subcategory, callback_query.from_user.id)
        buttons_text = []
        if callback_query.from_user.id in roles.admins and isinstance(list_subcategory, str):
            await bot.send_message(callback_query.from_user.id, 'Для начала необходимо заполнить Подкатегории')
            await state.finish()
        elif not isinstance(list_subcategory, str):
            for item in list_subcategory:
                if callback_query.from_user.id in roles.admins:
                    buttons_text.append(f'{item.subcategory_name}')
                else:
                    list_subcategory_container = []
                    for item2 in list_subcategory:
                        list_subcategory_container.append(item2)
                    for item3 in list_subcategory_container:
                        if item3.productList != []:
                            buttons_text.append(f'{item3.subcategory_name}')
                        else:
                            list_subcategory.remove(item3)
                    break
            await keyboards.generate_big_keyboard_without_add(list_subcategory, bot, callback_query,
                                                              form_state.menu_all_subcategories,
                                                              f'Подкатегории "{data["Category"].category_name}"',
                                                              buttons_text,
                                                              state, "id_subcategory_menu")


async def get_product(product, callback_query, data, basket):
    if len(product.productPhotosList) != 0:
        photos = types.MediaGroup()
        for item in product.productPhotosList:
            if item["url_photo"] != ' ':
                photos.attach_photo(item["url_photo"])
            else:
                import app
                main_dir = str(pathlib.Path(app.dir_path).parents[0])
                photos.attach_photo(InputFile(str(pathlib.Path(
                    main_dir, 'images', 'products_photo', f'{item["photo_name"]}'))))
        await bot.send_media_group(callback_query.from_user.id, photos)
    characteristics_list = await api.get_list(const.characteristics + f'/{data["id_subcategory"]}',
                                              Characteristics, callback_query.from_user.id)
    message_characteristics = ""
    if len(product.productCharacteristicsList) != 0:
        characteristic_name_list = []
        for item in product.productCharacteristicsList:
            characteristic_name = ""
            if characteristics_list != 'У данной подкатегории нет характеристик':
                for item2 in characteristics_list:
                    if item2.id == item["characteristics"]["id"]:
                        characteristic_name = item2.characteristic_name
                        break
                if characteristic_name not in characteristic_name_list:
                    message_characteristics += f'\n\n*{characteristic_name}*:' \
                                               f' {item["characteristc_value"]}'
                    characteristic_name_list.append(characteristic_name)
                else:
                    message_characteristics += f' | | {item["characteristc_value"]}'

    if basket is not None:
        for item_basket in data["Basket"]:
            if item_basket["Selectedproductcharacteristics"] != [] and message_characteristics != "":
                message_characteristics += '\n\n*Выбранные значения*:\n'
                characteristic_name_list = []
                for item in product.productCharacteristicsList:
                    characteristic_name = ""
                    for item2 in characteristics_list:
                        if item2.id == item["characteristics"]["id"]:
                            characteristic_name = item2.characteristic_name
                            break
                    if characteristic_name not in characteristic_name_list:
                        for selected_product_characterictic in item_basket["Selectedproductcharacteristics"]:
                            if selected_product_characterictic.productcharacteristics == item['id']:
                                message_characteristics += f'\n*{characteristic_name}*:' \
                                                           f' {item["characteristc_value"]}\n'
    message_from_user = f'*{product.product_name}*\n'
    if product.description != ' ':
        message_from_user += f'{product.description}\n'
    if message_characteristics != "":
        message_from_user += f'{message_characteristics}\n\n'
    message_from_user += f'*Цена*: {product.product_price} {product.currency["currency_name"]}'
    return message_from_user


async def get_basket(data, state, msg):
    if data["Basket"] == []:
        await bot.send_message(msg.from_user.id, "Корзина пуста")
        return
    currency = data["Basket"][0]["Product"].currency["currency_name"]
    total_price = 0
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    for button in data["Basket"]:
        keyboard.add(InlineKeyboardButton(
            text=f'{button["Product"].product_name} - {button["Selectedproduct"].product_quantity} шт'
                 f' \n {button["Price"]} {currency}',
            callback_data=data["Basket"].index(button))
        )
        total_price += button["Price"]
    keyboard.add(InlineKeyboardButton(text="Детальный просмотр", callback_data="Детальный просмотр"))
    keyboard.add(InlineKeyboardButton(text="Очистить корзину", callback_data="Очистить корзину"))
    keyboard.add(InlineKeyboardButton(text="Оформить заказ", callback_data="Оформить заказ"))
    keyboard.add(InlineKeyboardButton(text="Отмена", callback_data="Отмена"))
    send_message = await bot.send_message(msg.from_user.id, f'Итоговая сумма: {total_price} {currency}'
                                                            f'\nСодержимое корзины:', reply_markup=keyboard)
    await state.update_data({"id_basket_menu": send_message.message_id})
    await StateUsers.basket_menu.set()


class StateMyCompany(StatesGroup):
    add_company_name = State()
    add_company_description = State()
    add_logo = State()
    add_requisite_name = State()
    add_requisite_value = State()
    add_address_name = State()

    edit_company_name = State()
    edit_company_description = State()
    edit_requisite_name = State()
    edit_requisite_value = State()
    edit_address_name = State()

    menu_company = State()
    menu_requisites = State()
    menu_requisite = State()
    menu_addresses = State()
    menu_address = State()


class StateCategory(StatesGroup):
    add_category_name = State()

    edit_category_name = State()

    menu_all_categories = State()
    menu_selected_category = State()


class StateSubcategory(StatesGroup):
    add_subcategory_name = State()

    edit_subcategory_name = State()

    menu_all_categories = State()
    menu_all_subcategories = State()
    menu_selected_subcategory = State()


class StateCharacteristics(StatesGroup):
    menu_all_categories = State()
    menu_all_subcategories = State()
    menu_all_characteristics = State()
    menu_selected_characterictic = State()
    menu_all_pre_values = State()
    menu_selected_pre_value = State()

    add_characteristic_name = State()
    add_characteristic_data_type = State()

    edit_characteristic_name = State()
    edit_characteristic_data_type = State()

    add_pre_value = State()
    edit_pre_value = State()

    add_selectable = State()
    edit_selectable = State()


class StateProduct(StatesGroup):
    menu_all_categories = State()
    menu_all_subcategories = State()
    menu_all_product = State()
    menu_selected_product = State()
    menu_all_photos_product = State()
    menu_selected_photo = State()

    add_product_name = State()
    add_product_description = State()
    add_product_price = State()
    add_product_currency = State()

    edit_product_name = State()
    edit_product_description = State()
    edit_product_price = State()
    edit_product_currency = State()

    add_product_photo = State()
    edit_product_photo = State()


class StateTest(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()


class StateProductCharacteristics(StatesGroup):
    get_characteristics = State()
    get_checkboxes = State()
    get_date = State()


class StateUsers(StatesGroup):
    main_menu = State()
    menu_all_categories = State()
    menu_all_subcategories = State()
    menu_all_product = State()
    menu_selected_product = State()
    menu_basket = State()
    menu_shop = State()

    add_basket = State()
    set_characteristics = State()
    add_quantity = State()

    basket_menu = State()
    detail_basket_menu = State()

    add_order = State()

    order_menu = State()

    selected_order_menu = State()


class StateOrder(StatesGroup):
    get_status_order = State()

    order_menu = State()

    selected_order_menu = State()

    finished_order = State()

    selected_finished_order_menu = State()
