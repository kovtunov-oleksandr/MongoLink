import enum
from typing import Any, Iterable, Optional, TypeVar

from bson import ObjectId
from pydantic import BaseModel, Field, validator


class MongoModel(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')

    @validator('id', pre=True, always=True)
    def validate_id(cls, id_value):
        if id_value is not None and not ObjectId.is_valid(id_value):
            raise ValueError("Invalid ObjectId, ObjectId provides only by MongoDB")
        return id_value

    def __convert_enums_to_strings(self, obj: Any) -> Any:
        if isinstance(obj, dict):
            return {key: self.__convert_enums_to_strings(value) for key, value in obj.items()}
        elif isinstance(obj, Iterable) and not isinstance(obj, str):
            return type(obj)(self.__convert_enums_to_strings(item) for item in obj)
        elif isinstance(obj, enum.Enum):
            return obj.value
        else:
            return obj

    def mongo_dict(self, by_alias=True, **kwargs) -> dict:
        data = self.dict(**kwargs, by_alias=by_alias)
        if self.id is None and "_id" in data:
            data.pop("_id")
        return self.__convert_enums_to_strings(data)

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


ModelType = TypeVar('ModelType', bound=MongoModel)
