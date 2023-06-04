import pathlib

from aiogram import types
from aiogram.types import InputMediaPhoto
from aiogram_datepicker import Datepicker, DatepickerSettings

import app
from config import dp
from config import bot
from models.characteristics import Characteristics
from models.productcharacteristics import Productcharacteristics
from states.form import StateProduct, StateProductCharacteristics
from aiogram.dispatcher import FSMContext
from models.subcategory import Subcategory
from models.product import Product
from models.productphotos import Productphotos
from models.currency import Currency
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st
from config import validate_data as valid


@dp.message_handler(commands=['Товары'])
async def command_category(message: types.Message, state: FSMContext):
    if not await st.check_role(message.from_user.id, message, state):
        return
    await st.get_categories(message, state, StateProduct.menu_all_categories)


@dp.callback_query_handler(state=StateProduct.menu_all_categories)
async def form_menu_all_categories(callback_query: types.CallbackQuery, state: FSMContext):
    await st.get_subcategories(callback_query, state, StateProduct)


@dp.callback_query_handler(state=StateProduct.menu_all_subcategories)
async def form_menu_all_subcategories(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action(callback_query, state, bot, StateProduct.menu_all_categories,
                                  data["id_category_menu"]) is None:
        data = await st.update_data({'Subcategory': await api.get(const.subcategory + f'/{callback_query.data}',
                                                                  Subcategory(), callback_query.from_user.id)}, state)
        list_product = await api.get_list(const.products + f'/{data["Subcategory"].id}',
                                          Product, callback_query.from_user.id)
        buttons_text = []
        if not isinstance(list_product, str):
            for item in list_product:
                buttons_text.append(f'{item.product_name} - {item.product_price} {item.currency["currency_name"]}')
        await keyboards.generate_big_keyboard(list_product, bot, callback_query,
                                              StateProduct.menu_all_product,
                                              f'Товары',
                                              buttons_text,
                                              state, "id_product_menu")


@dp.callback_query_handler(state=StateProduct.menu_all_product)
async def form_menu_all_product(callback_query: types.CallbackQuery, state: FSMContext):
    data = await st.update_data({"call_selected_product": callback_query}, state)
    data = await st.update_data({"id_subcategory": data["Subcategory"].id}, state)
    if await keyboards.run_action(callback_query, state, bot, StateProduct.menu_all_subcategories,
                                  data["id_subcategory_menu"]) is None:
        if "Добавить" in callback_query.data:
            await state.update_data({"Product": Product()})
            await bot.send_message(callback_query.from_user.id, 'Введите наименование товара')
            await StateProduct.add_product_name.set()
        else:
            data = await st.update_data(
                {'Product': await api.get(const.product + f'/{callback_query.data}',
                                          Product(), callback_query.from_user.id)}, state)
            message_from_user = await st.get_product(data["Product"], callback_query, data, None)
            message_id = await callback_query.message.answer(message_from_user,
                                                             parse_mode="Markdown",
                                                             reply_markup=keyboards.generate_keyboard(
                                                                 ["Фотографии", "Редактировать", "Удалить",
                                                                  "Назад", "Отмена"]))
            await state.update_data({"id_selected_product": message_id["message_id"]})
            await StateProduct.menu_selected_product.set()


@dp.callback_query_handler(state=StateProduct.menu_selected_product)
async def form_selected_product(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateProduct.menu_all_product,
                                  data["id_product_menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   'Введите новое наименование товрав (Знак "-" если не хотите менять значение)')
            await StateProduct.edit_product_name.set()
        if "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.product + f'/{data["Product"].id}',
                                                    callback_query.from_user.id))
            await form_menu_all_subcategories(data["call"], state)
        if "Фотографии" in callback_query.data:
            data = await st.update_data({"call_product_photos": callback_query}, state)
            list_photos = await api.get_list(const.photos + f'/{data["Product"].id}',
                                             Productphotos, callback_query.from_user.id)
            photos = types.MediaGroup()
            if not isinstance(list_photos, str):
                for item in list_photos:
                    photos.attach_photo(item.url_photo)
                await bot.send_media_group(callback_query.from_user.id, photos)
                await state.update_data({"photos_count": len(list_photos)})
                buttons = ["Добавить", "Редактировать", "Удалить все фото", "Назад", "Отмена"]
                if len(list_photos) == 10:
                    buttons.pop(0)
                message_id = await bot.send_message(callback_query.from_user.id, "Выберете действие",
                                                    reply_markup=keyboards.generate_keyboard(buttons))
                await state.update_data({"id_product_photos": message_id["message_id"]})
            elif isinstance(list_photos, str):
                await state.update_data({"photos_count": 0})
                await bot.send_message(callback_query.from_user.id, list_photos,
                                       reply_markup=keyboards.generate_keyboard(["Добавить"]))
            await StateProduct.menu_all_photos_product.set()


@dp.callback_query_handler(state=StateProduct.menu_all_photos_product)
async def form_menu_all_photos(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateProduct.menu_selected_product,
                                  data["id_selected_product"]) is None:
        if "Добавить" in callback_query.data:
            if data["photos_count"] == 10:
                await bot.send_message(callback_query.from_user.id, "Максимальное кол-во фотографий 10 шт.")
                await form_selected_product(data["call_product_photos"], state)
            else:
                await state.update_data({"Productphotos": Productphotos()})
                await bot.send_message(callback_query.from_user.id, f'Отправьте фото товара '
                                                                    f'{data["Product"].product_name}')
                await StateProduct.add_product_photo.set()
        if "Удалить все фото" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.photos + f'/{data["Product"].id}',
                                                    callback_query.from_user.id))
            await form_menu_all_product(data["call_selected_product"], state)
        if "Редактировать" in callback_query.data:
            for item in data["Product"].productPhotosList:
                await bot.send_photo(callback_query.from_user.id, item["url_photo"],
                                     reply_markup=keyboards.generate_keyboard_with_id(
                                         ["Редактировать", "Удалить", "Назад", "Отмена"],
                                         [f'R{item["id"]}', f'D{item["id"]}', ' ', ' ']))
                await StateProduct.menu_selected_photo.set()


