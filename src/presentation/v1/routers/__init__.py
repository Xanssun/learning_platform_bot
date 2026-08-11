from aiogram import F, Router
from aiogram.filters import CommandStart

from src.presentation.common.tools.filters import HasAccessibleMessage, HasUser
from src.presentation.v1.keyboards.callbacks import LanguageCallback, MenuCallback
from src.presentation.v1.routers.knowledge import knowledge_callback
from src.presentation.v1.routers.language import language_callback
from src.presentation.v1.routers.profile import profile_callback
from src.presentation.v1.routers.settings import settings_callback
from src.presentation.v1.routers.start import start_router


def setup_routers() -> Router:
    router = Router(name=__name__)
    router.message.filter(HasUser())
    router.callback_query.filter(HasUser(), HasAccessibleMessage())

    router.message.register(start_router, CommandStart())

    router.callback_query.register(
        profile_callback,
        MenuCallback.filter(F.action == "profile"),
    )
    router.callback_query.register(
        knowledge_callback,
        MenuCallback.filter(F.action == "knowledge"),
    )
    router.callback_query.register(
        settings_callback,
        MenuCallback.filter(F.action == "settings"),
    )
    router.callback_query.register(
        language_callback,
        LanguageCallback.filter(),
    )

    return router
