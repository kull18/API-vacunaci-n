# presentation/controllers/UserCivilVaccinated_controller.py
from src.UserCivilVaccinated.application.services.UserCivilVaccinated_service import UserCivilVaccinatedService
from sqlalchemy.orm import Session
from fastapi import Depends
from shared.mysql import get_db
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema


class UserCivilVaccinatedController:
    def __init__(self):
        self.service = UserCivilVaccinatedService()

    def create_userCivilVaccinated(self, data: UserCivilVaccinatedSchema, db: Session = Depends(get_db)):
        return self.service.create_userCivilVaccinated(db, data)

    def get_userCivilVaccinated(self, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int, db: Session = Depends(get_db)):
        return self.service.get_userCivilVaccinated(db, user_civil_id, medic_vaccinator_id, vaccine_id)

    def get_all_userCivilVaccinated(self, db: Session = Depends(get_db)):
        return self.service.get_all_userCivilVaccinated(db)
    
    def get_all_usercivil_vaccinations(self, db: Session = Depends(get_db)):
        return self.service.get_all_Usercivil_vaccinations(db)
    
    def get_userCivilVaccinated_with_values(self, db: Session = Depends(get_db)):
        return self.service.get_userCivilVaccinated_with_values(db)

    def get_userCivilVaccinated_by_user(self, user_civil_id: int, db: Session = Depends(get_db)):
        return self.service.get_userCivilVaccinated_by_user(db, user_civil_id)

    def update_userCivilVaccinated(self, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int, update_data: UserCivilVaccinatedSchema, db: Session = Depends(get_db)):
        return self.service.update_userCivilVaccinated(db, user_civil_id, medic_vaccinator_id, vaccine_id, update_data)

    def delete_userCivilVaccinated(self, user_civil_id: int, medic_vaccinator_id: int, vaccine_id: int, db: Session = Depends(get_db)):
        return self.service.delete_userCivilVaccinated(db, user_civil_id, medic_vaccinator_id, vaccine_id)
    
    def get_userCivilVaccinated_with_values_id(self, id: int, db: Session = Depends(get_db)):
        return self.service.get_userCivilVaccinated_with_values_id(db, id)
    
    # 🆕 NUEVO MÉTODO
    def get_patient_vaccines(self, patient_id: int, db: Session = Depends(get_db)):
        """
        Obtiene todas las vacunas aplicadas a un paciente específico
        """
        return self.service.get_patient_vaccines(db, patient_id)
    
# En UserCivilVaccinatedController
    def get_patient_health_summary(self, patient_id: int, db: Session = Depends(get_db)):
      """
       Obtiene resumen completo de salud: última dosis, temperaturas, alertas
      """
      return self.service.get_patient_health_summary(patient_id, db)