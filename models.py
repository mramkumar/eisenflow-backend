from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, Date, Interval
from sqlalchemy.sql import func, expression
from database import Base

# Task model
class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text,nullable=True)
    created_date = Column(DateTime, server_default=func.now())
    assigned_date = Column(Date, nullable=True)
    priority = Column(Integer, ForeignKey('quadrant_priority.id'), nullable=False)
    assignee = Column(Integer, ForeignKey('users.id'),  nullable=False)
    status = Column(Integer, ForeignKey('status.id'),  server_default=expression.text('1')) # default: Open
    duration = Column(Interval, nullable=True)

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    status = Column(Integer, ForeignKey('status.id'), server_default=expression.text('3'))  # default: Enabled

# Status model
class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(20), unique=True, index=True)

# Priority model
class Quadrant_priority(Base):
    __tablename__ = "quadrant_priority"
    id = Column(Integer, primary_key=True, index=True)
    priority_name = Column(String(40), unique=True, index=True)