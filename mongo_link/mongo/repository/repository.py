from typing import Type

from mongo_link.mongo.driver.driver import Driver
from mongo_link.mongo.model import ModelType
from mongo_link.mongo.repository.exceptions import RepositoryDriverDoesNotExist
from mongo_link.utils.singleton import SingletonMeta


class MongoRepository(metaclass=SingletonMeta):
    driver: Driver = None

    database_name: str = None
    collection_name: str = None
    model_cls: Type[ModelType] = None

    _default_driver_cls = None

    def __init__(self):
        self._get_driver()

    def _get_driver(self):
        try:
            self.driver = SingletonMeta.get_instance(self._default_driver_cls)
        except ValueError:
            raise RepositoryDriverDoesNotExist(
                f"Driver does not exist. "
                + f"You should provide driver variable or create {self._default_driver_cls.__name__}"
            )
