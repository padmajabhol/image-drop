from fastapi import FastAPI
from db import models
from db.database import engine
from routers import users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(users.router)

@app.get("/")
def root():
    return "Initial commit!"

