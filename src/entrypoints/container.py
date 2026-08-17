from dishka import AsyncContainer, Provider, make_async_container

from src.application.provider import ApplicationProvider
from src.infrastructure.broker.provider import BrokerProvider
from src.infrastructure.provider import InfrastructureProvider
from src.presentation.provider import PresentationProvider
from src.settings.core import Settings
from src.settings.provider import SettingsProvider


def build_container(settings: Settings, *extra: Provider) -> AsyncContainer:
    return make_async_container(
        SettingsProvider(),
        InfrastructureProvider(),
        BrokerProvider(),
        ApplicationProvider(),
        PresentationProvider(),
        *extra,
        context={Settings: settings},
    )
