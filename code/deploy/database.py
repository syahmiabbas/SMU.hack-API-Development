import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# Database Setup
# SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL','sqlite+pysqlite:///./db.sqlite3:') # For MAC
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./db.sqlite3')  # For Windows
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

# Initialize Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Construct Base Class
Base = declarative_base()