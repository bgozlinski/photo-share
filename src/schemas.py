from datetime import datetime

from pydantic import BaseModel


class UsersModel(BaseModel):
    username: str
    email: str
    is_active: bool
    role: str
    created_at: datetime
