# Course Enrollment

## Run the Code

```bash
uvicorn app.main:app --reload
```

## Project Structure

```
course-enrollment/
├── app/
│   ├── core/
│   │   ├── config.py           # Config variables (DB URL, secrets)
│   │   └── security.py         # Authentication, password hashing, JWT utilities
│   ├── db/                     # Database connection and session management
│   │   ├── database.db
│   │   └── database.py         # Engine and SessionLocal creation
│   ├── models/                 # SQLAlchemy ORM table models
│   │   ├── course.py
│   │   ├── enrollment.py
│   │   └── student.py
│   ├── routers/                # API endpoints for CRUD operations for each entity
│   │   ├── course.py
│   │   ├── enrollment.py
│   │   └── student.py
│   ├── schemas/                # Pydantic models for validation & serialization
│   │   ├── course.py
│   │   ├── enrollment.py
│   │   └── student.py
│   ├── services/               # Business logic / CRUD operations
│   │   ├── student_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   ├── dependencies.py         # FastAPI dependencies (get_db)
│   └── main.py                 # FastAPI app instance and router registration
├── tests/                      # Unit and integration tests
│   ├── test_course.py
│   ├── test_enrollment.py
│   ├── test_main.py
│   └── test_student.py
├── .env
├── .gitignore
├── fast_commit.bash
├── README.md
└── requirements.txt
```

## Notes

* **Models vs Schemas:** Models define how data is stored in the database; schemas define how data is received/sent via API.
* **Routers vs Services:** Routers handle HTTP requests; services handle business logic and database interactions.

## Architecture Flow

```
Client Request
        │
        ▼
Routers (FastAPI endpoints)
        │
        ▼
Services (CRUD & business logic)
        │
        ▼
Models (SQLAlchemy ORM)
        │
        ▼
Database (SQLite or other databases)
```

* Clients sends requests to the API endpoints defined in **routers**.
* **Routers** validate input using **schemas** and call **services**.
* **Services** manipulate data via **models** and database sessions.
