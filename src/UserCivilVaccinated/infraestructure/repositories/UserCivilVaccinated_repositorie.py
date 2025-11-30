# infraestructure/repositories/UserCivilVaccinated_repositorie.py
from collections import defaultdict
from datetime import datetime
from typing import List, Optional
from sqlalchemy import func
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
            .outerjoin(Vaccine, UserCivilVaccinated.Vaccine_idVaccines == Vaccine.idVaccines)
            .outerjoin(Patient, UserCivilVaccinated.UserCivil_idUserCivil == Patient.idUserCivil)
            .outerjoin(Medic, UserCivilVaccinated.UserCivil_UserMedicVaccined == Medic.idUserCivil)
            .all()
        )

        output = []
        vaccine_count_map = defaultdict(int)

        for vaccinated, vaccine, patient, medic in results:
            if vaccine:
                vaccine_count_map[vaccine.nameVaccine] += 1
            output.append({
                "date": vaccinated.date,
                "patient": {
                    "id": patient.idUserCivil if patient else None,
                    "name": patient.name if patient else None,
                    "lastname": patient.firstLastname if patient else None,
                },
                "medic": {
                    "id": medic.idUserCivil if medic else None,
                    "name": medic.name if medic else None,
                    "lastname": medic.firstLastname if medic else None,
                },
                "vaccine": {
                    "id": vaccine.idVaccines if vaccine else None,
                    "name": vaccine.nameVaccine if vaccine else None,
                }
            })

        return {
            "vaccinations": output,
            "vaccineCounts": dict(vaccine_count_map)
        }
    
    def get_vaccine_counts(self, db: Session):
        results = (
            db.query(
                Vaccine.nameVaccine,
                func.count(UserCivilVaccinated.Vaccine_idVaccines).label('doses_applied')
            )
            .join(
                UserCivilVaccinated,
                Vaccine.idVaccines == UserCivilVaccinated.Vaccine_idVaccines
            )
            .group_by(Vaccine.nameVaccine)
            .order_by(func.count(UserCivilVaccinated.Vaccine_idVaccines).desc())
            .all()
        )

        return {
            "vaccineCounts": [
                {
                    "vaccineName": vaccine_name,
                    "dosesApplied": doses_applied
                }
                for vaccine_name, doses_applied in results
            ]
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

    # 🆕 NUEVO MÉTODO - AGREGAR AL FINAL DE LA CLASE
    def get_patient_vaccines_by_id(self, db: Session, patient_id: int):
        """
        Obtiene todas las vacunas aplicadas a un paciente específico por su ID
        """
        Patient = aliased(UserCivil)
        Medic = aliased(UserCivil)

        # Query principal
        results = (
            db.query(
                UserCivilVaccinated,
                Vaccine,
                Patient,
                Medic
            )
            .join(
                Vaccine, 
                UserCivilVaccinated.Vaccine_idVaccines == Vaccine.idVaccines
            )
            .join(
                Patient, 
                UserCivilVaccinated.UserCivil_idUserCivil == Patient.idUserCivil
            )
            .outerjoin(
                Medic, 
                UserCivilVaccinated.UserCivil_UserMedicVaccined == Medic.idUserCivil
            )
            .filter(UserCivilVaccinated.UserCivil_idUserCivil == patient_id)
            .order_by(UserCivilVaccinated.date.desc())
            .all()
        )

        # Si no hay resultados
        if not results:
            # Verificar si el paciente existe
            patient_exists = db.query(UserCivil).filter(
                UserCivil.idUserCivil == patient_id
            ).first()
            
            if not patient_exists:
                raise HTTPException(
                    status_code=404, 
                    detail=f"Paciente con ID {patient_id} no encontrado"
                )
            
            return {
                "patient": {
                    "id": patient_id,
                    "name": None,
                    "fullName": None,
                    "isVaccinated": 0
                },
                "vaccinations": [],
                "vaccineCounts": [],
                "totalVaccinations": 0,
                "summary": {
                    "hasVaccinations": False,
                    "uniqueVaccines": 0,
                    "lastVaccinationDate": None
                }
            }

        # Procesar resultados
        vaccinations = []
        vaccine_count_map = defaultdict(int)
        patient_info = None
        last_vaccination_date = None

        for vaccinated, vaccine, patient, medic in results:
            # Guardar info del paciente (solo una vez)
            if patient_info is None:
                patient_info = {
                    "id": patient.idUserCivil,
                    "name": patient.name,
                    "firstLastname": patient.firstLastname,
                    "secondLastname": patient.secondLastname,
                    "fullName": f"{patient.name} {patient.firstLastname} {patient.secondLastname or ''}".strip(),
                    "CURP": patient.CURP,
                    "isVaccinated": patient.isVaccinated
                }

            # Contar vacunas
            vaccine_count_map[vaccine.nameVaccine] += 1

            # Guardar fecha de la última vacunación
            if last_vaccination_date is None or vaccinated.date > last_vaccination_date:
                last_vaccination_date = vaccinated.date

            # Agregar vacunación a la lista
            vaccinations.append({
                "vaccinationId": {
                    "patientId": vaccinated.UserCivil_idUserCivil,
                    "medicId": vaccinated.UserCivil_UserMedicVaccined,
                    "vaccineId": vaccinated.Vaccine_idVaccines
                },
                "date": vaccinated.date.isoformat() if vaccinated.date else None,
                "vaccine": {
                    "id": vaccine.idVaccines,
                    "name": vaccine.nameVaccine
                },
                "medic": {
                    "id": medic.idUserCivil if medic else None,
                    "name": medic.name if medic else None,
                    "firstLastname": medic.firstLastname if medic else None,
                    "fullName": f"{medic.name} {medic.firstLastname}".strip() if medic else None
                }
            })

        # Convertir conteo a lista ordenada
        vaccine_counts_list = [
            {
                "vaccineName": vaccine_name,
                "dosesApplied": count
            }
            for vaccine_name, count in sorted(
                vaccine_count_map.items(),
                key=lambda x: x[1],
                reverse=True
            )
        ]

        return {
            "patient": patient_info,
            "vaccinations": vaccinations,
            "vaccineCounts": vaccine_counts_list,
            "totalVaccinations": len(vaccinations),
            "summary": {
                "hasVaccinations": len(vaccinations) > 0,
                "uniqueVaccines": len(vaccine_count_map),
                "lastVaccinationDate": last_vaccination_date.isoformat() if last_vaccination_date else None
            }
        }