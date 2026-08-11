from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide

from src.application.common.interfaces.cache import StrCache
from src.infrastructure.cache.redis import get_redis_pool
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
