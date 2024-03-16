from pydantic import BaseModel


class UsersModel(BaseModel):
    username: str
    email: str
    password: str

