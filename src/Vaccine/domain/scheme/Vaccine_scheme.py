from pydantic import BaseModel, Field


class VaccineScheme(BaseModel):
    nameVaccine: str    

class Vaccine(VaccineScheme):
    idVaccines: int

    class Config:
     from_attributes = True