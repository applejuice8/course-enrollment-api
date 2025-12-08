from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate, StudentGet, StudentUpdate
from app.services import student_service
from app.dependencies import get_db

router = APIRouter(prefix='/students', tags=['students'])

# Custom validation
def validate_student_id(
    student_id: int = Path(
        ...,
        gt=0,
        description='Student ID must be positive'
    )
) -> int:
    return student_id

# Create
@router.post('/', response_model=StudentGet)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, student)

# Read
@router.get('/', response_model=list[StudentGet])
def get_students(db: Session = Depends(get_db)):
    return student_service.get_student(db)

@router.get('/{student_id}', response_model=StudentGet)
def get_student(
    student_id: int = Depends(validate_student_id),
    db: Session = Depends(get_db)
):
    return student_service.get_student(db, student_id)

# Update
@router.patch('/{student_id}', response_model=StudentGet)
def update_student(
    student: StudentUpdate,
    student_id: int = Depends(validate_student_id),
    db: Session = Depends(get_db)
):
    return student_service.update_student(db, student_id, student)

# Delete
@router.delete('/{student_id}', status_code=204)
def delete_student(
    student_id: int = Depends(validate_student_id),
    db: Session = Depends(get_db)
):
    student_service.delete_student(db, student_id)
