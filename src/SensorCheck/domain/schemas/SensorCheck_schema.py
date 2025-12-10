from pydantic import BaseModel
from typing import Optional

class SensorCheckBase(BaseModel):
    measurementUnit: str
    nameSensor: str
    information: float
    UserCivil_idUserCivil: int
    idVaccineBox: int              # ✅ Nuevo campo
    idSensorsVaccine: int          # ✅ Nuevo campo

    class Config:
        from_attributes = True

class SensorCheckUpdate(BaseModel):
    measurementUnit: Optional[str] = None
    nameSensor: Optional[str] = None
    information: Optional[float] = None
    UserCivil_idUserCivil: Optional[int] = None
    idVaccineBox: Optional[int] = None         # ✅ Nuevo campo
    idSensorsVaccine: Optional[int] = None     # ✅ Nuevo campo

    class Config:
        from_attributes = True

class SensorCheckResponse(SensorCheckBase):
    idSensorCheck: int

    class Config:
        from_attributes = True
        orm_mode = True