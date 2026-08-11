from abc import ABC, abstractmethod
from typing import Union

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


class BaseKeyboardBuilder(ABC):
    @abstractmethod
    def build(self) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
        """Build and return the keyboard markup."""
        ...


class BaseReplyKeyboardBuilder(BaseKeyboardBuilder, ABC):
    """Abstract base class for reply keyboard builders."""

    @abstractmethod
    def build(self) -> ReplyKeyboardMarkup:
        """Build and return the reply keyboard markup."""
        ...


class BaseInlineKeyboardBuilder(BaseKeyboardBuilder, ABC):
    """Abstract base class for inline keyboard builders."""

    @abstractmethod
    def build(self) -> InlineKeyboardMarkup:
        """Build and return the inline keyboard markup."""
        ...
