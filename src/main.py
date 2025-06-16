
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .locals_monitoring.interface.routers.readings_route import reading_route
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

app.include_router(reading_route, prefix="/api/v1/edge-node", tags=["Sensor Readings"])