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
        name='UserCivil_idUserCivil'
    )
    medic_vaccinator_id = Column(
        Integer, 
        ForeignKey('UserCivil.UserMedicVaccined'),
        name='UserCivil_UserMedicVaccined',
        primary_key=True
    )
    vaccine_id = Column(
        Integer, 
        ForeignKey('Vaccine.idVaccines'),
        name='Vaccine_idVaccines',
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
