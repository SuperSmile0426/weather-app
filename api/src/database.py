from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import settings

DATABASE_USER = settings.DATABASE_USER
DATABASE_PASSWORD = settings.DATABASE_PASSWORD
DATABASE_DB = settings.DATABASE_DB

engine = create_engine("postgresql://"+DATABASE_USER+":"+DATABASE_PASSWORD+"@postgres:5432/"+DATABASE_DB)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
