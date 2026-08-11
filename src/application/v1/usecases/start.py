from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.start import StartResult


class StartRequest(Request):
    telegram_user_id: int
    username: str | None = None


@dataclass(slots=True)
class StartUseCase(UseCase[StartRequest, StartResult]):
    async def __call__(self, request: StartRequest) -> StartResult:
        return StartResult(
            text=f"Привет, {request.username}! Добро пожаловать в learning platform."
        )
