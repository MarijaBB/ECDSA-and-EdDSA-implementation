from private_and_public_key import *
message = b'Alice'

k = hash_message(prefix | message) % n
R = scalarmult_element(G, k)

s = (k + hash_message(encode(R) + encode(public_key) + message)*private_key) % n
