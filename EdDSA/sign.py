from private_and_public_key import *

message = input('Enter a message: ')

k = hash_message(prefix + message.encode()) % n
R = G.scalarmult(k)

s = (k + hash_message(R.to_bytes() + public_key.to_bytes() + message.encode())*private_key) % n

with open("data.txt", "w") as f:
    f.write(
        public_key.to_bytes().hex() + " " +
        R.to_bytes().hex() + " " +
        str(s) + " " +
        message
    )