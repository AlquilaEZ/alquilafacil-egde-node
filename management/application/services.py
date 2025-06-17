from locals.infrastructure.repositories import LocalRepository
from management.domain.services import ReadingService
from management.infrastructure.repositories import ReadingRepository
from management.interfaces.resources import SmokeSensorReadingResource, NoiseSensorReadingResource, CapacitySensorReadingResource


class ReadingApplicationService:
    def __init__(self):
        self.local_repository = LocalRepository()
        self.reading_repository = ReadingRepository()
        self.reading_service = ReadingService()

    async def create_smoke_reading(self, resource: SmokeSensorReadingResource):
        """
        Processes a smoke reading and reports to the backend if necessary.
        
        Args:
            resource (SmokeSensorReadingResource): The smoke reading resource to be processed.
        
        Returns:
            dict: The response containing the processed reading and any incidents reported.
        """

        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")
        local_id = local.id
        reading = self.reading_service.create_reading(local_id, "Smoke", resource.message, resource.timestamp)

        return self.reading_repository.save(reading)
    
    async def create_noise_reading(self, resource: NoiseSensorReadingResource):
        """
        Processes a noise reading and reports to the backend if necessary.
        
        Args:
            resource (NoiseSensorReadingResource): The noise reading resource to be processed.
        
        Returns:
            dict: The response containing the processed reading and any incidents reported.
        """
        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")
        local_id = local.id
        reading = self.reading_service.create_reading(local_id, "Noise", resource.message, resource.timestamp)

        return self.reading_repository.save(reading)
    
    async def create_capacity_reading(self, resource: CapacitySensorReadingResource):
        """
        Processes a capacity reading and reports to the backend if necessary.
        
        Args:
            resource (CapacitySensorReadingResource): The capacity reading resource to be processed.
        
        Returns:
            dict: The response containing the processed reading and any incidents reported.
        """
        local = self.local_repository.get_local()
        if not local:
            raise ValueError("Local not found. Please create a local first.")
        local_id = local.id
        reading = self.reading_service.create_reading(local_id, "Capacity", resource.message, resource.timestamp)

        return self.reading_repository.save(reading)
        