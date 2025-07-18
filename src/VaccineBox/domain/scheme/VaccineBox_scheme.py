from pydantic import BaseModel

class VaccineBoxSchema(BaseModel):
    amountVaccines: str

    class Config:
        orm_mode = True
