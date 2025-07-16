from src.UserCivilVaccinated.infraestructure.repositories.UserCivilVaccinated_repositorie import UserCivilVaccinatedRepository
from sqlalchemy.orm import Session
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema

class UserCivilVaccinated:
    repositorie: UserCivilVaccinatedRepository

    def __init__(self):
        self.repositorie =  UserCivilVaccinatedRepository()


    def create_userCivilVaccinated(self, db: Session, UserCivilVaccinated: UserCivilVaccinatedSchema):
        return self.repositorie.create_vaccination_record(db, UserCivilVaccinated)
    
    def get_userCivilVaccinated(self, db: Session,UserCivil_id: int, UserCivilMedic: int, Vaccine: int):
        return self.repositorie.get_vaccination_record(db,UserCivil_id, UserCivilMedic, Vaccine)
    

    def get_userCivilVaccinated_by_user(self, db: Session,UserCivil_id: int):
        return self.repositorie.get_vaccinations_by_user(db,UserCivil_id)
    
    def update_userCivilVaccinated(self,db: Session, UserCivil_id: int, UserCivilVaccinated: UserCivilVaccinatedSchema):
        return self.repositorie.update_vaccination_record(UserCivil_id, UserCivilVaccinated)
    
    def delete_userCivilVaccinated(self, ):
        return  self.repositorie.delete_vaccination_record()