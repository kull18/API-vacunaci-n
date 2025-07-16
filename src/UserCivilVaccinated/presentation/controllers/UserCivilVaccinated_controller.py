from src.UserCivilVaccinated.application.services.UserCivilVaccinated_service import UserCivilVaccinated
from sqlalchemy.orm import Session
from fastapi import Depends
from shared.mysql import get_db
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema

class UserCivilVaccinatedController:
    service: UserCivilVaccinated

    def __init__(self):
        self.service = UserCivilVaccinated()


    def create_userCivilVaccinated(self, UserCivilVaccinated: UserCivilVaccinatedSchema , db: Session = Depends(get_db)):
        return self.service.create_userCivilVaccinated(db, UserCivilVaccinated)
    
    def get_all_userCivilVaccinated(self, UserCivil_id: int, UserCivilMedic: int, Vaccine: int,db: Session = Depends(get_db)):
        return self.service.get_userCivilVaccinated(UserCivil_id, UserCivilMedic, Vaccine)
    
    
