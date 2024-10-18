from aiogram_dialog import Dialog

from .get_code import get_code_window
from .get_masterkey import get_masterkey_window
from .get_nick import get_nick_window
from .get_role import get_role_window


auth_dialog = Dialog(
    get_role_window, get_nick_window, get_code_window, get_masterkey_window
)


__all__ = ["auth_dialog"]
