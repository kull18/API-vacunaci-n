from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorCheckBase(BaseModel):
    measurement_unit: str
    name_sensor: str
    information: str
    user_civil_id: int
    
    class Config:
        from_attributes = True


class SensorCheckResponse(SensorCheckBase):
    id: int

    class Config:
        from_attributes = True
