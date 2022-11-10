from sqlalchemy import Column, String, Integer, Boolean, CheckConstraint
from database import Base


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email_usp = Column(String(100), nullable=False, unique=True)
    numero_usp = Column(String(50), nullable=False, unique=True)
    ocupacao = Column(String(15), nullable=False)
    isCoordenador = Column(Boolean, nullable=False, default=False)
    __table_args__ = (CheckConstraint(ocupacao.in_(['PROFESSOR', 'ALUNO'])), )
