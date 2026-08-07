from typing import Protocol, runtime_checkable

from src.application.common.events.base import Event
from src.application.common.interfaces.broker import BrokerType


@runtime_checkable
class EventWrapper(Protocol):
    async def execute(self, broker: BrokerType, message: Event, /) -> None: ...
