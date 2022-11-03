from pymongo import ReturnDocument
from pymongo.results import InsertOneResult
from pymongo.typings import _DocumentType
from fastapi_pagination.ext.pymongo import paginate
from settings.database import database
from utils.objectid import PyObjectId
from . import schemas


collection = database.get_collection('todo')


def get_paginated_todo_service():
    return paginate(collection)


def create_todo_service(todo: schemas.CreateTodo) -> InsertOneResult:
    obj = collection.insert_one(todo.dict())
    return collection.find_one({'_id': obj.inserted_id})


def update_todo_service(todo: schemas.UpdateTodo, pk: int) -> _DocumentType:
    return collection.find_one_and_update({'_id': PyObjectId(pk)}, {
        '$set': todo.dict()
    }, return_document=ReturnDocument.AFTER)


def delete_todo_service(pk: int) -> int:
    collection.find_one_and_delete({'_id': PyObjectId(pk)})
    return pk