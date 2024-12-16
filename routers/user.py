from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta, datetime
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from models.user import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from database import database

router = APIRouter(
    prefix='/user',
    tags=['user']
)

SECRET_KEY='6oJMkR2lJVyLkUGW5du25CeEK32YaHcGyruZXYe5Q8s'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/token')
users_collection = database['users']

class CreateUserRequest(BaseModel):
    username: str
    full_name: str
    phone_number: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if not user:
        return False
    if not bcrypt_context.verify(password, user["hashed_password"]):
        return False
    return user


def create_access_token(username: str, user_id: str, expires_delta: timedelta):
    # Create a payload for the JWT
    encode = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    
    # Encode the JWT
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post('/register')
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = User(
        username=create_user_request.username,
        full_name=create_user_request.full_name,
        phone_number=create_user_request.phone_number,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    # Convert the SQLAlchemy model to a dictionary for MongoDB
    user_dict = {
        "username": create_user_model.username,
        "full_name": create_user_model.full_name,
        "phone_number": create_user_model.phone_number,
        "hashed_password": create_user_model.hashed_password,
        "is_active": create_user_model.is_active,
    }
    
    result = users_collection.insert_one(user_dict)

    return {
        "message": "User registered successfully!",
        "user_id": str(result.inserted_id)
    }


@router.get('/all_users')
async def get_users():
    
    users_collection = database['users']
    users = users_collection.find()
    
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    
    return user_list


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(user["username"], str(user["_id"]), timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}