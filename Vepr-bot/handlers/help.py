import pathlib

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InputFile
from aiogram_datepicker import Datepicker, DatepickerSettings

from config import dp, keyboards
from config import bot
from config import roles
from states.form import StateUsers
from core.api_requests import ApiRequests as api
from config import const
from aiogram.utils.markdown import quote_html
from src import images
from app import dir_path


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message, state: FSMContext):
    if message.from_user.id in roles.admins:
        await bot.send_document(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'documents',
                                                                                 'user_guide.docx'))))
    else:
        message_from_user = 'Активирование бота со стороны клиента осуществляется при отправке команды «/start». ' \
                            'При нажатии на одну из кнопок клавиатура происходит переход бота в машинное состояние, ' \
                            'ожидающее определенное ' \
                            'действие от пользователя. Необходимо следовать указаниям бота, иначе он просто не будет ' \
                            'отвечать на ' \
                            'непредусмотренные действия.\nЕсли в браузерной версии пропала клавиатура, то вернуть '\
                            'её можно при помощи команды «/keyboard»'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'bot_states.png'))),
                             caption=message_from_user)
        message_from_user = 'Для простого понимания, машинное состояние представляет из себя меню, где кнопки ' \
                            'отвечают за переход в следующее меню. Кнопка «Отмена» является выходом из меню ( ' \
                            'машинного состояния), ' \
                            'а кнопка «Назад» является переходом в прошлое меню. '
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'bot_states_buttons.png'))),
                             caption=message_from_user)
        message_from_user = '«/Магазин» - вывод подробной информации о магазине\n' \
                            '«/Каталог» - просмотр каталога, заполненный продавцом, добавление товара в корзину ' \
                            'соответствующей кнопкой. \n«/Корзина» - просмотр корзины, изменение количества товара и ' \
                            'удаление товаров из ' \
                            'корзины, формирование заказа. \nИзменение количества товара осуществляется по кнопкам ' \
                            '«+» и «-».\n'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'edit_basket.png'))),
                             caption=message_from_user)
        message_from_user = '«Мои_Заказы» - просмотр сформированных заказов и их статусов. Заказ также можно ' \
                            'отменить по соответствующей кнопке, но удалить можно только тот заказ, который не ' \
                            'оформлен продавцом.'
        await bot.send_photo(message.from_user.id, InputFile(str(pathlib.Path(dir_path, 'src', 'images',
                                                                              'order.png'))),
                             caption=message_from_user)
