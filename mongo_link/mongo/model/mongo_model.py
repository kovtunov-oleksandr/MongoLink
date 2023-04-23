import json
from typing import Optional, TypeVar

from bson import ObjectId
from pydantic import BaseModel, Field, validator


class MongoModel(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')

    @validator('id', pre=True, always=True)
    def validate_id(cls, id_value):
        if id_value is not None and not ObjectId.is_valid(id_value):
            raise ValueError("Invalid ObjectId, ObjectId provides only by MongoDB")
        return id_value

    def json_like_dict(self) -> dict:
        data = json.loads(self.json(by_alias=True))
        if self.id is None and "_id" in data:
            data.pop("_id")
        else:
            data['_id'] = self.id
        return data

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


ModelType = TypeVar('ModelType', bound=MongoModel)
