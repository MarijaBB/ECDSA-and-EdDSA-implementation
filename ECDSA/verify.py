from public_data_and_methods import *

with open("data.txt", "r") as f:
    public_x, public_y, message, signature_r, signature_s = f.read().split(' ')

public_key = PointJacobi(SECP256k1.curve, int(public_x), int(public_y), 1)
signature = (int(signature_r), int(signature_s))
hashed_message = hash_message(message.encode())

def verify(hashed_message, signature, public_key):
    r = signature[0]
    s = signature[1]
    s_inv = pow(s, -1, n)
    w = s_inv % n
    u1 = hashed_message * w % n
    u2 = r * w % n
    X = u1*G + u2 * public_key
    return r == X.x() % n

if(verify(hashed_message, signature, public_key)):
    print('Signature is valid!')
else:
    print('Signature is invalid!')