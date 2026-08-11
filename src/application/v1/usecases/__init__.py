from src.application.common.bus import RequestBusImpl

from .start import StartRequest, StartUseCase


def setup_use_cases(request_bus: RequestBusImpl) -> None:
    request_bus.register(StartRequest, StartUseCase)


__all__ = (
    "StartRequest",
    "StartUseCase",
    "setup_use_cases",
)
