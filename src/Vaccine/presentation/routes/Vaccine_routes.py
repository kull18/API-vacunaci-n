from src.Vaccine.presentation.controllers.Vaccine_controller import VaccineController
from fastapi import APIRouter

vaccineRoutes = APIRouter(
    prefix="/Vaccine",
    tags=["/Vaccine"]
)

controller = VaccineController()

vaccineRoutes.post('/') (controller.create_vaccine)

vaccineRoutes.get('/') (controller.get_all_vaccines)

vaccineRoutes.put('/{id_vaccine}') (controller.update_vaccine)

vaccineRoutes.delete('/{id_vaccine}') (controller.delete_vaccine)