from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./database/app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

table_check = inspect(engine)

def delete_metadata():
    Base.metadata.drop_all(bind=engine)     #type: ignore
    
def check_metadata():
    if table_check.has_table('Student'):
        pass
    else:
        Base.metadata.create_all(bind=engine)    #type: ignore