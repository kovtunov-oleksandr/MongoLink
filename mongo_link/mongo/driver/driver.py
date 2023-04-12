class Driver:
    """Driver class for MongoDB"""

    DEFAULT_URI = "mongodb://localhost:27017"

    def __init__(self, database_name: str, uri: str = DEFAULT_URI):
        self.uri = uri
        self.database_name = database_name
