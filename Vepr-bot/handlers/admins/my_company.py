import os
import pathlib

from aiogram import types

import app
from config import dp
from config import bot
from models.addresses import Addresses
from models.requisites import Requisites
from states.form import StateMyCompany
from aiogram.dispatcher import FSMContext
from models.mycompany import Mycompany
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st
from aiogram.types import InputFile
import config.validate_data as valid


@dp.message_handler(commands=['Компания'])
async def command_company(message: types.Message, state: FSMContext, message_id=None):
    if not await st.check_role(message.from_user.id, message, state):
        return
    data = await st.update_data({"Company": await api.get(const.company, Mycompany(), message.from_user.id)}, state)
    await StateMyCompany.menu_company.set()
    if isinstance(data["Company"], str):
        await state.update_data({"Company": Mycompany()})
        message_id = await message.answer(data["Company"],
                                          reply_markup=keyboards.generate_keyboard(
                                              ["Добавить данные о компании", "Отмена"]))
    elif data["Company"].url_logo == ' ' and data["Company"].logo_name == ' ':
        message_id = await message.answer(f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                          parse_mode="Markdown",
                                          reply_markup=keyboards.generate_keyboard(
                                              ["Редактировать данные о компании", "Добавить логотип", "Реквизиты",
                                               "Адреса",
                                               "Отмена"]))
    else:
        if data["Company"].url_logo != ' ':
            message_id = await bot.send_photo(message.chat.id, data["Company"].url_logo,
                                              f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                              parse_mode="Markdown",
                                              reply_markup=keyboards.generate_keyboard(
                                                  ["Редактировать данные о компании", "Реквизиты", "Адреса",
                                                   "Изменить логотип",
                                                   "Отмена"]))
        elif data["Company"].logo_name != ' ':
            main_dir = str(pathlib.Path(app.dir_path).parents[0])
            message_id = await bot.send_photo(message.chat.id,
                                              InputFile(str(pathlib.Path(
                                                  main_dir, 'images', 'logo', f'{data["Company"].logo_name}'))),
                                              f'*{data["Company"].company_name}*\n{data["Company"].description}',
                                              parse_mode="Markdown",
                                              reply_markup=keyboards.generate_keyboard(
                                                  ["Редактировать данные о компании", "Реквизиты", "Адреса",
                                                   "Изменить логотип",
                                                   "Отмена"]))
    await state.update_data({"id_company_menu": message_id["message_id"]})


