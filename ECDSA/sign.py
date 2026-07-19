from ECDSA.private_and_public_key import *
from public_data_and_methods import *


def sign(hashed_message, private_key):
    k = secrets.randbelow(n-1)+1
    R = k * G
    r = R.x()
    k_inv = pow(k, -1, n)
    s = (k_inv * (hashed_message + private_key * r)) % n
    return (r,s)
    
message = b'Alice'
hashed_message = hash_message(message)
signature = sign(hashed_message, private_key)

print('Public_key: ', (public_key.x(), public_key.y()))
print('Message: ', message)
print('Signature: ', signature)