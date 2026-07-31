from public_data_and_methods import *
import os, hashlib

def clamping(h):
    h = bytearray(h)
    h[0] &= 248
    h[31] &= 63
    h[31] |= 64
    return h

seed = os.urandom(32)
h = hashlib.sha512(seed).digest()

private_key_bytes = clamping(h[:32])
prefix = h[32:]

private_key = int.from_bytes(private_key_bytes, "little")
public_key = G.scalarmult(private_key)