from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
import src.repository.users as repository_users
from src.schemas import UsersModel, UsersResponseModel

router = APIRouter(tags=["users"])


@router.post("/")
async def create_user(user_data: UsersModel,
                      db: Session = Depends(get_db)
                      ):

    return await repository_users.create_user(user_data=user_data, db=db)


@router.get("/{user_id}")
async def get_user(user_id: int,
                   db: Session = Depends(get_db)
                   ):

    return await repository_users.get_user(user_data=UsersResponseModel.id, db=db)







