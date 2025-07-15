from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.UserCivil.presentation.routes.UserCivil_routes import userCivilRoutes
from src.SensorCheck.presentation.routes.SensorCheck_routes import sensorRoutes

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

