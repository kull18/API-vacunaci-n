from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
import json
from scipy.stats import binom

from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase, SensorCheckUpdate


class SensorCheckRepository:

    def create_sensor_check(self, db: Session, sensor_data: SensorCheckBase) -> SensorCheck:
        try:
            new_sensor = SensorCheck(
                measurementUnit=sensor_data.measurementUnit,
                nameSensor=sensor_data.nameSensor,
                information=sensor_data.information,
                UserCivil_idUserCivil=sensor_data.UserCivil_idUserCivil
            )

            db.add(new_sensor)
            db.commit()
            db.refresh(new_sensor)

            return new_sensor
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al crear sensor: {str(e)}")

    def get_sensor_check_by_id(self, db: Session, sensor_id: int) -> SensorCheck:
        try:
            sensor = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == sensor_id).first()
            if sensor is None:
                raise HTTPException(status_code=404, detail="Sensor not found")
            return sensor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener el sensor: {str(e)}")

    def get_sensor_checks_by_user(self, db: Session, user_id: int) -> List[SensorCheck]:
        try:
            return db.query(SensorCheck).filter(SensorCheck.UserCivil_idUserCivil == user_id).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener sensores del usuario: {str(e)}")

    def get_all_sensor_checks(self, db: Session) -> List[SensorCheck]:
        try:
            return db.query(SensorCheck).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener todos los sensores: {str(e)}")

    def update_sensor_check(self, db: Session, sensor_id: int, update_data: SensorCheckUpdate) -> SensorCheck:
        try:
            sensor = self.get_sensor_check_by_id(db, sensor_id)

            update_dict = update_data.dict(exclude_unset=True)
            for key, value in update_dict.items():
                setattr(sensor, key, value)

            db.commit()
            db.refresh(sensor)
            return sensor
        except HTTPException:
            raise
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el sensor: {str(e)}")

    def delete_sensor_check(self, db: Session, sensor_id: int) -> JSONResponse:
        try:
            sensor = self.get_sensor_check_by_id(db, sensor_id)

            db.delete(sensor)
            db.commit()

            return JSONResponse(content={
                "message": "El sensor ha sido borrado correctamente"
            }, status_code=200)
        except HTTPException:
            raise
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar el sensor: {str(e)}")

    def get_alcohol_probabilities(self, db: Session):
        try:
            total = db.query(func.count(SensorCheck.idSensorCheck))\
                      .filter(SensorCheck.nameSensor == "alcoholemia")\
                      .scalar()

            if total == 0:
                return []

            results = db.query(SensorCheck.measurementUnit, func.count(SensorCheck.idSensorCheck))\
                        .filter(SensorCheck.nameSensor == "alcoholemia")\
                        .group_by(SensorCheck.measurementUnit)\
                        .all()

            probabilities = [
                {"category": level, "probability": count / total}
                for level, count in results
            ]

            return probabilities
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al calcular probabilidades: {str(e)}")

    def create_sensor_check_and_calc_binomial(self, db: Session, sensor_data: SensorCheck):
        try:
            n = 10  # número de pruebas
            k = 5   # éxitos deseados

            total = db.query(SensorCheck)\
                      .filter(SensorCheck.nameSensor == sensor_data.nameSensor)\
                      .count()

            exitos = db.query(SensorCheck)\
                       .filter(
                           SensorCheck.nameSensor == sensor_data.nameSensor,
                           SensorCheck.information == sensor_data.information
                       ).count()

            p = exitos / total if total > 0 else 0

            prob_binomial = binom.pmf(k, n, p)

            response = json.dumps({
                "sensor": {
                    "measurementUnit": sensor_data.measurementUnit,
                    "nameSensor": sensor_data.nameSensor,
                    "information": sensor_data.information,
                    "UserCivil_idUserCivil": sensor_data.UserCivil_idUserCivil
                },
                "probabilidad_binomial": prob_binomial,
                "parametros": {"n": n, "k": k, "p": p}
            })

            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al calcular binomial: {str(e)}")
