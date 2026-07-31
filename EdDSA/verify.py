from public_data_and_methods import *

def verify(message, signature, public_key):
    (R,s) = signature
    x1 = G.scalarmult(s)
    H = hash_message(R.to_bytes() + public_key.to_bytes() + message.encode()) % n
    x2 = R.add(public_key.scalarmult(H))
    return x1 == x2

with open("data.txt", "r") as f:
        data = f.read().split(" ")

public_key_bytes = bytes.fromhex(data[0])
R_bytes = bytes.fromhex(data[1])
public_key = bytes_to_element(public_key_bytes)
R = bytes_to_element(R_bytes)
s = int(data[2])

signature = (R,s)

message = data[3]
if(verify(message, signature, public_key)):
    print('Signature is valid!')
else:
    print('Signature is invalid!')