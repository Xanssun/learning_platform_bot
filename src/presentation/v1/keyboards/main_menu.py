from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.presentation.common.keyboards.base import BaseInlineKeyboardBuilder
from src.presentation.v1.keyboards.callbacks import MenuCallback


class MainMenuKeyboardBuilder(BaseInlineKeyboardBuilder):
    def build(self) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👤 Профиль",
                        callback_data=MenuCallback(action="profile").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="📚 База знаний",
                        callback_data=MenuCallback(action="knowledge").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙️ Настройки",
                        callback_data=MenuCallback(action="settings").pack(),
                    ),
                ],
            ],
        )
        return keyboard
