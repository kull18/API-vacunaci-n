from pydantic import BaseModel
from typing import Optional

class UserCivilSchema(BaseModel):
    fol: str
    corporalTemperature: float
    alcoholBreat: float
    isVaccinated: int
    name: str
    firstLastname: str
    secondLastname: str
    CURP: Optional[str]
    dayBirthday: Optional[int]
    monthBirthday: Optional[str]
    yearBirthday: Optional[str]
    yearsOld: Optional[int]
    school: Optional[str]
    schoolGrade: Optional[str]

class UserCivil(UserCivilSchema):
    idUserCivil: int

    class Config:
        orm_mode = True
