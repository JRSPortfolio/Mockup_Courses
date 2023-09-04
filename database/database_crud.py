from sqlalchemy import update
from data import models
from database.db_models import UserStudent
from database.database import SessionLocal, check_metadata
import datetime
        
DB_SESSION = SessionLocal()

def create_db_student(student: models.Student):
    db_student = UserStudent(name = student.name,
                             email = student.email,
                             password = student.password,
                             birth_date = student.birth_date,
                             profile_image_url = student.profile_image_url,
                             created_date = student.created_date,
                             last_login = student.last_login)
    check_metadata()
    DB_SESSION.add(db_student)
    DB_SESSION.commit()
    DB_SESSION.refresh(db_student)
    
def get_db_student_by_email(email: str):
    check_metadata()
    return DB_SESSION.query(UserStudent).filter(UserStudent.email == email).first()

def get_db_student_by_id(id):
    check_metadata()
    return DB_SESSION.query(UserStudent).filter(UserStudent.id == id).first()

def get_db_student_id(email: str):
    check_metadata()
    return DB_SESSION.query(UserStudent.id).filter(UserStudent.email == email).first()

def update_db_student_email(email: str, student):
    update_email = update(UserStudent).where(UserStudent.id == student.id).values(email = email)
    DB_SESSION.execute(update_email)
    DB_SESSION.commit()
    
def update_db_student_password(password: str, student):
    update_password = update(UserStudent).where(UserStudent.id == student.id).values(password = password)
    DB_SESSION.execute(update_password)
    DB_SESSION.commit()
    
def update_last_login(student):
    l_login_date = datetime.datetime.now()
    update_l_login = update(UserStudent).where(UserStudent.id == student.id).values(last_login = l_login_date.date())
    DB_SESSION.execute(update_l_login)
    DB_SESSION.commit()