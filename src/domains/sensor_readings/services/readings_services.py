
from ..repositories.readings_repository import ReadingsRepository
from ..schemas.ReadingSchema import SensorReadingResponseSchema
from ..utils.principal_service_cloud import get_limits_from_backend, report_incidents_to_backend


class ReadingsService:
    def __init__(self):
        self.readings_repository = ReadingsRepository()

 
    async def create_reading(self, payload: SensorReadingResponseSchema):
        
        
        limits = await get_limits_from_backend(payload.local_id)

        sensors_response = []
        incidents = []

        for reading in payload.readings:
            # Detectar incidentes
            incident = None

            if reading.type == "CAPACITY" and reading.value > limits.maxCapacity:
                incident = {
                    "type": "Aforo excedido",
                    "value": f"{int(reading.value)} / {limits.maxCapacity}",
                    "timestamp": reading.timestamp.isoformat(),
                    "local_id": payload.local_id
                }

            elif reading.type == "NOISE" and reading.value > limits.maxNoiseLevel:
                incident = {
                    "type": "Ruido excedido",
                    "value": f"{reading.value} dB / {limits.maxNoiseLevel} dB",
                    "timestamp": reading.timestamp.isoformat(),
                    "local_id": payload.local_id
                }

            elif reading.type == "SMOKE" and reading.value > 0 and limits.smokeDetectionEnabled:
                incident = {
                    "type": "Presencia de humo",
                    "value": "Sí",
                    "timestamp": reading.timestamp.isoformat(),
                    "local_id": payload.local_id
                }

            elif reading.type == "ACCESS" and reading.value > 0:
                incident = {
                    "type": "Movimiento en zona restringida",
                    "value": "Sí",
                    "timestamp": reading.timestamp.isoformat(),
                    "local_id": payload.local_id
                }

            if incident:
                incidents.append(incident)

            # Estructura para el frontend
            sensors_response.append({
                "type": reading.type,
                "readings": [{
                    "value": reading.value,
                    "unit": reading.unit,
                    "timestamp": reading.timestamp.isoformat()
                }]
            })

        # Guardar todas las lecturas
        await self.readings_repository.save_reading(payload.sensor_id, payload.readings)

        # Reportar incidentes
        if incidents:
            print("📢 Reportando incidentes al backend:", incidents)
            #await report_incidents_to_backend(incidents)

        # Retornar respuesta para frontend
        return {
            "sensors": sensors_response,
            "incidents": incidents
        }