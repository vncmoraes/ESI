from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
from database import engine, SessionLocal, Base
from schemas import SemiAnnualReportSchema, CreateSemiAnnualReportSchema, \
    StudentSchema, CreateStudentSchema, OrientatorSchema, CreateOrientatorSchema, CreateCoordinatorSchema, \
    CoordinatorSchema

Base.metadata.create_all(engine)  # Realiza a criação das tabelas presentes no módulo "orms.py"
api = FastAPI()  # Cria instância da biblioteca FastAPI


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @api.get("/persons/", response_model=List[PersonSchema])
# def get_persons(db: Session = Depends(get_db)):
#     persons = crud.get_persons(db)
#     return persons
#
#
# @api.delete("/persons/{number_usp}", response_model=PersonSchema)
# def delete_person_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
#     return crud.delete_person_by_number_usp(db, number_usp)



@api.post("/orientators/create/", response_model=OrientatorSchema)
def create_orientator(orientator: CreateOrientatorSchema, db: Session = Depends(get_db)):
    return crud.create_orientator(db, orientator)


@api.get("/orientators/", response_model=List[OrientatorSchema])
def get_orientators(db: Session = Depends(get_db)):
    orientators = crud.create_query_builder(db, models.Orientator).all()
    return orientators


@api.get("/orientators/{number_usp}", response_model=OrientatorSchema)
def get_orientator_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    orientator = crud.create_query_builder(db, models.Orientator, number_usp=number_usp).first()
    if orientator is None:
        raise HTTPException(status_code=400, detail=f"nenhum ORIENTADOR com numero usp: {number_usp} foi encontrado")
    return orientator


@api.post("/students/create/", response_model=StudentSchema)
def create_student(student: CreateStudentSchema, db: Session = Depends(get_db)):
    db_student = crud.create_student(db, student)
    if student.orientator_nusp:
        db_student = crud.set_student_orientator(db, db_student, student.orientator_nusp)
    return db_student


@api.get("/students/", response_model=List[StudentSchema])
def get_students(db: Session = Depends(get_db)):
    students = crud.create_query_builder(db, models.Student).all()
    return students


@api.get("/students/{number_usp}", response_model=StudentSchema)
def get_student_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    student = crud.create_query_builder(db, models.Student, number_usp=number_usp).first()
    if student is None:
        raise HTTPException(status_code=400, detail=f"nenhum ALUNO com numero usp: {number_usp} foi encontrado")
    return student


@api.post("/coordinators/create/", response_model=CoordinatorSchema)
def create_coordinator(coordinator: CreateCoordinatorSchema, db: Session = Depends(get_db)):
    return crud.create_coordinator(db, coordinator)


@api.get("/coordinators/", response_model=List[CoordinatorSchema])
def get_coordinators(db: Session = Depends(get_db)):
    coordinators = crud.create_query_builder(db, models.Coordinator).all()
    return coordinators


@api.get("/coordinators/{number_usp}/", response_model=CoordinatorSchema)
def get_coordinator_by_number_usp(number_usp: str, db: Session = Depends(get_db)):
    coordinator = crud.create_query_builder(db, models.Coordinator, number_usp=number_usp).first()
    if coordinator is None:
        raise HTTPException(status_code=400, detail=f"nenhum COORDENADOR com numero usp: {number_usp} foi encontrado")
    return coordinator


@api.post("/reports/create/", response_model=SemiAnnualReportSchema)
def create_semi_annual_report(report: CreateSemiAnnualReportSchema, db: Session = Depends(get_db)):
    return crud.create_semi_annual_report(db, report)
