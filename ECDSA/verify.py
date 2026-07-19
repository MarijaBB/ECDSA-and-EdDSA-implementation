from public_data_and_methods import *

public_key_in_coordinates = (0, 0)
public_key = PointJacobi(SECP256k1.curve, public_key_in_coordinates[0], public_key_in_coordinates[1], 1)
message = b''
signature = (0, 0)

hashed_message = hash_message(message)

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