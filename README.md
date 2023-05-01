# MongoLink

MongoLink: A Pythonic MongoDB ORM built on Pydantic 🐍🔗🌿

MongoLink is an intuitive and easy-to-use Python library for object-relational mapping (ORM) with MongoDB, built on top of Pydantic. It simplifies the interaction between your Python objects and MongoDB collections, allowing you to work with Pythonic models while leveraging MongoDB's flexibility and performance.

Key Features:

Seamless integration of MongoDB with Pydantic models
Asynchronous support for efficient and scalable operations
Customizable schema validation and alias handling
Clean, expressive, and easy-to-use API

Get started with MongoLink today and streamline your data management workflow with Python and MongoDB!

Full documentation is available at [doc](./doc/Doc.md).

## Installation

MongoLink is not available on PyPI, can be installed with pip:

```bash
pip install mongo-link
```

## Quickstart


### Driver
`Driver` is a class that provides a set of methods for interacting with MongoDB.
You can create a Driver by inheriting from the `Driver` class:

```python
from mongo_link.mongo.motor import MotorDriver

driver = MotorDriver("database_name")
```

The `MotorDriver` class uses the `motor` library to interact with MongoDB.
By default, the `MotorDriver` class connects to the MongoDB instance running on localhost:27017.

You also can specify the MongoDB connection string:

```python
from mongo_link.mongo.motor import MotorDriver

driver = MotorDriver("database_name", "mongodb://localhost:27017")
```

### Models
MongoLink is built on top of Pydantic models, so you can use all the features of Pydantic models in your 
MongoLink models.

```python
from typing import List
from mongo_link.mongo.model import MongoModel, MongoEmbeddedModel


class User(MongoEmbeddedModel):
    name: str
    age: int


class Group(MongoModel):
    name: str
    users: List[User]
```

* `MongoModel` is a model that can be stored in MongoDB. Also, it has an `id` field.
* `MongoEmbeddedModel` is a model that can be part of `MongoModel`, but it has no `id` field. 
It's just a nested object of mongo document.

### Repositories

To start working with your models, you need to create a `Repository` for each model. 
A Repository is a class that provides a set of methods for interacting with a MongoDB collection. 
You can create a Repository for a model by inheriting from the `Repository` class:

```python
from mongo_link.mongo.motor import MotorRepository
from mongo_link.mongo.repository import RepositoryDecorators
from mongo_link.mongo.model import MongoModel


class User(MongoModel):
    name: str
    age: int


@RepositoryDecorators.collection("users")
@RepositoryDecorators.model(User)
class UserRepo(MotorRepository):
    """User repository"""


async def main():
    user_repo = UserRepo()
    user = User(name="John", age=30)
    await user_repo.insert_one(user)
    user = await user_repo.find_one({"name": "John"})
    print(user)

```

* `@RepositoryDecorators.collection` decorator specifies the name of the MongoDB collection that the Repository will work with. 
* `@RepositoryDecorators.model` decorator specifies the model that the Repository will work with.

⚠️ **Warning:** Repository implements Singleton pattern, so you can use the same Repository instance for all operations.

