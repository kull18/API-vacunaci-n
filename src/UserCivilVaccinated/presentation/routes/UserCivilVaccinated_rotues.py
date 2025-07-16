from fastapi import APIRouter
from src.UserCivilVaccinated.presentation.controllers.UserCivilVaccinated_controller import UserCivilVaccinatedController

userCivilVaccinated = APIRouter(
    tags="UserCivilVaccinated",
    prefix=["/UserCivilVaccinated"]
)

controller = UserCivilVaccinatedController()

userCivilVaccinated.post('/') (controller.create_userCivilVaccinated)

userCivilVaccinated.get('/') (controller.get_all_userCivilVaccinated)
