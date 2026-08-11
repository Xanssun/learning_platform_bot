from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide

from src.application.common.interfaces.cache import StrCache
from src.infrastructure.cache.redis import get_redis_pool
from src.infrastructure.http.provider.aiohttp import AiohttpProvider
from src.settings.core import Settings


class InfrastructureProvider(Provider):
    scope = Scope.APP

    @provide
    async def cache(self, settings: Settings) -> AsyncIterator[StrCache]:
        redis = get_redis_pool(settings.redis)
        try:
            yield redis
        finally:
            await redis.close()

    @provide
    async def aiohttp_provider(self) -> AsyncIterator[AiohttpProvider]:
        provider = AiohttpProvider()
        try:
            yield provider
        finally:
            await provider.close_session()
