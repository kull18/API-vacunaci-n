from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckResponse, SensorCheckBase
from fastapi.responses import JSONResponse

class SensorCheckRepository:
    
    def create_sensor_check(self, db: Session, sensor_data: SensorCheckBase) -> SensorCheckResponse:

            new_sensor = SensorCheck(
                measurementUnit=sensor_data.measurementUnit,
                nameSensor=sensor_data.nameSensor,
                information=sensor_data.information,
                UserCivil_idUserCivil=sensor_data.UserCivil_idUserCivil
            )
            
            db.add(new_sensor)
            db.commit()
            db.refresh(new_sensor)
            
            response = JSONResponse(content={
                "idSensorCheck": new_sensor.idSensorCheck,
                "measurementUnit":new_sensor.measurementUnit,
                "nameSensor":new_sensor.nameSensor,
                "information":new_sensor.information,
                "UserCivil_idUserCivil": new_sensor.UserCivil_idUserCivil
            }, status_code=201)

            return response
            

    def get_sensor_check_by_id(self, db: Session, sensor_id: int) -> Optional[SensorCheck]:
        sensors = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == sensor_id).first()

        if sensors is None:
            raise HTTPException(status_code=404, detail="Error to find sensor")
        
        return sensors

    def get_sensor_checks_by_user(self, db: Session, user_id: int) -> List[SensorCheck]:
        sensors = db.query(SensorCheck).filter(SensorCheck.UserCivil_idUserCivil == user_id).all()

        return sensors if sensors else []
    
    def get_all_sensor_checks(self, db: Session) -> List[SensorCheck]:
        return db.query(SensorCheck).all()

    def update_sensor_check(self, db: Session, sensor_id: int, update_data: SensorCheckBase) -> SensorCheckBase:
        sensor = self.get_sensor_check_by_id(db, sensor_id)
        if not sensor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="SensorCheck not found"
            )
            
        update_dict = update_data.dict(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(sensor, key, value)
            
        db.commit()
        db.refresh(sensor)
        return sensor

    def delete_sensor_check(self, db: Session, sensor_id: int):
        sensor = self.get_sensor_check_by_id(db, sensor_id)

        if sensor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="SensorCheck not found"
            )
            
        db.delete(sensor)
        db.commit()

        return JSONResponse(content={
            "message": "El sensor ha sido borrado correctamente"
        }, status_code=200)

    def delete_sensorCheck(self, db: Session, id_user: int):
        sensor = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == id_user).first()

        if sensor is None:
            raise HTTPException(status_code=404, detail="Sensor not found")
        
        db.delete(sensor)
        db.commit()
        return JSONResponse(content={
            "message": "El sensor ha sido borrado correctamente"
        }, status_code=200)
