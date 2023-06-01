from aiogram import types


async def set_default_command(dp):
    """
    Постановка главных команд.
    @param dp: объект бота.
    """
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('keyboard', 'Клавиатура')
    ])
