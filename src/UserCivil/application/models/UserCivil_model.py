from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from shared.mysql import Base
from sqlalchemy import Column, Float

class UserCivil(Base):
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, autoincrement=True)
    fol = Column(String(45))
    corporalTemperature = Column(Float)
    alcoholBreat = Column(Float)
    isVaccinated = Column(Integer)
    name = Column(String(45))
    firstLastname = Column(String(45))
    secondLastname = Column(String(45))
    CURP = Column(String(45))
    dayBirthday = Column(Integer)
    monthBirthday = Column(String(45))
    yearBirthday = Column(String(45))
    yearsOld = Column(Integer)
    school = Column(String(45))
    schoolGrade = Column(String(45))

    # Relaciones inversas hacia UserCivilVaccinated, **dentro** de la clase
    vaccinations_as_patient = relationship(
        "UserCivilVaccinated",
        back_populates="usercivil_patient",
        foreign_keys="[UserCivilVaccinated.UserCivil_idUserCivil]"
    )

    vaccinations_as_medic = relationship(
        "UserCivilVaccinated",
        back_populates="usercivil_medic",
        foreign_keys="[UserCivilVaccinated.UserCivil_UserMedicVaccined]"
    )
