from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, Window
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.text import Const

from s21_bot.States.user_states import Auth, Menu


async def on_code_input(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, value: str
) -> None:
    if False:  # todo: Добавить проверку что введенный код валиден
        return

    # todo: Сохранить пользователя в базу данных

    await dialog_manager.start(state=Menu.main, show_mode=ShowMode.DELETE_AND_SEND)


async def on_error_input(
    message: Message, dialog_: Any, manager: DialogManager, error_: ValueError
) -> None:
    await message.answer("Некорректный ввод! Попробуйте снова.")
    await manager.switch_to(state=Auth.get_code, show_mode=ShowMode.DELETE_AND_SEND)


get_code_window = Window(
    Const("Сейчас тебе на почту придет код подтверждения."),
    Const("Введи его и мы продолжим!"),
    TextInput(id="input_email_code", on_success=on_code_input, on_error=on_error_input),
    state=Auth.get_code,
)
