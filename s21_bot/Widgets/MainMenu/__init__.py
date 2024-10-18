from aiogram_dialog import Dialog

from .menu import menu_window


main_menu_dialog = Dialog(menu_window)


__all__ = ["main_menu_dialog"]
