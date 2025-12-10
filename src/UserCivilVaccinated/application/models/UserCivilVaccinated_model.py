from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from zoneinfo import ZoneInfo
from src.Vaccine.application.models import Vaccine  
from shared.mysql import Base

class UserCivilVaccinated(Base):
    __tablename__ = 'UserCivilVaccinated'

    UserCivil_idUserCivil = Column(
        Integer, ForeignKey('UserCivil.idUserCivil'),
        primary_key=True
    )
    UserCivil_UserMedicVaccined = Column(
        Integer, ForeignKey('UserCivil.idUserCivil'),
        primary_key=True
    )
    Vaccine_idVaccines = Column(
        Integer, ForeignKey('Vaccine.idVaccines'),
        primary_key=True
    )

    # 👇 Cambiado aquí - usa una función lambda para la zona horaria
    date = Column(
        DateTime, 
        default=lambda: datetime.now(ZoneInfo("America/Mexico_City"))
    )

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