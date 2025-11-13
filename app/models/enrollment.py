from sqlalchemy import ForeignKey, DateTime, PrimaryKeyConstraint
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Enrollment(Base):
    __tablename__ = 'enrollment'

    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'), primary_key=True)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    student: Mapped[int] = relationship('Student', back_populates='enrollments')
    course: Mapped[int] = relationship('Course', back_populates='enrollments')

    def __repr__(self):
        return f'<Enrollment(student_id={self.student_id}, course_id={self.course_id}, date={self.date})>'
