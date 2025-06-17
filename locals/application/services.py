import httpx

from shared.config.settings import settings
from iam.application.services import AuthorizationApplicationService
from locals.domain.entities import Local
from locals.domain.services import LocalService
from locals.infrastructure.repositories import LocalRepository

class LocalApplicationService:
    """
    Application service for creating a local entity.
    """


    def __init__(self):
        """
        Initialize the LocalApplicationService with dependencies.
        """
        self.authorization_service = AuthorizationApplicationService()
        self.local_repository = LocalRepository()
        self.local_service = LocalService()

    async def create_local(self, local_id: int) -> Local:
        """
        Creates a new local if it does not already exist.

        Args:
            local_id (int): The ID of the local to be created.

        Returns:
            Local: An instance of Local containing the created data.

        Raises:
            ValueError: If the local cannot be created or the API call fails.
        """

        current_local = self.local_repository.get_local()

        if current_local and current_local.id == local_id:
            return current_local
        
        local_data = await self.get_local_data_by_id(local_id)
        if not local_data:
            raise ValueError("Local data not found or invalid.")
        
        local_entity = Local(
            id=local_data["id"],
            capacity=local_data["capacity"]
        )

        if local_entity.id != local_id:
            return self.local_repository.replace(local_entity)

        return self.local_repository.save(local_entity)
            


    async def get_local_data_by_id(self, local_id: int) -> dict:
        """
        Fetches local data from the external API.

        Args:
            local_id (int): ID of the local to fetch.

        Returns:
            dict: Data retrieved from the API.

        Raises:
            ValueError: If the API request fails or returns invalid data.
        """
        async with httpx.AsyncClient() as client:
            try:
                token = await self.authorization_service.sign_in("admin@gmail.com", "Admin@123")
                headers = {"Authorization": f"Bearer {token}"}
                response = await client.get(f"{settings.BACKEND_HOST}/locals/{local_id}", headers=headers)
                response.raise_for_status()
                local_response = response.json()
                if not local_response or "id" not in local_response:
                    raise ValueError("Invalid local data received from the API.")
                return local_response
            except httpx.HTTPStatusError as e:
                raise ValueError(f"Failed to fetch local data: {e.response.status_code} - {e.response.text}")