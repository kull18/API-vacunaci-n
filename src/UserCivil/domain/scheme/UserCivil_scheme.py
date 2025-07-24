from pydantic import BaseModel

class UserCivilSchema(BaseModel):
    fol: str
    corporalTemperature: int
    alcoholBreat: int
    isVaccinated: int
    UserMedicVaccined: int
    name: str
    lastname: str

class UserCivil(UserCivilSchema):
    idUserCivil: int

    class Config:
        orm_mode = True
