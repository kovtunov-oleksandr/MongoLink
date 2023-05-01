import asyncio
import json
import os

import pytest

from mongo_link.mongo.motor import MotorDriver
from tests.utils.config import TestsConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def config() -> TestsConfig:
    with open(os.path.join(BASE_DIR, "tests", "tests.json")) as f:
        return TestsConfig(**json.load(f))


@pytest.fixture(scope="session")
def motor_driver(config):
    return MotorDriver(
        database_name="test_database",
        uri=config.mongo.mongoUri,
    )
