from litestar import Controller, post
from utils import authenticate
from dataclasses import dataclass


@dataclass
class CipherRequest:
    message: str

class CaesarCipherController(Controller):
    path = '/caesar'
    
    @post('/encode', guards=[authenticate])
    async def caesar_cipher(self, data: CipherRequest) -> str:
        key = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for c in data.message.lower():
            try:
                i = (key.index(c) + 3) % 26
                result += key[i]
            except ValueError:
                result += c
        return result.lower()
    
    @post('/decode', guards=[authenticate])
    async def caesar_decipher(self, data: CipherRequest) -> str:
        key = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for c in data.message.lower():
            try:
                i = (key.index(c) - 3) % 26
                result += key[i]
            except ValueError:
                result += c
        return result.lower()