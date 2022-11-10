from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def create_person(db: Session, person: schemas.CreatePerson, occupation: str):
    db_person = get_person_by_email(db, email=person.email_usp)
    if db_person:
        raise HTTPException(status_code=400, detail="Email já registrado")
    db_person = get_person_by_number_usp(db, number_usp=person.number_usp)
    if db_person:
        raise HTTPException(status_code=400, detail="number_usp já registrado")

    db_person = models.Person(**person.dict(), occupation=occupation)
    db.add(db_person)
    db.commit()
    return db_person


def delete_person_by_number_usp(db: Session, number_usp: str):
    db_person = get_person_by_number_usp(db, number_usp=number_usp)
    if db_person is None:
        raise HTTPException(status_code=400, detail=f"nenhuma pessoa com numero usp: {number_usp} foi encontrada")
    db.delete(db_person)
    db.commit()
    return db_person


def get_persons(db: Session):
    return create_person_filter(db=db).all()


def get_persons_by_occupation(db: Session, occupation: str):
    return create_person_filter(db=db, occupation=occupation).all()


def get_person_by_email(db: Session, email: str):
    return create_person_filter(db=db, email_usp=email).first()


def get_person_by_email_and_occupation(db: Session, email: str, occupation: str):
    return create_person_filter(db=db, email_usp=email, occupation=occupation).first()


def get_person_by_number_usp(db: Session, number_usp: str):
    return create_person_filter(db=db, number_usp=number_usp).first()


def get_person_by_number_usp_and_occupation(db: Session, number_usp: str, occupation: str):
    return create_person_filter(db=db, number_usp=number_usp, occupation=occupation).first()


def create_person_filter(db: Session, **kwargs):
    query = db.query(models.Person)
    if kwargs.get("email_usp") is not None:
        query = query.filter(models.Person.email_usp == kwargs.get("email_usp"))
    if kwargs.get("number_usp") is not None:
        query = query.filter(models.Person.number_usp == kwargs.get("number_usp"))
    if kwargs.get("occupation") is not None:
        query = query.filter(models.Person.occupation == kwargs.get("occupation"))
    if kwargs.get("isCoordinator") is not None:
        query = query.filter(models.Person.isCoordinator == kwargs.get("isCoordinator"))
    return query


def add_teacher_to_coordination(number_usp: str, db: Session):
    teacher = get_person_by_number_usp_and_occupation(db, number_usp, "PROFESSOR")
    if teacher is None:
        raise HTTPException(status_code=400, detail=f"nenhum PROFESSOR com numero usp: {number_usp} foi encontrado")
    if teacher.isCoordinator is True:
        raise HTTPException(status_code=400, detail=f"{teacher.name} já faz parte da coordenacao")
    setattr(teacher, "isCoordinator", True)
    db.commit()
    return teacher


def remove_teacher_from_coordination(number_usp: str, db: Session):
    teacher = get_person_by_number_usp_and_occupation(db, number_usp, "PROFESSOR")
    if teacher is None:
        raise HTTPException(status_code=400, detail=f"nenhum PROFESSOR com numero usp: {number_usp} foi encontrado")
    if not teacher.isCoordinator:
        raise HTTPException(status_code=400, detail=f"{teacher.name} nao faz parte da coordenacao")
    setattr(teacher, "isCoordinator", False)
    db.commit()
    return teacher


def get_coordination(db: Session):
    return create_person_filter(db=db, occupation="PROFESSOR", isCoordinator=True).all()
