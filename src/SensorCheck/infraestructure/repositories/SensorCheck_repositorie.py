import numpy as np
from scipy.stats import shapiro
from typing import List
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import func, case
from sqlalchemy.orm import Session

from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.SensorCheck.domain.schemas.SensorCheck_schema import SensorCheckBase, SensorCheckUpdate
from src.UserCivil.application.models.UserCivil_model import UserCivil


class SensorCheckRepository:
    def create_sensor_check(self, db: Session, sensor_data: SensorCheckBase) -> SensorCheck:
        print("[DEBUG] Datos recibidos en repositorio SensorCheck:", sensor_data)
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
            print("[DEBUG] Sensor insertado en BD:", new_sensor)
            return new_sensor
        except Exception as e:
            db.rollback()
            print("[ERROR] Excepción al crear sensor:", e)
            raise HTTPException(status_code=500, detail=f"Error al crear sensor: {str(e)}")

    def get_sensor_check_by_id(self, db: Session, sensor_id: int) -> SensorCheck:
        sensor = db.query(SensorCheck).filter(SensorCheck.idSensorCheck == sensor_id).first()
        if not sensor:
            raise HTTPException(status_code=404, detail="Sensor no encontrado")
        return sensor

    def get_sensor_checks_by_user(self, db: Session, user_id: str) -> List[SensorCheck]:
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
            # Estadísticas básicas
            stats = db.query(
                func.count(UserCivil.idUserCivil).label("total_records"),
                func.avg(UserCivil.alcoholBreat).label("average"),
                func.min(UserCivil.alcoholBreat).label("minimum"),
                func.max(UserCivil.alcoholBreat).label("maximum"),
                func.sum(case((UserCivil.alcoholBreat > 0, 1), else_=0)).label("positive_cases")
            ).filter(UserCivil.alcoholBreat.isnot(None)).first()

            if stats.total_records == 0:
                return {
                    "message": "No hay datos de alcoholemia disponibles",
                    "statistics": None,
                    "distribution": []
                }

            alcohol_category = case(
                (UserCivil.alcoholBreat == 0, "Negativo"),
                (UserCivil.alcoholBreat.between(0.01, 0.25), "Bajo"),
                (UserCivil.alcoholBreat.between(0.26, 0.50), "Medio"),
                (UserCivil.alcoholBreat > 0.50, "Alto"),
                else_="Sin datos"
            )

            distribution = db.query(
                alcohol_category.label("category"),
                func.count(UserCivil.idUserCivil).label("count")
            ).filter(UserCivil.alcoholBreat.isnot(None)).group_by(alcohol_category).all()

            return {
                "statistics": {
                    "totalRecords": stats.total_records,
                    "average": round(float(stats.average or 0), 4),
                    "minimum": round(float(stats.minimum or 0), 4),
                    "maximum": round(float(stats.maximum or 0), 4),
                    "positiveCases": stats.positive_cases,
                    "positiveRate": round((stats.positive_cases / stats.total_records) * 100, 2)
                },
                "distribution": [
                    {
                        "category": category,
                        "count": count,
                        "probability": round(count / stats.total_records, 4),
                        "percentage": round((count / stats.total_records) * 100, 2)
                    }
                    for category, count in distribution
                ]
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error al calcular estadísticas de alcoholemia: {str(e)}"
            )

    def obtener_temperaturas_por_nombre_sensor(self, db: Session) -> List[float]:
        temperaturas = (
            db.query(SensorCheck.information)
            .filter(SensorCheck.nameSensor == "temperatura")
            .all()
        )
        return [t[0] for t in temperaturas if t[0] is not None]

    def analizar_temperaturas(self, db: Session):
        temperaturas = self.obtener_temperaturas_por_nombre_sensor(db)
        temperaturas = [t for t in temperaturas if not np.isnan(t)]

        if not temperaturas:
            raise HTTPException(status_code=404, detail="No se encontraron datos válidos de temperatura para analizar")

        media = np.mean(temperaturas)
        desviacion = np.std(temperaturas)

        if len(temperaturas) < 3:
            return {
                "media": float(media),
                "desviacion_estandar": float(desviacion),
                "shapiro_stat": None,
                "shapiro_p": None,
                "interpretacion": "No hay suficientes datos para aplicar el test de normalidad"
            }

        stat, p = shapiro(temperaturas)
        resultado = (
            "Probablemente sigue una distribución normal"
            if p > 0.05
            else "Probablemente NO sigue una distribución normal"
        )

        return {
            "media": float(media),
            "desviacion_estandar": float(desviacion),
            "shapiro_stat": float(stat),
            "shapiro_p": float(p),
            "interpretacion": resultado
        }
