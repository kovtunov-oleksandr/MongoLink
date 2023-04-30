from setuptools import setup, find_packages
from mongo_link.__version__ import VERSION


__version__ = ".".join(map(str, VERSION))

with open("README.md", "r") as fh:
    long_description = fh.read()

GITHUB_URL = "https://github.com/kovtunov-oleksandr/MongoLink"

setup(
    name="mongo_link",
    author="Kovtunov Oleksandr",
    author_email="kovtunov.oleksandr.00@gmail.com",
    description="Mongo link is a orm wrapper for motor and pymongo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "pydantic==1.10.7",
        "motor==3.1.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
