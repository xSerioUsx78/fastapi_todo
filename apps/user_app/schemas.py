from pydantic import BaseModel, constr
from utils.schemas import ObjectIDModelBase, ObjectIDConfig


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserRegister(BaseModel):
    first_name: str = None
    last_name: str = None
    username: constr(min_length=1)
    password: constr(min_length=1)


class UserOut(ObjectIDModelBase, ObjectIDConfig, BaseModel):
    username: str
    active: bool


class UserLogin(ObjectIDConfig, BaseModel):
    user: UserOut
    access_token: str
    refresh_token: str

class UserSystem(UserOut):
    password: str