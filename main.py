from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.UserCivil.presentation.routes.UserCivil_routes import userCivilRoutes
from src.UserCivilVaccinated.presentation.routes.UserCivilVaccinated_rotues import userCivilVaccinated
from src.SensorCheck.presentation.routes.SensorCheck_routes import sensorRoutes
from src.Vaccine.presentation.routes.Vaccine_routes import vaccineRoutes
from src.VaccineBox.presentation.routes.VaccineBox_routes import vaccineBoxRoutes
from src.VaccineBoxVaccine.presentation.routes.VaccineBoxVaccine_routes import vaccineBoxVaccineRotutes

#title: API-rest vacunación 
#version: 1.0.0

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

