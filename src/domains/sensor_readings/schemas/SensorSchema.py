from pydantic import BaseModel

class SensorLimitsRequestSchema(BaseModel):
    maxCapacity: int
    maxNoiseLevel: int
    smokeDetectionEnabled: bool
    restrictedArea: str