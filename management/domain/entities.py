class Reading:
    """Represents a reading from a sensor."""
    def __init__(self, local_id: int, sensor_type: str, message: str, timestamp: str):
        """Initialize a Reading instance.

        Args:
            local_id (int): The unique identifier for the local where the sensor is located.
            sensor_type (str): The type of the sensor (e.g., "smoke", "noise", "capacity").
            message (str): The message or value from the sensor.
            timestamp (str): The timestamp of the reading in ISO format.
        """
        self.local_id = local_id
        self.sensor_type = sensor_type
        self.message = message
        self.timestamp = timestamp

class SmokeSensorReading:
    """Represents a smoke sensor reading."""
    def __init__(self, device_id: int, message: str, timestamp: str):
        """Initialize a SmokeSensorReading instance.

        Args:
            device_id (int): The unique identifier for the smoke sensor.
            message (str): The message or value from the smoke sensor.
            timestamp (str): The timestamp of the reading in ISO format.
        """
        super().__init__("smoke", message, timestamp)
        self.device_id = device_id

class NoiseSensorReading:
    """Represents a noise sensor reading."""
    def __init__(self, device_id: int, message: str, timestamp: str):
        """Initialize a NoiseSensorReading instance.

        Args:
            device_id (int): The unique identifier for the noise sensor.
            message (str): The message or value from the noise sensor.
            timestamp (str): The timestamp of the reading in ISO format.
        """
        super().__init__("noise", message, timestamp)
        self.device_id = device_id

class CapacitySensorReading:
    """Represents a capacity sensor reading."""
    def __init__(self, device_id: int, message: str, timestamp: str):
        """Initialize a CapacitySensorReading instance.

        Args:
            device_id (int): The unique identifier for the capacity sensor.
            message (str): The message or value from the capacity sensor.
            timestamp (str): The timestamp of the reading in ISO format.
        """
        super().__init__("capacity", message, timestamp)
        self.device_id = device_id