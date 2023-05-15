import zipfile
import binascii
from typing import Union

file_name = "image12.zip"

pw = "you_are_a_white_hacker"
key = "this_is_xor_key_value_"


def unzipFile(file_name: str, pw: Union[str, bytes]):
    try:
        with zipfile.ZipFile(file_name) as zf:
            if type(pw) == str:
                zf.extractall(pwd=pw.encode())
            else:
                zf.extractall(pwd=pw)
            print(f"Success to unzip password with: {str(pw)}")
            input()
    except:
        print(f"Failed to unzip password with: {str(pw)}")
        return False

def bunch_try(file_name, pw):

    unzipFile(file_name, pw)
    # Unzip with xor reversed
    unzipFile(file_name, pw[::-1])
    # Unzip with xor as hex
    unzipFile(file_name, binascii.hexlify(pw.encode()))
    #
    unzipFile(file_name, bytes([ord(c) for c in pw]))
    # Unzip with xor as hex reversed
    unzipFile(file_name, str(bytes([ord(c) for c in pw]).hex()))
    unzipFile(file_name, str(bytes([ord(c) for c in pw]).hex())[::-1])
    # Unzip with xor as hex reversed as bytes
    unzipFile(file_name, bytes([ord(c) for c in pw]).hex().encode())

    unzipFile(file_name, str(int(bytes([ord(c) for c in pw]).hex(), 16)))
    unzipFile(file_name, str(int(bytes([ord(c) for c in pw]).hex(), 16))[::-1])

    # Unzip with key as hex to int reversed as bytes
    try:
        unzipFile(file_name, int(binascii.hexlify(key.encode()), 16).to_bytes(16, "little"))
    except:
        pass

    # Unzip with key as hex to int reversed as bytes
    try:
        unzipFile(file_name, int(binascii.hexlify(key.encode()), 16).to_bytes(16, "little"))
    except:
        pass




bunch_try(file_name, pw)
bunch_try(file_name, key)


# Unzip with xor
xor_min_key = ""
xor_max_key = ""
for i in range(len(min(key, pw))):
    xor_min_key += chr(ord(key[i]) ^ ord(pw[i]))

for i in range(len(max(key, pw))):
    xor_max_key += chr(ord(key[i % len(key)]) ^ ord(pw[i % len(pw)]))

bunch_try(file_name, xor_min_key)
bunch_try(file_name, xor_max_key)

add_key_min = ""
add_key_max = ""
for i in range(len(min(key, pw))):
    try:
        add_key_min += chr(ord(key[i]) + ord(pw[i]))
    except:
        pass
for i in range(len(max(key, pw))):
    try:
        add_key_max += chr(ord(key[i % len(key)]) + ord(pw[i % len(pw)]))
    except:
        pass
try:
    bunch_try(file_name, add_key_min)
    bunch_try(file_name, add_key_max)
except:
    pass

minus_key_min = ""
minus_key_max = ""
for i in range(len(min(key, pw))):
    try:
        minus_key_min += chr(ord(key[i]) - ord(pw[i]))
    except:
        pass

for i in range(len(max(key, pw))):
    try:
        minus_key_min += chr(ord(key[i % len(key)]) - ord(pw[i % len(pw)]))
    except:
        pass

try:
    bunch_try(file_name, minus_key_min)
    bunch_try(file_name, minus_key_max)
except:
    pass
