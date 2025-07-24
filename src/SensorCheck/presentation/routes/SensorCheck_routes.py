from fastapi import APIRouter, Depends, HTTPException, status
from src.SensorCheck.presentation.controllers.SensorCheck_controller import SensorCheckController
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckResponse, SensorCheckBase
from sqlalchemy.orm import Session
from shared.mysql import get_db
from typing import List

sensorController = SensorCheckController()

#init routes from sensor routes
sensorRoutes = APIRouter(
    prefix="/SensorCheck", 
    tags=["SensorCheck"]
)
 
sensorRoutes.post('/', status_code=status.HTTP_201_CREATED, response_model=SensorCheckResponse) (sensorController.create_sensorCheck)

sensorRoutes.get('/', status_code=status.HTTP_200_OK, response_model=List[SensorCheckResponse]) (sensorController.get_all_sensorCheck)


sensorRoutes.get('/alcoholemia', status_code=status.HTTP_200_OK) (sensorController.get_alcoholemia)

sensorRoutes.get('/{id_sensor}', status_code=status.HTTP_200_OK, response_model=SensorCheckResponse) (sensorController.get_sensorCheck_by_id)


sensorRoutes.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=List[SensorCheckResponse]) (sensorController.get_sensorCheck_by_user)

sensorRoutes.put('/{id_sensor}', status_code=status.HTTP_200_OK, response_model=SensorCheckResponse) (sensorController.update_sensorCheck)

sensorRoutes.delete('/{id_sensor}', status_code=status.HTTP_204_NO_CONTENT) (sensorController.delete_sensorCheck)