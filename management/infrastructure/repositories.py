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
            local_id= 2,
            type=reading.sensor_type,
            value=reading.message,
            timestamp=reading.timestamp
        )
        return Reading(
            id=reading_model.id,
            type=reading_model.type,
            value=reading_model.value,
            timestamp=reading_model.timestamp
        )