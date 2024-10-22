from dotenv import load_dotenv
import os
import jwt
from datetime import datetime, timedelta, timezone
from litestar.exceptions import NotAuthorizedException
from litestar.connection import ASGIConnection
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from passlib.context import CryptContext
import jwt.exceptions
from sqlalchemy import select

from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
    
async def authenticate_user(session: AsyncSession, name: str, password: str) -> bool:
    query = select(User).where(User.name == name)
    result = await session.execute(query)
    user:User|None = result.scalars().first()
    
    if user is None:
        return False
    
    return verify_password(password, user.hashed_password)

def generate_jwt_token(username: str) -> str:
    load_dotenv(override=True)
    payload = {
        "user_id": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }
    
    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm="HS256")
    return token

def decode_jwt_token(token: str) -> dict:
    load_dotenv(override=True)
    try:
        decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.ExpiredSignatureError:
        return None
    except jwt.exceptions.InvalidTokenError:
        return None

def authenticate(connection: ASGIConnection, _) -> None:
    try:
        token = connection.headers.get('authorization')
        if token:
            jwt_token = token.split(' ')[1]
            if decode_jwt_token(jwt_token) is None:
                raise NotAuthorizedException()
        else:
            raise NotAuthorizedException()
    except KeyError:
        raise NotAuthorizedException()

sessionmaker = async_sessionmaker(expire_on_commit=False)