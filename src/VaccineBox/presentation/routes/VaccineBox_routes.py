from fastapi import APIRouter, status
from src.VaccineBox.presentation.controller.VaccineBox_controller import VaccineBoxController

vaccineBoxRoutes = APIRouter(
    tags=["/VaccineBox"],
    prefix="/VaccineBox"
)

controller =    VaccineBoxController()

vaccineBoxRoutes.get('/', status_code=status.HTTP_200_OK) (controller.get_all_vaccine_boxes)

vaccineBoxRoutes.post('/', status_code=status.HTTP_201_CREATED) (controller.create_vaccine_box)

vaccineBoxRoutes.get('/{id_box}', status_code=status.HTTP_200_OK) (controller.get_vaccine_box)

vaccineBoxRoutes.put('/{id_box}', status_code=status.HTTP_200_OK) (controller.update_vaccine_box)

vaccineBoxRoutes.delete('/{id_box}', status_code=status.HTTP_204_NO_CONTENT) (controller.delete_vaccine_box)