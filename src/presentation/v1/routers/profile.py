from aiogram.types import CallbackQuery, Message, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results.profile import ProfileResult
from src.application.v1.usecases.profile import ProfileRequest


@inject
async def profile_callback(
    callback: CallbackQuery,
    message: Message,
    user: User,
    request_bus: FromDishka[RequestBus],
) -> None:
    result: ProfileResult = await request_bus.send(
        ProfileRequest(
            telegram_user_id=user.id,
        )
    )

    await callback.answer()

    await message.answer(
        result.text,
    )
