from sqlalchemy.orm import Session
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivil as UserCivilResponse
from src.UserCivil.application.models.UserCivil_model import UserCivil
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from typing import List
from src.UserCivil.application.models.UserCivil_model import UserCivil

class UserCivilRepository:

    def create_usercivil(self, db: Session, user: UserCivilSchema) -> UserCivil:
        new_user = UserCivil(
            fol=user.fol,
            corporalTemperature=user.corporalTemperature,
            alcoholBreat=user.alcoholBreat,
            isVaccinated=user.isVaccinated,
            UserMedicVaccined=user.UserMedicVaccined,
            name=user.name,
            lastname=user.lastname,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("user", new_user)

        return new_user  # Devuelves el objeto ORM para que el endpoint lo serialice


    def get_usercivil_by_id(self, db: Session, id_user: int):
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()

        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")
        
        return user
         

    def get_all_usercivils(self, db: Session) -> List[UserCivil]:
        return db.query(UserCivil).all()

    def update_usercivil(self, db: Session, id_user: int, user_data: UserCivilSchema):
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")
        for key, value in user_data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    def delete_usercivil(self, db: Session, id_user: int):
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()

        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")
        
        db.delete(user)
        db.commit()
        return True
