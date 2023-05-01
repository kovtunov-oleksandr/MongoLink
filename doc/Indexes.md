# Indexes

## MongoIndex

MongoIndex is a class that represents a MongoDB index. It is used to create indexes on collections.

### Example

**Create index**
```python
import pymongo
from mongo_link.mongo.indexes import MongoIndex, IndexKeyItem
from mongo_link.mongo.model import MongoModel
from mongo_link.mongo.repository import RepositoryDecorators
from mongo_link.mongo.motor import MotorRepository

class User(MongoModel):
    name: str
    age: int


@RepositoryDecorators.collection("users")
@RepositoryDecorators.model(User)
class UserRepo(MotorRepository):
    """User repository"""


async def main():
    user_repo = UserRepo()
    index = MongoIndex(
        keys=[IndexKeyItem(field_name="name", sort_order=pymongo.ASCENDING)],
        name="test_index",
        unique=True,
        background=True,
    )
    await user_repo.create_index(index)
```