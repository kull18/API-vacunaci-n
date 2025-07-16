from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from shared.mysql import Base

class UserCivilVaccinated(Base):
    __tablename__ = 'user_civil_vaccinated'

    user_civil_id = Column(
        Integer, 
        ForeignKey('UserCivil.idUserCivil'), 
        primary_key=True,
    )
    medic_vaccinator_id = Column(
        Integer, 
        ForeignKey('UserCivil.UserMedicVaccined'),
        primary_key=True
    )
    vaccine_id = Column(
        Integer, 
        ForeignKey('Vaccine.idVaccines'),
        primary_key=True
    )
    vaccination_date = Column(
        DateTime, 
        default=datetime.utcnow,
        name='date DATE TIME'  
    )

    user_civil = relationship("UserCivil", back_populates="vaccinations")
    vaccinator = relationship("UserMedicPersonal", back_populates="vaccinations_performed")
    vaccine = relationship("Vaccine", back_populates="vaccinations")
