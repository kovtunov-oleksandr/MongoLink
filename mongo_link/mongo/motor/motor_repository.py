from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorCollection

from mongo_link.mongo.exceptions import DocumentNotFound
from mongo_link.mongo.indexes.mongo_index import MongoIndex
from mongo_link.mongo.model import ModelType
from mongo_link.mongo.motor.motor_driver import MotorDriver
from mongo_link.mongo.repository import MongoRepository


class MotorRepository(MongoRepository):
    driver: MotorDriver = None
    _default_driver_cls = MotorDriver

    @property
    def collection(self) -> AsyncIOMotorCollection:
        return self.driver.db[self.collection_name]

    async def insert_one(self, model: ModelType) -> ModelType:
        """
        Insert one document to collection
        Example await user_repo.insert_one(User(name="John", age=18))
        """
        result = await self.collection.insert_one(model.mongo_dict())
        model.id = result.inserted_id
        return model

    async def insert_many(self, models: List[ModelType]) -> List[ModelType]:
        """
        Insert multiple documents to collection
        Example: await user_repo.insert_many([User(name="John", age=18), User(name="Jane", age=21)])
        """
        documents = [model.mongo_dict() for model in models]
        result = await self.collection.insert_many(documents)
        inserted_ids = result.inserted_ids
        for i, model in enumerate(models):
            model.id = inserted_ids[i]
        return models

    async def save(self, model: ModelType) -> ModelType:
        """
        Save a document to collection. If the document already exists, update it; otherwise, insert it.
        Example: await user_repo.save(User(name="John", age=18))
        """
        if model.id is None:
            return await self.insert_one(model)
        else:
            old_document = await self.find_one({'_id': model.id})
            if not old_document:
                raise DocumentNotFound(f"No document found with id {model.id}")
            new_document = model.mongo_dict()
            result = await self.collection.replace_one({'_id': model.id}, new_document)
            if result.matched_count == 0:
                raise DocumentNotFound(f"No document found with id {model.id}")
            return model

    async def find_one(self, filter_by: dict) -> Optional[ModelType]:
        """
        Find one document in collection
        Example: await user_repo.find_one({"age": {"$gte": 18}})
        """
        document = await self.collection.find_one(filter_by)
        if document:
            return self.model_cls(**document)
        return None

    async def find(self, filter_by: dict) -> List[ModelType]:
        """
        Find documents in collection
        Example: await user_repo.find({"age": {"$gte": 18}})
        """
        cursor = self.collection.find(filter_by)
        documents = await cursor.to_list(length=None)
        return [self.model_cls(**doc) for doc in documents]

    async def update_one(self, filter_by: dict, update: dict) -> None:
        """
        Update one document in collection
        Example: await user_repo.update_one({"age": {"$gte": 18}}, {"$set": {"status": "ACTIVE"}})
        """
        await self.collection.update_one(filter_by, update)

    async def delete_one(self, filter_by: dict) -> None:
        """
        Delete one document from collection
        Example: await user_repo.delete_one({"age": {"$gte": 18}})
        """
        await self.collection.delete_one(filter_by)

    async def count_documents(self, filter_by: dict) -> int:
        """
        Count documents in collection
        Example: await user_repo.count_documents({"age": {"$gte": 18}})
        """
        return self.collection.count_documents(filter_by)

    async def aggregate(self, pipeline: List[dict]) -> List[ModelType]:
        """
        Aggregate documents in collection
        Example: await user_repo.aggregate(
            [{"$match": {"age": {"$gte": 18}}}, {"$group": {"_id": "$status", "count": {"$sum": 1}}}]
        )
        """
        cursor = self.collection.aggregate(pipeline)
        documents = await cursor.to_list(length=None)
        return [self.model_cls(**doc) for doc in documents]

    async def create_index(self, index: MongoIndex):
        """
        Create an index on the collection.
        Example: await user_repo.create_index([('email', pymongo.ASCENDING)], unique=True)
        """
        await self.collection.create_index(index.mongo_keys, **index.mongo_index_settings)
