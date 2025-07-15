from fastapi import APIRouter, Depends, HTTPException, status, Header
from src.UserCivil.presentation.controllers.UserCivil_controller import UserCivilController
from shared.mysql import get_db
from sqlalchemy.orm import Session
from src.UserCivil.domain.scheme.UserCivil_scheme import UserCivil, UserCivilSchema

userCivilRoutes = APIRouter(
    prefix="/UserCivil",
    tags=["UserCivil"]
)

controller = UserCivilController()

@userCivilRoutes.post("/", status_code=status.HTTP_201_CREATED, response_model=UserCivil)
def create_usercivil(user: UserCivilSchema, db: Session = Depends(get_db)):
    return controller.create_userCivil(db, user)

@userCivilRoutes.get('/', status_code=status.HTTP_200_OK)
def get_all_userCivil(db: Session = Depends(get_db)):
    return controller.get_all_userCivil(db)

@userCivilRoutes.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserCivil)
def get_usercivil_by_id(user_id: int, db: Session = Depends(get_db)):
    return controller.get_userCivil_by_id(db,user_id)

@userCivilRoutes.delete("/{user_id}",status_code=status.HTTP_200_OK)
def delete_usercivil_by_header( user_id: int, db: Session = Depends(get_db)):
    return controller.delete_userCivil(db, user_id)

@userCivilRoutes.put('/{user_id}', status_code=status.HTTP_200_OK)
def update_userCivil(user_id: int, user: UserCivilSchema, db: Session = Depends(get_db)):
    return controller.update_userCivil(db, user_id, user)