# Definição da classe "Aluno" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por
# herança.
from pydantic import BaseModel, constr


# Definição da classe "Professor" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por
# herança.


class Pessoa(BaseModel):
    numero_usp: constr(max_length=10)
    nome: constr(max_length=50)
    email_usp: constr(max_length=100)
    ocupacao: constr(max_length=15)
    isCoordenador: bool

    class Config:
        orm_mode = True


class CreatePessoa(BaseModel):
    numero_usp: constr(max_length=10)
    nome: constr(max_length=50)
    email_usp: constr(max_length=100)

