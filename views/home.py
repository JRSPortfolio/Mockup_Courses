from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter
from starlette.requests import Request
from infrastructure.viewmodel import ViewModel
from services import (course_services,
                      student_services,
                      trainer_services)

router = APIRouter()

POPULAR_COURSES_COUNT = 3
SELECTED_TRAINERS_COUNT = 3
TESTIMONIAL_COUNT = 5

@router.get('/')
@template()
async def index():
    return index_viewmodel()
    
def index_viewmodel():
    return ViewModel(num_courses = course_services.course_count(),
                     num_students = student_services.student_count(),
                     num_trainers = trainer_services.trainer_count(),
                     num_events = 159,
                     popular_courses = course_services.most_popular_courses(POPULAR_COURSES_COUNT),
                     selected_trainers = trainer_services.selected_trainers(SELECTED_TRAINERS_COUNT))

@router.get('/about')
@template()
async def about(request: Request):
    return about_viewmodel()

def about_viewmodel():
     return ViewModel(num_courses = course_services.course_count(),
                      num_students = student_services.student_count(),
                      num_trainers = trainer_services.trainer_count(),
                      num_events = 159,
                      testimonials = student_services.get_testimonials(TESTIMONIAL_COUNT))