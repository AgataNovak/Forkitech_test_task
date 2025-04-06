from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import Base

engine = create_engine("sqlite:///tron.db")
Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()