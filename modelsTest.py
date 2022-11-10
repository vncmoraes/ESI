from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr
from sqlalchemy import Boolean

#Base = declarative_base()  # Cria instância da classe base do modelo de banco de dados


#  Definição da tabela "Formulário" no banco de dados
# class FormularioORM(Base):
#     __tablename__ = 'Formulario'
#     email_usp = Column(String(30), primary_key=False, nullable=False)
#     nome_aluno = Column(String(100), primary_key=False, nullable=False)
#     orientador = Column(String(100), primary_key=False, nullable=False)
#     numero_usp = Column(String(10), primary_key=False, nullable=False)
#     cv_lattes = Column(String(50), primary_key=False, nullable=False)
#     data_ultima_atualizacao_cv = Column(String(10), primary_key=True, nullable=False)
#     tipo_curso = Column(String(10), primary_key=False, nullable=False)
#     data_ingresso_aluno_regular = Column(String(10), primary_key=False, nullable=False)
#     resultado_ultimo_relatorio = Column(String(30), primary_key=False, nullable=False)
#     quantidade_aprovacoes_disciplinas_obrigatorias = Column(String(1), primary_key=False, nullable=False)
#     quantidade_aprovacoes_disciplinas_optativas = Column(String(1), primary_key=False, nullable=False)
#     quantidade_reprovacoes_primeiro_semestre = Column(String(1), primary_key=False, nullable=False)
#     quantidade_reprovacoes_totais = Column(String(1), primary_key=False, nullable=False)
#     exame_proficiencia_em_idiomas = Column(String(20), primary_key=False, nullable=False)
#     exame_qualificacao = Column(String(20), primary_key=False, nullable=False)
#     prazo_caso_nao_qualificado = Column(String(10), primary_key=False, nullable=False)
#     prazo_deposito_dissertacao = Column(String(10), primary_key=False, nullable=False)
#     quantidade_artigos_aceitos_ou_publicados = Column(String(1), primary_key=False, nullable=False)
#     quantidade_artigos_submetidos = Column(String(1), primary_key=False, nullable=False)
#     quantidade_artigos_em_revisao = Column(String(1), primary_key=False, nullable=False)
#     quantidade_artigos_em_escrita = Column(String(1), primary_key=False, nullable=False)
#     descricao_participacao_congresso_exterior_primeiro_semestre = Column(String(200), primary_key=False, nullable=False)
#     descricao_estagio_pesquisa_ou_visita_exterior_primeiro_semestre = Column(String(200), primary_key=False, nullable=False)
#     descricao_atuacao_PAE_primeiro_semestre = Column(String(100), primary_key=False, nullable=False)
#     descricao_prorrogacao_circular_covid19 = Column(String(100), primary_key=False, nullable=False)
#     resumo_atividades_pesquisa = Column(String(200), primary_key=False, nullable=False)
#     declaracoes_adicionais = Column(String(200), primary_key=False, nullable=False)
    #  Definir aqui os atributos relacionados com o preenchimento do formulário


#  Definição da tabela "Pessoa" no banco de dados
# class PessoaORM(Base):
#     __tablename__ = 'Pessoa'
#     numero_usp = Column(String(10), primary_key=True, nullable=False)
#     nome = Column(String(50), nullable=False)
#     email_usp = Column(String(100), nullable=False, unique=True)


#  Definição da tabela "Aluno" no banco de dados, relacionada com a tabela "Pessoa" através do número USP
# class AlunoORM(PessoaORM):
#     __tablename__ = 'Aluno'
#     numero_usp = Column(ForeignKey(PessoaORM.numero_usp), primary_key=True)


#  Definição da tabela "Professor" no banco de dados, relacionada com a tabela "Pessoa" através do número USP
# class ProfessorORM(PessoaORM):
#     __tablename__ = 'Professor'
#     numero_usp = Column(ForeignKey(PessoaORM.numero_usp), primary_key=True)
#     acesso_coordenador = Column(Boolean, nullable=False)
#

#  Definição da classe "Pessoa" que armazena os dados recebidos da API
# class Pessoa(BaseModel):
#     numero_usp: constr(max_length=10)
#     nome: constr(max_length=50)
#     email_usp: constr(max_length=100)
#
#     class Config:
#         orm_mode = True
#
#
#   Definição da classe "Aluno" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por herança.
# class Aluno(Pessoa):
#     pass


#  Definição da classe "Professor" que armazena os dados recebidos da API. Recebe os atributos da classe "Pessoa" por herança.
# class Professor(Pessoa):
#     pass
