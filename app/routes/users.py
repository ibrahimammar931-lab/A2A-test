from fastapi import APIRouter
from ..services import users_service
from .. import schemas
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
    return users_service.create_user(user)

@router.get("/")
def list_users():
    return users_service.get_users()