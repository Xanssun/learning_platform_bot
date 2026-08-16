from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.presentation.common.keyboards.base import BaseInlineKeyboardBuilder
from src.presentation.v1.keyboards.callbacks import LanguageCallback


class LanguageKeyboardBuilder(BaseInlineKeyboardBuilder):
    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🇷🇺 Русский",
                        callback_data=LanguageCallback(
                            locale="ru",
                        ).pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🇬🇧 English",
                        callback_data=LanguageCallback(
                            locale="en",
                        ).pack(),
                    ),
                ],
            ],
        )
