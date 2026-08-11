from aiogram.types import CallbackQuery, User
from dishka.integrations.aiogram import FromDishka, inject

from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.results.knowledge import KnowledgeResult
from src.application.v1.usecases.knowledge import KnowledgeRequest


@inject
async def knowledge_callback(
    callback: CallbackQuery,
    user: User,
    request_bus: FromDishka[RequestBus],
) -> None:
    result: KnowledgeResult = await request_bus.send(
        KnowledgeRequest(
            telegram_user_id=user.id,
        )
    )

    await callback.answer()

    if callback.message is None:
        return

    await callback.message.answer(
        result.text,
    )
