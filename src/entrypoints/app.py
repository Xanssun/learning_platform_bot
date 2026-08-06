import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import redis.asyncio as aioredis
import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.base import (
    DefaultKeyBuilder,
)
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_dialog import setup_dialogs
from dishka import AsyncContainer
from dishka.integrations.aiogram import AiogramProvider, setup_dishka

from src.entrypoints.container import build_container
from src.infrastructure.logging.setup import setup_logging
from src.settings.core import Settings, load_settings

log = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(settings: Settings) -> AsyncIterator[tuple[Dispatcher, Bot]]:
    log.info("Startup")
    dp, bot, container = await create_app(settings)

    try:
        yield dp, bot
    finally:
        log.info("Shutdown started")

        await dp.storage.close()
        await bot.session.close()
        await container.close()

        log.info("Shutdown finished")


async def create_app(settings: Settings) -> tuple[Dispatcher, Bot, AsyncContainer]:
    container = build_container(settings, AiogramProvider())

    bot = Bot(
        token=settings.app.token,
        default=DefaultBotProperties(parse_mode="HTML"),
    )

    redis = await container.get(aioredis.Redis)
    dp = Dispatcher(storage=RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
        )
    )

    setup_dishka(container, dp)
    setup_dialogs(dp)

    # setup routers
    # setup middlewares
    # setup exceptions handlers

    return dp, bot, container


async def run(settings: Settings) -> None:
    async with lifespan(settings) as (dp, bot):
        if settings.app.webhook_use:
            pass

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


def main() -> None:
    settings = load_settings()
    setup_logging(settings)
    asyncio.run(run(settings))


if __name__ == "__main__":
    main()
