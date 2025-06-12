
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .domains.sensor_readings.router.readings_route import readings_route
app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(readings_route, prefix="/api/v1/edge-node", tags=["Sensor Readings"])