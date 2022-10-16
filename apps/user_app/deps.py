from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from settings.database import database
from . import schemas
from . import consts


collection = database['user']


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/user/login/",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)) -> schemas.UserSystem:

    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, consts.JWT_SECRET_KEY, algorithms=[consts.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise credentials_exception
    except(jwt.JWTError, ValidationError):
        raise credentials_exception
        
    user = collection.find_one({'username': token_data.sub})
    
    if not user:
        raise credentials_exception
    
    return schemas.UserSystem(**user)