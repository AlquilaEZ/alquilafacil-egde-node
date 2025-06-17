import time
import httpx

from shared.config.settings import settings
from iam.interfaces.resources import TokenResource

class AuthorizationApplicationService:
    def __init__(self):
        self.token_cache = {
            "value": None,
            "expires_at": 0  # timestamp
        }
        self.TOKEN_EXPIRATION_SECONDS = 16200  # 15 minutos

    async def sign_in(self, email: str, password: str) -> str:

        if self.token_cache["value"] and time.time() < self.token_cache["expires_at"]:
            return self.token_cache["value"]

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{settings.BACKEND_HOST}/authentication/sign-in",
                    json={"email": email, "password": password}
                )
                print("✅ Sign-in request sent to backend:", response.status_code)
                response.raise_for_status()
                token_data = TokenResource(**response.json())

                self.token_cache["value"] = token_data.token
                self.token_cache["expires_at"] = time.time() + self.TOKEN_EXPIRATION_SECONDS

                return token_data.token

            except Exception as e:
                print("❌ Error during sign-in:", e)
                raise ValueError("Failed to sign in. Please check your credentials or try again later.")