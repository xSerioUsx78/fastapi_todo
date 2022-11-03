from fastapi import APIRouter
from utils.schemas import Page
from . import schemas
from . import services

router = APIRouter(
    prefix="/todo",
    tags=['todo']
)

@router.get("/", response_model=Page[schemas.Todo])
def todo_list():
    return services.get_paginated_todo_service()


@router.post("/", response_model=schemas.Todo)
def todo_create(todo: schemas.CreateTodo):
    return services.create_todo_service(todo)


@router.put("/{pk}/", response_model=schemas.Todo)
def todo_update(todo: schemas.UpdateTodo, pk):
    return services.update_todo_service(todo, pk)


@router.delete("/{pk}/")
def todo_delete(pk):
    return services.delete_todo_service(pk)