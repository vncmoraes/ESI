from sqlalchemy import Column, String, Integer, Boolean, CheckConstraint
from database import Base


class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email_usp = Column(String(100), nullable=False, unique=True)
    number_usp = Column(String(50), nullable=False, unique=True)
    occupation = Column(String(15), nullable=False)
    isCoordinator = Column(Boolean, nullable=False, default=False)
    __table_args__ = (CheckConstraint(occupation.in_(['PROFESSOR', 'ALUNO'])),)


# class FormularioORM(Base):
#     __tablename__ = 'Formulario'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     email_usp = Column(String(30), nullable=False)
#     name_student = Column(String(100), nullable=False)
#     orientador = Column(String(100), nullable=False)
#     number_usp = Column(String(10), nullable=False)
#     cv_lattes = Column(String(50), nullable=False)
#     data_ultima_att_cv = Column(String(10), nullable=False)
#     tipo_curso = Column(String(10), nullable=False)
#     data_ingresso_student_regular = Column(String(10), nullable=False)
#     resultado_ultimo_relatorio = Column(String(30), nullable=False)
#     quant_apr_disc_obg = Column(String(10), nullable=False)
#     quant_apr_disc_opt = Column(String(10), nullable=False)
#     quant_rpr_pr_sem = Column(String(10), nullable=False)
#     quant_rpr_totais = Column(String(10), nullable=False)
#     ex_proc_idiomas = Column(String(20), nullable=False)
#     ex_quali = Column(String(20), nullable=False)
#     prazo_nao_qualificado = Column(String(10), nullable=True)
#     prazo_deposito_dissertacao = Column(String(10), nullable=False)
#     quant_art_aceitos_ou_publicados = Column(String(10), nullable=False)
#     quant_art_submetidos = Column(String(10), nullable=False)
#     quant_art_em_revisao = Column(String(10), nullable=False)
#     quant_art_em_escrita = Column(String(10), nullable=False)
#     desc_participacao_congresso_exterior_pr_sem = Column(String(200), nullable=False)
#     desc_estagio_pesquisa_ou_visita_exterior_pr_sem = Column(String(200), nullable=False)
#     desc_atuacao_PAE_pr_sem = Column(String(100), nullable=False)
#     desc_prorrogacao_circular_covid19 = Column(String(100), nullable=False)
#     resumo_atividades_pesquisa = Column(String(200), nullable=False)
#     declaracoes_adicionais = Column(String(200), nullable=False)

# class Student(Base):
#     __tablename__ = 'Student'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     email_usp = Column(String(100), nullable=False, unique=True)
#     number_usp = Column(String(50), nullable=False, unique=True)
#     parecer_orientador
#     parecer_ccp
#
# class Professor(Base):
#     __tablename__ = 'Professor'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     email_usp = Column(String(100), nullable=False, unique=True)
#     number_usp = Column(String(50), nullable=False, unique=True)
#     is_coordinator= Column(Boolean, nullable=False, default=False)
#
#
#
# class Seem(Base):
#     id
#     id_student
#     id_professor
#     comentario
#     avaliacao
#     dat_seem