from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mongo_link.mongo.driver import Driver
from mongo_link.utils.singleton import SingletonMeta


class BaseMotorDriver(Driver):
    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase

    def __init__(
            self,
            database_name: str,
            uri: str = Driver.DEFAULT_URI,
            max_pool_connections_size: int = Driver.DEFAULT_MAX_POOL_CONNECTIONS_SIZE,
            **kwargs
    ):
        super().__init__(uri, database_name)
        self.client = AsyncIOMotorClient(uri, maxPoolSize=max_pool_connections_size, **kwargs)
        self.db = self.client[database_name]


class MotorDriver(BaseMotorDriver, metaclass=SingletonMeta):
    """Singleton class for MotorDriver"""
