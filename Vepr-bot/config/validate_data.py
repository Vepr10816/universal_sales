import os
import pathlib
import string


async def check_cancel(message):
    """
    Проверка ввода комментария пользователем.
    @param message: сообщение пользователя.
    @return: флаг.
    """
    if message.text == '-':
        return True
    else:
        return None


def clear_whitespace(value):
    """
    Получение строки без пробелов.
    @param value: строка.
    @return: строка без пробелов.
    """
    return value.translate({ord(c): None for c in string.whitespace})


async def check_double(message, state, value):
    """
    Валидация сообщения с десятичным числом.
    @param message: объект для отправки сообщения.
    @param state: состояние бота.
    @param value: сообщение пользователя.
    @return: флаг.
    """
    try:
        if float(value) < 0:
            await message.answer("Некорректный ввод, повторите ввод:")
            return None
        return float(value)
    except:
        await message.answer("Некорректный ввод, повторите ввод:")
        await state.set()
        return None


async def check_int(message, state, value):
    """
        Валидация сообщения с целым числом.
        @param message: объект для отправки сообщения.
        @param state: состояние бота.
        @param value: сообщение пользователя.
        @return: флаг.
    """
    try:
        if int(value) < 0:
            await message.answer("Некорректный ввод, повторите ввод:")
            return None
        return int(value)
    except:
        await message.answer("Некорректный ввод, повторите ввод:")
        await state.set()
        return None


def check_folders(main_dir):
    """
    проверка на наличие папок прокта.
    @param main_dir: главная дирректория проекта.
    """
    if not os.path.exists(str(pathlib.Path(main_dir, 'images'))):
        os.mkdir(pathlib.Path(main_dir, 'images'))
        os.mkdir(str(pathlib.Path(main_dir, 'images', 'logo')))
        os.mkdir(str(pathlib.Path(main_dir, 'images', 'products_photo')))
