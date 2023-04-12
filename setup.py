from setuptools import setup, find_packages
from mongo_link.__version__ import VERSION


__version__ = '.'.join(map(str, VERSION))


setup(
    name='mongo_link',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "pydantic==1.10.7",
        "motor==3.1.2"
    ],
)
