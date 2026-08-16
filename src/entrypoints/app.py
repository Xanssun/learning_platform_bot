import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

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
from src.infrastructure.cache.redis import create_redis_client
from src.infrastructure.logging.setup import setup_logging
from src.presentation.v1.routers import setup_routers
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

    dp = Dispatcher(
        storage=create_fsm_storage(settings),
    )

    dp.include_routers(setup_routers())

    setup_dishka(container, dp, auto_inject=True)
    setup_dialogs(dp)

    return dp, bot, container


def create_fsm_storage(settings: Settings) -> RedisStorage:
    redis = create_redis_client(
        settings.redis,
        max_connections=settings.redis.fsm_max_connections,
    )
    return RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(
            prefix=settings.redis.fsm_key_prefix,
            with_destiny=True,
        ),
    )


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
