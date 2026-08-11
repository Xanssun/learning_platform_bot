from src.application.common.bus import RequestBusImpl

from .knowledge import KnowledgeRequest, KnowledgeUseCase
from .profile import ProfileRequest, ProfileUseCase
from .settings import SettingsRequest, SettingsUseCase
from .start import StartRequest, StartUseCase


def setup_use_cases(request_bus: RequestBusImpl) -> None:
    request_bus.register(
        StartRequest,
        StartUseCase
    )
    request_bus.register(
        ProfileRequest,
        ProfileUseCase
    )
    request_bus.register(
        SettingsRequest,
        SettingsUseCase,
    )
    request_bus.register(
        KnowledgeRequest,
        KnowledgeUseCase,
    )


__all__ = (
    "KnowledgeRequest",
    "KnowledgeUseCase",
    "SettingsRequest",
    "SettingsUseCase",
    "ProfileRequest",
    "ProfileUseCase",
    "StartRequest",
    "StartUseCase",
    "setup_use_cases",
)
