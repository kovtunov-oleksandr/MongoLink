from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mongo_link.mongo.driver import SingletonDriver


class MotorDriver(SingletonDriver):
    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase

    def __init__(
            self,
            database_name: str,
            uri: str = SingletonDriver.DEFAULT_URI,
            max_pool_connections_size: int = SingletonDriver.DEFAULT_MAX_POOL_CONNECTIONS_SIZE,
            **kwargs
    ):
        super().__init__(uri, database_name)
        self.client = AsyncIOMotorClient(uri, maxPoolSize=max_pool_connections_size, **kwargs)
        self.db = self.client[database_name]
