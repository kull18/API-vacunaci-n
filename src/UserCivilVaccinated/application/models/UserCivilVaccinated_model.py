from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.Vaccine.application.models import Vaccine  
from shared.mysql import Base

class UserCivilVaccinated(Base):
    __tablename__ = 'UserCivilVaccinated'

    UserCivil_idUserCivil = Column(
        Integer, ForeignKey('UserCivil.idUserCivil'),
        primary_key=True
    )
    UserCivil_UserMedicVaccined = Column(
        Integer, ForeignKey('UserCivil.UserMedicVaccined'),
        primary_key=True
    )
    Vaccine_idVaccines = Column(
        Integer, ForeignKey('Vaccine.idVaccines'),
        primary_key=True
    )

    date = Column(DateTime, default=datetime.utcnow)

    usercivil_patient = relationship(
      "UserCivil",
      foreign_keys=[UserCivil_idUserCivil],
      back_populates="vaccinations_as_patient"
    )

    usercivil_medic = relationship(
      "UserCivil",
      foreign_keys=[UserCivil_UserMedicVaccined],
      back_populates="vaccinations_as_medic"
    )

    sensor_checks = relationship(
    "SensorCheck",
    back_populates="sensor_idUserCivil"
    )    

    vaccine = relationship("Vaccine", back_populates="usercivilvaccinateds")

