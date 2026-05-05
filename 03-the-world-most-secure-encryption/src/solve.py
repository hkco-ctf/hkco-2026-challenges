def solve(cipher):
    key1 = b"v3ry_c0mpl1cat4d_k4y"
    key2 = b"an0th3r_c0mpl4x_key"
    key3 = b"not_that_complex_key"

    def enc3(c, key):
        for i in range(0, len(key)):
            c = c + (((key[i] << 4) % 0xff) | (key[(i + 1) % len(key)] >> 4))
        return c

    def enc2(c, key):
        for k in key:
            c = enc3(c, key3) + c
        return c

    def enc1(c, key):
        for k in key:
            c = (c * k) % 0xffff
        return c

    lookup = {}
    for i in range(256):
        res = enc1(enc2(i, key2), key1)
        lookup[res] = i

    flag = bytes([lookup[val] for val in cipher])
    return flag.decode()

print(solve([29070, 7650, 64770, 44625, 21420, 35700, 21420, 58395, 24480, 8925, 29070, 28560, 16065, 27795, 7650, 28560, 51765, 57630, 27795, 35700, 43350, 27795, 14280, 51765, 64770, 23205, 38760, 37485, 8925, 28560, 44625, 51765, 27795, 64770, 13515, 51765, 27795, 6375, 50490, 27795, 50490, 13515, 16065, 21930, 510, 38760, 27795, 16065, 35700, 510, 60180, 50490, 57630, 27795, 1785, 16065, 28560, 51765, 36210, 27795, 13515, 27795, 510, 35700, 35700, 7650, 1785, 37485, 27795, 8925, 7140, 6375, 510, 14280, 49980, 49980, 49980, 10200]))