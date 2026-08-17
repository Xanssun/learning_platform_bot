from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.presentation.common.keyboards.base import BaseInlineKeyboardBuilder
from src.presentation.v1.keyboards.callbacks import MenuCallback


class MainMenuKeyboardBuilder(BaseInlineKeyboardBuilder):
    def build(self) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👤 Profile",
                        callback_data=MenuCallback(action="profile").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="📚 Knowledge Base",
                        callback_data=MenuCallback(action="knowledge").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙️ Settings",
                        callback_data=MenuCallback(action="settings").pack(),
                    ),
                ],
            ],
        )
        return keyboard
