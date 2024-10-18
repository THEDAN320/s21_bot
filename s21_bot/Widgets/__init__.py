from aiogram import Router

from .AdminPanel import admin_panel_dialog
from .Auth import auth_dialog
from .MainMenu import main_menu_dialog


widgets_router = Router()
widgets_router.include_routers(auth_dialog, admin_panel_dialog, main_menu_dialog)


__all__ = ["widgets_router"]
