#!/usr/bin/env python3
"""
Solver for 06-easy-encryption.

Each round the server emits 32 hex chars -- the output of one of three methods
applied to a random 7-digit number:

  1. AES-128-ECB with a 16-byte key derived from rand() before srand() is called.
  2. Two passes of base64.
  3. MD5 of the zero-padded 7-digit decimal string.

The three weaknesses:

  1. rand() with no srand() uses glibc's default seed (= 1), so the key is
     fully deterministic.  We reproduce it by calling libc.srand(1) and
     taking 16 rand() bytes, same as the server.
  2. The base64 function is just encoding.
  3. Only 10_000_000 possible inputs, so we build an MD5 rainbow table once
     and look each digest up in O(1).
"""

from pwn import remote, process, context, log
from tqdm import tqdm
import base64
import hashlib
from Crypto.Cipher import AES

context.log_level = "info"

# ---------- Weakness 1: recover the AES key ----------
# The server builds the key with 16 rand() calls before any srand().
# By the C standard that's equivalent to srand(1), and glibc's TYPE_3
# PRNG is deterministic from there.  The bytes below were produced by
# compiling and running get_key.c once -- same libc = same bytes.
AES_KEY = bytes.fromhex("67c6697351ff4aec29cdbaabf2fbe346")
log.info(f"AES key (hardcoded from get_key.c): {AES_KEY.hex()}")


# ---------- Weakness 3: precompute an MD5 rainbow table ----------
log.info("Building MD5 rainbow table for 0000000..9999999 (~10s) ...")
MD5_TABLE = {}
for i in tqdm(range(10000000)):
    MD5_TABLE[hashlib.md5(f"{i:07d}".encode()).digest()] = i
log.info(f"Table built ({len(MD5_TABLE):,} entries).")


def try_aes(raw16: bytes):
    pt = AES.new(AES_KEY, AES.MODE_ECB).decrypt(raw16)
    # Server builds the plaintext as memset(0)+snprintf("%07u"),
    # so bytes 7..15 are zero and 0..6 are ASCII digits.
    if pt[7:] != b"\x00" * 9:
        return None
    head = pt[:7]
    if not head.isdigit():
        return None
    return int(head)


def try_base64(raw16: bytes):
    try:
        once = base64.b64decode(raw16, validate=True)
        twice = base64.b64decode(once, validate=True)
    except Exception:
        return None
    if len(twice) == 7 and twice.isdigit():
        return int(twice)
    return None


def try_md5(raw16: bytes):
    return MD5_TABLE.get(raw16)


def solve_round(hex_line: str):
    raw = bytes.fromhex(hex_line)
    for fn, name in ((try_aes, "AES"), (try_base64, "base64"), (try_md5, "MD5")):
        answer = fn(raw)
        if answer is not None:
            return answer, name
    return None, None


# ---------- Play the 60 rounds ----------
io = remote("chall.icohk-test.one", 35006)
io.recvuntil(b"Guess the number to get the flag!")

for r in range(60):
    io.recvuntil(f"--------- Round {r + 1} ---------\n".encode())
    hex_line = io.recvline().strip().decode()
    answer, method = solve_round(hex_line)
    assert answer is not None, f"round {r} failed: {hex_line!r}"
    log.info(f"Round {r:2d} [{method:6s}] -> {answer}")
    io.sendlineafter(b"Your guess: ", str(answer).encode())

io.interactive()
