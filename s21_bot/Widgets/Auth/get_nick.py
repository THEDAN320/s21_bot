from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, Window
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.text import Const

from s21_bot.States.user_states import Auth


async def on_nick_input(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    value: str,
) -> None:
    if False:  # todo: Добавить валидацицю для ника
        return

    # todo: Запустить фоновую задачу для отправки кода на почту

    await dialog_manager.switch_to(
        state=Auth.get_code, show_mode=ShowMode.DELETE_AND_SEND
    )


async def on_error_input(
    message: Message,
    dialog_: Any,
    manager: DialogManager,
    error_: ValueError,
) -> None:
    await message.answer("Некорректный ввод! Попробуйте снова.")
    await manager.switch_to(state=Auth.get_nick, show_mode=ShowMode.DELETE_AND_SEND)


get_nick_window = Window(
    Const("Супер!"),
    Const("Введи свой ник с платформы (edu.21-school.ru)"),
    TextInput(id="input_school_nick", on_success=on_nick_input, on_error=on_error_input),
    state=Auth.get_nick,
)
