from src.UserCivil.infraestructure.repository.UserCivil_repository import UserCivilRepository
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema
from sqlalchemy.orm import Session
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivil

class UserCivilService:

    def __init__(self):
        self.repository = UserCivilRepository()

    def create_userCivil(self, db: Session, user: UserCivilSchema) -> UserCivil:
       return self.repository.create_usercivil(db,user)

    def get_all_userCivil(self, db: Session):
        return self.repository.get_all_usercivils(db)
    
    def get_userCivil_by_id(self, db: Session,id_user: int):
        return self.repository.get_usercivil_by_id(db, id_user)
    
    def delete_userCivil(self, db: Session, id_user: int):
        return self.repository.delete_usercivil(db, id_user)
    
    def update_userCivil(self, db: Session, id_user: int, user: UserCivilSchema):
        return self.repository.update_userCivil(db, id_user, user)
   
    def update_is_vaccinated(self, db: Session, id_user: int) -> UserCivil:
     return self.repository.update_is_vaccinated(db, id_user)
