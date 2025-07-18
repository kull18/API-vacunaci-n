from src.VaccineBox.application.services.VaccineBox_service import VaccineBoxService
from sqlalchemy.orm import Session
from fastapi import Depends
from shared.mysql import get_db
from src.VaccineBox.domain.scheme.VaccineBox_scheme import VaccineBoxSchema


class VaccineBoxController:
    def __init__(self):
        self.service = VaccineBoxService()

    def create_vaccine_box(self, data: VaccineBoxSchema, db: Session = Depends(get_db)):
        return self.service.create(db, data)

    def get_vaccine_box(self, id_box: int, db: Session = Depends(get_db)):
        return self.service.get_by_id(db, id_box)

    def get_all_vaccine_boxes(self, db: Session = Depends(get_db)):
        return self.service.get_all(db)

    def update_vaccine_box(self, id_box: int, update_data: VaccineBoxSchema, db: Session = Depends(get_db)):
        return self.service.update(db, id_box, update_data)

    def delete_vaccine_box(self, id_box: int, db: Session = Depends(get_db)):
        return self.service.delete(db, id_box)
