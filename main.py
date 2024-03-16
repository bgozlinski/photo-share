from fastapi import FastAPI

from src.routes import users

app = FastAPI()

app.include_router(users.router, prefix='/u')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
