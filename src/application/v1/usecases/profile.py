from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.profile import ProfileResult


class ProfileRequest(Request):
    telegram_user_id: int


@dataclass(slots=True)
class ProfileUseCase(UseCase[ProfileRequest, ProfileResult]):
    async def __call__(self, request: ProfileRequest) -> ProfileResult:
        return ProfileResult(
            text="Введется работа над профилем, скоро будет доступно!"
        )
