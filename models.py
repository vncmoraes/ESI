from sqlalchemy import Column, String, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, backref

from database import Base


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email_usp = Column(String(100), nullable=False, unique=True)
    number_usp = Column(String(50), nullable=False, unique=True)

    # __mapper_args__ = {
    #     "polymorphic_identity": "person",
    #     "polymorphic_on": type,
    # }


class Coordinator(Person):
    __tablename__ = 'coordinator'
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)

    # __mapper_args__ = {
    #     "polymorphic_identity": "coordinator",
    # }


class Student(Person):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    orientator_id = Column(ForeignKey("orientator.id"))

    orientator = relationship("Orientator", foreign_keys=[orientator_id],
                              back_populates='students')
    semiAnnualReports = relationship("SemiAnnualReport", back_populates="student")

    # __mapper_args__ = dict(
    #     polymorphic_identity='student',
    #     inherit_condition=(id == Person.id)
    # )


class Orientator(Person):
    __tablename__ = 'orientator'
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    students = relationship("Student", back_populates="orientator", foreign_keys=Student.orientator_id)

    # __mapper_args__ = dict(
    #     polymorphic_identity='orientator',
    #     inherit_condition=(id == Person.id)
    # )


class SemiAnnualReport(Base):
    __tablename__ = 'semiAnnualReport'
    id = Column(Integer, primary_key=True, autoincrement=True)

    cv_lattes = Column(String(50), nullable=False)
    data_ultima_att_cv = Column(String(10), nullable=False)
    tipo_curso = Column(String(10), nullable=False)
    data_ingresso_student_regular = Column(String(10), nullable=False)
    resultado_ultimo_relatorio = Column(String(30), nullable=False)
    quant_apr_disc_obg = Column(String(10), nullable=False)
    quant_apr_disc_opt = Column(String(10), nullable=False)
    quant_rpr_pr_sem = Column(String(10), nullable=False)
    quant_rpr_totais = Column(String(10), nullable=False)
    ex_proc_idiomas = Column(String(20), nullable=False)
    ex_quali = Column(String(20), nullable=False)
    prazo_nao_qualificado = Column(String(10), nullable=True)
    prazo_deposito_dissertacao = Column(String(10), nullable=False)
    quant_art_aceitos_ou_publicados = Column(String(10), nullable=False)
    quant_art_submetidos = Column(String(10), nullable=False)
    quant_art_em_revisao = Column(String(10), nullable=False)
    quant_art_em_escrita = Column(String(10), nullable=False)
    desc_participacao_congresso_exterior_pr_sem = Column(String(200), nullable=False)
    desc_estagio_pesquisa_ou_visita_exterior_pr_sem = Column(String(200), nullable=False)
    desc_atuacao_PAE_pr_sem = Column(String(100), nullable=False)
    desc_prorrogacao_circular_covid19 = Column(String(100), nullable=False)
    resumo_atividades_pesquisa = Column(String(200), nullable=False)
    declaracoes_adicionais = Column(String(200), nullable=False)
    comentario_orientador = Column(String(200), nullable=True)
    aval_orientardor = Column(String(50), nullable=True)
    comentario_ccp = Column(String(200), nullable=True)
    avaliacap_ccp = Column(String(50), nullable=True)

    student_id = Column(ForeignKey("student.id"))
    student = relationship("Student", back_populates="semiAnnualReports")

# form_history
# id
# id_aluno
# id forms
# avaliacao-final
# ano
# semestre

# avaliacao
# id
# id_forms
# id_person
# comentario
# nota
