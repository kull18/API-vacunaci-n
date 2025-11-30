# presentation/routes/UserCivilVaccinated_routes.py
from fastapi import APIRouter, status
from src.UserCivilVaccinated.presentation.controllers.UserCivilVaccinated_controller import UserCivilVaccinatedController
from src.UserCivilVaccinated.domain.scheme.UserCivilVaccinated_scheme import UserCivilVaccinatedSchema

userCivilVaccinated = APIRouter(
    prefix="/UserCivilVaccinated",
    tags=["UserCivilVaccinated"]
)

controller = UserCivilVaccinatedController()

# ✅ RUTAS MÁS ESPECÍFICAS PRIMERO (IMPORTANTE)
# Estas deben ir ANTES de las rutas con parámetros genéricos

# Obtener vacunas por paciente (DEBE IR PRIMERO)
userCivilVaccinated.get('/patient/{patient_id}/vaccines', status_code=status.HTTP_200_OK)(
    controller.get_patient_vaccines
)

# Obtener datos con valores
userCivilVaccinated.get('/with-values/', status_code=status.HTTP_200_OK)(
    controller.get_userCivilVaccinated_with_values
)

userCivilVaccinated.get('/with-values/{id}', status_code=status.HTTP_200_OK)(
    controller.get_userCivilVaccinated_with_values_id
)

# Obtener vacunaciones por usuario
userCivilVaccinated.get('/by-user/{user_civil_id}', status_code=status.HTTP_200_OK)(
    controller.get_userCivilVaccinated_by_user
)

# Crear nueva vacunación
userCivilVaccinated.post('/', status_code=status.HTTP_201_CREATED)(
    controller.create_userCivilVaccinated
)

# Obtener todas las vacunaciones
userCivilVaccinated.get('/', status_code=status.HTTP_200_OK)(
    controller.get_all_userCivilVaccinated
)

# ✅ RUTAS CON MÚLTIPLES PARÁMETROS AL FINAL
# Estas son más genéricas y pueden capturar cualquier cosa

# Obtener vacunación específica
userCivilVaccinated.get('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_200_OK)(
    controller.get_userCivilVaccinated
)

# Actualizar vacunación
userCivilVaccinated.put('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_200_OK)(
    controller.update_userCivilVaccinated
)

# Eliminar vacunación
userCivilVaccinated.delete('/{user_civil_id}/{medic_vaccinator_id}/{vaccine_id}', status_code=status.HTTP_204_NO_CONTENT)(
    controller.delete_userCivilVaccinated
)