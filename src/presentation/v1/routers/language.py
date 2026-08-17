from aiogram.types import CallbackQuery, Message, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.usecases.language import LanguageRequest
from src.presentation.v1.keyboards.callbacks import LanguageCallback
from src.presentation.v1.keyboards.main_menu import MainMenuKeyboardBuilder


@inject
async def language_callback(
    callback: CallbackQuery,
    message: Message,
    user: User,
    callback_data: LanguageCallback,
    request_bus: FromDishka[RequestBus],
    main_menu_keyboard: FromDishka[MainMenuKeyboardBuilder],
) -> None:
    await request_bus.send(
        LanguageRequest(
            telegram_user_id=user.id,
            locale=callback_data.locale,
        )
    )

    await callback.answer()

    await message.edit_text(
        f"Hello, {user.username}! Welcome to Learning Platform.",
        reply_markup=main_menu_keyboard.build(),
    )
