from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, Window
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.text import Const

from s21_bot.States.admin_states import AdminPanel
from s21_bot.States.user_states import Auth


async def on_masterkey_input(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, value: str
) -> None:
    if False:  # todo: Добавить проверку на валидный мастер ключ
        return

    data = {"masterkey": value}
    await dialog_manager.start(
        state=AdminPanel.main, data=data, show_mode=ShowMode.DELETE_AND_SEND
    )


async def on_error_input(
    message: Message, dialog_: Any, manager: DialogManager, error_: ValueError
) -> None:
    await message.answer("Некорректный ввод! Попробуйте снова.")
    await manager.switch_to(state=Auth.get_masterkey, show_mode=ShowMode.DELETE_AND_SEND)


get_masterkey_window = Window(
    Const("Нужно ввести мастер ключ, чтобы попасть в админ панель:"),
    TextInput(
        id="input_masterkey", on_success=on_masterkey_input, on_error=on_error_input
    ),
    state=Auth.get_masterkey,
)
