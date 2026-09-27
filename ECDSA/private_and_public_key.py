import secrets
from public_data_and_methods import *

private_key = secrets.randbelow(n - 1) + 1
public_key = private_key * G

with open("keys.txt", "w") as f:
    f.write(f"{public_key.x()} {public_key.y()} {private_key}")