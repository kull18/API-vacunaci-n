from sqlalchemy.orm import Session
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivil as UserCivilResponse
from src.UserCivil.application.models.UserCivil_model import UserCivil
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema
from fastapi.responses import JSONResponse

class UserCivilRepository:

    def create_usercivil(self, db: Session, user: UserCivilSchema) -> UserCivilResponse:
      
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

      response = JSONResponse(content={
            "idUserCivil": new_user.idUserCivil,
            "fol": new_user.fol,
            "corporalTemperature": new_user.corporalTemperature,
            "alcoholBreat": new_user.alcoholBreat,
            "isVaccinated": new_user.isVaccinated,
            "UserMedicVaccined": new_user.UserMedicVaccined,
            "name": new_user.name, 
            "lastname": new_user.lastname
      }, status_code=201)

      return response


    def get_usercivil_by_id(self, db: Session, id_user: int):
        return db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()

    def get_all_usercivils(self, db: Session):
        return db.query(UserCivil).all()

    def update_usercivil(self,db: Session, id_user: int, user_data: UserCivilSchema):
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if not user:
            return None
        for key, value in user_data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    def delete_usercivil(self, db: Session, id_user: int):
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True
