from routers.schemas import UserBase
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