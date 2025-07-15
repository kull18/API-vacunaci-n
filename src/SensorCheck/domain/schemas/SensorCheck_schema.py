from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorCheckBase(BaseModel):
    measurementUnit: str
    nameSensor: str
    information: str
    UserCivil_idUserCivil: int
    
    class Config:
        from_attributes = True


class SensorCheckResponse(SensorCheckBase):
    idSensorCheck: int

    class Config:
        from_attributes = True
