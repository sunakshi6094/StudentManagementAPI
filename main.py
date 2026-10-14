
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Student Management API",
    description="A REST API to manage student records",
    version="1.0.0"
)


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=2, max_length=100)
    email: EmailStr


students = {}
next_id = 1


@app.get("/")
def home():
    return {"message": "Student Management API is running!"}


@app.post("/students", status_code=201)
def create_student(student: Student):
    global next_id

    for existing in students.values():
        if existing["email"].lower() == str(student.email).lower():
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists"
            )

    student_id = next_id
    students[student_id] = {
        "id": student_id,
        **student.model_dump(mode="json")
    }
    next_id += 1

    return students[student_id]


@app.get("/students")
def get_students():
    return list(students.values())


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    for existing_id, existing in students.items():
        if (
            existing_id != student_id
            and existing["email"].lower() == str(student.email).lower()
        ):
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists"
            )

    students[student_id] = {
        "id": student_id,
        **student.model_dump(mode="json")
    }

    return students[student_id]


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
