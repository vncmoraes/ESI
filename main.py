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


@api.post("/professores/", response_model=schemas.Pessoa)
def create_professor(professor: schemas.CreatePessoa, db: Session = Depends(get_db)):
    return crud.create_pessoa(db, professor, "PROFESSOR")


@api.get("/professores/", response_model=List[schemas.Pessoa])
def get_professores(db: Session = Depends(get_db)):
    professores = crud.get_pessoas_by_ocupation(db, ocupacao="PROFESSOR")
    return professores


@api.get("/professores/{nusp}", response_model=schemas.Pessoa)
def get_professor_by_nusp(nusp: str, db: Session = Depends(get_db)):
    professor = crud.get_pessoa_by_numero_usp_and_ocupation(db, nusp, "PROFESSOR")
    return professor


@api.post("/alunos/", response_model=schemas.Pessoa)
def create_aluno(aluno: schemas.CreatePessoa, db: Session = Depends(get_db)):
    return crud.create_pessoa(db, aluno, "ALUNO")


@api.get("/alunos/", response_model=List[schemas.Pessoa])
def get_alunos(db: Session = Depends(get_db)):
    alunos = crud.get_pessoas_by_ocupation(db, ocupacao="ALUNO")
    return alunos


@api.get("/alunos/{nusp}", response_model=schemas.Pessoa)
def get_aluno_by_nusp(nusp: str, db: Session = Depends(get_db)):
    aluno = crud.get_pessoa_by_numero_usp_and_ocupation(db, nusp, "ALUNO")
    return aluno


@api.get("/pessoas/", response_model=List[schemas.Pessoa])
def get_pessoas(db: Session = Depends(get_db)):
    pessoas = crud.get_pessoas(db)
    return pessoas


@api.delete("/pessoas/{nusp}", response_model=schemas.Pessoa)
def delete_pessoa_by_numero_usp(nusp: str, db: Session = Depends(get_db)):
    return crud.delete_pessoa_by_numero_usp(db, nusp)


@api.get("/pessoas/{nusp}", response_model=schemas.Pessoa)
def get_pessoa_by_nusp(nusp: str, db: Session = Depends(get_db)):
    pessoa = crud.get_pessoa_by_numero_usp(db, nusp)
    return pessoa


@api.put("/coordenacao/{nusp}", response_model=schemas.Pessoa)
def add_professor_to_coordination(nusp: str, db: Session = Depends(get_db)):
    return crud.add_professor_to_coordination(nusp, db)


@api.delete("/coordenacao/{nusp}", response_model=schemas.Pessoa)
def add_professor_to_coordination(nusp: str, db: Session = Depends(get_db)):
    return crud.remove_professor_from_coordination(nusp, db)
