from pydantic import BaseModel
from typing import Optional


class SensorCheckBase(BaseModel):
    measurementUnit: str
    nameSensor: str
    information: str
    UserCivil_idUserCivil: int

    class Config:
        from_attributes = True

class SensorCheckUpdate(BaseModel):
    measurementUnit: Optional[str] = None
    nameSensor: Optional[str] = None
    information: Optional[str] = None
    UserCivil_idUserCivil: Optional[int] = None

    class Config:
        from_attributes = True


class SensorCheckResponse(SensorCheckBase):
    idSensorCheck: int

    class Config:
        from_attributes = True
        orm_mode = True 
