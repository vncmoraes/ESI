from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import engine, SessionLocal, Base

Base.metadata.create_all(engine)  # Realiza a criação das tabelas presentes no módulo "orms.py"
api = FastAPI()  # Cria instância da biblioteca FastAPI


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.post("/teachers/create/", response_model=schemas.Person)
def create_teacher(teacher: schemas.CreatePerson, db: Session = Depends(get_db)):
    return crud.create_person(db, teacher, "PROFESSOR")


@api.get("/teachers/", response_model=List[schemas.Person])
def get_teachers(db: Session = Depends(get_db)):
    teachers = crud.get_persons_by_occupation(db, occupation="PROFESSOR")
    return teachers


@api.get("/teachers/{number_usp}", response_model=schemas.Person)
def get_teacher_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    teacher = crud.get_person_by_number_usp_and_occupation(db, number_usp, "PROFESSOR")
    if teacher is None:
        raise HTTPException(status_code=400, detail=f"nenhum PROFESSOR com numero usp: {number_usp} foi encontrado")
    return teacher


@api.post("/students/create/", response_model=schemas.Person)
def create_student(student: schemas.CreatePerson, db: Session = Depends(get_db)):
    return crud.create_person(db, student, "ALUNO")


@api.get("/students/", response_model=List[schemas.Person])
def get_students(db: Session = Depends(get_db)):
    students = crud.get_persons_by_occupation(db, occupation="ALUNO")
    return students


@api.get("/students/{number_usp}", response_model=schemas.Person)
def get_student_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    student = crud.get_person_by_number_usp_and_occupation(db, number_usp, "ALUNO")
    if student is None:
        raise HTTPException(status_code=400, detail=f"nenhum ALUNO com numero usp: {number_usp} foi encontrado")
    return student


@api.get("/persons/", response_model=List[schemas.Person])
def get_persons(db: Session = Depends(get_db)):
    persons = crud.get_persons(db)
    return persons


@api.delete("/persons/{number_usp}", response_model=schemas.Person)
def delete_person_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    return crud.delete_person_by_number_usp(db, number_usp)


@api.get("/persons/{number_usp}", response_model=schemas.Person)
def get_person_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    person = crud.get_person_by_number_usp(db, number_usp)
    return person


@api.post("/coordination/add/{number_usp}", response_model=schemas.Person)
def add_teacher_to_coordination(number_usp: str, db: Session = Depends(get_db)):
    return crud.add_teacher_to_coordination(number_usp, db)


@api.post("/coordination/remove/{number_usp}", response_model=schemas.Person)
def remove_teacher_from_coordination(number_usp: str, db: Session = Depends(get_db)):
    return crud.remove_teacher_from_coordination(number_usp, db)
