import asyncio
import aiohttp
from config.const import protocol
from config.const import ip
from config.const import auth

"""
Стартовое значение к запросам
"""
url_start = f'{protocol}://{ip}'


async def get_token(tg_id):
    """
    Получение токена пользователя.
    @param tg_id: первичный ключ пользователя.
    @return: header для API запроса.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{protocol}://{ip}{auth}?tgID={str(tg_id)}') as resp:
            response = await resp.json()
            header = {'Authorization': 'Bearer ' + response['data']['refresh_token']}
            return header


async def refresh_token(tg_id):
    """
    Обновление токена пользователя.
    @param tg_id: первичный ключ пользователя.
    @return: header для API запроса.
    """
    async with aiohttp.ClientSession() as session:
        header = await get_token(tg_id)
        async with session.post(f'{protocol}://{ip}{auth}/{header["Authorization"].replace("Bearer ", "")}') as resp:
            response = await resp.json()
            return header


class ApiRequests:
    """
    Обработка запросов к API.
    """
    async def auth(url):
        """
        Авторизация в API.
        @param url: строка запроса.
        """
        async with aiohttp.ClientSession() as session:
            async with session.put(f'{protocol}://{ip}{url}') as resp:
                response = await resp.json()

    async def get(url, model, tg_id):
        """
        Отправка Get запроса к API.
        @param url: строка запроса.
        @param model: модель данных.
        @param tg_id: Первичный ключ пользователя.
        @return: ответ API.
        """
        response = None
        while response is None:
            async with aiohttp.ClientSession() as session:
                header = await get_token(tg_id)
                # !!!try:
                async with session.get(url_start + url, headers=header) as resp:
                    response = await resp.json()
                    if 'error' in response and response['error'] == 'JWT token expired!':
                        await refresh_token(tg_id)
                        response = None
        if "message" not in response:
            if model is not None:
                model = model.set(**response)
            else:
                return response
            return model
        return response["message"]

    async def post(url, model, tg_id):
        """
        Отправка Post запроса к API.
        @param url: строка запроса.
        @param model: модель данных.
        @param tg_id: Первичный ключ пользователя.
        @return: ответ API.
        """
        async with aiohttp.ClientSession() as session:
            header = await get_token(tg_id)
            if model is not None:
                if model is not None:
                    async with session.post(url_start + url, headers=header, json=model.get()) as resp:
                        response = await resp.json()
                else:
                    async with session.post(url_start + url, headers=header) as resp:
                        response = await resp.json()
            else:
                async with session.post(url_start + url, headers=header) as resp:
                    response = await resp.json()
            return response['message']

    async def put(url, model, tg_id):
        """
        Отправка Put запроса к API.
        @param url: строка запроса.
        @param model: модель данных.
        @param tg_id: Первичный ключ пользователя.
        @return: ответ API.
        """
        async with aiohttp.ClientSession() as session:
            header = await get_token(tg_id)
            async with session.put(url_start + url, headers=header, json=model.get()) as resp:
                response = await resp.json()
            return response['message']

    async def get_list(url, model, tg_id):
        """
        Отправка Put запроса к API.
        @param url: строка запроса.
        @param model: модель данных.
        @param tg_id: Первичный ключ пользователя.
        @return: ответ API.
        """
        response = None
        while response is None:
            async with aiohttp.ClientSession() as session:
                header = await get_token(tg_id)
                # !!!try:
                async with session.get(url_start + url, headers=header) as resp:
                    response = await resp.json()
                    if 'error' in response and response['error'] == 'JWT token expired!':
                        await refresh_token(tg_id)
                        response = None
        if "message" not in response:
            list_model = []
            for item in response:
                list_model.append(model().set(**item))
            return list_model
        return response["message"]

    async def delete(url, tg_id):
        """
        Отправка Delete запроса к API.
        @param tg_id: Первичный ключ пользователя.
        @return: ответ API.
        """
        async with aiohttp.ClientSession() as session:
            header = await get_token(tg_id)
            async with session.delete(url_start + url, headers=header) as resp:
                response = await resp.json()
            return response['message']
