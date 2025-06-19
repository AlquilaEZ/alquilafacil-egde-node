from pydantic import BaseModel

class CreateSmokeSensorReadingResource(BaseModel):
    device_id: int
    message: str

class CreateNoiseSensorReadingResource(BaseModel):
    device_id: int
    message: str


class CreateCapacitySensorReadingResource(BaseModel):
    device_id: int
    message: str

class CreateRestrictedAreaSensorReadingResource(BaseModel):
    device_id: int
    message: str

class ReadingResource(BaseModel):
    LocalId: int
    SensorTypeId: int
    Message: str
    Timestamp: str