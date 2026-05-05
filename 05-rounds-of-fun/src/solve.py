with open("output.txt", "rb") as f:
    ciphertext = f.read()

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

# Each Caesar shift is just an addition mod 26, so chaining 65537 of them
# is still a single Caesar shift with some unknown effective shift in [0, 25].
# We don't need the original keys — just brute-force the 26 possibilities
# and look for the flag prefix.
for shift in range(26):
    candidate = caesar(ciphertext, shift)
    if candidate.startswith(b"hkco2026{"):
        print(f"shift = {shift}: {candidate.decode()}")
