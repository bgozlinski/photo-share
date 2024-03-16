import uvicorn
from fastapi import FastAPI

from src.routes import users

app = FastAPI()

app.include_router(users.router, prefix='/u')

if __name__ == '__main__':
    uvicorn.run('main:app')
