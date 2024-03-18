from pydantic import BaseModel, ConfigDict


class UsersModel(BaseModel):
    username: str
    email: str
    password: str


class UsersResponseModel(UsersModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
