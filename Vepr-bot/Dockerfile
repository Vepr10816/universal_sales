# Базовый образ, на основе которого будет построен контейнер
FROM python:alpine

# Устанавка рабочей директории
WORKDIR /vepr-bot

# Копирование исходного кода приложения внутрь контейнера
ADD . /vepr-bot/

# Копирование в контейнер в текущей директории
COPY . .

# Установка необходимых зависимостей
RUN pip install aiogram
RUN pip install aiogram-datepicker
RUN pip install aiogram-dialog
RUN pip install aiohttp
RUN pip install asyncio
RUN pip install python-dotenv

# Запуск приложения при старте контейнера
CMD ["python","app.py"]