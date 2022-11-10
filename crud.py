from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def create_pessoa(db: Session, pessoa: schemas.CreatePessoa, ocupacao: str):
    db_pessoa = get_pessoa_by_email(db, email=pessoa.email_usp)
    if db_pessoa:
        raise HTTPException(status_code=400, detail="Email já registrado")
    db_pessoa = get_pessoa_by_numero_usp(db, numero_usp=pessoa.numero_usp)
    if db_pessoa:
        raise HTTPException(status_code=400, detail="NUSP já registrado")

    db_pessoa = models.Pessoa(**pessoa.dict(), ocupacao=ocupacao)
    db.add(db_pessoa)
    db.commit()
    return db_pessoa


def delete_pessoa_by_numero_usp(db: Session, numero_usp: str):
    db_pessoa = get_pessoa_by_numero_usp(db, numero_usp=numero_usp)
    if db_pessoa is None:
        raise HTTPException(status_code=400, detail=f"nenhuma pessoa com numero usp: {numero_usp} foi encontrada")
    db.delete(db_pessoa)
    db.commit()
    return db_pessoa


def get_pessoas(db: Session):
    return create_pessoa_filter(db=db).all()


def get_pessoas_by_ocupation(db: Session, ocupacao: str):
    return create_pessoa_filter(db=db, ocupacao=ocupacao).all()


def get_pessoa_by_email(db: Session, email: str):
    pessoa = create_pessoa_filter(db=db, email_usp=email).first()
    if pessoa is None:
        raise HTTPException(status_code=400, detail=f"nenhuma pessoa com email usp: {email} foi encontrado")
    return pessoa


def get_pessoa_by_email_and_ocupation(db: Session, email: str, ocupacao: str):
    pessoa = create_pessoa_filter(db=db, email_usp=email, ocupacao=ocupacao).first()
    if pessoa is None:
        raise HTTPException(status_code=400, detail=f"nenhum {ocupacao} com email usp: {email} foi encontrado")
    return pessoa


def get_pessoa_by_numero_usp(db: Session, numero_usp: str):
    pessoa = create_pessoa_filter(db=db, numero_usp=numero_usp).first()
    if pessoa is None:
        raise HTTPException(status_code=400, detail=f"nenhuma pessoa com numero usp: {numero_usp} foi encontrado")
    return pessoa


def get_pessoa_by_numero_usp_and_ocupation(db: Session, numero_usp: str, ocupacao: str):
    pessoa = create_pessoa_filter(db=db, numero_usp=numero_usp, ocupacao=ocupacao).first()
    if pessoa is None:
        raise HTTPException(status_code=400, detail=f"nenhum {ocupacao} com numero usp: {numero_usp} foi encontrado")
    return pessoa


def create_pessoa_filter(db: Session, **kwargs):
    query = db.query(models.Pessoa)
    if kwargs.get("email_usp") is not None:
        query = query.filter(models.Pessoa.email_usp == kwargs.get("email_usp"))
    if kwargs.get("numero_usp") is not None:
        query = query.filter(models.Pessoa.numero_usp == kwargs.get("numero_usp"))
    if kwargs.get("ocupacao") is not None:
        query = query.filter(models.Pessoa.ocupacao == kwargs.get("ocupacao"))
    if kwargs.get("isCoordinator") is not None:
        query = query.filter(models.Pessoa.isCoordinator == kwargs.get("isCoordinator"))
    return query


def add_professor_to_coordination(nusp: str, db: Session):
    professor = get_pessoa_by_numero_usp_and_ocupation(db, nusp, "PROFESSOR")
    if professor is None:
        raise HTTPException(status_code=400, detail=f"nenhum PROFESSOR com numero usp: {nusp} foi encontrado")
    if professor.isCoordenador is True:
        raise HTTPException(status_code=400, detail=f"{professor.nome} já faz parte da coordenacao")
    setattr(professor, "isCoordenador", True)
    db.commit()
    return professor


def remove_professor_from_coordination(nusp: str, db: Session):
    professor = get_pessoa_by_numero_usp_and_ocupation(db, nusp, "PROFESSOR")
    if professor is None:
        raise HTTPException(status_code=400, detail=f"nenhum PROFESSOR com numero usp: {nusp} foi encontrado")
    if professor.isCoordenador is False:
        raise HTTPException(status_code=400, detail=f"{professor.nome} nao faz parte da coordenacao")
    setattr(professor, "isCoordenador", False)
    db.commit()
    return professor

def get_coordenacao(db: Session):
    return create_pessoa_filter(db=db, ocupacao="PROFESSOR").all()
