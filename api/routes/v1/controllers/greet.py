from litestar import Controller, get
from utils import authenticate

class GreetController(Controller):
    path = '/greet'
    
    @get('/', guards=[authenticate])
    async def greetings(self, recipient: str|None = None) -> str:
        if recipient is None:
            recipient = "world"
        return f'Hello {recipient}!'