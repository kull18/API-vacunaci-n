from pydantic import BaseModel, Field
from datetime import datetime

class UserCivilVaccinatedSchema(BaseModel):
    UserCivil_idUserCivil: int
    UserCivil_UserMedicVaccined: int
    Vaccine_idVaccines: int
    date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True