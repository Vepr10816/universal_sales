from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Window, Dialog
from states.form import StateUsers

"""
Формирование клавиатур и Inline кнопок для пользователей.
"""


def generate_keyboard(buttons):
    """
    Генерация клавиатуры из списка Inline кнопок.
    @param buttons: текстовый список контента кнопок.
    @return: builder кнопок.
    """
    builder = InlineKeyboardMarkup()
    builder.row_width = 1
    for button in buttons:
        builder.add(InlineKeyboardButton(
            text=button,
            callback_data=button)
        )
    return builder


def generate_keyboard_from_user(id_product):
    """
    Генерация Inline клавиатуры для покупателя.
    @param id_product: первичный ключ товара.
    @return: клавиатура.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        InlineKeyboardButton(
            text="Добавить в корзину",
            callback_data=id_product
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data="Назад"
        ),
        InlineKeyboardButton(
            text="Отмена",
            callback_data="Отмена"
        ),
    )
    return keyboard


def generate_keyboard_from_basket_product(data, product):
    """
    Генерация Inline клавиатуры для товаров в корзине.
    @param data: временная память.
    @param product: товар.
    @return: клавиатура.
    """
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(
        f'Итоговая цена: {product["Price"]} {product["Product"].currency["currency_name"]}',
        callback_data='None'))
    btn_minus = InlineKeyboardButton('-', callback_data=f'-|{data["Basket"].index(product)}')
    quantity = InlineKeyboardButton(f'{product["Selectedproduct"].product_quantity} шт', callback_data='None')
    btn_plus = InlineKeyboardButton('+', callback_data=f'+|{data["Basket"].index(product)}')
    keyboard.row(btn_minus, quantity, btn_plus)
    keyboard.add(InlineKeyboardButton("Удалить из корзины", callback_data=data["Basket"].index(product)))
    keyboard.add(InlineKeyboardButton("Назад", callback_data="Назад"))
    keyboard.add(InlineKeyboardButton("Отмена", callback_data="Отмена"))
    return keyboard


def generate_keyboard_with_id(buttons_text, buttons_data):
    """
    Генерация Inline клавиатуры c первичными ключами.
    @param buttons_text: строковый список контента кнопок.
    @param buttons_data: строковый список первичных ключей.
    @return: builder клавиатуры.
    """
    while len(buttons_text) != len(buttons_data):
        buttons_data.append(' ')
    builder = InlineKeyboardMarkup()
    builder.row_width = 1
    for i in range(len(buttons_text)):
        if buttons_data[i] != ' ':
            builder.add(InlineKeyboardButton(
                text=buttons_text[i],
                callback_data=buttons_data[i])
            )
        else:
            builder.add(InlineKeyboardButton(
                text=buttons_text[i],
                callback_data=buttons_text[i])
            )
    return builder


def keyboard_cancel_back():
    """
    Генерация Inline клавиатуры с кнопками назад и отмена.
    @return:
    """
    builder = InlineKeyboardMarkup()
    builder.row_width = 1
    builder.add(

        InlineKeyboardButton(
            text='Назад',
            callback_data='Назад'),

        InlineKeyboardButton(
            text='Отмена',
            callback_data='Отмена'),
    )
    return builder


async def delete_message(form_state, callback_query, bot, first_message):
    """
    Удаление сообщений для фокусирования внимания пользователя на конкретном сообщении (в обратном порядке
    от последнего к первому).
    @param form_state: машинное состояние бота.
    @param callback_query: объект хранящий первичный ключ сообщения с которого надо начать удалять.
    @param bot: объект самого бота.
    @param first_message: первичный ключ сообщения до которого надо удалять.
    """
    await form_state.set()
    last_message = callback_query.message.message_id
    current_message = last_message + 1
    while last_message != first_message:
        try:
            await bot.delete_message(callback_query.message.chat.id, current_message)
            current_message += 1
        except:
            try:
                await bot.delete_message(callback_query.message.chat.id, last_message)
                last_message = last_message - 1
            except:
                last_message = last_message - 1


async def run_action(callback_query: types.CallbackQuery, state: FSMContext, bot, form_state, first_message):
    """
    Проверка на нажате кнопок "Назад" или "Отмена".
    @param callback_query: объект управления сообщениями.
    @param state: машинное состояние бота.
    @param bot: объект бота.
    @param form_state: машинное состояние в которое необходимо перенаправить бота.
    @param first_message: первичный ключ сообщения до которого нужно удалять сообщения.
    @return: действие бота.
    """
    if 'Отмена' in callback_query.data:
        await state.finish()
        await bot.send_message(callback_query.from_user.id, 'Выход из меню')
        return True
    elif 'Назад' in callback_query.data:
        await delete_message(form_state, callback_query, bot, first_message)
        return True
    else:
        return None


async def run_action_user(callback_query: types.CallbackQuery, state: FSMContext, bot, form_state, first_message):
    """
    Проверка на нажате кнопок "Назад" или "Отмена" покупателем.
    @param callback_query: объект управления сообщениями.
    @param state: машинное состояние бота.
    @param bot: объект бота.
    @param form_state: машинное состояние в которое необходимо перенаправить бота.
    @param first_message: первичный ключ сообщения до которого нужно удалять сообщения.
    @return: действие бота.
    """
    if 'Отмена' in callback_query.data:
        await StateUsers.main_menu.set()
        await bot.send_message(callback_query.from_user.id, 'Выход из меню')
        return True
    elif 'Назад' in callback_query.data:
        await delete_message(form_state, callback_query, bot, first_message)
        return True
    elif 'Режим администратора' in callback_query.data:
        await state.finish()
        await bot.send_message(callback_query.from_user.id, 'Режим администратора активирован')
        return True
    else:
        return None


async def generate_big_keyboard(data, bot, callback_query, form, name_model, buttons_text, state, menu_name):
    """
    Генерация Inline клавиатуры с дополнительными кнопками.
    @param data: объект временной памяти.
    @param bot: объект бота.
    @param callback_query: объект управления сообщениями.
    @param form: машинное состояние в которое необходимо перенаправить бота.
    @param name_model: название модели.
    @param buttons_text: текстовый список контента кнопок.
    @param state: машинное состояние бота.
    @param menu_name: наименование меню.
    """
    buttons_data = []
    if isinstance(data, str):
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model} не заполнены',
                                            reply_markup=generate_keyboard(["Добавить", "Назад", "Отмена"]))
    else:
        for item in data:
            buttons_data.append(f'{item.id}')
        buttons_text.append(f'Добавить {name_model}')
        buttons_text.append("Назад")
        buttons_text.append("Отмена")
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model}:',
                                            reply_markup=generate_keyboard_with_id(buttons_text, buttons_data))
    await state.update_data({menu_name: message_id["message_id"]})
    await form.set()


async def generate_big_keyboard_without_back(data, bot, callback_query, form, name_model, buttons_text, state,
                                             menu_name):
    """
        Генерация Inline клавиатуры с дополнительными кнопками без кнопки назад.
        @param data: объект временной памяти.
        @param bot: объект бота.
        @param callback_query: объект управления сообщениями.
        @param form: машинное состояние в которое необходимо перенаправить бота.
        @param name_model: название модели.
        @param buttons_text: текстовый список контента кнопок.
        @param state: машинное состояние бота.
        @param menu_name: наименование меню.
    """
    buttons_data = []
    if isinstance(data, str):
        await bot.send_message(callback_query.from_user.id, f'{name_model} не заполнены',
                               reply_markup=generate_keyboard(["Добавить", "Отмена"]))
    else:
        for item in data:
            buttons_data.append(f'{item.id}')
        buttons_text.append(f'Добавить {name_model}')
        buttons_text.append("Отмена")
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model}:',
                                            reply_markup=generate_keyboard_with_id(buttons_text, buttons_data))
        await state.update_data({menu_name: message_id["message_id"]})
    await form.set()


async def generate_big_keyboard_without_help_buttons(data, bot, callback_query, form, name_model, buttons_text, state,
                                                     menu_name):
    """
        Генерация Inline клавиатуры без дополнительных кнопок.
        @param data: объект временной памяти.
        @param bot: объект бота.
        @param callback_query: объект управления сообщениями.
        @param form: машинное состояние в которое необходимо перенаправить бота.
        @param name_model: название модели.
        @param buttons_text: текстовый список контента кнопок.
        @param state: машинное состояние бота.
        @param menu_name: наименование меню.
    """
    buttons_data = []
    if isinstance(data, str):
        await bot.send_message(callback_query.from_user.id, f'{name_model} не заполнены',
                               reply_markup=generate_keyboard(["Отмена"]))
    else:
        for item in data:
            buttons_data.append(f'{item.id}')
        buttons_text.append("Отмена")
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model}:',
                                            reply_markup=generate_keyboard_with_id(buttons_text, buttons_data))
        await state.update_data({menu_name: message_id["message_id"]})
    await form.set()


async def generate_big_keyboard_without_add(data, bot, callback_query, form, name_model, buttons_text, state,
                                            menu_name):
    """
            Генерация Inline клавиатуры без кнопки добавления.
            @param data: объект временной памяти.
            @param bot: объект бота.
            @param callback_query: объект управления сообщениями.
            @param form: машинное состояние в которое необходимо перенаправить бота.
            @param name_model: название модели.
            @param buttons_text: текстовый список контента кнопок.
            @param state: машинное состояние бота.
            @param menu_name: наименование меню.
    """
    buttons_data = []
    if isinstance(data, str):
        await bot.send_message(callback_query.from_user.id, f'{name_model} не заполнены',
                               reply_markup=generate_keyboard(["Добавить", "Отмена"]))
    else:
        for item in data:
            buttons_data.append(f'{item.id}')
        buttons_text.append(f'Назад')
        buttons_text.append("Отмена")
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model}:',
                                            reply_markup=generate_keyboard_with_id(buttons_text, buttons_data))
        await state.update_data({menu_name: message_id["message_id"]})
    await form.set()


async def generate_big_keyboard_from_user(data, bot, callback_query, form, name_model, buttons_text, state,
                                          menu_name):
    """
            Генерация Inline клавиатуры для покупателя.
            @param data: объект временной памяти.
            @param bot: объект бота.
            @param callback_query: объект управления сообщениями.
            @param form: машинное состояние в которое необходимо перенаправить бота.
            @param name_model: название модели.
            @param buttons_text: текстовый список контента кнопок.
            @param state: машинное состояние бота.
            @param menu_name: наименование меню.
    """
    buttons_data = []
    if isinstance(data, str):
        await bot.send_message(callback_query.from_user.id, f'Вы ещё не заполнили данный раздел')
    else:
        for item in data:
            buttons_data.append(f'{item.id}')
        buttons_text.append(f'Назад')
        buttons_text.append("Отмена")
        buttons_text.append("Просмотр всего каталога")
        message_id = await bot.send_message(callback_query.from_user.id, f'{name_model}:',
                                            reply_markup=generate_keyboard_with_id(buttons_text, buttons_data))
        await state.update_data({menu_name: message_id["message_id"]})
        await form.set()


"""
Основные клавиатуры для пользователей
"""
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/Компания')).add(
    KeyboardButton('/Категории')).add(KeyboardButton('/Подкатегории')).add(
    KeyboardButton('/Характеристики_Подкатегории')).add(KeyboardButton('/Товары')).add(
    KeyboardButton('/Режим_Покупателя')).add(KeyboardButton('/Заказы'))

button_case_users = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/Каталог')).add(
    KeyboardButton('/Корзина')).add(KeyboardButton('/Мои_Заказы')).add(KeyboardButton('/Магазин'))

button_case_admin_switch_mode = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/Каталог')).add(
    KeyboardButton('/Корзина')).add(KeyboardButton('/Мои_Заказы')).add(KeyboardButton('/Магазин')).add(
    KeyboardButton('/Режим_Администратора'))


def get_date_picker(form, func):
    """
    Получение календаря.
    @param form: машинное состояние бота.
    @param func: функция.
    @return: диалоговое сообщение с календарём.
    """
    dialog = Dialog(
        Window(
            Const("Выберете дату"),
            Calendar(id='calendar', on_click=func),
            state=form,
        ))
    return dialog
