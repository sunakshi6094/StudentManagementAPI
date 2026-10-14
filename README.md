
# Student Management API

A REST API built using Python and FastAPI to manage student records.

## Features

- Create a new student
- View all students
- View a student by ID
- Update student information
- Delete a student
- Validate student details and email addresses
- Handle duplicate email addresses
- Return appropriate HTTP error responses
- Automated tests using Pytest

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- HTTPX

## Project Structure

```text
StudentManagementAPI/
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
└── venv/
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Run Automated Tests

```bash
pytest -v
```

The test suite checks student creation, retrieval, updates, deletion,
input validation, duplicate emails, and error handling.

## Storage

Student records are stored in memory. Data resets when the application
restarts. A database can be added in a future version.

## Purpose

This project demonstrates REST API development, input validation,
error handling, and automated testing using Python.
