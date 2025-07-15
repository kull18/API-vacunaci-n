from fastapi import APIRouter, Depends, HTTPException, status
from src.SensorCheck.presentation.controllers.SensorCheck_controller import SensorCheckController
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckResponse, SensorCheckBase
from sqlalchemy.orm import Session
from shared.mysql import get_db
from typing import List

sensorController = SensorCheckController()

sensorRoutes = APIRouter(
    prefix="/SensorCheck", 
    tags=["SensorCheck"]
)

@sensorRoutes.post('/', status_code=status.HTTP_201_CREATED, response_model=SensorCheckResponse)
def create_sensorCheck(sensor: SensorCheckBase, db: Session = Depends(get_db)):
    return sensorController.create_sensorCheck(db, sensor)


@sensorRoutes.get('/', status_code=status.HTTP_200_OK, response_model=List[SensorCheckResponse])
def get_all_sensoresCheck(db: Session = Depends(get_db)):
    return sensorController.get_all_sensorCheck(db)


@sensorRoutes.get('/{id_sensor}', status_code=status.HTTP_200_OK, response_model=SensorCheckResponse)
def get_sensorCheck_by_id(id_sensor: int, db: Session = Depends(get_db)):
    result = sensorController.get_sensorCheck_by_id(db, id_sensor)
    if not result:
        raise HTTPException(status_code=404, detail="SensorCheck not found")
    return result


@sensorRoutes.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=List[SensorCheckResponse])
def get_sensorCheck_by_user(user_id: int, db: Session = Depends(get_db)):
    return sensorController.get_sensorCheck_by_user(db, user_id)


@sensorRoutes.put('/{id_sensor}', status_code=status.HTTP_200_OK, response_model=SensorCheckResponse)
def update_sensorCheck(id_sensor: int, sensor: SensorCheckBase, db: Session = Depends(get_db)):
    return sensorController.update_sensorCheck(db, id_sensor, sensor)

@sensorRoutes.delete('/{id_sensor}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sensorCheck(id_sensor: int, db: Session = Depends(get_db)):
    sensorController.delete_sensorCheck(db, id_sensor)
    return {"detail": "SensorCheck deleted successfully"}
