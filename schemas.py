from typing import List, Optional

from pydantic import BaseModel, constr


class PersonBaseSchema(BaseModel):
    number_usp: constr(max_length=10)
    name: constr(max_length=50)
    email_usp: constr(max_length=100)

    class Config:
        orm_mode = True


class OrientatorBaseSchema(PersonBaseSchema):
    pass


class CreateOrientatorSchema(OrientatorBaseSchema):
    pass


class StudentBaseSchema(PersonBaseSchema):
    pass


class CoordinatorSchema(PersonBaseSchema):
    pass


class CreateCoordinatorSchema(CoordinatorSchema):
    pass


class OrientatorSchema(PersonBaseSchema):
    students: List[StudentBaseSchema] = []

    class Config:
        orm_mode = True


class SemiAnnualReportBaseSchema(BaseModel):
    cv_lattes = constr(max_length=50)
    data_ultima_att_cv = constr(max_length=10)
    tipo_curso = constr(max_length=10)
    data_ingresso_student_regular = constr(max_length=10)
    resultado_ultimo_relatorio = constr(max_length=30)
    quant_apr_disc_obg = constr(max_length=10)
    quant_apr_disc_opt = constr(max_length=10)
    quant_rpr_pr_sem = constr(max_length=10)
    quant_rpr_totais = constr(max_length=10)
    ex_proc_idiomas = constr(max_length=20)
    ex_quali = constr(max_length=20)
    prazo_nao_qualificado = constr(max_length=10)
    prazo_deposito_dissertacao = constr(max_length=10)
    quant_art_aceitos_ou_publicados = constr(max_length=10)
    quant_art_submetidos = constr(max_length=10)
    quant_art_em_revisao = constr(max_length=10)
    quant_art_em_escrita = constr(max_length=10)
    desc_participacao_congresso_exterior_pr_sem = constr(max_length=200)
    desc_estagio_pesquisa_ou_visita_exterior_pr_sem = constr(max_length=200)
    desc_atuacao_PAE_pr_sem = constr(max_length=100)
    desc_prorrogacao_circular_covid19 = constr(max_length=100)
    resumo_atividades_pesquisa = constr(max_length=200)
    declaracoes_adicionais = constr(max_length=200)

    class Config:
        orm_mode = True


class CreateSemiAnnualReportSchema(SemiAnnualReportBaseSchema):
    student_nusp = constr(max_length=10)


class SemiAnnualReportSchema(SemiAnnualReportBaseSchema):
    id: int
    student: StudentBaseSchema
    comentario_orientador: Optional[constr(max_length=200)]
    aval_orientardor: Optional[constr(max_length=50)]
    comentario_ccp: Optional[constr(max_length=200)]
    avaliacap_ccp: Optional[constr(max_length=50)]

    class Config:
        orm_mode = True


class SetReportNote(BaseModel):
    id_form: int
    comentario: Optional[constr(max_length=200)]
    avaliacao: Optional[constr(max_length=50)]


class StudentSchema(PersonBaseSchema):
    semiAnnualReports: List[SemiAnnualReportSchema] = []
    orientator: Optional[OrientatorBaseSchema]

    class Config:
        orm_mode = True


class CreateStudentSchema(PersonBaseSchema):
    orientator_nusp: Optional[constr(max_length=10)]


class CreatePersonSchema(PersonBaseSchema):
    pass

    class Config:
        orm_mode = True
