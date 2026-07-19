from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create(task: schemas.TaskCreate):
    db: Session = SessionLocal()
    return crud.create_task(db, task)


@router.get("/")
def list_tasks():
    db: Session = SessionLocal()
    return crud.get_tasks(db)


@router.put("/{task_id}")
def update(task_id: int, task: schemas.TaskUpdate):
    db: Session = SessionLocal()

    updated = crud.update_task(db, task_id, task)

    if not updated:
        raise HTTPException(404, "Task not found")

    return updated


@router.delete("/{task_id}")
def delete(task_id: int):
    db: Session = SessionLocal()

    deleted = crud.delete_task(db, task_id)

    if not deleted:
        raise HTTPException(404, "Task not found")

    return {"message": "Deleted"}