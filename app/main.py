from fastapi import FastAPI
from app.routers import course, enrollment, student

app = FastAPI()

app.include_router(course.router)
app.include_router(enrollment.router)
app.include_router(student.router)
