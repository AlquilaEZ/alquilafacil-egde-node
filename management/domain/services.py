from management.domain.entities import Reading


class ReadingService:
    """Service for managing reading-related operations."""

    @staticmethod
    def create_reading(local_id: int, sensor_type: str, message: str, timestamp: str) -> dict:
        """
        Create a smoke sensor reading.

        Args:
            local_id (int): The unique identifier for the local where the sensor is located.
            sensor_type (str): The type of the sensor (e.g., "smoke", "noise", "capacity").
            message (str): The message or value from the smoke sensor.
            timestamp (str): The timestamp of the reading in ISO format.

        Returns:
            Reading: An instance of Reading containing the smoke sensor data.
        """
        return Reading(
            local_id=local_id,
            sensor_type=sensor_type,
            message=message,
            timestamp=timestamp
        )