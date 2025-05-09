from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from app.models import Base  # import the models

load_dotenv()
DATABASE_URL = os.getenv("MYSQL_URI")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create all tables if they don't exist
    Base.metadata.create_all(bind=engine)
