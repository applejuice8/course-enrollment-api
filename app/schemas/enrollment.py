from pydantic import BaseModel
from datetime import datetime

# Don't allow users to set or change date
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentGet(BaseModel):
    student_id: int
    course_id: int
    date: datetime

    class Config:
        orm_mode = True
