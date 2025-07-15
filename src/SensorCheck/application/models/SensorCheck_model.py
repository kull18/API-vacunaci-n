from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shared.mysql import Base

class SensorCheck(Base):
    __tablename__ = 'SensorCheck'

    idSensorCheck = Column(Integer, primary_key=True,autoincrement=True)   
    measurement_unit = Column(String(45))
    name_sensor = Column(String(45))
    information = Column(String(45))
    user_civil_id = Column(Integer,ForeignKey('user_civil.idUserCivil'))
    user_civil = relationship("UserCivil", back_populates="sensor_checks")
