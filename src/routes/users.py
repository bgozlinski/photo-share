from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
import src.repository.users as repository_users
from src.schemas import UsersModel

router = APIRouter(tags=["users"])


@router.post("/")
async def create_user(user_data: UsersModel,
                      db: Session = Depends(get_db)
                      ):

    return await repository_users.create_user(user_data=user_data, db=db)






