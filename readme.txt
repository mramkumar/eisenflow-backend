
# starting webserver
uvicorn main:app --reload

# database migration
alembic revision --autogenerate -m "Add created_date and assignee to Task"
alembic upgrade head

