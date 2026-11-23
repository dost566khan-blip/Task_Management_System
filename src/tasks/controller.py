from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel

def create_task(body: TaskSchema, db: Session):
    new_task = TaskModel(**body.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks

def get_one_task(task_id: int, db: Session):
    task = db.get(TaskModel, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID is incorrect")
    return task

def update_task(body: TaskSchema, task_id: int, db: Session):
    task = db.get(TaskModel, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID is incorrect")

    for field, value in body.model_dump().items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id: int, db: Session):
    task = db.get(TaskModel, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID is incorrect")
    db.delete(task)
    db.commit()