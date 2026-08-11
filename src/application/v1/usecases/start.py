from dataclasses import dataclass

from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.start import StartResult
from src.infrastructure.http.clients.learning_platform.response import UserResponse


class StartRequest(Request):
    telegram_user_id: int
    username: str | None = None


@dataclass(slots=True)
class StartUseCase(UseCase[StartRequest, StartResult]):
    async def __call__(self, request: StartRequest) -> StartResult:

        #TODO: Request on the backend, select or create a user.

        # Temporary stub until Learning Platform integration is implemented.
        user = UserResponse(
            id=request.telegram_user_id,
            language=None,  # TODO: Get the user's language from the backend.
        )

        if user.language is None:
            return StartResult(
                text="Выберите язык:",
                language_required=True,
            )

        return StartResult(
            text=f"Привет, {request.username}! Добро пожаловать в learning platform.",
            language_required=False,
        )
