from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Checkbox, ManagedCheckboxAdapter, Multiselect, Row, SwitchTo, Next, Back, \
    Calendar
from aiogram_dialog.widgets.text import Const, Format, Jinja
import operator
from datetime import date
from typing import Any

storage = MemoryStorage()
bot = Bot(token='5174124946:AAH9QA7wz4VYIMiHFeehrWPAe9yxjzAzBdI')
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


class DialogSG(StatesGroup):
    first = State()
    second = State()
    third = State()

# let's assume this is our window data getter
async def get_data(**kwargs):
    return {
        "title": "Animals list",
        "animals": ["cat", "dog", "my brother's tortoise"]
    }


html_text = Jinja("""
<b>{{title}}</b>
{% for animal in animals %}
* <a href="https://yandex.ru/search/?text={{ animal }}">{{ animal|capitalize }}</a>
{% endfor %}
""")


async def on_date_selected(c: CallbackQuery, widget, manager: DialogManager, selected_date: date):
    await c.answer(str(selected_date))


async def on_value_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    print("Fruit selected: ", item_id)


dialog = Dialog(
    Window(
        SwitchTo(Const("To second"), id="sec", state=DialogSG.second),
        html_text,
        parse_mode=ParseMode.HTML,
        state=DialogSG.first,
        getter=get_data
    ),
    Window(
        Const("Second"),
        Calendar(id='calendar', on_click=on_date_selected),
        Row(
            Back(),
            Next(),
        ),
        state=DialogSG.second,
    ),
    Window(
        Const("Third"),
        Multiselect(
            Format("✓ {item[0]}"),  # E.g `✓ Apple`
            Format("{item[0]}"),
            id="m_fruits",
            item_id_getter=operator.itemgetter(1),
            items=[
                ("Apple", '1'),
                ("Pear", '2'),
                ("Orange", '3'),
                ("Banana", '4'),
            ],
            on_state_changed=on_value_selected
        ),
        Back(),
        state=DialogSG.third,
    )
)
registry.register(dialog)

"""fruits_kbd = Multiselect(
    Format("✓ {item[0]}"),  # E.g `✓ Apple`
    Format("{item[0]}"),
    id="m_fruits",
    item_id_getter=operator.itemgetter(1),
    items="fruits",
)

main_window2 = Window(
    fruits_kbd,
    state=MySG.main,
)

dialog2 = Dialog(main_window2)
registry.register(dialog2)"""


questions = {
    "вопрос 1": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ],
    "вопрос 2": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ],
    "вопрос 3": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ]
}


class Dialog(StatesGroup):
    name = State()
    victorina = State()


@dp.message_handler(commands="help")
async def start(msg: types.Message):
    await Dialog.name.set()


@dp.message_handler(state=Dialog.name)
async def take_name_and_start_questions(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answers'] = []
        data['cur_question'] = 1
        data['name'] = msg.text

        for i, question in enumerate(questions):
            # тут выводим только первый вопрос
            if i != 0:
                break
            answers = questions[question]
            kb = create_kb(len(answers))
            text = question + "\n"
            for j, answer in enumerate(answers):
                text += f'{j + 1}) {answer} \n'

        await msg.answer(text, reply_markup=kb)

    await Dialog.victorina.set()


# тут должны обрабатываться ответы
@dp.message_handler(state=Dialog.victorina)
async def save_answer(msg: types.Message, state: FSMContext):
    text = None
    # добавляем ответ в массив
    async with state.proxy() as data:
        data['answers'].append(int(msg.text))

        # ну и выводим некст вопрос
        for i, question in enumerate(questions):
            # выводит только след вопрос
            if i == data['cur_question']:
                kb = create_kb(len(questions[question]))
                text = question + "\n"
                for j, answer in enumerate(questions[question]):
                    text += f'{i}) {answer} \n'
                # ну и чтобы зря не работал for брейкаем его
                break
        # делаем сразу некст вопрос
        data['cur_question'] += 1
    # ну и если вопросы кончились то никакого text ни kb не будет делаем проверку
    if text is not None:
        await msg.answer(text, reply_markup=kb)
    else:
        # собственно если нету то удалаем клавиатуру и пишем что-то
        answ = ''
        for item in data["answers"]:
            answ += f' {item}'
        await msg.answer(f'конец викторины: {answ}', reply_markup=ReplyKeyboardRemove())
        # а также в зависимости как вы работаете с стейтом делате или
        await state.finish()
        # или удаляете переменные в стейт ручками по типу
        #del data['answers']
        # и тд... Ну и само собой не забудьте забрать нужные вам данные до их удаление. Тобишь выше но в блоке елс


# создание клавиатуры с ответами 1-2-3 в зависимости от их числа
def create_kb(count: int):
    kb = ReplyKeyboardMarkup()
    for num in range(1, count + 1):
        button = KeyboardButton(text=f"{num}")
        kb.add(button)
    return kb


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(DialogSG.first, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
