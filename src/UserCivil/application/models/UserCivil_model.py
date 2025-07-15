from sqlalchemy import Column, Integer, String
from shared.mysql import Base

class UserCivil(Base):
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fol = Column(String(45))
    corporalTemperature = Column(Integer)
    alcoholBreat = Column(Integer)
    isVaccinated = Column(Integer)
    UserMedicVaccined = Column(Integer)
    name = Column(String(45))
    lastname = Column(String(45))
