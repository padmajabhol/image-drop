from sqlalchemy.orm.session import Session
from db.models import DbComment
from routers.schemas import CommentBase
from datetime import datetime

def create(request: CommentBase, db: Session):
    new_comment = DbComment(
        text = request.text,
        username = request.username,
        timestamp = datetime.now(),
        post_id = request.post_id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
    

def get_all(db: Session, post_id: int):
    comment = db.query(DbComment).filter(DbComment.id == post_id).first()
    return comment