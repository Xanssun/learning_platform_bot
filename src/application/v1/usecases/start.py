from dataclasses import dataclass

from src.application.common.interfaces.cache import StrCache
from src.application.common.interfaces.usecase import UseCase
from src.application.common.request import Request
from src.application.v1.results.start import StartResult
from src.infrastructure.http.clients.learning_platform.response import UserResponse


class StartRequest(Request):
    telegram_user_id: int
    username: str | None = None


@dataclass(slots=True)
class StartUseCase(UseCase[StartRequest, StartResult]):
    cache: StrCache

    async def __call__(self, request: StartRequest) -> StartResult:

        #TODO: Request on the backend, select or create a user.

        # Temporary stub until Learning Platform integration is implemented.
        user = UserResponse(
            id=request.telegram_user_id,
            username="frogload",
            locale=None,  # Get the user's language from the backend.
        )

        return StartResult(
            username=user.username,
            locale=user.locale,
        )
