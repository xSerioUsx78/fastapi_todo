from pydantic import BaseModel, constr
from utils.schemas import ObjectIDModelBase


class BaseTodo(BaseModel):
    pass


class Todo(BaseTodo, ObjectIDModelBase):
    title: str
    description: str


class CreateTodo(BaseTodo):
    title: constr(min_length=1)
    description: constr(min_length=1)

class UpdateTodo(BaseTodo):
    title: constr(min_length=1)
    description: constr(min_length=1)