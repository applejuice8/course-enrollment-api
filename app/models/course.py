from sqlalchemy import Integer, String
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .enrollment import Enrollment

class Course(Base):
    __tablename__ = 'course'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    credit_hours: Mapped[int] = mapped_column(Integer(2), nullable=False)

    enrollments: Mapped[list['Enrollment']] = relationship('Enrollment', back_populates='course')

    def __repr__(self):
        return f'<Course(id={self.id}, code={self.code}, name={self.name}, credit_hours={self.credit_hours})>'
