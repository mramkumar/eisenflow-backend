import crud
import os
import schemas
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from sqlalchemy.orm import Session
from datetime import date, datetime
from database import engine, get_db, Base

app = FastAPI()

# origins = os.getenv("ALLOWED_ORIGINS").split(",")

origins = ['*']
# Load Google OAuth credentials from environment variables
# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

# Secret key for session encryption
SECRET_KEY = "your-very-secure-secret-key"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

GOOGLE_CLIENT_ID = "913592494800-o4eg6tpse1oo1bt5dhapko4d7nh4sh85.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_REDIRECT_URI = "http://eisenflow.com:8000/auth/callback"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth Configuration
oauth = OAuth()
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    access_token_url="https://oauth2.googleapis.com/token",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/auth/login")
async def login(request: Request):
    return await oauth.google.authorize_redirect(request, GOOGLE_REDIRECT_URI)

@app.get("/auth/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)

    if not user_info:
        raise HTTPException(status_code=400, detail="Invalid token")

    return {
        "email": user_info["email"],
        "name": user_info["name"],
        "picture": user_info["picture"],
        "access_token": token["access_token"]
    }

# create database table
Base.metadata.create_all(bind=engine)

@app.post("/task", response_model=schemas.TaskResponse)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db), start_date: datetime = Query(..., description="Start date in YYYY-MM-DD format"), end_date: datetime = Query(..., description="End date in YYYY-MM-DD format")):
    return crud.get_tasks(db, start_date, end_date)

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

@app.patch("/task/{task_id}", response_model=schemas.TaskResponse)
def partially_update_task(task_id: int, task: schemas.TaskPartialUpdate, db: Session = Depends(get_db)):
    task = crud.partially_update_task(db, task_id, task)
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