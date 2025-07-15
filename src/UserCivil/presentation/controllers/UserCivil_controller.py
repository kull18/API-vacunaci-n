from src.UserCivil.application.services.UserCivil_service import UserCivilRepository
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema, UserCivil
from sqlalchemy.orm import Session

class UserCivilController:

    def __init__(self):
        self.service = UserCivilRepository()

    def create_userCivil(self, db: Session, user: UserCivilSchema) -> UserCivil:
        return self.service.create_usercivil(db, user)
    
    def get_all_userCivil(self, db: Session):
        return self.service.get_all_usercivils(db)
    
    def get_userCivil_by_id(self, db: Session, id_user: int):
        return self.get_userCivil_by_id(db, id_user)
    
    def delete_userCivil(self, db: Session, id_user: int):
        return self.delete_userCivil(db, id_user)