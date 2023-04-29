from typing import Optional, List, Tuple

import pydantic
import pymongo


class IndexKeyItem(pydantic.BaseModel):
    field_name: str
    sort_order: int = pydantic.Field(default=pymongo.ASCENDING)

    @pydantic.validator("sort_order")
    def sort_order_validator(cls, v):
        if v not in [pymongo.ASCENDING, pymongo.DESCENDING, 1, -1]:
            raise ValueError(
                "sort order must be 1 (ascending) or -1 (descending)"
            )
        return v

    def to_tuple(self) -> tuple:
        return self.field_name, self.sort_order

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        frozen = True


class MongoIndex(pydantic.BaseModel):
    keys: List[IndexKeyItem]
    name: Optional[str]
    unique: bool = pydantic.Field(default=False)
    background: bool = pydantic.Field(default=False)
    sparse: bool = pydantic.Field(default=False)
    expireAfterSeconds: Optional[int] = None

    @property
    def mongo_keys(self) -> Tuple[Tuple[str, int], ...]:
        return tuple(key.to_tuple() for key in self.keys)

    @property
    def mongo_index_settings(self) -> dict:
        index_settings = {
            "unique": self.unique,
            "background": self.background,
            "sparse": self.sparse,
        }
        if self.name is not None:
            index_settings["name"] = self.name
        if self.expireAfterSeconds is not None:
            index_settings["expireAfterSeconds"] = self.expireAfterSeconds
        return index_settings

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        frozen = True
