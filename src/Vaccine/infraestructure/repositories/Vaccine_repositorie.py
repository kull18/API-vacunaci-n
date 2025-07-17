from src.Vaccine.domain.scheme.Vaccine_scheme import VaccineScheme
from sqlalchemy.orm import Session
from src.Vaccine.application.models.Vaccine import Vaccine
from fastapi.responses import JSONResponse
from fastapi import HTTPException 
from typing import List

class VaccineRepositorie:

    def create_vaccine(self, db: Session, vaccine: VaccineScheme):

        new_vaccine = Vaccine(
            nameVaccine= vaccine.nameVaccine
        )

        db.add(new_vaccine)
        db.commit()
        db.refresh(new_vaccine)

        vaccine = JSONResponse(content={
            "idVaccines": new_vaccine.idVaccines,
            "nameVaccine": new_vaccine.nameVaccine
        }, status_code=201)
        
        return vaccine
    
    def get_all_vaccines(self, db: Session) -> List[Vaccine]:
        return db.query(Vaccine).all()
    
    def get_vaccine_by_id(self, db: Session, id_vaccine: int):
        vaccine = db.query(Vaccine).filter(Vaccine.idVaccines == id_vaccine).first()

        if vaccine is None:
            return HTTPException(status_code=404, detail="La vacuna no ha sido encontrada")
        
        return vaccine
    
    def update_vaccine(self, db: Session, id_vaccine: int, vaccine_data: VaccineScheme):
        vaccine = db.query(Vaccine).filter(Vaccine.idVaccines == id_vaccine).first()

        if vaccine is None:
            return HTTPException(status_code=404, detail="La vacuna no ha sido encontrada")
        

        update_data = vaccine_data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(vaccine, key, value)

        db.commit()
        db.refresh(vaccine)

        return vaccine
    
    def delete_vaccine(self, db: Session, id_vaccine: int):
        vaccine = db.query(Vaccine).filter(Vaccine.idVaccines == id_vaccine).first()

        if vaccine is None:
            return HTTPException(status_code=404, detail="La vacuna no ha sido encontrada")
        
        db.delete(vaccine)
        db.commit()

        return JSONResponse(content={
            "message": "La vacuna ha sido borrada"
        }, status_code=201)