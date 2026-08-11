from aiogram import Router
from aiogram.filters import CommandStart

from .start import start_router


def setup_routers() -> Router:
    router = Router(name=__name__)
    router.message.register(start_router, CommandStart())

    return router
