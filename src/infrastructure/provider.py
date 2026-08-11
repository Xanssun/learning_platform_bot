from collections.abc import AsyncIterator

import redis.asyncio as aioredis
from dishka import Provider, Scope, provide

from src.application.common.interfaces.cache import StrCache
from src.infrastructure.cache.redis import RedisCache
from src.settings.core import Settings


class InfrastructureProvider(Provider):
    scope = Scope.APP

    @provide
    async def redis(self, settings: Settings) -> AsyncIterator[aioredis.Redis]:
        redis = aioredis.Redis(
            host=settings.redis.host,
            port=settings.redis.port,
            password=settings.redis.password,
            decode_responses=True,
        )
        try:
            yield redis
        finally:
            await redis.close(close_connection_pool=True)

    @provide
    def cache(self, redis: aioredis.Redis) -> StrCache:
        return RedisCache(redis)
