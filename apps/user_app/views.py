from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from settings.database import database
from . import schemas
from . import utils
from . import deps

collection = database.get_collection('user')

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post('/register/', response_model=schemas.UserOut)
def user_register(data: schemas.UserRegister):
    user = collection.find_one({'username': data.username})
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists!"
        )
    data.password = utils.get_hashed_password(data.password)
    dict_data = data.dict()
    dict_data.update({'active': True})
    result = collection.insert_one(dict_data)
    return collection.find_one({'_id': result.inserted_id})


@router.post(
    '/login', 
    response_model=schemas.UserLogin
)
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = collection.find_one({'username': form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password."
        )

    hashed_pass = user['password']
    if not utils.verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password."
        )
    
    return {
        'user': user,
        'access_token': utils.create_access_token(user['username']),
        'refresh_token':  utils.create_refresh_token(user['username'])
    }


@router.get('/me', response_model=schemas.UserOut)
async def get_me(user: schemas.UserOut = Depends(deps.get_current_user)):
    return user