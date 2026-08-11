from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message, User


class HasUser(BaseFilter):
    async def __call__(
        self,
        event: Message | CallbackQuery,
    ) -> dict[str, User] | bool:
        if event.from_user is None:
            return False

        return {"user": event.from_user}


class HasMessage(BaseFilter):
    async def __call__(
        self,
        callback: CallbackQuery,
    ) -> bool:
        return callback.message is not None
