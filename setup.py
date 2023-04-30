from setuptools import setup, find_packages
from mongo_link.__version__ import VERSION


__version__ = ".".join(map(str, VERSION))


GITHUB_URL = "https://github.com/kovtunov-oleksandr/MongoLink"

LONG_DESCRIPTION = """MongoLink: A Pythonic MongoDB ORM built on Pydantic 🐍🔗🌿

MongoLink is an intuitive and easy-to-use Python library for object-relational mapping (ORM) with MongoDB, built on top of Pydantic. It simplifies the interaction between your Python objects and MongoDB collections, allowing you to work with Pythonic models while leveraging MongoDB's flexibility and performance.

Key Features:

Seamless integration of MongoDB with Pydantic models
Asynchronous support for efficient and scalable operations
Customizable schema validation and alias handling
Clean, expressive, and easy-to-use API

Get started with MongoLink today and streamline your data management workflow with Python and MongoDB!

"""


setup(
    name="mongo_link",
    author="Kovtunov Oleksandr",
    author_email="kovtunov.oleksandr.00@gmail.com",
    description="Mongo link is a orm wrapper for motor and pymongo",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "pydantic==1.10.7",
        "motor==3.1.2"
    ],
    python_requires=">=3.6",
)
