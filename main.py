import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from locals.application.services import LocalApplicationService
from management.interfaces.services import reading_api
from shared.infrastructure.database import init_db
from contextlib import asynccontextmanager

local_service = LocalApplicationService()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources at startup
    init_db()
    await local_service.create_local(1)
    yield

app = FastAPI(lifespan=lifespan)


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

app.include_router(reading_api, prefix="/api/v1/edge-node", tags=["Sensor Readings"])
