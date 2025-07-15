from src.SensorCheck.infraestructure.repositories.SensorCheck_repositorie import SensorCheckRepository
from sqlalchemy.orm import Session
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase
from fastapi.responses import JSONResponse


class SensorCheckService:

    def __init__(self):
        self.repositorie = SensorCheckRepository()

    def create_sensorCheck(self, db: Session, sensor: SensorCheckBase) -> JSONResponse:
        return self.repositorie.create_sensor_check(db, sensor)
    
    def get_all_sensorCheck(self, db: Session):
        return self.repositorie.get_all_sensor_checks(db)
    
    def get_sensorCheck_by_id(self, db: Session, id_sensor: int):
        return self.repositorie.get_sensor_check_by_id(db, id_sensor)
    
    def delete_sensorCheck(self, db: Session, id_sensor: int):
        return self.repositorie.delete_sensor_check(db, id_sensor)

    def update_sensorCheck(self, db: Session, id_sensor: int, sensor: SensorCheckBase) -> bool:
        return self.repositorie.update_sensor_check(db, id_sensor, sensor)

    def get_sensorCheck_by_user(self, db: Session, user_id: int):
        return self.repositorie.get_sensor_checks_by_user(db, user_id)
