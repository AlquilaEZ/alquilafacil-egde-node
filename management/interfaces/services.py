
from fastapi import APIRouter

from management.application.services import ReadingApplicationService
from management.interfaces.resources import CreateSmokeSensorReadingResource, CreateNoiseSensorReadingResource, CreateCapacitySensorReadingResource, CreateRestrictedAreaSensorReadingResource

reading_api = APIRouter()
reading_service = ReadingApplicationService()

@reading_api.post("/edge/readings/smoke")
async def create_smoke_reading(resource: CreateSmokeSensorReadingResource):
    """
    Endpoint to create a smoke reading.
    This endpoint processes a smoke reading and reports to the backend if necessary.
    """
    return await reading_service.create_smoke_reading(resource)

@reading_api.post("/edge/readings/noise")
async def create_noise_reading(resource: CreateNoiseSensorReadingResource):
    """
    Endpoint to create a noise reading.
    This endpoint processes a noise reading and reports to the backend if necessary.
    """
    return await reading_service.create_noise_reading(resource)

@reading_api.post("/edge/readings/capacity")
async def create_capacity_reading(resource: CreateCapacitySensorReadingResource):
    """
    Endpoint to create a capacity reading.
    This endpoint processes a capacity reading and reports to the backend if necessary.
    """
    return await reading_service.create_capacity_reading(resource)

@reading_api.post("/edge/readings/restricted-area")
async def create_restricted_area_reading(resource: CreateRestrictedAreaSensorReadingResource):
    """
    Endpoint to create a restricted area reading.
    This endpoint processes a restricted area reading and reports to the backend if necessary.
    """
    return await reading_service.create_restricted_area_reading(resource)

@reading_api.get("/edge/readings/local-id/{local_id}")
async def get_readings_by_local_id(local_id: int):
    """
    Endpoint to get readings by local ID.
    This endpoint retrieves all readings associated with a specific local ID.
    """
    return await reading_service.get_readings_by_local_id(local_id)
