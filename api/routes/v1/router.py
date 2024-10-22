from litestar import Router

from routes.v1.controllers import greet, caesar, atbash, vigenere


V1Router = Router(
    path='/api/v1',
    tags=["Protected Resources"],
    
    route_handlers=[
        # greet.GreetController,
        caesar.CaesarCipherController,
        atbash.AtbashCipherController ,
        vigenere.VigenereCipherController
    ]
)