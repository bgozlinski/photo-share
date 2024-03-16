from sqlalchemy.orm import Session
from src.database.models import Users
from src.schemas import UsersModel


async def create_user(user_data: UsersModel,
                      db: Session
                      ) -> Users:

    user = Users(**user_data.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def get_user(user_id: int,
                   db: Session
                   ) -> Users:

    user = db.query(Users).filter(Users.id == user_id).first()
    return user


