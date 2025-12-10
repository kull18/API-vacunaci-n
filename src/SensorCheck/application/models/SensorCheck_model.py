from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from shared.mysql import Base
from src.UserCivilVaccinated.application.models.UserCivilVaccinated_model import UserCivilVaccinated

class SensorCheck(Base):
    __tablename__ = 'SensorCheck'

    idSensorCheck = Column(Integer, primary_key=True, autoincrement=True)   
    measurementUnit = Column(String(45))
    nameSensor = Column(String(45))
    information = Column(Float)   
    UserCivil_idUserCivil = Column(Integer, ForeignKey('UserCivilVaccinated.UserCivil_idUserCivil'))
    idVaccineBox = Column(Integer)          # ✅ Nuevo campo
    idSensorsVaccine = Column(Integer)      # ✅ Nuevo campo

    sensor_idUserCivil = relationship(
        "UserCivilVaccinated",
        foreign_keys=[UserCivil_idUserCivil],
        back_populates="sensor_checks"
    )