from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import UserBase, UserDisplay
from db.database import get_db
from db.db_user import create

router = APIRouter(prefix="/users", tags=['user'])

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return create(request, db)