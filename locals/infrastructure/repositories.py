from locals.domain.entities import Local
from locals.infrastructure.models import Local as LocalModel

class LocalRepository:
    """
    Repository for managing Local persistence.
    """

    @staticmethod
    def save(local: Local) -> Local:
        """
        Saves a new local to the database.
        
        Args:
            local (Local): An instance of Local containing the data to be saved.
        
        Returns:
            Local: An instance of Local containing the saved data.
        """
        local_model = LocalModel.create(
            capacity=local.capacity
        )
        return Local(
            id=local_model.id,
            capacity=local_model.capacity
        )
  
    @staticmethod
    def replace(new_local: Local) -> Local:
        """
        Replaces the existing local in the database with a new one.
        
        Args:
            local (Local): An instance of Local containing the data to be replaced.
        
        Returns:
            Local: An instance of Local containing the replaced data.
        """
        old_local = LocalModel.select().first()
        
        new_local = LocalModel.create(
            id=new_local.id,
            capacity=new_local.capacity
        )

        old_local.delete_instance()

        return Local(
            id=new_local.id,
            capacity=new_local.capacity
        )

    @staticmethod
    def get_local() -> Local:
        """
        Retrieves the current local from the database.
        
        Returns:
            Local: An instance of Local containing the current data.
        """
        local = LocalModel.select().first()

        if not local:
            return None

        return Local(
            id=local.id,
            capacity=local.capacity
        ) 
    @staticmethod
    def get_current_capacity() -> int:
        """
        Retrieves the current capacity of the local.
        
        Returns:
            int: The current capacity of the local.
        """
        local = LocalModel.select().first()
        if not local:
            return None
        return local.current_capacity
    
    @staticmethod
    def update_capacity(new_capacity: int) -> Local:
        """
        Updates the current capacity of the local.
        
        Args:
            new_capacity (int): The new capacity to be set.
        
        Returns:
            Local: An instance of Local containing the updated data.
        """
        local = LocalModel.select().first()
        if not local:
            raise ValueError("Local not found. Please create a local first.")
        
        local.current_capacity = new_capacity
        local.save()
        
        return Local(
            id=local.id,
            capacity=local.capacity
        )