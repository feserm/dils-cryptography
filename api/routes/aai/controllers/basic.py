from litestar import Controller, post
from litestar.exceptions import PermissionDeniedException
from dataclasses import dataclass
from litestar.datastructures import State


from utils import generate_jwt_token, sessionmaker, get_password_hash, authenticate_user
from models import User

@dataclass
class RegisterRequest:
    username: str
    password: str

@dataclass
class RegisterResponse:
    message: str

@dataclass
class LoginRequest:
    username: str
    password: str

@dataclass
class LoginResponse:
    access_token: str
    
class BasicController(Controller):
    path="/"
    
    @post("/register", security=[{}])
    async def register(self, state: State, data: RegisterRequest) -> RegisterResponse:
        async with sessionmaker(bind=state['engine']) as session:
            async with session.begin():
                user = User(name=data.username, hashed_password=get_password_hash(data.password))
                session.add(user)
        
        return RegisterResponse("Registered")
    
    @post("/login", security=[{}])
    async def login(self, state: State, data: LoginRequest) -> LoginResponse:
        async with sessionmaker(bind=state['engine']) as session:
            if await authenticate_user(session, data.username, data.password):
                return LoginResponse(generate_jwt_token(data.username))
            else:
                raise PermissionDeniedException()
        