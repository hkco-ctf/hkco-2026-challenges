import random
from secret import flag

ROUNDS = 65537

def caesar(text, k):
    result = bytearray(len(text))
    for i in range(len(text)):
        c = text[i]
        if ord('A') <= c <= ord('Z'):
            result[i] = (c - ord('A') + k) % 26 + ord('A')
        elif ord('a') <= c <= ord('z'):
            result[i] = (c - ord('a') + k) % 26 + ord('a')
        else:
            result[i] = c
    return bytes(result)

keys = [random.randint(0, 25) for _ in range(ROUNDS)]

ciphertext = flag
for k in keys:
    ciphertext = caesar(ciphertext, k)

with open("output.txt", "wb") as f:
    f.write(ciphertext)
