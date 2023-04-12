from pydantic import BaseModel


class MongoNestedModel(BaseModel):
    """Don't use id field in nested model"""
