from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import date
from database import engine, get_db, Base
import crud
import schemas


app = FastAPI()

origins = [
    "http://192.168.106.101:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database table
Base.metadata.create_all(bind=engine)

@app.post("/task", response_model=schemas.TaskResponse)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db), assigned_date: date = Query(None, description="Date in YYYY-MM-DD format")):
    return crud.get_tasks(db, assigned_date)

@app.get("/task/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/task/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/task/{task_id}", response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_users(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.post("/user", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/status", response_model=schemas.StatusResponse)
def create_status(status: schemas.StatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db, status)

@app.get("/quadrants", response_model=list[schemas.QuadrantResponse])
def get_quadrants(db: Session = Depends(get_db)):
    return crud.get_quadrants(db)