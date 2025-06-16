from ....shared.config.settings import settings
from fastapi import HTTPException
from typing import List
import httpx
from ...domain.schemas.SensorSchema import SensorLimitsRequestSchema
from pydantic import BaseModel
from httpx import AsyncClient
import time

# ----- Cache de Token -----
_token_cache = {
    "value": None,
    "expires_at": 0  # timestamp
}
TOKEN_EXPIRATION_SECONDS = 16200  # 15 minutos


# ----- Esquema de respuesta del backend -----
class TokenResponse(BaseModel):
    id: int
    username: str
    token: str




# ----- Obtener token con caching -----
async def get_token_from_backend(email: str, password: str) -> str:
    global _token_cache

    if _token_cache["value"] and time.time() < _token_cache["expires_at"]:
        return _token_cache["value"]

    async with AsyncClient() as client:
        try:
            response = await client.post(
                f"{settings.BACKEND_HOST}/authentication/sign-in",
                json={"email": email, "password": password}
            )
            response.raise_for_status()
            token_data = TokenResponse(**response.json())

            _token_cache["value"] = token_data.token
            _token_cache["expires_at"] = time.time() + TOKEN_EXPIRATION_SECONDS

            return token_data.token

        except Exception as e:
            print("❌ Error obteniendo token:", e)
            raise HTTPException(status_code=502, detail="No se pudo obtener el token del backend.")


# ----- Obtener límites del backend -----
async def get_limits_from_backend(local_id: int) -> SensorLimitsRequestSchema:
    token = await get_token_from_backend("admin@gmail.com", "Admin@123")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(
                f"{settings.BACKEND_HOST}/locals/{local_id}",
                headers=headers
            )
            res.raise_for_status()

            data = res.json()
            formatted = {
                "maxCapacity": data.get("capacity", 0),
                "maxNoiseLevel": data.get("noiseLevel", 0),
                "smokeDetectionEnabled": data.get("smokeDetection", False),
                "restrictedArea": data.get("restrictedArea", "")
            }

            return SensorLimitsRequestSchema(**formatted)

        except Exception as e:
            print("❌ Error obteniendo límites:", e)
            raise HTTPException(status_code=502, detail="No se pudieron obtener los límites del backend.")


# ----- Reportar incidentes al backend -----
async def report_incidents_to_backend(incidents: List[dict]):
    token = await get_token_from_backend("admin@gmail.com", "Admin@123")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(
                f"{settings.BACKEND_HOST}/incidents",
                headers=headers,
                json=incidents
            )
            res.raise_for_status()
        except Exception as e:
            print("❌ Error reportando incidentes:", e)
