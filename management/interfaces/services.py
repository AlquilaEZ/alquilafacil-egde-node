
from fastapi import APIRouter

from management.application.services import ReadingApplicationService
from management.interfaces.resources import SmokeSensorReadingResource, NoiseSensorReadingResource

reading_api = APIRouter()
reading_service = ReadingApplicationService()

@reading_api.post("/edge/readings/smoke")
async def create_smoke_reading(resource: SmokeSensorReadingResource):
    """
    Endpoint to create a smoke reading.
    This endpoint processes a smoke reading and reports to the backend if necessary.
    """
    return await reading_service.create_smoke_reading(resource)

@reading_api.post("/edge/readings/noise")
async def create_noise_reading(resource: NoiseSensorReadingResource):
    """
    Endpoint to create a noise reading.
    This endpoint processes a noise reading and reports to the backend if necessary.
    """
    return await reading_service.create_noise_reading(resource)

