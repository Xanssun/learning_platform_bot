from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    language: str | None = None
