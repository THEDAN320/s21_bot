from aiogram_dialog import Dialog

from .admin_panel import admin_panel_window


admin_panel_dialog = Dialog(admin_panel_window)


__all__ = ["admin_panel_dialog"]
