from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilResponse
from pydantic import BaseModel
from datetime import datetime

class UserCivilVaccinatedSchema(BaseModel):
    UserCivil_idUserCivil: int
    UserCivil_UserMedicVaccined: int
    Vaccine_idVaccines: int
    date: datetime.utcnow

    class Config:
        from_attributes = True