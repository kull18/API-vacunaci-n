from src.SensorCheck.application.services.SensorCheck_service import SensorCheckService
from sqlalchemy.orm import Session
from fastapi import Depends
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase
from shared.mysql import get_db

class SensorCheckController:

    def __init__(self):
        self.service = SensorCheckService()

    def create_sensorCheck(self, sensor: SensorCheckBase, db: Session = Depends(get_db)):
        return self.service.create_sensorCheck(db, sensor)

    def get_all_sensorCheck(self, db: Session = Depends(get_db)):
        return self.service.get_all_sensorCheck(db)

    def get_sensorCheck_by_id(self, id_sensor: int, db: Session = Depends(get_db)):
        return self.service.get_sensorCheck_by_id(db, id_sensor)

    def update_sensorCheck(self, id_sensor: int, sensor: SensorCheckBase, db: Session = Depends(get_db)):
        return self.service.update_sensorCheck(db, id_sensor, sensor)

    def delete_sensorCheck(self,  id_sensor: int, db: Session = Depends(get_db)):
        return self.service.delete_sensorCheck(db, id_sensor)

    def get_sensorCheck_by_user(self, user_id: int, db: Session = Depends(get_db)):
        return self.service.get_sensorCheck_by_user(db, user_id)
