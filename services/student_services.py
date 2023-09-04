from data.models import Testimonial, Student
from datetime import date
from database import database_crud as db_c


def student_count():
    return 2315

def create_account(name: str,
                   email: str,
                   password: str,
                   birth_date: date):
    
    if db_c.get_db_student_by_email(email):
        raise ValueError(f"Utilizador com email {email} já se encontra registado.")
    student = Student(name = name,
                      email = email,
                      password = hash_password(password),
                      birth_date = birth_date)
    db_c.create_db_student(student)
    return student

def authenticate_student_by_email(email: str, password: str):
    if student := db_c.get_db_student_by_email(email):
        if hash_password(password) == student.password:
            return student
    return None

def confirm_student_password(password: str, student):
    if student.password == password:
       return True 
    else:
        return False
    
def match_new_password(password1: str, password2: str):
    if password1 == password2:
        return True
    else:
        return False

def get_testimonials(count: int):
    return[Testimonial(user_id = 239,
                       user_name = 'Saul Goodman',
                       user_occupation = 'CEO & Founder',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1001,
                       user_name = 'Sara Wilson',
                       user_occupation = 'Designer',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 704,
                       user_name = 'Jena Karlis',
                       user_occupation = 'Store Owner',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1002,
                       user_name = 'Matt Brandon',
                       user_occupation = 'Freelancer',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1589,
                       user_name = 'John Larson',
                       user_occupation = 'Entrepreneur',
                       text = 'Algum texto de testemunho')]

def hash_password(password: str):
    return password + '-hashpw'