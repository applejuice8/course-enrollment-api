from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseGet, CourseUpdate
from app.services import course_service
from app.dependencies import get_db

router = APIRouter(prefix='/courses', tags=['courses'])

# Custom validation
def validate_course_id(
    course_id: int = Path(..., gt=0, description='Course ID must be positive')
):
    return course_id

# Create
@router.post('/', response_model=CourseGet)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return course_service.create_course(db, course)

# Read
@router.get('/', response_model=list[CourseGet])
def get_courses(db: Session = Depends(get_db)):
    return course_service.get_course(db)

@router.get('/{course_id}', response_model=CourseGet)
def get_course(
    course_id: int = Depends(validate_course_id),
    db: Session = Depends(get_db)
):
    return course_service.get_course(db, course_id)

# Update
@router.patch('/{course_id}', response_model=CourseGet)
def update_course(
    course: CourseUpdate,
    course_id: int = Depends(validate_course_id),
    db: Session = Depends(get_db)
):
    return course_service.update_course(db, course_id, course)

# Delete
@router.delete('/{course_id}', status_code=204)
def delete_course(
    course_id: int = Depends(validate_course_id),
    db: Session = Depends(get_db)
):
    course_service.delete_course(db, course_id)
