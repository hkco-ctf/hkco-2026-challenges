key1 = b"v3ry_c0mpl1cat4d_k4y"
key2 = b"an0th3r_c0mpl4x_key"
key3 = b"not_that_complex_key"

def enc1(c, key):
    for k in key:
        c = (c * k) % 0xffff
    return c

def enc2(c, key):
    for k in key:
        c = enc3(c, key3) + c
    return c

def enc3(c, key):
    for i in range(0, len(key)):
        c = c + (((key[i] << 4) % 0xff) | (key[(i + 1) % len(key)] >> 4))
    return c

def main():
    print("Welcome to the World Most Secure Encryption (I Hope) UwU")
    print("Give me a text, and I will return you the ciphertext :D")
    flag = input("input: ").encode()
    enc = []
    for i in range(0, len(flag)):
        enc += [enc1(enc2(flag[i], key2), key1)]
    print(f"output: {enc}")

if __name__ == "__main__":
    main()