from pydantic import BaseModel

class SmokeSensorReadingResource(BaseModel):
    device_id: int
    message: str
    timestamp: str


class NoiseSensorReadingResource(BaseModel):
    device_id: int
    message: str
    timestamp: str


class CapacitySensorReadingResource(BaseModel):
    device_id: int
    message: str
    timestamp: str