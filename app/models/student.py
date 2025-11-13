from sqlalchemy import Integer, String
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .enrollment import Enrollment

class Student(Base):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer(3), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    enrollments: Mapped[list['Enrollment']] = relationship('Enrollment', back_populates='student')

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name}, age={self.age})>'
