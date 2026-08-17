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


class HasAccessibleMessage(BaseFilter):
    async def __call__(
        self,
        callback: CallbackQuery,
    ) -> dict[str, Message] | bool:
        if not isinstance(callback.message, Message):
            return False
        return {"message": callback.message}
