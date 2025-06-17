class Local:
    """Represents a local entity with a specific capacity.

    Attributes:
        capacity (int): The maximum capacity of the local.
    """

    def __init__(self, capacity: int, id: int = None):
        """Initialize a Local instance.

        Args:
            capacity (int): The capacity of the local.
            id (int, optional): The unique identifier for the local. Defaults to None.
        """
        self.id = id
        self.capacity = capacity