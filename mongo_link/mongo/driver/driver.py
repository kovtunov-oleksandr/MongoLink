class Driver:
    """Driver class for MongoDB"""

    DEFAULT_URI = "mongodb://localhost:27017"
    DEFAULT_MAX_POOL_CONNECTIONS_SIZE = 10

    def __init__(
            self,
            database_name: str,
            uri: str = DEFAULT_URI,
            max_pool_connections_size: int = DEFAULT_MAX_POOL_CONNECTIONS_SIZE
    ):
        self.uri = uri
        self.database_name = database_name
        self.max_pool_connections_size = max_pool_connections_size
