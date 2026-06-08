from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# database.py is where we will set up our database connection and create a session. We will use SQLAlchemy for this purpose.

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
	# Fallback to a local SQLite file when DATABASE_URL is not set
	DATABASE_URL = "sqlite:///./test.db"
	engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
	engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()