from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate

def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        code=course.code,
        name=course.name,
        credit_hours=course.credit_hours
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int = None):
    if course_id:
        db_course = db.query(Course).filter_by(id=course_id).first()
        if not db_course:
            raise HTTPException(status_code=404, detail='Course not found')
        return db_course
    return db.query(Course).all()

def update_course(db: Session, course_id: int, course: CourseUpdate):
    db_course = db.query(Course).filter_by(id=course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')

    if course.code is not None:
        db_course.code = course.code
    if course.name is not None:
        db_course.name = course.name
    if course.credit_hours is not None:
        db_course.credit_hours = course.credit_hours

    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter_by(id=course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    db.delete(db_course)
    db.commit()
