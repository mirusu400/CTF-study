payload = [
    0x67,0x55,0x5c,0x53,0x5f,0x5d,0x55,0x10,
    0x44,0x5f,0x10,0x51,0x43,0x43,0x55,0x5d,
    0x52,0x5c,0x49,0x10,0x47,0x5f,0x42,0x5c,
    0x54,0x11,0x00,0x00,0x00,0x00,0x00,0x00
]
for i in range(len(payload)):
    payload[i] = payload[i] ^ 0x30
print(''.join(map(chr, payload)))