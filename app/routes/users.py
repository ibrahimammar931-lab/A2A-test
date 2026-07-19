from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from ..auth import oauth2_scheme, verify_token

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create(user: schemas.UserCreate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    return crud.create_user(db, user)

@router.get("/")
def list_users():
    db: Session = SessionLocal()
    return crud.get_users(db)