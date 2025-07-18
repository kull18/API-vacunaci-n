from sqlalchemy.orm import Session
from src.VaccineBoxVaccine.infraestructure.repositories.VaccineBoxVaccine_repository import VaccineBoxVaccineRepository
from src.VaccineBoxVaccine.domain.schema.VaccineBoxVaccine_schema import VaccineBoxVaccineSchema


class VaccineBoxVaccineService:
    def __init__(self):
        self.repository = VaccineBoxVaccineRepository()

    def create(self, db: Session, data: VaccineBoxVaccineSchema):
        return self.repository.create(db, data)

    def get_by_ids(self, db: Session, box_id: int, vaccine_id: int):
        return self.repository.get_by_ids(db, box_id, vaccine_id)

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def delete(self, db: Session, box_id: int, vaccine_id: int):
        return self.repository.delete(db, box_id, vaccine_id)
