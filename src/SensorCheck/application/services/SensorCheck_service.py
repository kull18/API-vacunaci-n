import json
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.SensorCheck.infraestructure.repositories.SensorCheck_repositorie import SensorCheckRepository
from src.SensorCheck.infraestructure.repositories.SensorCheckRabbitmq_repositorie import RabbitMQRepository
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase
from src.SensorCheck.infraestructure.repositories.SensorCheckSocket_repositorie import WebSocketClientRepository
from dotenv import load_dotenv
import os
from fastapi.exceptions import HTTPException

load_dotenv()


class SensorCheckService:

    def __init__(self):
        self.repositorie = SensorCheckRepository()
        self.rabbitRepositorie = RabbitMQRepository()
        self.socketrepositorie = WebSocketClientRepository()

    async def create_sensorCheck(self, db: Session, sensor: SensorCheckBase) -> JSONResponse:
        message = self.repositorie.create_sensor_check(db, sensor)

        if not message:
            raise HTTPException(status_code=500, detail="No se pudo crear el sensor")

        try:
            probabilities = self.repositorie.get_alcohol_probabilities(db)
            await self.socketrepositorie.send_sensor_data(probabilities)

        except Exception as e:
            print("Error enviando por WebSocket:", e)

        return JSONResponse(
            content={
                "idSensorCheck": message.idSensorCheck,
                "measurementUnit": message.measurementUnit,
                "nameSensor": message.nameSensor,
                "information": message.information,
                "UserCivil_idUserCivil": message.UserCivil_idUserCivil,
                "idVaccineBox": message.idVaccineBox,          # ✅ Nuevo campo
                "idSensorsVaccine": message.idSensorsVaccine,  # ✅ Nuevo campo
            },
            status_code=201
        )

    async def get_alcoholemia(self, db: Session):
        return self.repositorie.get_alcohol_probabilities(db)

    async def get_queue_name_by_sensor_type(self, sensor_type: str) -> str:
        sensor_type = sensor_type.lower()
        match sensor_type:
            case "temperature":
                return "temperature_queue"
            case "humidity":
                return "humidity_queue"
            case "light":
                return "light_queue"
            case _:
                return "default_sensor_queue"
            
    async def get_all_sensorCheck(self, db: Session):
        return self.repositorie.get_all_sensor_checks(db)

    async def get_sensorCheck_by_id(self, db: Session, id_sensor: int):
        return self.repositorie.get_sensor_check_by_id(db, id_sensor)

    async def delete_sensorCheck(self, db: Session, id_sensor: int):
        return self.repositorie.delete_sensor_check(db, id_sensor)

    async def update_sensorCheck(self, db: Session, id_sensor: int, sensor: SensorCheckBase) -> bool:
        return self.repositorie.update_sensor_check(db, id_sensor, sensor)

    async def get_sensorCheck_by_user(self, db: Session, user_id: int):
        return self.repositorie.get_sensor_checks_by_user(db, user_id)
    
    async def get_anilze_temperatures(self, db: Session):
        return self.repositorie.analizar_temperaturas(db)
