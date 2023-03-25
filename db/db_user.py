from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from .models import DbUser

def create(request: UserBase, db: Session):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        #TODO hash password
        password = request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user