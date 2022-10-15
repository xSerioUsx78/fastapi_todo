from pydantic import BaseModel, constr
from utils.schemas import ObjectIDModel


class BaseTodo(BaseModel):
    pass


class Todo(BaseTodo, ObjectIDModel):
    title: str
    description: str


class CreateTodo(BaseTodo):
    title: constr(min_length=1)
    description: constr(min_length=1)

class UpdateTodo(BaseTodo):
    title: constr(min_length=1)
    description: constr(min_length=1)