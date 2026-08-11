from dishka import Provider, Scope, provide

from src.application.common.bus import RequestBusImpl
from src.application.common.interfaces.cache import StrCache
from src.application.common.interfaces.event_bus import EventBus
from src.application.common.interfaces.request_bus import RequestBus
from src.application.v1.usecases import setup_use_cases


class ApplicationProvider(Provider):
    scope = Scope.APP

    @provide
    def request_bus(
        self,
        cache: StrCache,
        event_bus: EventBus,
    ) -> RequestBus:
        return (
            RequestBusImpl.builder()
            .dependencies(
                cache=cache,
                event_bus=event_bus,
            )
            .use_cases(setup_use_cases)
            .build()
        )
