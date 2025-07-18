from fastapi import Depends
from sqlalchemy.orm import Session
from shared.mysql import get_db
from src.VaccineBoxVaccine.application.services.VaccineBoxVaccine_service import VaccineBoxVaccineService
from src.VaccineBoxVaccine.domain.schema.VaccineBoxVaccine_schema import VaccineBoxVaccineSchema


class VaccineBoxVaccineController:
    def __init__(self):
        self.service = VaccineBoxVaccineService()

    def create(self, data: VaccineBoxVaccineSchema, db: Session = Depends(get_db)):
        return self.service.create(db, data)

    def get_by_ids(self, box_id: int, vaccine_id: int, db: Session = Depends(get_db)):
        return self.service.get_by_ids(db, box_id, vaccine_id)

    def get_all(self, db: Session = Depends(get_db)):
        return self.service.get_all(db)

    def delete(self, box_id: int, vaccine_id: int, db: Session = Depends(get_db)):
        return self.service.delete(db, box_id, vaccine_id)
