from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from shared.mysql import Base

class Vaccine(Base):
    __tablename__ = 'Vaccine'

    idVaccines = Column(Integer, primary_key=True, autoincrement=True)
    nameVaccine = Column(String(45))

    usercivilvaccinated = relationship("UserCivilVaccinated", back_populates="vaccine")
