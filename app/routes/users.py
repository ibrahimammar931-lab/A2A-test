from fastapi import APIRouter
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create(user: schemas.UserCreate):
    db: Session = SessionLocal()
    return crud.create_user(db, user)


@router.get("/")
def list_users():
    db: Session = SessionLocal()
    return crud.get_users(db)