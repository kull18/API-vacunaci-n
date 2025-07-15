from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilResponse
from src.UserMedicPersonal.domain.scheme.UserMedicPersonal_scheme import UserMedicPersonalResponse
from src.Vaccine.domain.scheme.Vaccine_scheme import VaccineResponse

class UserCivilVaccinatedSchema(BaseModel):
    user_civil: UserCivilResponse
    vaccinator: UserMedicPersonalResponse
    vaccine: VaccineResponse

    class Config:
        from_attributes = True