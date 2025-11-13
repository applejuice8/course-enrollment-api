from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int

class StudentRead(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None
    password: str | None = None
