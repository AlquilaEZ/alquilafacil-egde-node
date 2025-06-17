from locals.domain.entities import Local

class LocalService:
    """Service for managing local data."""

    def __init__(self):
        """Initialize the LocalService"""
    
    @staticmethod
    def create_local(capacity) -> Local:
        """
        Create a new local with the specified capacity.
        
          Args:
              capacity (int): The capacity of the local.
        
          Returns:
              Local: An instance of Local containing the created data.

          Raises:
              ValueError: If the capacity is invalid or if the creation fails.
        """
        try:
            if capacity <= 0:
                raise ValueError("Capacity must be a positive integer.")
        except ValueError as e:
            raise ValueError(f"Invalid capacity value: {e}")
        
        return Local(capacity)