from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#title: API-rest pacientes 
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
app.add_route()

