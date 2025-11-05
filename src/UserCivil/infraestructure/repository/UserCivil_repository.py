from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException

from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivilSchema
from src.UserCivil.application.models.UserCivil_model import UserCivil

class UserCivilRepository:

    def create_usercivil(self, db: Session, user: UserCivilSchema) -> UserCivil:
        new_user = UserCivil(
            fol=user.fol,
            corporalTemperature=user.corporalTemperature,
            alcoholBreat=user.alcoholBreat,
            isVaccinated=user.isVaccinated,
            name=user.name,
            firstLastname=user.firstLastname,
            secondLastname=user.secondLastname,
            CURP=user.CURP,
            dayBirthday=user.dayBirthday,
            monthBirthday=user.monthBirthday,
            yearBirthday=user.yearBirthday,
            yearsOld=user.yearsOld,
            school=user.school,
            schoolGrade=user.schoolGrade,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("Created UserCivil:", new_user)

        return new_user

    def get_usercivil_by_id(self, db: Session, id_user: int) -> UserCivil:
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")
        return user

    def get_all_usercivils(self, db: Session) -> List[UserCivil]:
        return db.query(UserCivil).all()

    def update_usercivil(self, db: Session, id_user: int, user_data: UserCivilSchema) -> UserCivil:
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")

        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        print("Updated UserCivil:", user)
        return user

    def delete_usercivil(self, db: Session, id_user: int) -> bool:
        user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
        if user is None:
            raise HTTPException(status_code=404, detail="UserCivil not found")
        
        db.delete(user)
        db.commit()
        print(f"Deleted UserCivil with id {id_user}")
        return True
    def update_is_vaccinated(self, db: Session, id_user: int) -> UserCivil:
      user = db.query(UserCivil).filter(UserCivil.idUserCivil == id_user).first()
      if user is None:
        raise HTTPException(status_code=404, detail="UserCivil not found")

      user.isVaccinated = 1
      db.commit()
      db.refresh(user)
      print(f"Updated isVaccinated for UserCivil id {id_user} 1")
      return user
