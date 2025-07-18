from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from typing import Optional, List
from src.VaccineBox.application.models.VaccineBox import VaccineBox
from src.VaccineBox.domain.scheme.VaccineBox_scheme import VaccineBoxSchema

class VaccineBoxRepository:

    def create_vaccine_box(self, db: Session, box_data: VaccineBoxSchema) -> JSONResponse:
        new_box = VaccineBox(
            amountVaccines=box_data.amountVaccines
        )

        db.add(new_box)
        db.commit()
        db.refresh(new_box)

        return JSONResponse(content={
            "idVaccineBox": new_box.idVaccineBox,
            "amountVaccines": new_box.amountVaccines
        }, status_code=201)

    def get_vaccine_box(self, db: Session, id_box: int) -> Optional[VaccineBox]:
        return db.query(VaccineBox).filter(VaccineBox.idVaccineBox == id_box).first()

    def get_all_vaccine_boxes(self, db: Session) -> List[VaccineBox]:
        return db.query(VaccineBox).all()

    def update_vaccine_box(self, db: Session, id_box: int, update_data: VaccineBoxSchema) -> VaccineBox:
        box = self.get_vaccine_box(db, id_box)
        if box is None:
            raise HTTPException(status_code=404, detail="VaccineBox not found")

        if update_data.amountVaccines is not None:
            box.amountVaccines = update_data.amountVaccines

        db.commit()
        db.refresh(box)
        return box

    def delete_vaccine_box(self, db: Session, id_box: int) -> JSONResponse:
        box = self.get_vaccine_box(db, id_box)
        if box is None:
            raise HTTPException(status_code=404, detail="VaccineBox not found")

        db.delete(box)
        db.commit()

        return JSONResponse(content={
            "message": "VaccineBox ha sido borrado"
        }, status_code=200)
