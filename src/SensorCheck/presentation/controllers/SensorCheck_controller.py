from src.SensorCheck.application.services.SensorCheck_service import SensorCheckService
from sqlalchemy.orm import Session
from fastapi import Depends
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase
from shared.mysql import get_db

class SensorCheckController:

    def __init__(self):
        self.service = SensorCheckService()

    async def create_sensorCheck(self, sensor: SensorCheckBase, db: Session = Depends(get_db)):
        return await self.service.create_sensorCheck(db, sensor)

    async def get_all_sensorCheck(self, db: Session = Depends(get_db)):
        return await self.service.get_all_sensorCheck(db)

    async def get_sensorCheck_by_id(self, id_sensor: int, db: Session = Depends(get_db)):
        return await self.service.get_sensorCheck_by_id(db, id_sensor)
    
    async def get_alcoholemia(self, db: Session = Depends(get_db)):
        return await self.service.get_alcoholemia(db)

    async def update_sensorCheck(self, id_sensor: int, sensor: SensorCheckBase, db: Session = Depends(get_db)):
        return await self.service.update_sensorCheck(db, id_sensor, sensor)

    async def delete_sensorCheck(self,  id_sensor: int, db: Session = Depends(get_db)):
        return await self.service.delete_sensorCheck(db, id_sensor)

    async def get_sensorCheck_by_user(self, user_id: int, db: Session = Depends(get_db)):
        return await self.service.get_sensorCheck_by_user(db, user_id)
    
    async def get_analize_temperature(self, db: Session = Depends(get_db)):
        return await self.service.get_anilze_temperatures(db)