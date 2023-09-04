from decimal import Decimal as dec
from typing import List
from data.models import Course

def course_count():
    return 99

def most_popular_courses(count: int):
    return [
        Course(id = 1,
               category = "Hotelaria e Turismo",
               price = dec(179),
               name = "Gestor Turistico",
               summary = "Um sumário do curso aqui",
               description = "A descrição do curso vêm aqui",
               trainer_id = 1,
               trainer_name = "Osmar",
               schedule = "Segundas e Quintas, 17h ás 20h",
               available_seats = 40),
        Course(id = 2,
               category = "Programação em C++",
               price = dec(250),
               name = "Estruturas de Dados em C++",
               summary = "Um sumário do curso aqui",
               description = "A descrição do curso vêm aqui",
               trainer_id = 4,
               trainer_name = "Bernardo",
               schedule = "Terças e Quartas, 17h:30 ás 20h:30",
               available_seats = 20),
        Course(id = 3,
               category = "Natação",
               price = dec(250),
               name = "Estilo Borboleta",
               summary = "Um sumário do curso aqui",
               description = "A descrição do curso vêm aqui",
               trainer_id = 2,
               trainer_name = "Alberta",
               schedule = "Terças e Sextas, 10h ás 13h",
               available_seats = 16),
        
    ][:count]
    
def available_courses(count: int):
    return [Course(id = 5,
                   category = 'Programação Web',
                   price = dec(190),
                   name = 'Desenvolvimento de Websites',
                   summary = 'Sumario do curso',
                   description = "A descrição do curso vêm aqui",
                   trainer_id = 1,
                   trainer_name = 'Osmar',
                   schedule = "Terças e Sextas, 10h ás 13h",
                   available_seats = 16),
            Course(id = 6,
                   category = 'Marketing',
                   price = dec(250),
                   name = 'SEO - Optimizações Motores de Busca',
                   summary = 'Sumario de curso',
                   description = "A descrição do curso vêm aqui",
                   trainer_id = 4,
                   trainer_name = 'Bernardo',
                   schedule = "Terças e Quartas, 17h:30 ás 20h:30",
                   available_seats = 20),
            Course(id = 7,
                   category = 'Programação',
                   price = dec(250),
                   name = 'Programação de Device Drivers',
                   summary = 'Sumario de curso',
                   description = "A descrição do curso vêm aqui",
                   trainer_id = 2,
                   trainer_name = 'Alberta',
                   schedule = "Segundas e Quintas, 17h ás 20h",
                   available_seats = 40),
            Course(id = 8,
                   category = 'Electrónica',
                   price = dec(280),
                   name = 'Microsoldadura de SMD',
                   summary = 'Sumario de curso',
                   description = "A descrição do curso vêm aqui",
                   trainer_id = 6,
                   trainer_name = 'Roberta',
                   schedule = "Terças e Quartas, 17h:30 ás 20h:30",
                   available_seats = 20)][:count]
    
def get_course_by_id(course_id: int) -> Course | None:
    courses = available_courses(1500)
    for course in courses:
        if course.id == course_id:
            return course
    return None
