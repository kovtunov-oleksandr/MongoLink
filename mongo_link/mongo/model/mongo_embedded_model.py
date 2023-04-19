from pydantic import BaseModel


class MongoEmbeddedModel(BaseModel):
    """Don't use id field"""
