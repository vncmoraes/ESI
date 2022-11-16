from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
from schemas import CreatePersonSchema, CreateSemiAnnualReportSchema, CreateStudentSchema, CreateOrientatorSchema, \
    CreateCoordinatorSchema


def create_orientator(db: Session, orientator: CreateOrientatorSchema):
    if exist_person_with_email_or_number_usp(db, orientator.email_usp, orientator.number_usp):
        raise HTTPException(status_code=400, detail="Email e/ou Numero USP já registrados")

    db_orientator = models.Orientator(**orientator.dict())
    db.add(db_orientator)
    db.commit()
    return db_orientator


def create_coordinator(db: Session, coordinator: CreateCoordinatorSchema):
    if exist_person_with_email_or_number_usp(db, coordinator.email_usp, coordinator.number_usp):
        raise HTTPException(status_code=400, detail="Email e/ou Numero USP já registrados")

    db_coordinator = models.Coordinator(**coordinator.dict())
    db.add(db_coordinator)
    db.commit()
    return db_coordinator


def create_student(db: Session, student: CreateStudentSchema):
    if exist_person_with_email_or_number_usp(db, student.email_usp, student.number_usp):
        raise HTTPException(status_code=400, detail="Email e/ou Numero USP já registrados")

    db_student = models.Student(number_usp=student.number_usp, name=student.name, email_usp=student.email_usp)
    db.add(db_student)
    db.commit()
    return db_student


def exist_person_with_email_or_number_usp(db: Session, email: str, number_usp: str):
    db_person = db.query(models.Person).filter(models.Person.email_usp == email).filter(
        models.Person.number_usp == number_usp).first()
    if db_person is None:
        return False
    return True


def set_student_orientator(db: Session, student: models.Person, orientator_number_usp):
    orientator = create_query_builder(db, models.Orientator, number_usp=orientator_number_usp).first()
    if orientator is None:
        raise HTTPException(status_code=400,
                            detail=f"nenhum orientador com numero usp: {orientator_number_usp} foi encontrado")
    setattr(student, 'orientator', orientator)
    db.commit()
    db.refresh(student)
    return student


def delete_person_by_number_usp(db: Session, number_usp: str):
    db_person = create_query_builder(db, models.Person, number_usp=number_usp).first()
    if db_person is None:
        raise HTTPException(status_code=400, detail=f"nenhuma pessoa com numero usp: {number_usp} foi encontrada")
    db.delete(db_person)
    db.commit()
    return db_person


def get_persons(db: Session):
    return create_query_builder(db, models.Person).all()


def create_query_builder(db: Session, class_name, **kwargs):
    query = db.query(class_name)
    if kwargs.get("email_usp") is not None:
        query = query.filter(class_name.email_usp == kwargs.get("email_usp"))
    if kwargs.get("number_usp") is not None:
        query = query.filter(class_name.number_usp == kwargs.get("number_usp"))
    return query


def create_semi_annual_report(db: Session, report_input: CreateSemiAnnualReportSchema):
    student = create_query_builder(db, models.Student, number_usp=report_input.student_nusp).first()
    if student is None:
        raise HTTPException(status_code=400,
                            detail=f"nenhum ALUNO com numero usp: {report_input.student_nusp} foi encontrado")
    db_report = models.SemiAnnualReportModel(**report_input.dict(), student=student)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report
