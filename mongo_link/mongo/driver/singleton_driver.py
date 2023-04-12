from mongo_link.mongo.driver.driver import Driver
from mongo_link.utils.singleton import SingletonMeta


class SingletonDriver(Driver, metaclass=SingletonMeta):
    """Singleton class for Driver"""
