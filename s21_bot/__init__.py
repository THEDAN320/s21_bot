from typing import cast

from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import CallbackQuery, ErrorEvent, Message
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.api.exceptions import OutdatedIntent, UnknownIntent

from s21_bot.States.user_states import Auth, Menu

from .Handlers import handlers_router
from .Widgets import widgets_router


main_router = Router()


@main_router.error(ExceptionTypeFilter(UnknownIntent, OutdatedIntent))
async def handle_context_intent(
    event: ErrorEvent, dialog_manager: DialogManager
) -> None:
    error_message = "Что-то пошло не так, бот будет перезапущен."
    if event.update.callback_query:
        await cast(Message, event.update.callback_query.message).answer(error_message)
    else:
        await cast(
            Message, cast(CallbackQuery, event.update.callback_query).message
        ).answer(error_message)

    await dialog_manager.reset_stack(True)

    if False:  # todo: добавить проверку что пользователь находиться в бд
        await dialog_manager.start(
            Menu.main, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND
        )
    else:
        await dialog_manager.start(
            Auth.get_role, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND
        )


main_router.include_router(handlers_router)
main_router.include_router(widgets_router)


__all__ = ["main_router"]
