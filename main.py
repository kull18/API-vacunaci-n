from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.UserCivil.presentation.routes.UserCivil_routes import userCivilRoutes
from src.UserCivilVaccinated.presentation.routes.UserCivilVaccinated_rotues import userCivilVaccinated
from src.SensorCheck.presentation.routes.SensorCheck_routes import sensorRoutes
from src.Vaccine.presentation.routes.Vaccine_routes import vaccineRoutes
from src.VaccineBox.presentation.routes.VaccineBox_routes import vaccineBoxRoutes
from src.VaccineBoxVaccine.presentation.routes.VaccineBoxVaccine_routes import vaccineBoxVaccineRotutes
from shared.mysql import Base, engine

# Importar todos los modelos para que SQLAlchemy los registre
from src.UserCivil.application.models.UserCivil_model import UserCivil
from src.Vaccine.application.models.Vaccine import Vaccine
from src.VaccineBox.application.models.VaccineBox import VaccineBox
from src.UserCivilVaccinated.application.models.UserCivilVaccinated_model import UserCivilVaccinated
from src.SensorCheck.application.models.SensorCheck_model import SensorCheck
from src.VaccineBoxVaccine.application.models.VaccineBoxVaccine_model import VaccineBoxVaccine

#title: API-rest vacunación 
#version: 1.0.0

# Crear todas las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#init routes 
app.include_router(userCivilRoutes)
app.include_router(sensorRoutes)
app.include_router(userCivilVaccinated)
app.include_router(vaccineRoutes)
app.include_router(vaccineBoxRoutes)
app.include_router(vaccineBoxVaccineRotutes)

