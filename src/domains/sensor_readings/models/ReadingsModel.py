
from sqlalchemy import Column, Integer, String, Float, DateTime
from ....config.db.Base import Base

class ReadingsModel(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(Integer, nullable=False)
    sensor_type = Column(String(20), nullable=False)
    
    value = Column(Float, nullable=False)
    unit = Column(String(10), nullable=False)
    timestamp = Column(DateTime, nullable=False)
