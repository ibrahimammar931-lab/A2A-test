from .. import crud, schemas
from ..database import SessionLocal

def create_user(user: schemas.UserCreate):
    db: Session = SessionLocal()
    return crud.create_user(db, user)

def get_users():
    db: Session = SessionLocal()
    return crud.get_users(db)