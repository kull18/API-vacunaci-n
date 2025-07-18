from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from shared.mysql import Base

class VaccineBoxVaccine(Base):
    __tablename__ = "VaccineBoxVaccine"

    VaccineBox_idVaccineBox = Column(Integer, ForeignKey("VaccineBox.idVaccineBox"), primary_key=True)
    Vaccine_idVaccines = Column(Integer, ForeignKey("Vaccine.idVaccines"), primary_key=True)

    vaccine_box = relationship("VaccineBox", back_populates="vaccines")
    vaccine = relationship("Vaccine", back_populates="vaccine_boxes")
