from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter
from services import course_services
from infrastructure.viewmodel import ViewModel

router = APIRouter()

AVAILABLE_COURSES = 5

@router.get('/courses')
@template()
async def courses():
    return courses_viewmodel()

def courses_viewmodel():
    return ViewModel(available_courses = course_services.available_courses(AVAILABLE_COURSES))

@router.get('/courses/{course_id}')
@template()
async def course_details(course_id: int):
    return course_details_viewmodel(course_id)

def course_details_viewmodel(course_id: int):
    if course := course_services.get_course_by_id(course_id):
        return ViewModel(course = course)
    return ViewModel(error = True,
                     error_msg = 'Course not found')