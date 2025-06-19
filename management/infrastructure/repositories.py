from management.domain.entities import Reading
from management.infrastructure.models import Reading as ReadingModel

class ReadingRepository:
    """
    Repository for managing Reading persistence.
    """

    @staticmethod
    def save(reading: Reading) -> Reading:
        """
        Saves a new reading to the database.

        Args:
            reading (Reading): An instance of Reading containing the data to be saved.

        Returns:
            Reading: An instance of Reading containing the saved data.
        """
        reading_model = ReadingModel.create(
            local_id= reading.local_id,
            sensor_type=reading.sensor_type,
            message=reading.message,
            timestamp=reading.timestamp
        )
        return Reading(
            local_id=reading_model.local_id,
            sensor_type=reading_model.sensor_type,
            message=reading_model.message,
            timestamp=reading_model.timestamp
        )

    @staticmethod
    def get_readings_by_local_id(local_id: int) -> list[Reading]:
        """
        Retrieves all readings for a specific local ID.

        Args:
            local_id (int): The unique identifier for the local.

        Returns:
            list[Reading]: A list of Reading instances associated with the specified local ID.
        """
        readings = ReadingModel.select().where(ReadingModel.local_id == local_id)
        return [Reading(
            local_id=reading.local_id,
            sensor_type=reading.sensor_type,
            message=reading.message,
            timestamp=reading.timestamp
        ) for reading in readings]