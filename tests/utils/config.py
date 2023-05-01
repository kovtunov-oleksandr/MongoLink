from pydantic import BaseConfig, BaseModel


class Config(BaseConfig):
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    frozen = True


class Mongo(BaseModel):
    mongoUri: str

    Config = Config


class TestsConfig(BaseModel):
    mongo: Mongo

    Config = Config
