from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from .objectid import PyObjectId


class ObjectIDConfig(BaseModel):

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ObjectIDModelBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


class ObjectIDModel(ObjectIDModelBase, ObjectIDConfig):
    pass