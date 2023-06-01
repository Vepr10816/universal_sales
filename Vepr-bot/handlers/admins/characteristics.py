from aiogram import types
from config import dp
from config import bot
from models.datatype import Datatype
from states.form import StateCharacteristics
from aiogram.dispatcher import FSMContext
from models.subcategory import Subcategory
from models.characteristics import Characteristics
from models.prevalues import Prevalues
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st


@dp.message_handler(commands=['Характеристики_Подкатегории'])
async def command_category(message: types.Message, state: FSMContext):
    if not await st.check_role(message.from_user.id, message, state):
        return
    await st.get_categories(message, state, StateCharacteristics.menu_all_categories)


@dp.callback_query_handler(state=StateCharacteristics.menu_all_categories)
async def form_menu_all_categories(callback_query: types.CallbackQuery, state: FSMContext):
    # await st.update_data({"call": callback_query}, state)
    await st.get_subcategories(callback_query, state, StateCharacteristics)


@dp.callback_query_handler(state=StateCharacteristics.menu_all_subcategories)
async def form_menu_all_subcategories(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action(callback_query, state, bot, StateCharacteristics.menu_all_categories,
                                  data["id_category_menu"]) is None:
        data = await st.update_data({'Subcategory': await api.get(const.subcategory + f'/{callback_query.data}',
                                                                  Subcategory(), callback_query.from_user.id)}, state)
        list_characteristics = await api.get_list(const.characteristics + f'/{data["Subcategory"].id}',
                                                  Characteristics, callback_query.from_user.id)
        buttons_text = []
        if not isinstance(list_characteristics, str):
            for item in list_characteristics:
                if item.selectable == False:
                    buttons_text.append(f'{item.characteristic_name} - {item.datatype["type_name"]}')
                else:
                    buttons_text.append(f'✓ {item.characteristic_name} - {item.datatype["type_name"]}')
        await keyboards.generate_big_keyboard(list_characteristics, bot, callback_query,
                                              StateCharacteristics.menu_all_characteristics,
                                              f'Характеристики',
                                              buttons_text,
                                              state, "id_characteristics_menu")


@dp.callback_query_handler(state=StateCharacteristics.menu_all_characteristics)
async def form_menu_all_characteristics(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateCharacteristics.menu_all_subcategories,
                                  data["id_subcategory_menu"]) is None:
        if "Добавить" in callback_query.data:
            await state.update_data({"Characteristics": Characteristics()})
            await bot.send_message(callback_query.from_user.id, 'Введите наименование характеристики')
            await StateCharacteristics.add_characteristic_name.set()
        else:
            data = await st.update_data(
                {'Characteristics': await api.get(const.characteristic + f'/{callback_query.data}',
                                                  Characteristics(), callback_query.from_user.id)},
                state)
            message_id = await callback_query.message.answer(f'{data["Characteristics"].characteristic_name} - '
                                                             f'{data["Characteristics"].datatype["type_name"]}',
                                                             reply_markup=keyboards.generate_keyboard(
                                                                 ["Редактировать", "Удалить",
                                                                  "Предопределённые значения",
                                                                  "Назад", "Отмена"]))
            await state.update_data({"id_selected_characteristic": message_id["message_id"]})
            await StateCharacteristics.menu_selected_characterictic.set()


@dp.callback_query_handler(state=StateCharacteristics.menu_selected_characterictic)
async def form_selected_characteristic(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateCharacteristics.menu_all_characteristics,
                                  data["id_characteristics_menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   'Введите новое наименование характеристики (Знак "-" если не хотите менять значение)')
            await StateCharacteristics.edit_characteristic_name.set()
        if "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.characteristic + f'/{data["Characteristics"].id}',
                                                    callback_query.from_user.id))
            await form_menu_all_subcategories(data["call"], state)
        if "Предопределённые значения" in callback_query.data:
            data = await st.update_data({"call_characteristic": callback_query}, state)
            list_pre_values = await api.get_list(const.pre_values + f'/{data["Characteristics"].id}',
                                                 Prevalues, callback_query.from_user.id)
            buttons_text = []
            if not isinstance(list_pre_values, str):
                for item in list_pre_values:
                    buttons_text.append(f'{item.pre_value}')
            await keyboards.generate_big_keyboard(list_pre_values, bot, callback_query,
                                                  StateCharacteristics.menu_all_characteristics,
                                                  f'Значения характеристики',
                                                  buttons_text,
                                                  state, "id_pre_values_menu")
            await StateCharacteristics.menu_all_pre_values.set()


@dp.callback_query_handler(state=StateCharacteristics.menu_all_pre_values)
async def form_menu_all_pre_values(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateCharacteristics.menu_selected_characterictic,
                                  data["id_selected_characteristic"]) is None:
        if "Добавить" in callback_query.data:
            await state.update_data({"Prevalues": Prevalues()})
            await bot.send_message(callback_query.from_user.id, f'Введите предопределенное значение характеристики '
                                                                f'{data["Characteristics"].characteristic_name}')
            await StateCharacteristics.add_pre_value.set()
        else:
            data = await st.update_data(
                {'Prevalues': await api.get(const.pre_value + f'/{callback_query.data}',
                                            Prevalues(), callback_query.from_user.id)}, state)
            await callback_query.message.answer(f'{data["Prevalues"].pre_value}',
                                                reply_markup=keyboards.generate_keyboard(
                                                    ["Редактировать", "Удалить",
                                                     "Назад", "Отмена"]))
            await StateCharacteristics.menu_selected_pre_value.set()


@dp.callback_query_handler(state=StateCharacteristics.menu_selected_pre_value)
async def form_menu_select_pre_values(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateCharacteristics.menu_selected_characterictic,
                                  data["id_pre_values_menu"]) is None:
        if callback_query.data == "Редактировать":
            await bot.send_message(callback_query.from_user.id, f'Введите новое предопределенное значение характеристики '
                                                                f'{data["Characteristics"].characteristic_name}')
            await StateCharacteristics.edit_pre_value.set()
        if callback_query.data == "Удалить":
            await callback_query.message.answer(await api.delete(const.pre_value + f'/{data["Prevalues"].id}',
                                                                 callback_query.from_user.id))
            await form_selected_characteristic(data["call_characteristic"], state)


@dp.message_handler(state={StateCharacteristics.add_pre_value, StateCharacteristics.edit_pre_value})
async def form_get_pre_value(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Prevalues"].characteristics = data["Characteristics"].id
    await state.update_data(data)
    if await state.get_state() == 'StateCharacteristics:add_pre_value':
        data["Prevalues"].pre_value = message.text
        await message.answer(await api.post(const.pre_value, data["Prevalues"], message.from_user.id))
    if await state.get_state() == 'StateCharacteristics:edit_pre_value' and message.text != '-':
        data["Prevalues"].pre_value = message.text
        await message.answer(
            await api.put(const.pre_value + f'/{data["Prevalues"].id}', data["Prevalues"],
                          message.from_user.id))
    #await message.answer("Доступно ли значение для выбора покупателем?", reply_markup=keyboards.generate_keyboard(["Да", "Нет"]))
    await form_selected_characteristic(data["call_characteristic"], state)


@dp.message_handler(state={StateCharacteristics.add_characteristic_name, StateCharacteristics.edit_characteristic_name})
async def form_get_characteristic_name(message: types.Message, state: FSMContext):
    buttons_text = []
    data = await state.get_data()
    if await state.get_state() == 'StateCharacteristics:edit_characteristic_name' and message.text != "-":
        data["Characteristics"].characteristic_name = message.text
    elif await state.get_state() == 'StateCharacteristics:add_characteristic_name':
        data["Characteristics"].characteristic_name = message.text
    data["Characteristics"].subcategory = data["Subcategory"].id
    await state.update_data(data)
    list_data_type = await api.get_list(const.data_types, Datatype, message.from_user.id)
    if not isinstance(list_data_type, str):
        for item in list_data_type:
            buttons_text.append(f'{item.type_name}')
        if await state.get_state() == 'StateCharacteristics:edit_characteristic_name':
            form_state = StateCharacteristics.edit_characteristic_data_type
            buttons_text.append("Не изменять")
        else:
            form_state = StateCharacteristics.add_characteristic_data_type
        await keyboards.generate_big_keyboard_without_help_buttons(list_data_type, bot, message,
                                                                   form_state,
                                                                   f'Выберете тип данных',
                                                                   buttons_text,
                                                                   state, "id_data_type_menu")
    else:
        await message.answer("В БД нет типов данных")
        await state.finish()


@dp.callback_query_handler(state={StateCharacteristics.add_characteristic_data_type,
                                  StateCharacteristics.edit_characteristic_data_type})
async def form_get_characteristic_data_type(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not ("Отмена" in callback_query.data) and not ("Не изменять" in callback_query.data):
        data["Characteristics"].datatype = int(callback_query.data)
        await state.update_data(data)
    elif "Отмена" in callback_query.data:
        await bot.send_message(callback_query.from_user.id, "Отмена")
        await form_menu_all_subcategories(data["call"], state)
        return
    elif "Не изменять" in callback_query.data:
        data["Characteristics"].datatype = data["Characteristics"].datatype["id"]
    if await state.get_state() == 'StateCharacteristics:add_characteristic_data_type':
        await StateCharacteristics.add_selectable.set()
    if await state.get_state() == 'StateCharacteristics:edit_characteristic_data_type':
        await StateCharacteristics.edit_selectable.set()
    await state.update_data(data)
    await callback_query.message.answer("Доступна ли характеристика для выбора покупателем?",
                         reply_markup=keyboards.generate_keyboard(["Да", "Нет"]))


@dp.callback_query_handler(state={StateCharacteristics.add_selectable, StateCharacteristics.edit_selectable})
async def form_get_selectable(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback_query.data == "Да":
        data["Characteristics"].selectable = True
    else:
        data["Characteristics"].selectable = False
    await state.update_data(data)
    if await state.get_state() == 'StateCharacteristics:add_selectable':
        await bot.send_message(callback_query.from_user.id,
                               await api.post(const.characteristic, data["Characteristics"],
                                              callback_query.from_user.id))
    if await state.get_state() == 'StateCharacteristics:edit_selectable':
        await bot.send_message(callback_query.from_user.id,
                               await api.put(const.characteristic + f'/{data["Characteristics"].id}',
                                             data["Characteristics"],
                                             callback_query.from_user.id))
    await form_menu_all_subcategories(data["call"], state)
