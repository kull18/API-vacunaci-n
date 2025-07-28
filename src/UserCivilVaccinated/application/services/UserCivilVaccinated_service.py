from src.UserCivilVaccinated.infraestructure.repositories.UserCivilVaccinated_repositorie import UserCivilVaccinatedRepository
from sqlalchemy.orm import Session
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema


class UserCivilVaccinatedService:
    def __init__(self):
        self.repositorie = UserCivilVaccinatedRepository()

    def create_userCivilVaccinated(self, db: Session, data: UserCivilVaccinatedSchema):
        return self.repositorie.create_vaccination_record(db, data)

    def get_userCivilVaccinated(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int):
        return self.repositorie.get_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
    

    def get_all_Usercivil_vaccinations(self, db: Session):
        return self.repositorie.get_all_user_civil_vaccinations(db)
    
    def get_userCivilVaccinated_with_values(self, db: Session):
        return self.repositorie.get_vaccinations_with_values(db)
    
    def get_userCivilVaccinated_by_user(self, db: Session, user_civil_id: int):
        return self.repositorie.get_vaccinations_by_user(db, user_civil_id)

    def get_all_userCivilVaccinated(self, db: Session):
        return self.repositorie.get_all_vaccination_record(db)

    def update_userCivilVaccinated(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int, update_data: UserCivilVaccinatedSchema):
        return self.repositorie.update_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id, update_data)

    def delete_userCivilVaccinated(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int):
        return self.repositorie.delete_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
    
    def get_userCivilVaccinated_with_values_id(self, db: Session, id: int):
        return self.repositorie.get_vaccinations_with_values_id(db, id)