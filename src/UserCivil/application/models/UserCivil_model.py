from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shared.mysql import Base
from src.UserCivil.application.models.User import User

class UserCivil(Base):
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, autoincrement=True)
    fol = Column(String(45))
    corporalTemperature = Column(Integer)
    alcoholBreat = Column(Integer)
    isVaccinated = Column(Integer)
    
    # Aquí se declara explícitamente como ForeignKey
    UserMedicVaccined = Column(Integer, ForeignKey("User.idUser"))

    name = Column(String(45))
    lastname = Column(String(45))

    # Relaciones con UserCivilVaccinated (si es necesario)
    vaccinations_as_patient = relationship(
      "UserCivilVaccinated",
      foreign_keys="[UserCivilVaccinated.UserCivil_idUserCivil]",
      back_populates="usercivil_patient" 
    )

    vaccinations_as_medic = relationship(
      "UserCivilVaccinated",
       foreign_keys="[UserCivilVaccinated.UserCivil_UserMedicVaccined]",
       back_populates="usercivil_medic"  
    )

    medic = relationship("User", backref="civils_vaccinated")
