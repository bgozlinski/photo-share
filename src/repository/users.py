from sqlalchemy.orm import Session

from src.auth import get_password_hash
from src.database.models import Users
from src.schemas import UsersModel, UsersResponseModel


async def create_user(user_data: UsersModel,
                      db: Session
                      ) -> Users:

    hashed_password = get_password_hash(user_data.password)
    user_dict = user_data.dict()
    user_dict['password'] = hashed_password

    user = Users(**user_dict)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def get_user(user_id: int,
                   db: Session
                   ) -> Users:

    user = db.query(Users).filter(Users.id == user_id).first()
    return user


