# Pwntools Cheatsheet

pwntools 는 python의 라이브러리이다.

## 기본 사용법

### import 하기

```python
from pwn import *
...
```

### 각종 통신 연결법
* `Netcat` 연결
> 참고로 Netcat은 소켓 통신과 동일하기 때문에, 소켓 통신도 이러한 방법으로 통신 가능합니다.

```python
p = remote("localhost", 1234)
print(p.recvline())
```

* `Local` 연결
```python
p = process("./test")
print(p.recvline())
```

* `SSH` 연결
> 참고로 위의 `remote`로도 접속이 가능합니다.
```python
p = ssh("username", "localhost", port=22, password="test")
p2 = p.run("/bin/sh")
```
```python
>>> p = ssh("kali", "192.168.1.77", port=22, password="kali")
[x] Connecting to 192.168.1.77 on port 22
[+] Connecting to 192.168.1.77 on port 22: Done
[ERROR] Could not find 'as' installed for ContextType(arch = 'i386', aslr = True, bits = 32, endian = 'little', log_level = 40, os = 'linux')
    Try installing binutils for this architecture:
    https://docs.pwntools.com/en/stable/install/binutils.html
[*] kali@192.168.1.77:
    Distro    Kali 2021.3
    OS:       linux
    Arch:     amd64
    Version:  5.10.0
    ASLR:     Enabled
>>> p2 = p.run("/bin/sh")
[x] Opening new channel: '/bin/sh'
[+] Opening new channel: '/bin/sh': Done
```


### 명령 보내기

