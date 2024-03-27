from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
import src.repository.users as repository_users
from src.schemas import UsersModel, UsersUpdateModel, UsersDisplayModel

router = APIRouter(tags=["users"])


@router.post("/", response_model=UsersModel)
async def create_user(user_data: UsersModel,
                      db: Session = Depends(get_db)
                      ):

    return await repository_users.create_user(user_data=user_data, db=db)


@router.get("/all", response_model=List[UsersDisplayModel])
async def get_all_users(db: Session = Depends(get_db)):
    return await repository_users.get_all_users(db=db)


@router.get("/{user_id}", response_model=UsersModel)
async def get_user(user_id: int,
                   db: Session = Depends(get_db)
                   ):

    return await repository_users.get_user(user_id=user_id, db=db)


@router.delete("/{user_id}", response_model=UsersModel)
async def delete_user(user_id: int,
                      db: Session = Depends(get_db)
                      ):

    return await repository_users.delete_user(user_id=user_id, db=db)


@router.put("/{user_id}", response_model=UsersModel)
async def update_user(user_id: int,
                      update_data: UsersUpdateModel,
                      db: Session = Depends(get_db)):

    return await repository_users.update_user(user_id=user_id, update_data=update_data, db=db)