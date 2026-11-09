
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    id: int
    name: str
    marks: float

students = {}

# POST - Add student
@app.post("/students")
def add(s: student):
    if s.id in students:
        raise HTTPException(400, "Student already exists")
    students[s.id] = s
    return s

# GET - Get all students
@app.get("/students")
def getall():
    return list(students.values())

# GET - Get one student
@app.get("/students/{id}")
def getone(id: int):
    if id not in students:
        raise HTTPException(404, "Student not found")
    return students[id]

# PUT - Update student
@app.put("/students/{id}")
def update(id: int, s: student):
    if id not in students:
        raise HTTPException(404, "Student not found")
    if s.id != id:
        raise HTTPException(400, "ID Mismatch")

    students[id] = s
    return s

# DELETE - Delete student
@app.delete("/students/{id}")
def delete(id: int):
    if id not in students:
        raise HTTPException(404, "Student not found")

    del students[id]
    return {"message": "Student data deleted"}
