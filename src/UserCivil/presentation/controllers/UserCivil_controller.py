from src.UserCivil.application.services.UserCivil_service import UserCivilRepository
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema, UserCivil
from sqlalchemy.orm import Session
from src.UserCivil.application.services.UserCivil_service import UserCivilService
from shared.mysql import get_db
from fastapi import Depends

class UserCivilController:

    def __init__(self):
        self.service = UserCivilService()
 
    # Quita async y await aquí, porque la función llamada no es async
    def create_userCivil(self, user: UserCivilSchema, db: Session = Depends(get_db)) -> UserCivil:
       return self.service.create_userCivil(db, user)
        
    
    def get_all_userCivil(self, db: Session = Depends(get_db)):
        return self.service.get_all_userCivil(db)
    
    def get_userCivil_by_id(self,id_user: int, db: Session = Depends(get_db)):
        return self.service.get_userCivil_by_id(db, id_user)
    
    def delete_userCivil(self, id_user: int, db: Session = Depends(get_db)):
        return self.service.delete_usercivil(db, id_user)
    
    def update_userCivil(self,  user: UserCivilSchema,  id_user: int, db: Session = Depends(get_db)):
        return self.service.update_usercivil(db, id_user, user)
