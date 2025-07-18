from pydantic import BaseModel

class VaccineBoxVaccineSchema(BaseModel):
    VaccineBox_idVaccineBox: int
    Vaccine_idVaccines: int

    class Config:
        orm_mode = True
