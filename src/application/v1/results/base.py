from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Result(BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)


class StatusResult(Result):
    status: bool
