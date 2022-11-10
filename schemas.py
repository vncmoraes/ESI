from pydantic import BaseModel, constr


class Person(BaseModel):
    number_usp: constr(max_length=10)
    name: constr(max_length=50)
    email_usp: constr(max_length=100)
    occupation: constr(max_length=15)
    isCoordinator: bool

    class Config:
        orm_mode = True


class CreatePerson(BaseModel):
    number_usp: constr(max_length=10)
    name: constr(max_length=50)
    email_usp: constr(max_length=100)
