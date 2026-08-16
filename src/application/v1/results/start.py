from src.application.v1.results.base import Result


class StartResult(Result):
    username: str
    locale: str | None
