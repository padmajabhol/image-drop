from fastapi import FastAPI
import uvicorn
from db import models
from db.database import engine
from routers import posts, users, comment
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comment.router)

@app.get("/")
def root():
    return "Initial commit!"

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_header=["*"]
)

app.mount('/images', StaticFiles(directory='images'), name='images')

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)

