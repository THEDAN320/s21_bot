from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, SwitchTo
from aiogram_dialog.widgets.text import Const

from s21_bot.States.admin_states import AdminPanel
from s21_bot.States.user_states import Menu


admin_panel_window = Window(
    Const("Добро пожаловать в Админ панель!"),
    Const("Какие планы у нас на сегодня?"),
    Start(Const("Настолки"), id="board_games", state=Menu.board_games),
    Start(Const("Книжки"), id="books", state=Menu.books),
    Start(Const("Переговорки"), id="negotiation_rooms", state=Menu.negotiation_rooms),
    SwitchTo(Const("Неотдавашки"), id="debtors", state=AdminPanel.debtors),
    state=AdminPanel.main,
)
