from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_datepicker import Datepicker, DatepickerSettings

from config import dp, keyboards
from config import bot
from config import roles
from models.characteristics import Characteristics
from models.product import Product
from models.productcharacteristics import Productcharacteristics
from models.selectedproduct import Selectedproduct
from models.selectedproductcharacteristics import Selectedproductcharacteristics
from states.form import StateUsers
from states import form as st
from core.api_requests import ApiRequests as api
from config import const
from config import validate_data as valid


@dp.callback_query_handler(state=StateUsers.basket_menu)
async def form_menu_basket(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await keyboards.run_action_user(callback_query, state, bot, StateUsers.menu_basket,
                                       data["id_basket_menu"]) is None:
        if callback_query.data == "Детальный просмотр":
            for product in data["Basket"]:
                message_from_user = await st.get_product(product["Product"], callback_query, data, 1)
                keyboard = keyboards.generate_keyboard_from_basket_product(data, product)
                await callback_query.message.answer(message_from_user, parse_mode="Markdown", reply_markup=keyboard)
                await StateUsers.detail_basket_menu.set()
        elif callback_query.data == "Очистить корзину":
            data["Basket"].clear()
            await state.update_data(data)
            await callback_query.message.answer("Корзина очищена")
            await StateUsers.main_menu.set()
        elif callback_query.data == "Оформить заказ":
            await callback_query.message.answer('Введите комментарий к заказу (Знак "-" если комментарий не нужен')
            await StateUsers.add_order.set()
        else:
            try:
                message_from_user = await st.get_product(data["Basket"][int(callback_query.data)]["Product"],
                                                         callback_query, data, 1)
                keyboard = keyboards.generate_keyboard_from_basket_product(data,
                                                                           data["Basket"][int(callback_query.data)])
                await callback_query.message.answer(message_from_user, parse_mode="Markdown", reply_markup=keyboard)
                await StateUsers.detail_basket_menu.set()
            except Exception as err:
                await callback_query.message.answer("Ошибка. повторите попытку")
                print(err)
                await StateUsers.main_menu.set()
                return


@dp.message_handler(state=StateUsers.add_order)
async def form_add_order(message: types.Message, state: FSMContext):
    data = await state.get_data()
    url = const.order + '?'
    idProductList = []
    quantityList = []
    totalPrice = 0
    comment = message.text
    idProductCharacteristicsList = []
    for item in data["Basket"]:
        idProductList.append(item["Product"].id)
        quantityList.append(item["Selectedproduct"].product_quantity)
        totalPrice += item["Price"]
        if item["Selectedproductcharacteristics"] != []:
            for item2 in item["Selectedproductcharacteristics"]:
                idProductCharacteristicsList.append(item2.productcharacteristics)
        idProductCharacteristicsList.append(0)
    for item in idProductList:
        url += f'idProductList={item}&'
    for item in quantityList:
        url += f'quantityList={item}&'
    url += f'totalPrice={totalPrice}&'
    url += f'comment="{comment}"'
    for item in idProductCharacteristicsList:
        url += f'&idProductCharacteristicsList={item}'
    await message.answer(await api.post(url, None, message.from_user.id))
    await message.answer("Ожидайте, в ближайшее время с вами свяжется наш сотрудник.")
    await state.finish()
    await state.update_data({"Basket": []})
    await StateUsers.main_menu.set()


@dp.callback_query_handler(state=StateUsers.detail_basket_menu)
async def form_menu_detail_basket(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback_query.data == 'Назад':
        await keyboards.delete_message(StateUsers.basket_menu, callback_query, bot, data["id_basket_menu"])
        await st.get_basket(data, state, callback_query)
    elif await keyboards.run_action_user(callback_query, state, bot, StateUsers.basket_menu,
                                         data["id_basket_menu"]) is None:
        if '-' in callback_query.data or '+' in callback_query.data:
            callback = callback_query.data.split("|")
            quantity = 1 if callback[0] == '-' else -1
            price = data["Basket"][int(callback[1])]["Product"].product_price if callback[0] == '-' \
                else data["Basket"][int(callback[1])]["Product"].product_price * -1
            if data["Basket"][int(callback[1])]["Selectedproduct"].product_quantity == 1 and callback[0] == '-':
                return
            data["Basket"][int(callback[1])]["Selectedproduct"].product_quantity -= quantity
            data["Basket"][int(callback[1])]["Price"] -= price
            await state.update_data(data)
            data = await state.get_data()
            await bot.edit_message_reply_markup(
                callback_query.message.chat.id,
                callback_query.message.message_id,
                reply_markup=keyboards.generate_keyboard_from_basket_product(data,
                                                                             data["Basket"][int(callback[1])])
            )
        elif callback_query.data != "None":
            try:
                data["Basket"].pop(int(callback_query.data))
                await state.update_data(data)
                await callback_query.message.answer("Успешное удаление товара из корзины")
                await st.get_basket(data, state, callback_query)
            except Exception as err:
                await callback_query.message.answer("Ошибка. повторите попытку")
                print(err)
                StateUsers.main_menu.set()
