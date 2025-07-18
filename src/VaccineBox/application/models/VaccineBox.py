from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from shared.mysql import  Base


class VaccineBox(Base):
    __tablename__ = "VaccineBox"

    idVaccineBox = Column(Integer, primary_key=True, index=True)
    amountVaccines = Column(String(45))

    vaccines = relationship("VaccineBoxVaccine", back_populates="vaccine_box")
