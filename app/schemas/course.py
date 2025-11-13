from pydantic import BaseModel

class CourseCreate(BaseModel):
    code: str
    name: str
    credit_hours: int

class CourseGet(BaseModel):
    id: int
    code: str
    name: str
    credit_hours: int

    class Config:
        orm_mode = True

class CourseUpdate(BaseModel):
    code: str | None = None
    name: str | None = None
    credit_hours: int | None = None
