from public_data_and_methods import *
import ast

with open("keys.txt", "r") as f:
    public_key, private_key, prefix = f.read().split('\n')
    private_key = int(private_key)

message = input('Enter a message: ')

k = hash_message(ast.literal_eval(prefix) + message.encode()) % n
R = G.scalarmult(k)

s = (k + hash_message(R.to_bytes() + ast.literal_eval(public_key) + message.encode())*private_key) % n

with open("data.txt", "w") as f:
    f.write(
        ast.literal_eval(public_key).hex() + " " +
        R.to_bytes().hex() + " " +
        str(s) + " " +
        message
    )