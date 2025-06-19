import httpx
from datetime import datetime, timezone

from shared.configuration.settings import settings
from iam.application.services import AuthorizationApplicationService
from locals.infrastructure.repositories import LocalRepository
from management.domain.valueobjects import SENSOR_TYPES
from management.domain.services import ReadingService
from management.infrastructure.repositories import ReadingRepository
from management.interfaces.resources import CreateSmokeSensorReadingResource, CreateNoiseSensorReadingResource, CreateCapacitySensorReadingResource, CreateRestrictedAreaSensorReadingResource, ReadingResource


class ReadingApplicationService:
    def __init__(self):
        self.authorization_service = AuthorizationApplicationService()
        self.local_repository = LocalRepository()
        self.reading_repository = ReadingRepository()
        self.reading_service = ReadingService()

    def get_current_iso_timestamp(self) -> str:
        """Returns the current UTC timestamp in ISO 8601 format with milliseconds and 'Z'."""
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    async def send_reading_to_backend(self, local_id: int, sensor_type_id: int, message: str, timestamp: str):
        reading_resource = ReadingResource(
            LocalId=local_id,
            SensorTypeId=sensor_type_id,
            Message=message,
            Timestamp=timestamp
        )

        async with httpx.AsyncClient() as client:
            try:
                token = await self.authorization_service.sign_in()
                headers = {"Authorization": f"Bearer {token}"}
                response = await client.post(
                    f"{settings.BACKEND_API_BASE_URL}/readings",
                    headers=headers,
                    json=reading_resource.model_dump()
                )
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise ValueError(f"Failed to send reading: {e.response.status_code} - {e.response.text}")    

    async def create_smoke_reading(self, resource: CreateSmokeSensorReadingResource):
        """
        Processes a smoke reading and reports to the backend if necessary.
        
        Args:
            resource (CreateSmokeSensorReadingResource): The smoke reading resource to be processed.
        
        Returns:
            Reading: The response containing the processed reading and any incidents reported.
        """

        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")

        local_id = local.id
        timestamp = self.get_current_iso_timestamp()
        sensor_type_id, sensor_type_name = SENSOR_TYPES["Smoke"]

        await self.send_reading_to_backend(local_id, sensor_type_id, resource.message, timestamp)
        reading = self.reading_service.create_reading(local_id, sensor_type_name, resource.message, timestamp)

        return self.reading_repository.save(reading)
    
    
    async def create_noise_reading(self, resource: CreateNoiseSensorReadingResource):
        """
        Processes a noise reading and reports to the backend if necessary.
        
        Args:
            resource (CreateNoiseSensorReadingResource): The noise reading resource to be processed.
        
        Returns:
            Reading: The response containing the processed reading and any incidents reported.
        """
        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")

        local_id = local.id
        timestamp = self.get_current_iso_timestamp()
        sensor_type_id, sensor_type_name = SENSOR_TYPES["Smoke"]

        await self.send_reading_to_backend(local_id, sensor_type_id, resource.message, timestamp)
        reading = self.reading_service.create_reading(local_id, sensor_type_name, resource.message, timestamp)

        return self.reading_repository.save(reading)
    
    
    async def create_capacity_reading(self, resource: CreateCapacitySensorReadingResource):
        """
        Processes a capacity reading and reports to the backend if necessary.
        
        Args:
            resource (CreateCapacitySensorReadingResource): The capacity reading resource to be processed.
        
        Returns:
            Reading: The response containing the processed reading and any incidents reported.
        """
        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")
        local_id = local.id

        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")

        local_id = local.id
        timestamp = self.get_current_iso_timestamp()
        sensor_type_id, sensor_type_name = SENSOR_TYPES["Capacity"]

        await self.send_reading_to_backend(local_id, sensor_type_id, resource.message, timestamp)
        reading = self.reading_service.create_reading(local_id, sensor_type_name, resource.message, timestamp)
        return self.reading_repository.save(reading)
    
    
    async def create_restricted_area_reading(self, resource: CreateRestrictedAreaSensorReadingResource):
        """
        Processes a restricted area reading and reports to the backend if necessary.

        Args:
            resource (CreateCapacitySensorReadingResource): The restricted area reading resource to be processed.

        Returns:
            Reading: The response containing the processed reading and any incidents reported.
        """
        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")

        local_id = local.id
        timestamp = self.get_current_iso_timestamp()
        sensor_type_id, sensor_type_name = SENSOR_TYPES["RestrictedArea"]

        await self.send_reading_to_backend(local_id, sensor_type_id, resource.message, timestamp)
        reading = self.reading_service.create_reading(local_id, sensor_type_name, resource.message, timestamp)
        return self.reading_repository.save(reading)
    
        
    async def get_readings_by_local_id(self, local_id: int):
        """
        Retrieves all readings associated with a specific local ID.

        Args:
            local_id (int): The unique identifier for the local.

        Returns:
            list: A list of readings associated with the specified local ID.
        """
        return self.reading_repository.get_readings_by_local_id(local_id)