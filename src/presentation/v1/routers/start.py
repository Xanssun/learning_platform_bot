import structlog
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results import StartResult
from src.application.v1.usecases import StartRequest

log = structlog.get_logger(__name__)


@inject
async def start_router(
    msg: Message,
    request_bus: FromDishka[RequestBus],
) -> None:
    result: StartResult = await request_bus.send(
        StartRequest(
            telegram_user_id=msg.from_user.id,  # type: ignore[union-attr]
            username=msg.from_user.username,  # type: ignore[union-attr]
        )
    )

    await msg.answer(result.text)
