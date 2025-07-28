from fastapi import APIRouter, status
from src.UserCivilVaccinated.presentation.controllers.UserCivilVaccinated_controller import UserCivilVaccinatedController
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema

userCivilVaccinated = APIRouter(
    prefix="/UserCivilVaccinated",
    tags=["UserCivilVaccinated"]
)

controller = UserCivilVaccinatedController()

userCivilVaccinated.post('/', status_code=status.HTTP_201_CREATED) (controller.create_userCivilVaccinated)

userCivilVaccinated.get('/', status_code=status.HTTP_200_OK) (controller.get_all_userCivilVaccinated)

userCivilVaccinated.get('/by-user/{user_civil_id}', status_code=status.HTTP_200_OK) (controller.get_userCivilVaccinated_by_user)



userCivilVaccinated.get('/with-values/', status_code=status.HTTP_200_OK)(controller.get_userCivilVaccinated_with_values)

userCivilVaccinated.get('/with-values/{id}', status_code=status.HTTP_200_OK)(controller.get_userCivilVaccinated_with_values_id)

userCivilVaccinated.get('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_200_OK) (controller.get_userCivilVaccinated)

userCivilVaccinated.put('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_200_OK) (controller.update_userCivilVaccinated)

userCivilVaccinated.delete('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_204_NO_CONTENT) (controller.delete_userCivilVaccinated)
