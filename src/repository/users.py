from typing import List

from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.auth import get_password_hash
from src.database.models import Users
from src.schemas import UsersModel, UsersUpdateModel


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
        raise HTTPException(status_code=400, detail="Username or email already exists")

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


async def get_all_users(db: Session) -> List[Users]:
    return db.query(Users).all()


async def delete_user(user_id: int,
                      db: Session
                      ):

    user = db.query(Users).filter(Users.id == user_id).first()
    db.delete(user)
    db.commit()


async def update_user(user_id: int,
                      update_data: UsersUpdateModel,
                      db: Session
                      ) -> Users:

    user = db.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if update_data.username:
        existing_user = db.query(Users).filter(
            Users.username == update_data.username,
            Users.id != user_id
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists.")

    if update_data.email:
        existing_user = db.query(Users).filter(
            Users.email == update_data.email,
            Users.id != user_id
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists.")

    if update_data.username:
        user.username = update_data.username
    if update_data.email:
        user.email = update_data.email

    db.commit()
    db.refresh(user)

    return user

