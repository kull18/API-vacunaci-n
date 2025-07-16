from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from shared.mysql import Base

class UserCivilVaccinated(Base):
    __tablename__ = 'user_civil_vaccinated'

    UserCivil_idUserCivil = Column(
        Integer, 
        ForeignKey('UserCivil.idUserCivil'), 
        primary_key=True,
    )
    UserCivil_UserMedicVaccined = Column(
        Integer, 
        ForeignKey('UserCivil.UserMedicVaccined'),
        primary_key=True
    )
    Vaccine_idVaccines = Column(
        Integer, 
        ForeignKey('Vaccine.idVaccines'),
        primary_key=True
    )

    date = Column(
        DateTime, 
        default=datetime.utcnow,
    )

    UserCivil_idUserCivil = relationship("UserCivil", back_populates="vaccinations")
    UserCivil_UserMedicVaccined = relationship("UserMedicPersonal", back_populates="vaccinations_performed")
    Vaccine_idVaccines = relationship("Vaccine", back_populates="vaccinations")
