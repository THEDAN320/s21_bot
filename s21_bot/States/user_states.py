"""default states for users."""

from aiogram.filters.state import State, StatesGroup


class Auth(StatesGroup):
    """state group for auntification user."""

    get_role = State()
    get_nick = State()
    get_code = State()

    get_masterkey = State()


class Menu(StatesGroup):
    """state group for menu."""

    main = State()

    board_games = State()
    books = State()
    negotiation_rooms = State()
