from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.auth import get_password_hash
from src.database.models import Users
from src.schemas import UsersModel, UsersResponseModel


async def create_user(user_data: UsersModel,
                      db: Session
                      ) -> Users:

    existing_user = db.query(Users).filter(
        or_(
            Users.username == user_data.username,
            Users.email == user_data.email
        )
    ).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Username or email already exists")

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


async def delete_user(user_id: int,
                      db: Session
                      ):

    user = db.query(Users).filter(Users.id == user_id).first()
    db.delete(user)
    db.commit()
