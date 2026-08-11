from aiogram import Router
from aiogram.filters import CommandStart

from src.presentation.common.filters import HasUser

from .start import start_router


def setup_routers() -> Router:
    router = Router(name=__name__)
    router.message.filter(HasUser())

    router.message.register(start_router, CommandStart())

    return router
