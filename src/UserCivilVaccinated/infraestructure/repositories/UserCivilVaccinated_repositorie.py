from collections import defaultdict
from datetime import datetime
from typing import List, Optional

from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload, aliased

from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema
from src.UserCivilVaccinated.application.models.UserCivilVaccinated_model import UserCivilVaccinated
from src.Vaccine.application.models.Vaccine import Vaccine
from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.UserCivil.application.models.UserCivil_model import UserCivil


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

        return JSONResponse(content={
            "UserCivil_idUserCivil": new_vaccination.UserCivil_idUserCivil,
            "UserCivil_UserMedicVaccined": new_vaccination.UserCivil_UserMedicVaccined,
            "Vaccine_idVaccines": new_vaccination.Vaccine_idVaccines,
            "date": new_vaccination.date.isoformat()
        }, status_code=201)

    def get_vaccination_record(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int) -> Optional[UserCivilVaccinated]:
        return db.query(UserCivilVaccinated).filter(
            UserCivilVaccinated.UserCivil_idUserCivil == user_civil_id,
            UserCivilVaccinated.UserCivil_UserMedicVaccined == medic_vaccinator_id,
            UserCivilVaccinated.Vaccine_idVaccines == vaccine_id
        ).first()

    def get_all_user_civil_vaccinations(self, db: Session):
        return db.query(UserCivilVaccinated).options(
            joinedload(UserCivilVaccinated.usercivil_patient),
            joinedload(UserCivilVaccinated.usercivil_medic),
            joinedload(UserCivilVaccinated.vaccine)
        ).all()

    def get_all_vaccination_record(self, db: Session):
        return db.query(UserCivilVaccinated).all()

    def get_vaccinations_by_user(self, db: Session, user_civil_id: int) -> List[UserCivilVaccinated]:
        return db.query(UserCivilVaccinated).filter(
            UserCivilVaccinated.UserCivil_idUserCivil == user_civil_id
        ).all()

    def update_vaccination_record(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int, update_data: UserCivilVaccinatedSchema) -> UserCivilVaccinated:
        vaccination = self.get_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
        if vaccination is None:
            raise HTTPException(status_code=404, detail="Vaccination record not found")

        if update_data.date is not None:
            vaccination.date = update_data.date

        db.commit()
        db.refresh(vaccination)
        return vaccination

    def delete_vaccination_record(self, db: Session, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int):
        vaccination = self.get_vaccination_record(db, user_civil_id, medic_vaccinator_id, vaccine_id)
        if vaccination is None:
            raise HTTPException(status_code=404, detail="Vaccination record not found")

        db.delete(vaccination)
        db.commit()

        return JSONResponse(content={
            "message": "UserCivilVaccinated ha sido borrado"
        }, status_code=201)

    def get_vaccinations_with_values(self, db: Session):
        Patient = aliased(UserCivil)
        Medic = aliased(UserCivil)

        results = (
            db.query(
                UserCivilVaccinated,
                Vaccine,
                Patient,
                Medic
            )
            .join(Vaccine, UserCivilVaccinated.Vaccine_idVaccines == Vaccine.idVaccines)
            .join(Patient, UserCivilVaccinated.UserCivil_idUserCivil == Patient.idUserCivil)
            .join(Medic, UserCivilVaccinated.UserCivil_UserMedicVaccined == Medic.idUserCivil)
            .all()
        )

        output = []
        vaccine_count_map = defaultdict(int)

        for vaccinated, vaccine, patient, medic in results:
            vaccine_count_map[vaccine.nameVaccine] += 1
            output.append({
                "date": vaccinated.date,
                "patient": {
                    "id": patient.idUserCivil,
                    "name": patient.name,
                    "lastname": patient.firstLastname,
                },
                "medic": {
                    "id": medic.idUserCivil,
                    "name": medic.name,
                    "lastname": medic.firstLastname,
                },
                "vaccine": {
                    "id": vaccine.idVaccines,
                    "name": vaccine.nameVaccine,
                }
            })

        return {
            "vaccinations": output,
            "vaccineCounts": dict(vaccine_count_map)
        }

    def get_vaccinations_with_values_id(self, db: Session, id: int):
        Patient = aliased(UserCivil)
        Medic = aliased(UserCivil)

        results = (
            db.query(
                UserCivilVaccinated,
                Vaccine,
                Patient,
                Medic
            )
            .join(Vaccine, UserCivilVaccinated.Vaccine_idVaccines == Vaccine.idVaccines)
            .join(Patient, UserCivilVaccinated.UserCivil_idUserCivil == Patient.idUserCivil)
            .join(Medic, UserCivilVaccinated.UserCivil_UserMedicVaccined == Medic.idUserCivil)
            .filter(Patient.idUserCivil == id)
            .all()
        )

        if not results:
            return {
                "vaccinations": [],
                "vaccineCounts": {}
            }

        output = []
        vaccine_count_map = defaultdict(int)

        for vaccinated, vaccine, patient, medic in results:
            vaccine_count_map[vaccine.nameVaccine] += 1
            output.append({
                "date": vaccinated.date,
                "patient": {
                    "id": patient.idUserCivil,
                    "name": patient.name,
                    "lastname": patient.firstLastname,
                },
                "medic": {
                    "id": medic.idUserCivil,
                    "name": medic.name,
                    "lastname": medic.firstLastname,
                },
                "vaccine": {
                    "id": vaccine.idVaccines,
                    "name": vaccine.nameVaccine,
                }
            })

        return {
            "vaccinations": output,
            "vaccineCounts": dict(vaccine_count_map)
        }
