import string
from fastapi import APIRouter, Depends, HTTPException, status, File
from fastapi.datastructures import UploadFile
from sqlalchemy.orm import Session
from typing import List
from .schemas import PostBase, PostDisplay, UserAuth
from db.database import get_db
from db.db_post import create, get_all, delete
import random
import shutil
from auth.oauth2 import get_current_user

router = APIRouter(prefix="/posts", tags=['post'])

image_url_types = ['absolute', 'relative']

@router.post("/", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail= "Parameter image_url_type can only take values 'absolute' and 'relative'.")
    return create(request, db)

@router.get("/all", response_model=List[PostDisplay])
def post(db: Session = Depends(get_db)):
    return get_all(db)

@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}

@router.delete('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return delete(id, db, current_user.id)



