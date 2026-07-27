from pure25519.basic import Base, L
from pure25519.basic import scalarmult_element, add_elements

G = Base
n = L

import hashlib
def hash_message(message):
    hash_bytes = hashlib.sha256(message).digest()
    return int.from_bytes(hash_bytes, "big")