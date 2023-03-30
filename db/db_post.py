from routers.schemas import PostBase
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from .models import DbPost
from datetime import datetime


def create(request: PostBase,  db: Session):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    posts = db.query(DbPost).all()
    return posts


def delete(id: int, db: Session, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    if not post.user_id == user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized.")
    db.delete(post)
    db.commit()
    return 'done'
