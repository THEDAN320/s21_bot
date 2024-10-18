from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from s21_bot.States.user_states import Auth


get_role_window = Window(
    Format("Привет {middleware_data[event_chat].first_name}!"),
    Const("Для начала представся"),
    Const("Кто ты?"),
    SwitchTo(Const("Пир"), id="is_peer", state=Auth.get_nick),
    SwitchTo(Const("Стафф"), id="is_staff", state=Auth.get_masterkey),
    state=Auth.get_role,
)
