from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.knowledge import KnowledgeResult


class KnowledgeRequest(Request):
    telegram_user_id: int


@dataclass(slots=True)
class KnowledgeUseCase(UseCase[KnowledgeRequest, KnowledgeResult]):
    async def __call__(self, request: KnowledgeRequest) -> KnowledgeResult:
        return KnowledgeResult(
            text="Введется работа над знаниями, скоро будет доступно!"
        )
