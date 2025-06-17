import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from locals.application.services import LocalApplicationService
from management.interfaces.services import reading_api
from shared.infrastructure.database import init_db
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

init_db()

local_service = LocalApplicationService()
asyncio.run(local_service.create_local(6))

app.include_router(reading_api, prefix="/api/v1/edge-node", tags=["Sensor Readings"])