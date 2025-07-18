from src.Vaccine.application.services.Vaccine_service import VaccineService
from src.Vaccine.domain.scheme.Vaccine_scheme import VaccineScheme
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from shared.mysql import get_db

class VaccineController:
    service: VaccineService

    def __init__(self):
        self.service = VaccineService()

    def create_vaccine(self, vaccine: VaccineScheme, db: Session = Depends(get_db)):
        return self.service.create_vaccine(db, vaccine)

    def get_all_vaccines(self, db: Session = Depends(get_db)):
        return self.service.get_vaccines(db)

    def update_vaccine(self, id_vaccine: int, vaccine_data: VaccineScheme, db: Session = Depends(get_db)):
        return self.service.update_vaccine(db, id_vaccine, vaccine_data)

    def delete_vaccine(self, id_vaccine: int, db: Session = Depends(get_db)):
        return self.service.delete_vaccine(db, id_vaccine)
