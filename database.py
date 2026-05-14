from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Professional practice: Use Environment Variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://dev_user:dev_password@localhost:5432/intelligence_db")

# Create the Engine with a Connection Pool
engine = create_engine(
    DATABASE_URL,
    pool_size=5,        # Keeps 5 connections ready
    max_overflow=10,    # Can open up to 10 more if needed
    pool_pre_ping=True  # Checks if connection is alive before using
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
