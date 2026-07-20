from .. import crud, schemas
from ..database import SessionLocal
from datetime import datetime

def create_task(task: schemas.TaskCreate):
    db: Session = SessionLocal()
    return crud.create_task(db, task)

def get_tasks):
    db: Session = SessionLocal()
    return crud.get_tasks(db)

def update_task(task_id: int, task: schemas.TaskUpdate):
    db: Session = SessionLocal()
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(404, "Task not found")
    return updated

def delete_task(task_id: int):
    db: Session = SessionLocal()
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(404, "Task not found")
    return {"message": "Deleted"}

def get_overdue_tasks():
    db: Session = SessionLocal()
    overdue_tasks = db.query(Task).filter(Task.due_date < datetime.now()).all()
    return overdue_tasks