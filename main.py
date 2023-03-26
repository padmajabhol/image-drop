from fastapi import FastAPI
from db import models
from db.database import engine
from routers import posts, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def root():
    return "Initial commit!"

app.mount('/images', StaticFiles(directory='images'), name='images')

