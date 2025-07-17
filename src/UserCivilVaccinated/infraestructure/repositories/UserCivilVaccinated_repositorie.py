from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from datetime import datetime
from typing import List, Optional
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema
from src.UserCivilVaccinated.application.models.UserCivilVaccinated_model import UserCivilVaccinated
from src.Vaccine.application.models.Vaccine import Vaccine
from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.UserCivil.application.models.UserCivil_model import UserCivil
from sqlalchemy.orm import aliased

class UserCivilVaccinatedRepository:

    def create_vaccination_record(self, db: Session, vaccination_data: UserCivilVaccinatedSchema):
        
        new_vaccination = UserCivilVaccinated(
            UserCivil_idUserCivil=vaccination_data.UserCivil_idUserCivil,
            UserCivil_UserMedicVaccined=vaccination_data.UserCivil_UserMedicVaccined,
            Vaccine_idVaccines=vaccination_data.Vaccine_idVaccines,
            date=vaccination_data.date or datetime.utcnow()
        )

        db.add(new_vaccination)
        db.commit()
        db.refresh(new_vaccination)

        response = JSONResponse(content={
            "UserCivil_idUserCivil": new_vaccination.UserCivil_idUserCivil,
            "UserCivil_UserMedicVaccined": new_vaccination.UserCivil_UserMedicVaccined,
            "Vaccine_idVaccines": new_vaccination.Vaccine_idVaccines,
            "date": new_vaccination.date.isoformat()
        }, status_code=201)

        return response

    def get_vaccination_record(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int) -> Optional[UserCivilVaccinated]:
        return db.query(UserCivilVaccinated).filter(
            UserCivilVaccinated.UserCivil_idUserCivil == user_civil_id,
            UserCivilVaccinated.UserCivil_UserMedicVaccined == medic_vaccinator_id,
            UserCivilVaccinated.Vaccine_idVaccines == vaccine_id
        ).first()
    
    def get_all_vaccination_record(self, db: Session):
        return db.query(UserCivilVaccinated).all()
    
    def get_vaccinations_with_values(self, db: Session):

        UserMedicVaccined = aliased(UserCivil)

        return (
            db.query(UserCivil,UserCivilVaccinated,Vaccine)
            .join(UserCivil, UserCivilVaccinated.UserCivil_idUserCivil == UserCivil.idUserCivil)
            .join(UserMedicVaccined, UserMedicVaccined.UserMedicVaccined == UserCivilVaccinated.UserCivil_UserMedicVaccined)
            .join(Vaccine, Vaccine.idVaccines == UserCivilVaccinated.Vaccine_idVaccines)
            .all()
        )

    def get_vaccinations_by_user(self, db: Session, user_civil_id: int) -> List[UserCivilVaccinated]:
        return db.query(UserCivilVaccinated).filter(
            UserCivilVaccinated.UserCivil_idUserCivil == user_civil_id
        ).all()

    def update_vaccination_record(self,db: Session,user_civil_id: int,medic_vaccinator_id: int,vaccine_id: int,update_data: UserCivilVaccinatedSchema) -> UserCivilVaccinated:
        vaccination = self.get_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
        if vaccination is None:
            raise HTTPException(status_code=404, detail="Vaccination record not found")

        if update_data.date is not None:
            vaccination.date = update_data.date

        db.commit()
        db.refresh(vaccination)
        return vaccination

    def delete_vaccination_record(self,db: Session,user_civil_id: int,medic_vaccinator_id: int,vaccine_id: int):
        vaccination = self.get_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
        if vaccination is None:
            raise HTTPException(status_code=404, detail="Vaccination record not found")

        db.delete(vaccination)
        db.commit()
        return JSONResponse(content={
            "message": "UserCivilVaccinated ha sido borrado"
        }, status_code=201)