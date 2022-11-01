from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr
from sqlalchemy import Boolean

Base = declarative_base()  # Cria instância da classe base do modelo de banco de dados


#  Definição da tabela "Pessoa" no banco de dados
class PessoaORM(Base):
    __tablename__ = 'Pessoa'
    numero_usp = Column(String(10), primary_key=True, nullable=False)
    nome = Column(String(50), nullable=False)
    email_usp = Column(String(100), nullable=False, unique=True)


#  Definição da tabela "Aluno" no banco de dados, relacionada com a tabela "Pessoa" através do número USP
class AlunoORM(PessoaORM):
    __tablename__ = 'Aluno'
    numero_usp = Column(ForeignKey(PessoaORM.numero_usp), primary_key=True)


#  Definição da tabela "Professor" no banco de dados, relacionada com a tabela "Pessoa" através do número USP
class ProfessorORM(PessoaORM):
    __tablename__ = 'Professor'
    numero_usp = Column(ForeignKey(PessoaORM.numero_usp), primary_key=True)
    acesso_coordenador = Column(Boolean, nullable=False)


#  Definição da classe "Pessoa" que armazena os dados recebidos da API
class Pessoa(BaseModel):
    numero_usp: constr(max_length=10)
    nome: constr(max_length=50)
    email_usp: constr(max_length=100)

    class Config:
        orm_mode = True


#  Definição da classe "Aluno" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por herança.
class Aluno(Pessoa):
    pass


#  Definição da classe "Professor" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por herança.
class Professor(Pessoa):
    pass



