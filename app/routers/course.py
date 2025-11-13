from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseGet, CourseUpdate
from app.services import course_service
from app.dependencies import get_db

router = APIRouter(prefix='/courses', tags=['courses'])

# Create
@router.post('/', response_model=CourseGet)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return course_service.create_course(db=db, course=course)

# Read
@router.get('/', response_model=CourseGet)
def get_course(db: Session = Depends(get_db)):
    return course_service.get_course(db=db)

@router.get('/{course_id}', response_model=CourseGet)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return course_service.get_course(db=db, course_id=course_id)

# Update
@router.patch('/{course_id}', response_model=CourseGet)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    return course_service.update_course(db=db, course_id=course_id, course=course)

# Delete
@router.delete('/{course_id}')
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course_service.
