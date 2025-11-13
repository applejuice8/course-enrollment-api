from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate

def create_enrollment(db: Session, enrollment: EnrollmentCreate):
    db_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_enrollment(db: Session, student_id: int = None, course_id: int = None):
    if student_id and course_id:
        db_enrollment = db.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    elif student_id:
        db_enrollment = db.query(Enrollment).filter_by(student_id=student_id).all()
    elif course_id:
        db_enrollment = db.query(Enrollment).filter_by(course_id=course_id).all()
    else:
        db_enrollment = db.query(Enrollment).all()

    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    return db_enrollment

def delete_enrollment(db: Session, enrollment_id: int):
    db_enrollment = db.query(Enrollment).filter_by(id=enrollment_id).first()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    db.delete(db_enrollment)
    db.commit()
