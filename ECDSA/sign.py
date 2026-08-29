from private_and_public_key import *
from public_data_and_methods import *


def sign(hashed_message, private_key):
    k = secrets.randbelow(n-1)+1
    R = k * G
    r = R.x()
    k_inv = pow(k, -1, n)
    s = (k_inv * (hashed_message + private_key * r)) % n
    return (r,s)
    
message = input('Enter a message: ')
hashed_message = hash_message(message.encode())
signature = sign(hashed_message, private_key)

with open("data.txt", "w") as f:
    f.write(f"{public_key.x()} {public_key.y()} {message} {signature[0]} {signature[1]}")
    