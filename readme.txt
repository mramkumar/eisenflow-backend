# EisenFlow — Backend

EisenFlow is a productivity-focused task management app inspired by the Eisenhower Matrix. This backend, built with **FastAPI**, powers the core APIs for task handling, user authentication, and more.

## ⚙️ Features

- 🧠 **Task API** — Create, update, and manage tasks within quadrants
- 🔐 **JWT Authentication** — Secure login and token-based auth
- 👥 **User Management** — Register, login, and manage user profiles
- 🗓️ **Due Dates & Reminders** — Support for task deadlines
- 📊 **Status Management** — Open/Closed status via reference table
- 🌐 **CORS & API versioning** — Ready for modern frontend integrations

## 🛠️ Tech Stack

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy** / **Tortoise ORM**
- **PostgreSQL** (or SQLite for local dev)
- **Pydantic**
- **JWT** for authentication
- **Alembic** (if using SQLAlchemy for migrations)
- **Uvicorn** for ASGI server
