from typing import Type

from mongo_link.mongo.driver.driver import Driver
from mongo_link.mongo.model import ModelType
from mongo_link.mongo.repository.repository import MongoRepository


def validate_cls(cls: Type[MongoRepository]):
    if not issubclass(cls, MongoRepository):
        raise TypeError(f"Class {cls.__name__} is not MongoRepository")


class RepositoryDecorators:

    @classmethod
    def driver(cls, driver_inst: Driver):
        def decorator(cls_obj: Type[MongoRepository]):
            validate_cls(cls_obj)
            cls_obj.driver = driver_inst
            return cls_obj
        return decorator

    @classmethod
    def collection(cls, collection_name: str):
        def decorator(cls_obj: Type[MongoRepository]):
            validate_cls(cls_obj)
            cls_obj.collection_name = collection_name
            return cls_obj
        return decorator

    @classmethod
    def model(cls, model_cls: Type[ModelType]):
        def decorator(cls_obj: Type[MongoRepository]):
            validate_cls(cls_obj)
            cls_obj.model_cls = model_cls
            return cls_obj
        return decorator
