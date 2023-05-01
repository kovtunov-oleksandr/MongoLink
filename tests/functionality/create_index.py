import pymongo
import pytest
import pytest_asyncio

from mongo_link.mongo.indexes import IndexKeyItem, MongoIndex
from mongo_link.mongo.model import MongoModel
from mongo_link.mongo.motor import MotorRepository
from mongo_link.mongo.repository import RepositoryDecorators


@pytest.mark.functionality
@pytest.mark.create_index
@pytest.mark.asyncio
class TestCreateIndex:
    """Test the create_index function."""

    TEST_COLLECTION = "test_collection"
    TEST_INDEX = "test_index"

    class TestModel(MongoModel):
        name: str
        age: int

    @RepositoryDecorators.model(TestModel)
    @RepositoryDecorators.collection(TEST_COLLECTION)
    class TestRepo(MotorRepository):
        """Test repository."""

    @pytest_asyncio.fixture()
    async def motor_repository(self, motor_driver) -> TestRepo:
        repository = self.TestRepo()
        yield repository
        # await repository.collection.drop()

    @pytest.mark.asyncio
    async def test_create_index(self, motor_repository):
        index = MongoIndex(
            keys=[
                IndexKeyItem(field_name="name", sort_order=pymongo.ASCENDING),
                IndexKeyItem(field_name="age", sort_order=pymongo.DESCENDING),
            ],
            name=self.TEST_INDEX,
            unique=True,
            background=True,
        )
        await motor_repository.create_index(index)

        index_info = await motor_repository.collection.index_information()
        assert self.TEST_INDEX in index_info
        assert index_info[self.TEST_INDEX]["key"] == [("name", pymongo.ASCENDING), ("age", pymongo.DESCENDING)]
        assert index_info[self.TEST_INDEX]["unique"] is True
        assert index_info[self.TEST_INDEX]["background"] is True
