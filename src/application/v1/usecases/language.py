from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.language import LanguageResult


class LanguageRequest(Request):
    telegram_user_id: int
    username: str | None = None
    language: str


@dataclass(slots=True)
class LanguageUseCase(UseCase[LanguageRequest, LanguageResult]):
    async def __call__(self, request: LanguageRequest) -> LanguageResult:
        return LanguageResult(
            text=(
                f"Привет, {request.username}! "
                "Добро пожаловать в learning platform."
            ),
        )
