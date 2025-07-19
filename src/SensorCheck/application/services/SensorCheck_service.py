import json
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.SensorCheck.infraestructure.repositories.SensorCheck_repositorie import SensorCheckRepository
from src.SensorCheck.infraestructure.repositories.SensorCheckRabbitmq_repositorie import RabbitMQRepository
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase

class SensorCheckService:

    def __init__(self):
        self.repositorie = SensorCheckRepository()
        self.rabbitRepositorie = RabbitMQRepository()     

    def create_sensorCheck(self, db: Session, sensor: SensorCheckBase) -> JSONResponse:
        message = self.repositorie.create_sensor_check(db, sensor)

        sensor_data = {
            "idSensorCheck": message.idSensorCheck,
            "measurementUnit": message.measurementUnit,
            "nameSensor": message.nameSensor,
            "information": message.information,
            "UserCivil_idUserCivil": message.UserCivil_idUserCivil
        }

        message_json = json.dumps(sensor_data)

        queue_name = self.get_queue_name_by_sensor_type(sensor.nameSensor)
        self.rabbitRepositorie.send_message(queue_name, message_json)

        return JSONResponse(content=sensor_data, status_code=201)


    def get_queue_name_by_sensor_type(self, sensor_type: str) -> str:
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
