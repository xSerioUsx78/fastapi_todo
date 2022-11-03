from fastapi import APIRouter, Depends
from utils.schemas import Page
from apps.user_app.deps import get_current_user
from apps.user_app.schemas import UserOut
from . import schemas
from . import services

router = APIRouter(
    prefix="/todo",
    tags=['todo']
)

@router.get("/", response_model=Page[schemas.Todo])
def todo_list(_: UserOut = Depends(get_current_user)):
    return services.get_paginated_todo_service()


@router.post("/", response_model=schemas.Todo)
def todo_create(todo: schemas.CreateTodo, _: UserOut = Depends(get_current_user)):
    return services.create_todo_service(todo)


@router.put("/{pk}/", response_model=schemas.Todo)
def todo_update(todo: schemas.UpdateTodo, pk, _: UserOut = Depends(get_current_user)):
    return services.update_todo_service(todo, pk)


@router.delete("/{pk}/")
def todo_delete(pk, _: UserOut = Depends(get_current_user)):
    return services.delete_todo_service(pk)