
from fastapi import APIRouter
from ...domain.schemas.ReadingSchema import SensorReadingResponseSchema
from ...application.services.readings_services import ReadingsService

reading_route = APIRouter()


@reading_route.post("/edge/receive-readings")
async def receive_readings(payload: SensorReadingResponseSchema):
    """
    Endpoint to receive sensor readings from the edge device.
    It processes the readings, checks for incidents, and saves them to the database.
    """
    readings_service = ReadingsService()
    return await readings_service.create_reading(payload)