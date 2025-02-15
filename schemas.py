from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Task
class TaskBase(BaseModel):
    title: str
    description: str = ""
    priority: int = 1
    status: Optional[int] = 1
    assignee: int


class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_date: datetime

    class Config:
        from_attributes = True

# User
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    status: Optional[int] = 3

class UserResponse(UserBase):
    id: int
    status: int
    class Config:
        from_attributes = True

# Status
class StatusBase(BaseModel):
    status: str

class StatusCreate(StatusBase):
    pass

class StatusResponse(StatusBase):
    id: int
    status: str
    class Config:
        from_attributes = True