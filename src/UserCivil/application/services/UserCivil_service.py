from src.UserCivil.infraestructure.repository.UserCivil_repository import UserCivilRepository
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema
from sqlalchemy.orm import Session
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivil

class UserCivil:

    def __init__(self):
        self.repository = UserCivilRepository()

    def create_userCivil(self, db: Session, user: UserCivilSchema) -> UserCivil:
       return self.repository.create_usercivil(db,user)

    def get_all_userCivil(self):
        return self.repository.get_all_usercivils()
    
    def get_userCivil_by_id(self, db: Session,id_user: int):
        return self.get_userCivil_by_id(db, id_user)
    
    def delete_userCivil(self, db: Session, id_user: int):
        return self.delete_userCivil(db, id_user)
