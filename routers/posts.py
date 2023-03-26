from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .schemas import PostBase, PostDisplay
from db.database import get_db
from db.db_post import create, get_all

router = APIRouter(prefix="/posts", tags=['post'])

image_url_types = ['absolute', 'relative']

@router.post("/", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail= "Parameter image_url_type can only take values 'absolute' and 'relative'.")
    return create(request, db)

@router.get("/all", response_model=List[PostDisplay])
def post(db: Session = Depends(get_db)):
    return get_all(db)
