from ...domain.models.ReadingsModel import ReadingsModel
from ....shared.infrastructure.database.DatabaseConnection import db
from typing import List
from ...domain.schemas.ReadingSchema import ReadingSensorRequestSchema

class ReadingsRepository:
    def __init__(self):
        self.session_factory = db.session_factory

    async def save_reading(self, sensor_id: int, reading_list: List[ReadingSensorRequestSchema]):
        
        async with self.session_factory() as session:
             
             try:
                for reading in reading_list:
                    new_reading = ReadingsModel(
                        sensor_id=sensor_id,
                        sensor_type=reading.type,
                        value=reading.value,
                        unit=reading.unit,
                        timestamp=reading.timestamp
                    )
                    session.add(new_reading)
                await session.commit()
                await session.refresh(new_reading)
                return new_reading
                
                
             except Exception as e:
                await session.rollback()

                print(f"An error occurred: {e}")
            
            