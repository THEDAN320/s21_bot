"""handle /start command."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from s21_bot.States.user_states import Auth, Menu


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager) -> None:
    """/start handler."""
    if False:  # todo: Добавить проверку что пользователь уже в базе данных
        await dialog_manager.start(
            state=Menu.main,
            mode=StartMode.RESET_STACK,
            show_mode=ShowMode.DELETE_AND_SEND,
        )
    else:
        await dialog_manager.start(
            state=Auth.get_role,
            mode=StartMode.RESET_STACK,
            show_mode=ShowMode.DELETE_AND_SEND,
        )
