def encData(data, key):
    out = []
    for i in range(0, len(data)):
        out.append((data[i] + key[i % len(key)]) & 0xff)
    return out

key = [ 0x7d, 0x60, 0x6c, 0x8c, 0xc8, 0x8f, 0x9a, 0x5c, 0x3f, 0x92, 0xfa, 0x1b, 0x1c, 0x67, 0x17, 0x2b ]

flag = b"hkco2026{rev3rs1ng_a_c0mp1l3d_pr0gram_1s_n0t_th4t_h4rd_UwU}"

enc = encData(flag, key)
print(enc)
print([f"0x{x:02x}" for x in enc])