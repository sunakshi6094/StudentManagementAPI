
import pytest
from fastapi.testclient import TestClient
from main import app, students
import main

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_students():
    students.clear()
    main.next_id = 1


def sample_student():
    return {
        "name": "Aarav Patil",
        "age": 21,
        "course": "Computer Engineering",
        "email": "aarav@example.com"
    }


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == (
        "Student Management API is running!"
    )


def test_create_student():
    response = client.post(
        "/students",
        json=sample_student()
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Aarav Patil"
    assert response.json()["id"] == 1


def test_get_all_students():
    client.post("/students", json=sample_student())

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_single_student():
    client.post("/students", json=sample_student())

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json()["email"] == "aarav@example.com"


def test_student_not_found():
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


def test_duplicate_email():
    client.post("/students", json=sample_student())

    duplicate = sample_student()
    duplicate["name"] = "Riya Patil"

    response = client.post("/students", json=duplicate)

    assert response.status_code == 409


def test_invalid_student_age():
    student = sample_student()
    student["age"] = -5

    response = client.post("/students", json=student)

    assert response.status_code == 422


def test_update_student():
    client.post("/students", json=sample_student())

    updated = sample_student()
    updated["name"] = "Aarav Sharma"

    response = client.put("/students/1", json=updated)

    assert response.status_code == 200
    assert response.json()["name"] == "Aarav Sharma"


def test_delete_student():
    client.post("/students", json=sample_student())

    response = client.delete("/students/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"
    assert client.get("/students/1").status_code == 404
