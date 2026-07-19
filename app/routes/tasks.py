from fastapi import APIRouter, HTTPException, Depends
from ..services import tasks_service
from .. import schemas
from ..auth import oauth2_scheme, verify_token

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create(task: schemas.TaskCreate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    return tasks_service.create_task(task)

@router.get("/")
def list_tasks():
    return tasks_service.get_tasks()

@router.put("/{task_id}")
def update(task_id: int, task: schemas.TaskUpdate, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    updated = tasks_service.update_task(task_id, task)
    if not updated:
        raise HTTPException(404, "Task not found")
    return updated

@router.delete("/{task_id}")
def delete(task_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    deleted = tasks_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(404, "Task not found")
    return {"message": "Deleted"}