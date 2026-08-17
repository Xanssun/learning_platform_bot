from aiogram.types import CallbackQuery, Message, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results.settings import SettingsResult
from src.application.v1.usecases.settings import SettingsRequest


@inject
async def settings_callback(
    callback: CallbackQuery,
    message: Message,
    user: User,
    request_bus: FromDishka[RequestBus],
) -> None:
    result: SettingsResult = await request_bus.send(
        SettingsRequest(
            telegram_user_id=user.id,
        )
    )

    await callback.answer()

    await message.answer(
        result.text,
    )
