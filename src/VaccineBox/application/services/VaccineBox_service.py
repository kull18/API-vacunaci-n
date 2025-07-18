from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from typing import Optional, List
from src.VaccineBox.domain.scheme.VaccineBox_scheme import VaccineBoxSchema
from src.VaccineBox.infraestructure.repositories.VaccineBox_repositorie import VaccineBoxRepository
from src.VaccineBox.application.models.VaccineBox import VaccineBox


class VaccineBoxService:
    def __init__(self):
        self.repository = VaccineBoxRepository()

    def create(self, db: Session, box_data: VaccineBoxSchema) -> JSONResponse:
        return self.repository.create_vaccine_box(db, box_data)

    def get_by_id(self, db: Session, id_box: int) -> Optional[VaccineBox]:
        return self.repository.get_vaccine_box(db, id_box)


    def get_all(self, db: Session) -> List[VaccineBox]:
        return self.repository.get_all_vaccine_boxes(db)

    def update(self, db: Session, id_box: int, update_data: VaccineBoxSchema) -> VaccineBox:
        return self.repository.update_vaccine_box(db, id_box, update_data)

    def delete(self, db: Session, id_box: int) -> JSONResponse:
        return self.repository.delete_vaccine_box(db, id_box)
