from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 


DB_PASSWORD = os.getenv("DB_PASSWORD", "")

DATABASE_URL = "mysql://eisenflowadmin:{DB_PASSWORD}@localhost/eisenflow"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
