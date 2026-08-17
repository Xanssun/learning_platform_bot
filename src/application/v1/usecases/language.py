from dataclasses import dataclass

from src.application.common.interfaces.cache import StrCache
from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.language import LanguageResult


class LanguageRequest(Request):
    telegram_user_id: int
    locale: str


@dataclass(slots=True)
class LanguageUseCase(UseCase[LanguageRequest, LanguageResult]):
    cache: StrCache

    async def __call__(self, request: LanguageRequest) -> LanguageResult:

        # TODO: save language in backend

        return LanguageResult()
