import numpy as np
from scipy.stats import binom, shapiro
from typing import List
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import func
from sqlalchemy.orm import Session

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
        sensor = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == sensor_id).first()
        if not sensor:
            raise HTTPException(status_code=404, detail="Sensor no encontrado")
        return sensor

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
        sensor = self.get_sensor_check_by_id(db, sensor_id)
        try:
            update_dict = update_data.dict(exclude_unset=True)
            for key, value in update_dict.items():
                setattr(sensor, key, value)
            db.commit()
            db.refresh(sensor)
            return sensor
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el sensor: {str(e)}")

    def delete_sensor_check(self, db: Session, sensor_id: int) -> JSONResponse:
        sensor = self.get_sensor_check_by_id(db, sensor_id)
        try:
            db.delete(sensor)
            db.commit()
            return JSONResponse(content={"message": "Sensor eliminado correctamente"}, status_code=200)
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

            return [
                {"category": level, "probability": count / total}
                for level, count in results
            ]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al calcular probabilidades: {str(e)}")

    def obtener_temperaturas_por_nombre_sensor(self, db: Session):
        from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
        temperaturas = db.query(SensorCheck.information).filter(SensorCheck.nameSensor == "temperature").all()
        return [float(t[0]) for t in temperaturas if t[0] is not None]

    def analizar_temperaturas(self, db: Session):
        temperaturas = self.obtener_temperaturas_por_nombre_sensor(db)

        temperaturas = [t for t in temperaturas if t is not None and not np.isnan(t)]

        if not temperaturas:
            raise HTTPException(status_code=404, detail="No se encontraron datos válidos de temperatura para analizar")

        media = np.mean(temperaturas)
        desviacion = np.std(temperaturas)

        if len(temperaturas) < 3:
            return {
                "media": float(media) if not np.isnan(media) else None,
                "desviacion_estandar": float(desviacion) if not np.isnan(desviacion) else None,
                "shapiro_stat": None,
                "shapiro_p": None,
                "interpretacion": "No hay suficientes datos para aplicar el test de normalidad"
            }

        stat, p = shapiro(temperaturas)

        resultado = "Probablemente sigue una distribución normal" if p > 0.05 else "Probablemente NO sigue una distribución normal"

        return {
            "media": float(media) if not np.isnan(media) else None,
            "desviacion_estandar": float(desviacion) if not np.isnan(desviacion) else None,
            "shapiro_stat": float(stat) if not np.isnan(stat) else None,
            "shapiro_p": float(p) if not np.isnan(p) else None,
            "interpretacion": resultado
        }