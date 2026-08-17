from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    username: str
    locale: str | None
