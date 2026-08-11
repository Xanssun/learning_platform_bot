import os
from pathlib import Path
from typing import Final, Union

from pydantic_settings import BaseSettings, SettingsConfigDict

_PathLike = Union[os.PathLike[str], str, Path]


LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "DEBUG")
PROJECT_NAME = os.getenv("APP_TITLE", "app")
PROJECT_VERSION = os.getenv("APP_VERSION", "0.0.1")

LOGGING_FORMAT: Final[str] = "%(asctime)s %(name)s %(levelname)s -> %(message)s"
DATETIME_FORMAT: Final[str] = "%Y.%m.%d %H:%M"


def root_dir() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def path(*paths: _PathLike, base_path: _PathLike | None = None) -> str:
    if base_path is None:
        base_path = root_dir()

    return os.path.join(base_path, *paths)


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_prefix="APP_",
        extra="ignore",
    )
    token: str = ""
    webhook_use: bool = False
    production: bool = True
    log_level: str = "DEBUG"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="SERVER_",
        extra="ignore",
        env_file="./.env",
    )


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="REDIS_",
        extra="ignore",
        env_file="./.env",
    )

    host: str = "127.0.0.1"
    port: int = 6379
    password: str | None = None
    app_key_prefix: str = "bot:app:"
    fsm_key_prefix: str = "bot:fsm"
    max_connections: int = 10
    fsm_max_connections: int = 5


class NatsSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        case_sensitive=False,
        env_prefix="NATS_",
        extra="ignore",
    )

    servers: list[str] = []
    user: str = ""
    password: str = ""


class Settings(BaseSettings):
    app: AppSettings
    server: ServerSettings
    redis: RedisSettings
    nats: NatsSettings


def load_settings(
    server: ServerSettings | None = None,
    app: AppSettings | None = None,
    redis: RedisSettings | None = None,
    nats: NatsSettings | None = None,
) -> Settings:
    return Settings(
        app=app or AppSettings(),
        server=server or ServerSettings(),
        redis=redis or RedisSettings(),
        nats=nats or NatsSettings(),
    )
