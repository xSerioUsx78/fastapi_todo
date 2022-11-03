from typing import Sequence, Generic
from pydantic import BaseModel, Field, conint
from bson.objectid import ObjectId
from fastapi_pagination import Page as FastApiPaginationPage, Params
from fastapi_pagination.bases import AbstractParams, BasePage, T
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


class Page(ObjectIDConfig, BasePage[T], Generic[T]):
    page: conint(ge=1)  # type: ignore
    size: conint(ge=1)  # type: ignore

    __params_type__ = Params

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: AbstractParams,
    ) -> FastApiPaginationPage[T]:
        if not isinstance(params, Params):
            raise ValueError("Page should be used with Params")

        return cls(
            total=total,
            items=items,
            page=params.page,
            size=params.size,
        )