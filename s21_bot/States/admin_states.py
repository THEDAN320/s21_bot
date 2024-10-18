"""states for staffs."""

from aiogram.filters.state import State, StatesGroup


class AdminPanel(StatesGroup):
    """state group for admin panel."""

    main = State()
    debtors = State()
