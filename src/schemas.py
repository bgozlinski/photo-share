from pydantic import BaseModel, EmailStr


class UsersModel(BaseModel):
    username: str
    email: str
    password: str


class UsersUpdateModel(BaseModel):
    username: str | None = None
    email: EmailStr | None = None


class UsersDisplayModel(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
