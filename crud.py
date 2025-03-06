from sqlalchemy.orm import Session
from datetime import date 
from models import Task, User, Status, Quadrant_priority
from schemas import TaskCreate, TaskUpdate, UserCreate, StatusCreate


def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        title=task.title, 
        description = task.description, 
        priority = task.priority, 
        assignee = task.assignee,
        assigned_date =  task.assigned_date, 
        status = task.status,
        duration=task.duration)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session, assigned_date):
    return db.query(Task).filter(Task.assigned_date == assigned_date).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task: 
        task_data_dict = task_data.model_dump(exclude_unset=True)
        for key, value in task_data_dict.items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
        
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()
    return task

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, status=user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_status(db: Session, status: StatusCreate):
    db_status = Status(status=status.status)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_quadrants(db: Session):
    return db.query(Quadrant_priority).all()