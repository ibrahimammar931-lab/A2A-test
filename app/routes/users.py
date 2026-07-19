from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from ..auth import oauth2_scheme, verify_token
from .enums import Role

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create(user: schemas.UserCreate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user_exists = crud.get_user(db, user.email)
    if user_exists:
        raise HTTPException(400, "Email already in use")
    if user.role not in [Role.admin, Role.manager, Role.developer]:
        raise HTTPException(400, "Invalid role")
    user = crud.create_user(db, user)
    return user

@router.get("/")
def list_users(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user = crud.get_user(db, token_data.sub)
    if user.role == Role.developer:
        return [user]
    return crud.get_users(db)