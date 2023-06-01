import asyncio
import os
import pathlib

from models.order import Order
from models.product import Product
from models.selectedproduct import Selectedproduct
from models.selectedproductcharacteristics import Selectedproductcharacteristics
from core.api_requests import ApiRequests as api
from config import const

product = Product()
ch = Selectedproductcharacteristics()
chs = Selectedproductcharacteristics()
chw = Selectedproductcharacteristics()
chq = Selectedproductcharacteristics()
ch.selectedproduct = 3
ch.productcharacteristics = 13
ch1 = ch
chs.selectedproduct = 7
chs.productcharacteristics = 11
ch2 = chs
chw.selectedproduct = 1
chw.productcharacteristics = 9
ch3 = chw

chq.selectedproduct = 10
chq.productcharacteristics = 9
ch4 = chw
sl = Selectedproduct()

Basket = []

Basket.append(
    {
        "Product": 3,
        "SelectedProduct": sl.set(30, 3, 3),
        "Price": 6700,
        "SelectedProductCharacteristics": [ch1, ch2]
    }
)

Basket.append(
    {
        "Product": 2,
        "SelectedProduct": sl.set(25, 2, 1),
        "Price": 2500,
        "SelectedProductCharacteristics": [ch3]
    }
)

"""price = 0
for item in Basket:
    price += item["Price"]
print(price)

order = Order()
order.user = 27382372387
order.comment = "Комментарий"
order.total_price = price

print(Basket[0]["Price"])

for item in Basket:
    price += item["Price"]
print(price)"""

Basket[0]["SelectedProductCharacteristics"].append(ch4)

print(Basket[0]["SelectedProductCharacteristics"])


async def get():
    response = await api.get(const.order, None, 723192577)
    print(response)
    for item in response:
        print(item["Order"]["comment"])
        for item2 in item["Products"]:
            print(item2["Product"]["product_name"])

asyncio.run(get())

# Получаем строку, содержащую путь к рабочей директории:
dir_path = pathlib.Path.cwd()

# Объединяем полученную строку с недостающими частями пути
#path = pathlib.Path(dir_path, 'src', 'images','bot_states.png')

# выведем значение переменной path:
print(str(pathlib.Path(dir_path).parents[0]))

print(len(os.listdir(pathlib.Path(dir_path).parents[0])))

if not os.path.exists(str(pathlib.Path(dir_path).parents[0])+'/images'):
    os.makedirs(str(pathlib.Path(dir_path).parents[0])+'/images/logo')
    os.makedirs(str(pathlib.Path(dir_path).parents[0])+'/images/product_images')



a = [1, 2, 4]

'''
button_text = []
button_data = []
message_text = ""
for i in range(selectable_characteristics_list):
    item = selectable_characteristics_list[i]
    button_text.append(item.characteristc_value)
    button_data.append(item.id)
    if item == selectable_characteristics_list[-1]:
        button_text.append("Отмена")
    if item.characteristics["id"] != selectable_characteristics_list[i+1]\
            or item = selectable_characteristics_list[-1]:
        selectable_characterisrics.append(
            {
                "message_text": message_text,
                "button_text": button_text,
                "button_data": button_data,
            }
        )
        button_text = []
        button_data = []







id = 0
            button_text = []
            button_data = []
            message_text = ""
            for item in selectable_characteristics_list:
                if item.characteristics["id"] != id:
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
                    id = item.characteristics["id"]
                if item.characteristics["id"] == id:
                    button_text.append(item.characteristc_value)
                    button_data.append(item.id)
                    if item == selectable_characteristics_list[-1]:
                        button_text.append("Отмена")
                if (id != 0 and item.characteristics["id"] != id) or item == selectable_characteristics_list[-1]:
                    if item != selectable_characteristics_list[-1]:
                        button_text.append("Отмена")
                    selectable_characterisrics.append(
                        {
                            "message_text": message_text,
                            "button_text": button_text,
                            "button_data": button_data,
                        }
                    )'''