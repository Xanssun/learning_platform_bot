from aiogram.filters.callback_data import CallbackData


class MenuCallback(CallbackData, prefix="menu"):
    action: str


class LanguageCallback(CallbackData, prefix="language"):
    language: str
