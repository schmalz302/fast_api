from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from models import *

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
    # echo=True,
    # pool_size=5,
    # max_overflow=10,
)

Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()