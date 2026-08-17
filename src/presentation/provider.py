from dishka import Provider, Scope, provide

from src.presentation.v1.keyboards.language import LanguageKeyboardBuilder
from src.presentation.v1.keyboards.main_menu import MainMenuKeyboardBuilder


class PresentationProvider(Provider):
    scope = Scope.APP

    @provide
    def main_menu_keyboard(self) -> MainMenuKeyboardBuilder:
        return MainMenuKeyboardBuilder()

    @provide
    def language_keyboard(self) -> LanguageKeyboardBuilder:
        return LanguageKeyboardBuilder()
