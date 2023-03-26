from routers.schemas import UserBase
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from .models import DbUser
from .hasing import Hash

def create(request: UserBase, db: Session):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with username {username} not found")
    return user
    

