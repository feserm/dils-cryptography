from litestar import Controller, post
from utils import authenticate
from dataclasses import dataclass


@dataclass
class CipherRequest:
    message: str

class VigenereCipherController(Controller):
    path = '/vigenere'
    
    def key_vigenere(key):
        keyArray = []
        for i in range(0, len(key)):
            keyElement = ord(key[i]) - 65
            keyArray.append(keyElement)
        return keyArray
    
    secret_key = 'DECLARATION'
    key = key_vigenere(secret_key)
        
    def shiftEnc(self, c, n):
        return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))
    
    def enc(self, plaintext, key):
        secret = "".join([self.shiftEnc(plaintext[i], key[i % len(key)]) for i in range(len(plaintext))])
        return secret
    
    def shiftDec(self, c: str, n):
        c = c.upper()
        return chr(((ord(c) - ord('A') - n) % 26) + ord('a'))
    
    def dec(self, ciphertext, key):
        plain = "".join([self.shiftDec(ciphertext[i], key[i % len(key)]) for i in range(len(ciphertext))])
        return plain
        
    
    @post('/encode', guards=[authenticate])
    async def atbash_cipher(self, data: CipherRequest) -> str:
       return self.enc(data.message, self.key)
    
    @post('/decode', guards=[authenticate])
    async def atbash_decipher(self, data: CipherRequest) -> str:
        return self.dec(data.message, self.key)