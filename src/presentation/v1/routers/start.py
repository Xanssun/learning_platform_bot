from aiogram.types import Message, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results import StartResult
from src.application.v1.usecases import StartRequest


@inject
async def start_router(
    msg: Message,
    user: User,
    request_bus: FromDishka[RequestBus],
) -> None:
    result: StartResult = await request_bus.send(
        StartRequest(
            telegram_user_id=user.id,
            username=user.username,
        )
    )

    await msg.answer(result.text)
