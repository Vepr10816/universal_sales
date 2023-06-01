from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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


@dp.message_handler(commands=['Категории'])
async def command_category(message: types.Message, state: FSMContext, message_id=None):
    if not await st.check_role(message.from_user.id, message, state):
        return
    data = await st.update_data({"Company": await api.get(const.company, Mycompany(), message.from_user.id)}, state)
    data = await st.update_data({"Category": await api.get_list(const.categories + f'/1', Category,
                                                                message.from_user.id)}, state)
    data = await st.update_data({"message": message}, state)
    await StateCategory.menu_all_categories.set()
    if isinstance(data["Category"], str):
        message_id = await message.answer(data["Category"],
                                          reply_markup=keyboards.generate_keyboard(["Добавить категорию", "Отмена"]))
        await state.update_data({"id_category_menu": message_id["message_id"]})
    else:
        list_category = await api.get_list(const.categories + f'/1', Category, message.from_user.id)
        buttons_text = []
        if not isinstance(list_category, str):
            for item in list_category:
                buttons_text.append(f'{item.category_name}')
        await keyboards.generate_big_keyboard_without_back(list_category, bot, message,
                                                           StateCategory.menu_all_categories, 'Категории', buttons_text,
                                                           state, "id_category_menu")


@dp.callback_query_handler(state=StateCategory.menu_all_categories)
async def form_select_menu_all_categories(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await st.update_data({"call": callback_query}, state)
    if await keyboards.run_action(callback_query, state, bot, StateCategory, data["id_category_menu"]) is None:
        if "Добавить" in callback_query.data:
            await state.update_data({"Category": Category()})
            await bot.send_message(callback_query.from_user.id, 'Введите наименование категории')
            await StateCategory.add_category_name.set()
        else:
            data = await st.update_data({'Category': await api.get(const.category + f'/{callback_query.data}',
                                                                   Category(), callback_query.from_user.id)}, state)
            await callback_query.message.answer(data["Category"].category_name,
                                                reply_markup=keyboards.generate_keyboard(
                                                    ["Редактировать", "Удалить", "Назад", "Отмена"]))
            await StateCategory.menu_selected_category.set()


@dp.callback_query_handler(state=StateCategory.menu_selected_category)
async def form_select_menu_selected_category(callback_query: types.CallbackQuery, state: FSMContext, message_id=None):
    data = await state.get_data()
    if await keyboards.run_action(callback_query, state, bot, StateCategory.menu_all_categories,
                                  data["id_category_menu"]) is None:
        if "Редактировать" in callback_query.data:
            await bot.send_message(callback_query.from_user.id, 'Введите новое наименование категории')
            await StateCategory.edit_category_name.set()
        if "Удалить" in callback_query.data:
            await bot.send_message(callback_query.from_user.id,
                                   await api.delete(const.category + f'/{data["Category"].id}',
                                                    callback_query.from_user.id))
            await command_category(data["message"], state)


@dp.message_handler(state={StateCategory.add_category_name, StateCategory.edit_category_name})
async def form_get_category_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data["Category"].category_name = message.text
    data["Category"].mycompany = data["Company"].id
    await state.update_data(data)
    if await state.get_state() == 'StateCategory:add_category_name':
        await message.answer(await api.post(const.category, data["Category"], message.from_user.id))
    if await state.get_state() == 'StateCategory:edit_category_name':
        await message.answer(
            await api.put(const.category + f'/{data["Category"].id}', data["Category"], message.from_user.id)
        )
    await state.finish()
    await command_category(message, state)
