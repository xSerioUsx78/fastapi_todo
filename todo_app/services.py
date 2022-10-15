from typing import List
from pymongo import ReturnDocument
from pymongo.results import InsertOneResult
from pymongo.typings import _DocumentType
from settings.database import database
from utils.objectid import PyObjectId
from . import schemas


collection = database.get_collection('todo')


def get_todo_list_service() -> List:
    data = []
    for obj in collection.find({}):
        data.append(obj)
    return data


def create_todo_service(todo: schemas.CreateTodo) -> InsertOneResult:
    obj = collection.insert_one(todo.dict())
    return collection.find_one({'_id': obj.inserted_id})


def update_todo_service(todo: schemas.UpdateTodo, pk: int) -> _DocumentType:
    return collection.find_one_and_update({'_id': PyObjectId(pk)}, {
        '$set': todo.dict()
    }, return_document=ReturnDocument.AFTER)


def delete_todo_service(pk: int) -> None:
    collection.find_one_and_delete({'_id': PyObjectId(pk)})
    return None