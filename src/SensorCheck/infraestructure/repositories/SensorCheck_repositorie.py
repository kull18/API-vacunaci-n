from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckResponse, SensorCheckBase
from fastapi.responses import JSONResponse

class SensorCheckRepository:
    
    def create_sensor_check(self, db: Session, sensor_data: SensorCheckBase) -> SensorCheckResponse:

            new_sensor = SensorCheck(
                measurement_unit=sensor_data.measurement_unit,
                name_sensor=sensor_data.name_sensor,
                information=sensor_data.information,
                user_civil_id=sensor_data.user_civil_id
            )
            
            db.add(new_sensor)
            db.commit()
            db.refresh(new_sensor)
            
            response = JSONResponse(content={
                "idSensorCheck": new_sensor.idSensorCheck,
                "measurement_unit":new_sensor.measurement_unit,
                "name_sensor":new_sensor.name_sensor,
                "information":new_sensor.information,
                "user_civil_id": new_sensor.user_civil_id
            }, status_code=201)

            return response
            

    def get_sensor_check_by_id(self, db: Session, sensor_id: int) -> Optional[SensorCheck]:
        return db.query(SensorCheck).filter(SensorCheck.id == sensor_id).first()

    def get_sensor_checks_by_user(self, db: Session, user_id: int) -> List[SensorCheck]:
        return db.query(SensorCheck).filter(SensorCheck.user_civil_id == user_id).all()

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

    def delete_sensor_check(self, db: Session, sensor_id: int) -> bool:
        sensor = self.get_sensor_check_by_id(db, sensor_id)

        if sensor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="SensorCheck not found"
            )
            
        db.delete(sensor)
        db.commit()
        return True
    
    def delete_sensorCheck(self, db: Session, id_user: int):
        sensor = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == id_user).first()

        if sensor is None:
            raise HTTPException(status_code=404, detail="Sensor not found")
        
        db.delete(sensor)
        db.commit()
        return True
