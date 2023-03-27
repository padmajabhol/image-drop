from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import CommentBase, Comment, UserAuth
from repository.db_comments import get_all, create
from db.database import get_db
from auth.oauth2 import get_current_user

router  = APIRouter(prefix="/comments",  tags=["comments"])

@router.get("/all/{post_id}")
def comments(post_id: int, db: Session =  Depends(get_db)):
    return get_all(db, post_id)

@router.post("/create", response_model=Comment)
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return create(request, db)
