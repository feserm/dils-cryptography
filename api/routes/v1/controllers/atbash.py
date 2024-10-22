from litestar import Controller, post
from utils import authenticate
from dataclasses import dataclass


@dataclass
class CipherRequest:
    message: str

class AtbashCipherController(Controller):
    path = '/atbash'
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    reverse_alphabet = list('zyxwvutsrqponmlkjihgfedcba')
    code_dictionary = dict(zip(alphabet, reverse_alphabet))
        
    def toAtbash(self, text: str):    
        characters = list(text.lower())
        result = ''
        for c in characters:
            if c in self.code_dictionary:
                result += self.code_dictionary.get(c)
            else:
                result += c
        return result               
        
    
    @post('/encode', guards=[authenticate])
    async def atbash_cipher(self, data: CipherRequest) -> str:
       return self.toAtbash(data.message)
    
    @post('/decode', guards=[authenticate])
    async def atbash_decipher(self, data: CipherRequest) -> str:
        return self.toAtbash(data.message)