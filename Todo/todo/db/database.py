from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from ellar.core import Config

# SQLALCHEMY_URL = "postgresql://postgres:140498@localhost/todo"

def get_engine(config: Config):
    engine = create_engine(config.DATABASE_URL)
    return engine

def get_session_maker(config: Config):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine(config))
    return SessionLocal


Base = declarative_base()