@dp.callback_query_handler(state=StateMyCompany.menu_company)
async def form_select_action1(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action(callback_query, state, bot, StateMyCompany, data["id_company_menu"]) is None:
        if "логотип" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Отправьте логотип вашей компании')
            await StateMyCompany.add_logo.set()
        elif "Добавить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Введите наименование вашей компании')
            await StateMyCompany.add_company_name.set()
        elif "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   'Введите новое наименование вашей компании (Знак "-" если не хотите менять значение)')
            await StateMyCompany.edit_company_name.set()
        elif "Реквизиты" in callback_query.data:
            data = await st.update_data(
                {"list_requisites": await api.get_list(const.requisites + f'/1',
                                                       Requisites, callback_query.from_user.id)}, state)
            buttons_text = []
            if not isinstance(data["list_requisites"], str):
                for item in data["list_requisites"]:
                    buttons_text.append(f'{item.requisites_name} - {item.requisites_value}')
            await keyboards.generate_big_keyboard(data["list_requisites"], bot, callback_query,
                                                  StateMyCompany.menu_requisites, 'Реквизиты', buttons_text, state,
                                                  "menu")
        elif "Адреса" in callback_query.data:
            data = await st.update_data(
                {"list_addresses": await api.get_list(const.addresses + f'/1',
                                                      Addresses, callback_query.from_user.id)}, state)
            buttons_text = []
            if not isinstance(data["list_addresses"], str):
                for item in data["list_addresses"]:
                    buttons_text.append(f'{item.address_name}')
            await keyboards.generate_big_keyboard(data["list_addresses"], bot, callback_query,
                                                  StateMyCompany.menu_addresses, 'Адреса',
                                                  buttons_text, state, "menu")


@dp.callback_query_handler(state=StateMyCompany.menu_requisites)
async def form_select_action2(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateMyCompany.menu_company,
                                  data["id_company_menu"]) is None:
        if "Добавить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Введите наименование реквизита')
            await StateMyCompany.add_requisite_name.set()
        else:
            data = await st.update_data({'Requisites': await api.get(const.requisite + f'/{callback_query.data}',
                                                                     Requisites(), callback_query.from_user.id)}, state)
            await bot.send_message(callback_query.from_user.id,
                                   f'{data["Requisites"].requisites_name} - {data["Requisites"].requisites_value}',
                                   reply_markup=keyboards.generate_keyboard(
                                       ["Редактировать", "Удалить", "Назад", "Отмена"]))
            await StateMyCompany.menu_requisite.set()


@dp.callback_query_handler(state=StateMyCompany.menu_requisite)
async def form_select_action3(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateMyCompany.menu_requisites, data["menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   'Введите новое наименование реквизита (Знак "-" если не хотите изменить)')
            await StateMyCompany.edit_requisite_name.set()
        elif "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.requisite + f'/{data["Requisites"].id}',
                                                    callback_query.from_user.id))
            await StateMyCompany.menu_company.set()
            callback_query.data = 'Реквизиты'
            await form_select_action1(callback_query, state)


@dp.callback_query_handler(state=StateMyCompany.menu_addresses)
async def form_menu_addresses(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateMyCompany.menu_company,
                                  data["id_company_menu"]) is None:
        if "Добавить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Введите адрес')
            await StateMyCompany.add_address_name.set()
        else:
            data = await st.update_data({'Addresses': await api.get(const.address + f'/{callback_query.data}',
                                                                    Addresses(), callback_query.from_user.id)}, state)
            await bot.send_message(callback_query.from_user.id, f'{data["Addresses"].address_name}',
                                   reply_markup=keyboards.generate_keyboard(
                                       ["Редактировать", "Удалить", "Назад", "Отмена"]))
            await StateMyCompany.menu_address.set()


@dp.callback_query_handler(state=StateMyCompany.menu_address)
async def form_select_address(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateMyCompany.menu_addresses, data["menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   'Введите новый адрес')
            await StateMyCompany.edit_address_name.set()
        elif "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.address + f'/{data["Addresses"].id}',
                                                    callback_query.from_user.id))
            await StateMyCompany.menu_company.set()
            callback_query.data = 'Адреса'
            await form_select_action1(callback_query, state)


@dp.message_handler(state=StateMyCompany.add_company_name)
async def form_get_company_name(messge: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Company"].company_name = messge.text
    await state.update_data(data)
    await messge.answer('Введите описание вашей компании')
    await StateMyCompany.next()


@dp.message_handler(state=StateMyCompany.add_company_description)
async def form_get_company_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Company"].description = message.text
    await message.answer(await api.post(const.company, data["Company"], message.from_user.id))
    await state.finish()
    await command_company(message, state)


@dp.message_handler(content_types=['photo'], state=StateMyCompany.add_logo)
async def load_img(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Company"].url_logo = message.photo[0].file_id
    main_dir = str(pathlib.Path(app.dir_path).parents[0])
    if len(main_dir) > 3:
        valid.check_folders(main_dir)
        await message.photo[-1].download(
            destination_file=str(pathlib.Path(main_dir, 'Vepr-site', 'Vepr-site', 'wwwroot','images', f'{data["Company"].url_logo}.jpg')))
        data["Company"].logo_name = f'{data["Company"].id}.jpg'
    await message.answer(await api.put(f'{const.company}/1', data["Company"], message.from_user.id))
    await state.finish()
    await command_company(message, state)


@dp.message_handler(state=StateMyCompany.add_requisite_name)
async def form_add_requisites_name(message: types.Message, state: FSMContext):
    await state.update_data({'Requisites': Requisites()})
    data = await state.get_data()
    data['Requisites'].requisites_name = message.text
    await state.update_data(data)
    await message.answer('Введите значение реквизита: ')
    await StateMyCompany.next()


@dp.message_handler(state=StateMyCompany.add_requisite_value)
async def form_add_requisites_value(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['Requisites'].requisites_value = message.text
    data['Requisites'].mycompany = data["Company"].id
    await state.update_data(data)

    await message.answer(await api.post(const.requisite, data['Requisites'], message.from_user.id))
    data["call"].data = "Реквизиты"
    await StateMyCompany.menu_requisites.set()
    await form_select_action1(data["call"], state)


@dp.message_handler(state=StateMyCompany.add_address_name)
async def form_add_address_name(message: types.Message, state: FSMContext):
    data = await st.update_data({'Addresses': Addresses()}, state)
    data['Addresses'].address_name = message.text
    data['Addresses'].mycompany = data["Company"].id
    await state.update_data(data)
    await message.answer(await api.post(const.address, data['Addresses'], message.from_user.id))
    data["call"].data = "Адреса"
    await StateMyCompany.menu_addresses.set()
    await form_select_action1(data["call"], state)


@dp.message_handler(state=StateMyCompany.edit_company_name)
async def form_edit_company_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text != '-':
        data["Company"].company_name = message.text
        await state.update_data(data)
    await message.answer('Введите новое описание компании (Знак "-" если не хотите менять значение)')
    await StateMyCompany.next()


@dp.message_handler(state=StateMyCompany.edit_company_description)
async def form_edit_company_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text != '-':
        data["Company"].description = message.text
        await state.update_data(data)
    await message.answer(await api.put(f'{const.company}/1', data["Company"], message.from_user.id))
    await state.finish()
    await command_company(message, state)


@dp.message_handler(state=StateMyCompany.edit_requisite_name)
async def form_edit_requisites_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text != '-':
        data['Requisites'].requisites_name = message.text
        # data = await st.update_data({'Requisites': data['Requisites'].requisites_name}, state)
    await state.update_data(data)
    await message.answer('Введите значение реквизита: ')
    await StateMyCompany.next()


@dp.message_handler(state=StateMyCompany.edit_requisite_value)
async def form_edit_requisites_value(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['Requisites'].mycompany = data["Company"].id
    if message.text != '-':
        data['Requisites'].requisites_value = message.text
    await state.update_data(data)
    await message.answer(
        await api.put(const.requisite + f'/{data["Requisites"].id}', data['Requisites'], message.from_user.id))
    data["call"].data = "Реквизиты"
    await StateMyCompany.menu_requisites.set()
    await form_select_action1(data["call"], state)


@dp.message_handler(state=StateMyCompany.edit_address_name)
async def form_edit_requisites_value(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['Addresses'].mycompany = data["Company"].id
    if message.text != '-':
        data['Addresses'].address_name = message.text
    await state.update_data(data)
    await message.answer(
        await api.put(const.address + f'/{data["Addresses"].id}', data['Addresses'], message.from_user.id))
    data["call"].data = "Адреса"
    await StateMyCompany.menu_addresses.set()
    await form_select_action1(data["call"], state)
