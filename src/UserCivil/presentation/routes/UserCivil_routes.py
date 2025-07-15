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

@userCivilRoutes.get("/")
def get_usercivil_by_header(user_id: int = Header(..., alias="X-user_id")):
    return controller.get_userCivil_by_id(user_id)

@userCivilRoutes.delete("/")
def get_usercivil_by_header(user_id: int = Header(..., alias="X-user_id")):
    return controller.get_userCivil_by_id(user_id)
