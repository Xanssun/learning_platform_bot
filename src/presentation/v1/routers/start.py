from aiogram.types import Message, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results import StartResult
from src.application.v1.usecases import StartRequest
from src.presentation.v1.keyboards.language import LanguageKeyboardBuilder
from src.presentation.v1.keyboards.main_menu import MainMenuKeyboardBuilder


@inject
async def start_router(
    msg: Message,
    user: User,
    request_bus: FromDishka[RequestBus],
    main_menu_keyboard: FromDishka[MainMenuKeyboardBuilder],
    language_keyboard: FromDishka[LanguageKeyboardBuilder],
) -> None:
    result: StartResult = await request_bus.send(
        StartRequest(
            telegram_user_id=user.id,
            username=user.username,
        )
    )

    if result.language_required:
        await msg.answer(
            result.text,
            reply_markup=language_keyboard.build(),
        )
        return

    await msg.answer(
        result.text,
        reply_markup=main_menu_keyboard.build(),
    )
