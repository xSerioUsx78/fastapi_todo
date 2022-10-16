from typing import List
from fastapi import APIRouter
from settings.database import database
from . import schemas
from . import services

collection = database.get_collection('todo')

router = APIRouter(
    prefix="/todo",
    tags=['todo']
)

@router.get("/", response_model=List[schemas.Todo])
def todo_list():
    return services.get_todo_list_service()


@router.post("/", response_model=schemas.Todo)
def todo_create(todo: schemas.CreateTodo):
    return services.create_todo_service(todo)


@router.put("/{pk}/", response_model=schemas.Todo)
def todo_update(todo: schemas.UpdateTodo, pk):
    return services.update_todo_service(todo, pk)


@router.delete("/{pk}/")
def todo_delete(pk):
    services.delete_todo_service(pk)
    return pk