from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.settings import SettingsResult


class SettingsRequest(Request):
    telegram_user_id: int


@dataclass(slots=True)
class SettingsUseCase(UseCase[SettingsRequest, SettingsResult]):
    async def __call__(self, request: SettingsRequest) -> SettingsResult:
        return SettingsResult(
            text="Введется работа над настройками, скоро будет доступно!"
        )
