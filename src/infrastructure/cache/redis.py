from datetime import timedelta
from typing import Any

import redis.asyncio as aioredis

from src.settings.core import RedisSettings


class RedisCache:
    __slots__ = ("_key_prefix", "_redis")

    def __init__(
        self,
        redis: aioredis.Redis, # type: ignore
        key_prefix: str = "",
    ) -> None:
        self._redis = redis
        self._key_prefix = key_prefix

    async def get(self, key: str) -> str | None:
        return await self._redis.get(self._key(key))

    async def set(
        self, key: str, value: Any, expire: float | timedelta | None = None, **kw: Any
    ) -> None:
        await self._redis.set(self._key(key), value, ex=expire, **kw)

    async def delete(self, *keys: str) -> None:
        found_keys = [
            found for key in keys async for found in self._redis.scan_iter(self._key(key))
        ]
        if found_keys:
            await self._redis.delete(*found_keys)

    async def set_list(
        self, key: str, *values: Any, expire: float | timedelta | None = None, **kw: Any
    ) -> None:
        namespaced_key = self._key(key)
        await self._redis.lpush(namespaced_key, *(v for v in values))

        if expire:
            await self._redis.expire(
                namespaced_key,
                expire if isinstance(expire, timedelta) else timedelta(seconds=expire),
                **kw,
            )

    async def get_list(self, key: str, **kw: Any) -> list[str]:
        start, end = kw.pop("start", 0), kw.pop("end", -1)
        return await self._redis.lrange(self._key(key), start, end)

    async def discard(self, key: str, value: Any, **kw: Any) -> None:
        count = kw.pop("count", 0)
        await self._redis.lrem(self._key(key), count, value)

    async def clear(self) -> None:
        keys = [key async for key in self._redis.scan_iter(self._key("*"))]
        if keys:
            await self._redis.delete(*keys)

    async def setnx(
        self, key: str, value: Any, expire: float | timedelta | None = None
    ) -> bool:
        return bool(await self._redis.set(self._key(key), value, ex=expire, nx=True))

    async def exists(self, key: str) -> bool:
        return bool(await self._redis.exists(self._key(key)))

    async def keys(self, pattern: str | None = None) -> list[str]:
        keys = [key async for key in self._redis.scan_iter(self._key(pattern or "*"))]
        return [self._strip_prefix(key) for key in keys]

    async def close(self) -> None:
        await self._redis.aclose(close_connection_pool=True)  # type: ignore

    def _key(self, key: str) -> str:
        if not self._key_prefix or key.startswith(self._key_prefix):
            return key
        return f"{self._key_prefix}{key}"

    def _strip_prefix(self, key: str) -> str:
        if self._key_prefix and key.startswith(self._key_prefix):
            return key.removeprefix(self._key_prefix)
        return key


def create_redis_client(settings: RedisSettings, **kw: Any) -> aioredis.Redis: # type: ignore
    max_connections = kw.pop("max_connections", settings.max_connections)
    return aioredis.Redis(
        host=settings.host,
        port=settings.port,
        password=settings.password,
        decode_responses=True,
        max_connections=max_connections,
        **kw,
    )


def get_redis_pool(settings: RedisSettings, **kw: Any) -> RedisCache:
    return RedisCache(create_redis_client(settings, **kw))
