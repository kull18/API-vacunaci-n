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

userCivilRoutes.post("/", status_code=status.HTTP_201_CREATED, response_model=UserCivil) (controller.create_userCivil)
     
userCivilRoutes.get('/', status_code=status.HTTP_200_OK) (controller.get_all_userCivil)

userCivilRoutes.put('/vaccinated/{id_user}') (controller.update_isVaccinated)

userCivilRoutes.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserCivil) (controller.get_userCivil_by_id)
    
userCivilRoutes.delete("/{user_id}",status_code=status.HTTP_200_OK) (controller.delete_userCivil)
   
userCivilRoutes.put('/{user_id}', status_code=status.HTTP_204_NO_CONTENT) (controller.update_userCivil)
    