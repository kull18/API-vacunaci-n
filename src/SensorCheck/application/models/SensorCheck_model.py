from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shared.mysql import Base
from src.UserCivilVaccinated.application.models.UserCivilVaccinated_model import UserCivilVaccinated

class SensorCheck(Base):
    __tablename__ = 'SensorCheck'

    idSensorCheck = Column(Integer, primary_key=True,autoincrement=True)   
    measurementUnit = Column(String(45))
    nameSensor = Column(String(45))
    information = Column(String(45))
    UserCivil_idUserCivil = Column(Integer,ForeignKey('UserCivilVaccinated.UserCivil_idUserCivil'))

    sensor_idUserCivil = relationship(
      "UserCivilVaccinated",
       foreign_keys=[UserCivil_idUserCivil],
       back_populates="sensor_checks"
    )
