from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from typing import List, Optional
from src.VaccineBoxVaccine.application.models.VaccineBoxVaccine_model import VaccineBoxVaccine
from src.VaccineBoxVaccine.domain.schema.VaccineBoxVaccine_schema import VaccineBoxVaccineSchema


class VaccineBoxVaccineRepository:

    def create(self, db: Session, data: VaccineBoxVaccineSchema) -> JSONResponse:
        new_record = VaccineBoxVaccine(
            VaccineBox_idVaccineBox=data.VaccineBox_idVaccineBox,
            Vaccine_idVaccines=data.Vaccine_idVaccines
        )

        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        return JSONResponse(content={
            "VaccineBox_idVaccineBox": new_record.VaccineBox_idVaccineBox,
            "Vaccine_idVaccines": new_record.Vaccine_idVaccines
        }, status_code=201)

    def get_by_ids(self, db: Session, box_id: int, vaccine_id: int) -> Optional[VaccineBoxVaccine]:
        return db.query(VaccineBoxVaccine).filter(
            VaccineBoxVaccine.VaccineBox_idVaccineBox == box_id,
            VaccineBoxVaccine.Vaccine_idVaccines == vaccine_id
        ).first()

    def get_all(self, db: Session) -> List[VaccineBoxVaccine]:
        return db.query(VaccineBoxVaccine).all()

    def delete(self, db: Session, box_id: int, vaccine_id: int) -> JSONResponse:
        record = self.get_by_ids(db, box_id, vaccine_id)
        if not record:
            raise HTTPException(status_code=404, detail="VaccineBoxVaccine no encontrada")

        db.delete(record)
        db.commit()

        return JSONResponse(content={
            "message": "VaccineBoxVaccine ha sido eliminada"
        }, status_code=200)