@dp.callback_query_handler(state=StateProduct.menu_selected_photo)
async def form_menu_selected_photo(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateProduct.menu_all_photos_product,
                                  data["id_product_photos"]) is None:
        if "R" in callback_query.data:
            photo = Productphotos()
            photo.id = int(callback_query.data.replace("R", ""))
            await state.update_data({"Productphotos": photo})
            await bot.send_message(callback_query.from_user.id, "Отправьте новую фотографию")
            await StateProduct.edit_product_photo.set()
        if "D" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.photo + f'/{callback_query.data.replace("D", "")}',
                                                    callback_query.from_user.id))
            await form_selected_product(data["call_product_photos"], state)


@dp.message_handler(content_types=['photo'], state={StateProduct.add_product_photo, StateProduct.edit_product_photo})
async def load_img(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Productphotos"].url_photo = message.photo[0].file_id
    data["Productphotos"].product = data["Product"].id
    await state.update_data(data)
    main_dir = str(pathlib.Path(app.dir_path).parents[0])
    if len(main_dir) > 3:
        valid.check_folders(main_dir)
        await message.photo[-1].download(
            destination_file=str(pathlib.Path(main_dir, 'Vepr-site', 'Vepr-site', 'wwwroot','images', f'{message.photo[-1].file_id}.jpg')))
        data["Productphotos"].photo_name = f'{message.photo[-1].file_id}.jpg'
    if await state.get_state() == 'StateProduct:add_product_photo':
        await message.answer(await api.post(const.photo, data["Productphotos"], message.from_user.id))
        data = await st.update_data(
            {'Product': await api.get(const.product + f'/{data["Product"].id}',
                                      Product(), message.from_user.id)}, state)
        await form_selected_product(data["call_product_photos"], state)
    elif await state.get_state() == 'StateProduct:edit_product_photo':
        await message.answer(await api.put(const.photo + f'/{data["Productphotos"].id}',
                                           data["Productphotos"], message.from_user.id))
        data = await st.update_data(
            {'Product': await api.get(const.product + f'/{data["Product"].id}',
                                      Product(), message.from_user.id)}, state)
        await form_selected_product(data["call_product_photos"], state)


@dp.message_handler(state={StateProduct.add_product_name, StateProduct.edit_product_name})
async def form_get_product_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    a = await state.get_state()
    if await state.get_state() == 'StateProduct:edit_product_name' and message.text != '-':
        data["Product"].product_name = message.text
        await StateProduct.edit_product_description.set()
    elif await state.get_state() == 'StateProduct:add_product_name':
        data["Product"].product_name = message.text
        await StateProduct.add_product_description.set()
    elif await state.get_state() == 'StateProduct:edit_product_name':
        await StateProduct.edit_product_description.set()
    data["Product"].subcategory = data["Subcategory"].id
    await state.update_data(data)
    await message.answer('Введите описание товара (Знак "-" если описание не нужно)):')


@dp.message_handler(state={StateProduct.add_product_description, StateProduct.edit_product_description})
async def form_get_product_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if await state.get_state() == 'StateProduct:edit_product_description' and message.text != "-":
        data["Product"].description = message.text
        await StateProduct.edit_product_price.set()
        await message.answer('Введите цену товара (Знак "-" если не хотите менять значение):')
    elif await state.get_state() == 'StateProduct:add_product_description' and message.text != "-":
        data["Product"].description = message.text
        await StateProduct.add_product_price.set()
        await message.answer("Введите цену товара:")
    elif await state.get_state() == 'StateProduct:add_product_description' and message.text == "-":
        await StateProduct.add_product_price.set()
        await message.answer("Введите цену товара:")
    elif await state.get_state() == 'StateProduct:edit_product_description' and message.text == "-":
        await StateProduct.edit_product_price.set()
        await message.answer('Введите цену товара (Знак "-" если не хотите менять значение):')
    await state.update_data(data)


@dp.message_handler(state={StateProduct.add_product_price, StateProduct.edit_product_price})
async def form_get_product_price(message: types.Message, state: FSMContext):
    data = await state.get_data()
    buttons_text = []
    if await state.get_state() == 'StateProduct:edit_product_price' and message.text != "-":
        data["Product"].product_price = await valid.check_double(message, StateProduct.edit_product_price, message.text)
    elif await state.get_state() == 'StateProduct:add_product_price':
        data["Product"].product_price = await valid.check_double(message, StateProduct.add_product_price, message.text)
    if data["Product"].product_price is not None:
        await state.update_data(data)
        list_currency = await api.get_list(const.currencies, Currency, message.from_user.id)
        if not isinstance(list_currency, str):
            for item in list_currency:
                buttons_text.append(f'{item.currency_name}')
            if await state.get_state() == 'StateProduct:edit_product_price':
                form_state = StateProduct.edit_product_currency
                buttons_text.append("Не изменять")
            else:
                form_state = StateProduct.add_product_currency
            await keyboards.generate_big_keyboard_without_help_buttons(list_currency, bot, message,
                                                                       form_state,
                                                                       f'Выберете валюту',
                                                                       buttons_text,
                                                                       state, "id_currency")
        else:
            await message.answer("В БД нет валют")
            await state.finish()


@dp.callback_query_handler(state={StateProduct.add_product_currency,
                                  StateProduct.edit_product_currency})
async def form_get_product_currency(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not ("Отмена" in callback_query.data) and not ("Не изменять" in callback_query.data):
        data["Product"].currency = int(callback_query.data)
        await state.update_data(data)
    elif "Отмена" in callback_query.data:
        await bot.send_message(callback_query.from_user.id, "Отмена")
        await form_menu_all_subcategories(data["call"], state)
    elif "Не изменять" in callback_query.data:
        data["Product"].currency = int(data["Product"].currency["id"])
    if await state.get_state() == 'StateProduct:add_product_currency':
        id_product = int(await api.post(const.product, data["Product"], callback_query.from_user.id))
        data["Product"] = await api.get(const.product + f'/{id_product}', Product(), callback_query.from_user.id)
        await state.update_data(data)
        data = await state.get_data()
        characteristics_list = await api.get_list(const.characteristics + f'/{data["Subcategory"].id}',
                                                  Characteristics, callback_query.from_user.id)
        if isinstance(characteristics_list, str):
            await bot.send_message(callback_query.from_user.id, 'Успешное создание товара')
            await form_menu_all_subcategories(data["call"], state)
            return
        await state.update_data({"characteristics_list": []})
        data = await state.get_data()
        for item in characteristics_list:
            ch = Characteristics()
            ch.id = item.id
            ch.datatype = item.datatype["type_name"]
            ch.preValuesList = item.preValuesList
            ch.characteristic_name = item.characteristic_name
            data["characteristics_list"].append(ch)
        await state.update_data(data)
        await state.update_data({"counter": 0})
        await state.update_data({"answers": ""})
        await check_values(state, callback_query)

    if await state.get_state() == 'StateProduct:edit_product_currency':
        await api.put(const.product + f'/{data["Product"].id}', data["Product"], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, "Успешное редактирование товара")
        await form_menu_all_product(data["call_selected_product"], state)


async def check_values(state: FSMContext, msg):
    data = await state.get_data()
    if data["counter"] == len(data["characteristics_list"]):
        await bot.send_message(msg.from_user.id, 'Успешное создание товара')
        await form_menu_all_subcategories(data["call"], state)
    elif data["characteristics_list"][data["counter"]].datatype == "Дата":
        await bot.send_message(msg.from_user.id,
                               f'Заполните {data["characteristics_list"][data["counter"]].characteristic_name} '
                               f'({data["characteristics_list"][data["counter"]].datatype})')
        await bot.send_message(msg.from_user.id, 'Выберете дату: ',
                               reply_markup=Datepicker(DatepickerSettings()).start_calendar())
        await StateProductCharacteristics.get_date.set()
    elif data["characteristics_list"][data["counter"]].preValuesList == []:
        await bot.send_message(msg.from_user.id,
                               f'Заполните {data["characteristics_list"][data["counter"]].characteristic_name} '
                               f'({data["characteristics_list"][data["counter"]].datatype})')
        await StateProductCharacteristics.get_characteristics.set()
    elif data["characteristics_list"][data["counter"]].preValuesList != []:
        await bot.send_message(msg.from_user.id,
                               f'Заполните {data["characteristics_list"][data["counter"]].characteristic_name} '
                               f'({data["characteristics_list"][data["counter"]].datatype})')
        button_text = []
        button_data = []
        for item in data["characteristics_list"][data["counter"]].preValuesList:
            button_text.append(item["pre_value"])
            button_data.append(item["id"])
        button_text.append("Готово")
        button_data.append("Готово")
        await bot.send_message(msg.from_user.id, 'Выберете значение',
                               reply_markup=keyboards.generate_keyboard_with_id(button_text, button_data))
        await state.update_data({"button_text": button_text, "button_data": button_data})
        await state.update_data({"checkbox": []})
        await StateProductCharacteristics.get_checkboxes.set()


@dp.message_handler(state=StateProductCharacteristics.get_characteristics)
async def form_get_strings(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data["characteristics_list"][data["counter"]].datatype == "Целое число":
        message.text = await valid.check_int(message, StateProductCharacteristics.get_characteristics, message.text)
    if data["characteristics_list"][data["counter"]].datatype == "Число с запятой":
        message.text = await valid.check_double(message, StateProductCharacteristics.get_characteristics,
                                                message.text)
    if message.text is not None:
        """data["answers"] += data["characteristics_list"][data["counter"]].characteristic_name + ' ' + str(
            message.text) + '\n'"""
        product_characteristic = Productcharacteristics()
        product_characteristic.product = data["Product"].id
        product_characteristic.characteristc_value = str(message.text)
        product_characteristic.characteristics = data["characteristics_list"][data["counter"]].id
        await api.post(const.product_characteristic, product_characteristic, message.from_user.id)
        data["counter"] = data["counter"] + 1
    await state.update_data(data)
    await check_values(state, message)


@dp.callback_query_handler(Datepicker.datepicker_callback.filter(), state=StateProductCharacteristics.get_date)
async def _process_datepicker(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    datepicker = Datepicker(DatepickerSettings())

    _date = await datepicker.process(callback_query, callback_data)
    if _date:
        await callback_query.message.answer(_date.strftime('%d/%m/%Y'))
        await callback_query.message.delete()
        # data["answers"] += _date.strftime('%d/%m/%Y') + '\n'
        product_characteristic = Productcharacteristics()
        product_characteristic.product = data["Product"].id
        product_characteristic.characteristics = data["characteristics_list"][data["counter"]].id
        product_characteristic.characteristc_value = str(_date.strftime('%Y-%m-%d'))
        await api.post(const.product_characteristic, product_characteristic, callback_query.from_user.id)
        data["counter"] += 1
        await state.update_data(data)
        await check_values(state, callback_query)
    await callback_query.answer()


@dp.callback_query_handler(state=StateProductCharacteristics.get_checkboxes)
async def process_checkbox(callback_query: types.CallbackQuery, state: FSMContext, ):
    data = await state.get_data()
    if callback_query.data == 'Готово':
        if data["checkbox"] == []:
            await bot.send_message(callback_query.from_user.id, "Должно быть выбрано хотябы одно значение")
        else:
            for item in data["checkbox"]:
                product_characteristic = Productcharacteristics()
                product_characteristic.product = data["Product"].id
                product_characteristic.characteristics = data["characteristics_list"][data["counter"]].id
                product_characteristic.characteristc_value = data["button_text"][
                    data["button_data"].index(int(item))].replace('✓ ', '')
                await api.post(const.product_characteristic, product_characteristic, callback_query.from_user.id)
            data["counter"] += 1
            await state.update_data(data)
            await check_values(state, callback_query)
    else:
        selected_value = data["button_text"][data["button_data"].index(int(callback_query.data))]
        if '✓ ' not in selected_value:
            data["button_text"][data["button_data"].index(int(callback_query.data))] = '✓ ' + selected_value
            data["checkbox"].append(callback_query.data)
        else:
            data["button_text"][data["button_data"].index(int(callback_query.data))] = selected_value.replace('✓ ', '')
            data["checkbox"].remove(callback_query.data)
        await state.update_data(data)
        await bot.edit_message_reply_markup(
            callback_query.message.chat.id,
            callback_query.message.message_id,
            reply_markup=keyboards.generate_keyboard_with_id(data["button_text"], data["button_data"])
        )
