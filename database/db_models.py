from sqlalchemy import (Column,
                        Integer,
                        String,
                        text,
                        Date)
from database.database import Base

class UserStudent(Base):
    __tablename__ = 'Student'
    
    id = Column(Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
                server_default="10000")
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    password =Column(String, nullable = False)
    birth_date = Column(Date, nullable = False) 
    profile_image_url = Column(String, nullable = True)
    created_date = Column(Date, nullable = False)  
    last_login = Column(Date, nullable = False) 