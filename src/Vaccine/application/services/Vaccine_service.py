from src.Vaccine.infraestructure.repositories.Vaccine_repositorie import VaccineRepositorie
from src.Vaccine.domain.scheme.Vaccine_scheme import VaccineScheme
from sqlalchemy.orm import Session
''
class VaccineService:
    repositorie: VaccineRepositorie

    def __init__(self):
        self.repositorie = VaccineRepositorie()

    def create_vaccine(self, db: Session,vaccine: VaccineScheme):
        return self.repositorie.create_vaccine(db, vaccine)
    
    def get_vaccines(self, db: Session):
        return self.repositorie.get_all_vaccines(db)
    
    def update_vaccine(self,db: Session, id_vaccine: int, vaccine_data: VaccineScheme):
        return self.repositorie.update_vaccine(db, id_vaccine, vaccine_data)
    
    def delete_vaccine(self,db: Session, id_vaccine: int):
        return self.repositorie.delete_vaccine(db, id_vaccine)