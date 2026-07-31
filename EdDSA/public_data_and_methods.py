from pure25519.basic import Base, L
from pure25519.basic import scalarmult_element, encodepoint, bytes_to_element

G = Base
n = L

import hashlib
def hash_message(message):
    hash_bytes = hashlib.sha512(message).digest()
    return int.from_bytes(hash_bytes, "little")