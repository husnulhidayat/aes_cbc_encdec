from Crypto import Random
from Crypto.Cipher import AES
import base64

BS = AES.block_size

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

key = f'{SECRETKEY}'.encode()
iv = f'{INITIALIZATION_VECTOR}'.encode()
print(key, iv)

def encrypt(message):
    message = pad(message)
    aes = AES.new(key, AES.MODE_CBC, iv)
    x = base64.b64encode(iv + aes.encrypt(message.encode()))
    return x
    
def decrypt(enc):
    enc = base64.b64decode(enc)
    ivv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode()

enc = encrypt('test')
decrypt(enc)
