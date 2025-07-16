from sqlalchemy import Column, Integer, String
from shared.mysql import Base
from sqlalchemy.orm import relationship

class UserCivil(Base):
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fol = Column(String(45))
    corporalTemperature = Column(Integer)
    alcoholBreat = Column(Integer)
    isVaccinated = Column(Integer)  
    UserMedicVaccined = Column(Integer, unique=True)  

    name = Column(String(45))
    lastname = Column(String(45))

    vaccinations_as_patient = relationship(
        "UserCivilVaccinated",
        foreign_keys="[UserCivilVaccinated.UserCivil_idUserCivil]",
        back_populates="usercivil"
    )

    vaccinations_as_medic = relationship(
        "UserCivilVaccinated",
        foreign_keys="[UserCivilVaccinated.UserCivil_UserMedicVaccined]",
        back_populates="user_medic"
    )
