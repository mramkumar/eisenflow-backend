from sqlalchemy.orm import Session
from models import Task, User, Status
from schemas import TaskCreate, TaskResponse, UserCreate, StatusCreate


def create_task(db: Session, task: TaskCreate):
    new_task = Task(title=task.title, description = task.description, priority = task.priority, assignee = task.assignee, status = task.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_data: TaskCreate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task: 
        task.title = task_data.title
        task.description = task_data.description
        task.assignee = task_data.assignee
        task.status = task_data.status
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
    