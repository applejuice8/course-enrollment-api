from http.client import HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_pw
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        age=student.age,
        password=hash_pw(student.password)
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int = None):
    if student_id:
        db_student = db.query(Student).filter_by(id=student_id).first()
        if not db_student:
            raise HTTPException(status_code=404, detail='Student not found')
        return db_student
    return db.query(Student).all()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter_by(id=student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')

    if student.name is not None:
        db_student.name = student.name
    if student.age is not None:
        db_student.age = student.age
    if student.password is not None:
        db_student.password = hash_pw(student.password)

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter_by(id=student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    db.delete(db_student)
    db.commit()
