import sqlalchemy.exc
from fastapi import FastAPI
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///database.db', echo=True)  # Cria instância do banco de dados
Base.metadata.create_all(engine)  # Realiza a criação das tabelas presentes no módulo "models.py"
api = FastAPI()  # Cria instância da biblioteca FastAPI

#  Página inicial
@api.get("/")
def index():
    return "teste"


#  Correção: adicionar tratamento de exceção no método
@api.post("/novo-aluno/")
def novo_aluno(aluno: Aluno):
    with Session(engine) as session:
        objeto_aluno = AlunoORM(**aluno.dict())
        session.add(objeto_aluno)

        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {'Erro': 'O número USP e/ou email já está cadastrado!'}
            #  retornar codigo http de erro

    return {'Sucesso': 'Aluno cadastrado com sucesso!'}
