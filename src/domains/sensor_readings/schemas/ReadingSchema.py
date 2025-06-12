from datetime import datetime
from pydantic import BaseModel
from typing import List

class ReadingSensorRequestSchema(BaseModel):
    type: str
    value: float
    unit: str
    timestamp: datetime


class SensorReadingResponseSchema(BaseModel):
    local_id: int
    sensor_id: int
    readings: List[ReadingSensorRequestSchema]
    