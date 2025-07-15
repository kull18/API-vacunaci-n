from src.SensorCheck.application.services.SensorCheck_service import SensorCheckService
from sqlalchemy.orm import Session
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase


class SensorCheckController:

    def __init__(self):
        self.service = SensorCheckService()

    def create_sensorCheck(self, db: Session, sensor: SensorCheckBase):
        return self.service.create_sensorCheck(db, sensor)

    def get_all_sensorCheck(self, db: Session):
        return self.service.get_all_sensorCheck(db)

    def get_sensorCheck_by_id(self, db: Session, id_sensor: int):
        return self.service.get_sensorCheck_by_id(db, id_sensor)

    def update_sensorCheck(self, db: Session, id_sensor: int, sensor: SensorCheckBase):
        return self.service.update_sensorCheck(db, id_sensor, sensor)

    def delete_sensorCheck(self, db: Session, id_sensor: int):
        return self.service.delete_sensorCheck(db, id_sensor)

    def get_sensorCheck_by_user(self, db: Session, user_id: int):
        return self.service.get_sensorCheck_by_user(db, user_id)
