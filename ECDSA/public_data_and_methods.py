
from ecdsa.ellipticcurve import PointJacobi
from ecdsa.curves import SECP256k1

import hashlib

el_curve = SECP256k1
G = el_curve.generator
n = el_curve.order

def hash_message(message):
    hash_bytes = hashlib.sha256(message).digest()
    return int.from_bytes(hash_bytes, "big")