from fastapi import APIRouter, status
from src.VaccineBoxVaccine.presentation.controllers.VaccineBoxVaccine_controller import VaccineBoxVaccineController

vaccineBoxVaccineRotutes = APIRouter( 
    prefix="/VaccineBoxVaccine",
    tags=["/VaccineBoxVaccine"]
)

controller = VaccineBoxVaccineController()

vaccineBoxVaccineRotutes.get('/', status_code=status.HTTP_200_OK) (controller.get_all)

