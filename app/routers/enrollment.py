from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.enrollment import EnrollmentCreate, EnrollmentGet
from app.services import enrollment_service
from app.dependencies import get_db

router = APIRouter(prefix='/enrollments', tags=['enrollments'])

# Create
@router.post('/', response_model=EnrollmentGet)
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    return enrollment_service.create_enrollment(db, enrollment)

# Read
@router.get('/', response_model=list[EnrollmentGet])
def get_enrollments(db: Session = Depends(get_db)):
    return enrollment_service.get_enrollment(db)

@router.get('/{enrollment_id}', response_model=EnrollmentGet)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    return enrollment_service.get_enrollment(db, enrollment_id)

# Delete
@router.delete('/{enrollment_id}', status_code=204)
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment_service.delete_enrollment(db, enrollment_id)
