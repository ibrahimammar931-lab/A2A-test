from sqlalchemy.orm import Session

from .models import User, Task


def create_user(db: Session, user):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db):
    return db.query(User).all()


def create_task(db, task):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db):
    return db.query(Task).all()


def update_task(db, task_id, update):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    for key, value in update.model_dump(exclude_none=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(db, task_id):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return False

    db.delete(task)
    db.commit()

    return True