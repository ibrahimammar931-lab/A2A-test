from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from ..auth import oauth2_scheme, verify_token
from .enums import Role

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create(task: schemas.TaskCreate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user = crud.get_user_by_email(db, token_data.email)
    if user.role not in [Role.admin, Role.manager]:
        raise HTTPException(403, "Forbidden")
    return crud.create_task(db, task)

@router.get("/")
def list_tasks(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user = crud.get_user_by_email(db, token_data.email)
    if user.role == Role.developer:
        return crud.get_tasks_by_user(db, user.id)
    return crud.get_tasks(db)

@router.put("/{task_id}")
def update(task_id: int, task: schemas.TaskUpdate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user = crud.get_user_by_email(db, token_data.email)
    if user.role not in [Role.admin, Role.manager]:
        raise HTTPException(403, "Forbidden")
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(404, "Task not found")
    return updated

@router.delete("/{task_id}")
def delete(task_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={{"WWW-Authenticate": "Bearer"}},
    )
    token_data = verify_token(token, credentials_exception)
    db: Session = SessionLocal()
    user = crud.get_user_by_email(db, token_data.email)
    if user.role != Role.admin:
        raise HTTPException(403, "Forbidden")
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(404, "Task not found")
    return {{"message": "Deleted"}}