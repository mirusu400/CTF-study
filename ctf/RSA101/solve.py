from Crypto.Util.number import long_to_bytes
from base64 import b64encode
from pwn import *

a = b64encode(long_to_bytes(103))
b = b64encode(long_to_bytes(69525558883514113))

remote = remote('rsa101.sstf.site', 1104)

r = remote.recvuntil('> ')
remote.sendline('2')
r = remote.recvuntil(': ')
remote.sendline(a)
r = remote.recvuntil(': ')
signed1 = remote.recvline()
print(signed1)