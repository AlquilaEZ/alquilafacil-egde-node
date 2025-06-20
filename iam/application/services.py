import time
import httpx
from httpx import ReadTimeout
from shared.configuration.settings import settings
from iam.interfaces.resources import TokenResource

class AuthorizationApplicationService:
    def __init__(self):
        self.token_cache = {
            "value": None,
            "expires_at": 0  # timestamp
        }
        self.TOKEN_EXPIRATION_SECONDS = settings.TOKEN_EXPIRATION_SECONDS

            
            
    async def sign_in(self) -> str:
        if self.token_cache["value"] and time.time() < self.token_cache["expires_at"]:
            return self.token_cache["value"]

        async with httpx.AsyncClient(timeout=10.0) as client:  # ⏱ Timeout explícito
            try:
                response = await client.post(
                    f"{settings.BACKEND_API_BASE_URL}/authentication/sign-in",
                    json={
                        "email": settings.AUTHENTICATION_EMAIL,
                        "password": settings.AUTHENTICATION_PASSWORD
                    }
                )
                print("✅ Sign-in request sent to backend:", response.status_code)
                response.raise_for_status()

                token_data = TokenResource(**response.json())

                self.token_cache["value"] = token_data.token
                self.token_cache["expires_at"] = time.time() + self.TOKEN_EXPIRATION_SECONDS

                return token_data.token

            except ReadTimeout:
                print("⏱❌ Timeout al intentar conectar con el backend.")
                raise ValueError("El servidor tardó demasiado en responder. Intenta más tarde.")
            
            except httpx.HTTPStatusError as e:
                print(f"🔒 Error HTTP: {e.response.status_code} - {e.response.text}")
                raise ValueError("Credenciales inválidas o error en el backend.")
            
            except Exception as e:
                print("❌ Error inesperado durante el inicio de sesión:", e)
                raise ValueError("Fallo inesperado al iniciar sesión. Verifica la conexión.")