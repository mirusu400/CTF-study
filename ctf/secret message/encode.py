out = []
with open("secretMessage.enc", "rb") as f:
    ain = f.read()
    now_char = 0
    prev_char = 0
    idx = 0
    while True:
        if idx >= len(ain):
            break
        prev_char = now_char
        now_char = ain[idx]
        out.append(now_char)
        if now_char == prev_char:
            # if idx == len(ain) - 1:
                # break
            idx += 1
            count = ain[idx]
            print(f"count: {count}")
            for i in range(count):
                out.append(now_char)
        
        idx += 1
with open("secretMessage.raw", "wb") as f:
    f.write(bytes(out))
# print(out)