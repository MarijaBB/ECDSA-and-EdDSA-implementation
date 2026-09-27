from public_data_and_methods import *
import secrets

def clamping(h):
    h = bytearray(h)
    h[0] &= 248
    h[31] &= 63
    h[31] |= 64
    return h

seed = secrets.token_bytes(32)
hashed_seed = hashlib.sha512(seed).digest()

private_key_bytes = clamping(hashed_seed[:32])
prefix = hashed_seed[32:]

private_key = int.from_bytes(private_key_bytes, "little")
public_key = G.scalarmult(private_key)

with open("keys.txt", "w") as f:
    f.write(f"{public_key.to_bytes()}\n{private_key}\n{prefix}")