import os
from dotenv import load_dotenv

# Получение токена телеграмм бота, маршрутов API из переменных окружения.

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

protocol = str(os.getenv("protocol"))

ip = str(os.getenv("ip"))

auth = str(os.getenv("auth"))

company = str(os.getenv("company"))

requisites = str(os.getenv("requisites"))

requisite = str(os.getenv("requisite"))

addresses = str(os.getenv("addresses"))

address = str(os.getenv("address"))

categories = str(os.getenv("categories"))

category = str(os.getenv("category"))

subcategory = str(os.getenv("subcategory"))

subcategories = str(os.getenv("subcategories"))

characteristic = str(os.getenv("characteristic"))

characteristics = str(os.getenv("characteristics"))

pre_values = str(os.getenv("pre_values"))

pre_value = str(os.getenv("pre_value"))

data_types = str(os.getenv("data_types"))

data_type = str(os.getenv("data_type"))

products = str(os.getenv("products"))

product = str(os.getenv("product"))

currencies = str(os.getenv("currencies"))

currency = str(os.getenv("currency"))

photos = str(os.getenv("photos"))

photo = str(os.getenv("photo"))

product_characteristics = str(os.getenv("product_characteristics"))
product_characteristic = str(os.getenv("product_characteristic"))

selectable_characteristics = str(os.getenv("selectable_characteristics"))
order = str(os.getenv("order"))
orders = str(os.getenv("orders"))
status = str(os.getenv("status"))