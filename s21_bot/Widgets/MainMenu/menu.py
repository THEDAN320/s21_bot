from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from s21_bot.States.user_states import Menu


menu_window = Window(
    Const("Добро пожаловать в главное меню!"),
    Const("Что сегодня забронируем?"),
    SwitchTo(Const("Настолки"), id="board_games", state=Menu.board_games),
    SwitchTo(Const("Книжки"), id="books", state=Menu.books),
    SwitchTo(Const("Переговорки"), id="negotiation_rooms", state=Menu.negotiation_rooms),
    state=Menu.main,
)
