from aiogram import types
from config import dp
from config import bot
from states.form import StateSubcategory
from aiogram.dispatcher import FSMContext
from models.category import Category
from models.subcategory import Subcategory
from core.api_requests import ApiRequests as api
from config import const
from config import keyboards
from states import form as st


@dp.message_handler(commands=['Подкатегории'])
async def command_category(message: types.Message, state: FSMContext):
    if not await st.check_role(message.from_user.id, message, state):
        return
    await st.get_categories(message, state, StateSubcategory.menu_all_categories)


@dp.callback_query_handler(state=StateSubcategory.menu_all_categories)
async def form_menu_all_categories(callback_query: types.CallbackQuery, state: FSMContext):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action(callback_query, state, bot, StateSubcategory, data["id_category_menu"]) is None:
        data = await st.update_data({'Category': await api.get(const.category + f'/{callback_query.data}',
                                                                Category(), callback_query.from_user.id)}, state)
        list_subcategory = await api.get_list(const.subcategories + f'/{data["Category"].id}',
                                                 Subcategory, callback_query.from_user.id)
        buttons_text = []
        if not isinstance(list_subcategory, str):
            for item in list_subcategory:
                buttons_text.append(f'{item.subcategory_name}')
        await keyboards.generate_big_keyboard(list_subcategory, bot, callback_query,
                                                                   StateSubcategory.menu_all_subcategories,
                                                                   'Подкатегории',
                                                                   buttons_text,
                                                                   state, "id_subcategory_menu")


@dp.callback_query_handler(state=StateSubcategory.menu_all_subcategories)
async def form_select_menu_all_subcategories(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateSubcategory.menu_all_categories,
                                  data["id_category_menu"]) is None:
        if "Добавить" in callback_query.data:
            await state.update_data({"Subcategory": Subcategory()})
            await bot.send_message(callback_query.from_user.id, 'Введите наименование подкатегории')
            await StateSubcategory.add_subcategory_name.set()
        else:
            data = await st.update_data({'Subcategory': await api.get(const.subcategory + f'/{callback_query.data}',
                                                                   Subcategory(), callback_query.from_user.id)}, state)
            await callback_query.message.answer(data["Subcategory"].subcategory_name,
                                                reply_markup=keyboards.generate_keyboard(
                                                    ["Редактировать", "Удалить", "Назад", "Отмена"]))
            await StateSubcategory.menu_selected_subcategory.set()


@dp.callback_query_handler(state=StateSubcategory.menu_selected_subcategory)
async def form_select_menu_selected_subcategory(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateSubcategory.menu_all_subcategories,
                                  data["id_subcategory_menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Введите новое наименование подкатегории')
            await StateSubcategory.edit_subcategory_name.set()
        if "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.subcategory + f'/{data["Subcategory"].id}',
                                                    callback_query.from_user.id))
            await form_menu_all_categories(data["call"], state)


@dp.message_handler(state={StateSubcategory.add_subcategory_name, StateSubcategory.edit_subcategory_name})
async def form_get_subcategory_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Subcategory"].subcategory_name = message.text
    data["Subcategory"].category = data["Category"].id
    await state.update_data(data)
    if await state.get_state() == 'StateSubcategory:add_subcategory_name':
        await message.answer(await api.post(const.subcategory, data["Subcategory"], message.from_user.id))
    if await state.get_state() == 'StateSubcategory:edit_subcategory_name':
        await message.answer(await api.put(const.subcategory + f'/{data["Subcategory"].id}', data["Subcategory"],
                                           message.from_user.id))
    await form_menu_all_categories(data["call"], state)
