# Johntheripper

오프라인 패스워드 브루트포스 도구입니다.

```
John the Ripper 1.9.0-jumbo-1 OMP [linux-gnu 64-bit x86_64 AVX AC]
Copyright (c) 1996-2019 by Solar Designer and others
Homepage: http://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]
--single[=SECTION[,..]]    "single crack" mode, using default or named rules
--single=:rule[,..]        same, using "immediate" rule(s)
--wordlist[=FILE] --stdin  wordlist mode, read words from FILE or stdin
                  --pipe   like --stdin, but bulk reads, and allows rules
--loopback[=FILE]          like --wordlist, but extract words from a .pot file
--dupe-suppression         suppress all dupes in wordlist (and force preload)
--prince[=FILE]            PRINCE mode, read words from FILE
--encoding=NAME            input encoding (eg. UTF-8, ISO-8859-1). See also
                           doc/ENCODINGS and --list=hidden-options.
--rules[=SECTION[,..]]     enable word mangling rules (for wordlist or PRINCE
                           modes), using default or named rules
--rules=:rule[;..]]        same, using "immediate" rule(s)
--rules-stack=SECTION[,..] stacked rules, applied after regular rules or to
                           modes that otherwise don't support rules
--rules-stack=:rule[;..]   same, using "immediate" rule(s)
--incremental[=MODE]       "incremental" mode [using section MODE]
--mask[=MASK]              mask mode using MASK (or default from john.conf)
--markov[=OPTIONS]         "Markov" mode (see doc/MARKOV)
--external=MODE            external mode or word filter
--subsets[=CHARSET]        "subsets" mode (see doc/SUBSETS)
--stdout[=LENGTH]          just output candidate passwords [cut at LENGTH]
--restore[=NAME]           restore an interrupted session [called NAME]
--session=NAME             give a new session the NAME
--status[=NAME]            print status of a session [called NAME]
--make-charset=FILE        make a charset file. It will be overwritten
--show[=left]              show cracked passwords [if =left, then uncracked]
--test[=TIME]              run tests and benchmarks for TIME seconds each
--users=[-]LOGIN|UID[,..]  [do not] load this (these) user(s) only
--groups=[-]GID[,..]       load users [not] of this (these) group(s) only
--shells=[-]SHELL[,..]     load users with[out] this (these) shell(s) only
--salts=[-]COUNT[:MAX]     load salts with[out] COUNT [to MAX] hashes
--costs=[-]C[:M][,...]     load salts with[out] cost value Cn [to Mn]. For
                           tunable cost parameters, see doc/OPTIONS
--save-memory=LEVEL        enable memory saving, at LEVEL 1..3
--node=MIN[-MAX]/TOTAL     this node's number range out of TOTAL count
--fork=N                   fork N processes
--pot=NAME                 pot file to use
--list=WHAT                list capabilities, see --list=help or doc/OPTIONS
--format=NAME              force hash of type NAME. The supported formats can
                           be seen with --list=formats and --list=subformats
```

주로 리눅스의 `/etc/shadow` 파일 크래킹에 중점을 두고 만들어진 프로그램이다.

## 사용법

1. 먼저 `/etc/passwd` 파일과 `/etc/shadow` 파일을 병합하기위해 `unshadow` 프로그램을 이용한다.
```bash
unshadow /etc/passwd /etc/shadow > mypasswd
```
2. 다음으로 만들어진 파일 권한을 수정한다.
```bash
chmod 777 mypasswd
```
3. john 으로 크랙한다.
```bash
john ./mypasswd
```

## 사용법 (심화)

### zip 파일 패스워드 크래킹

1. zip 파일을 john 이 읽을수 있는 파일로 변환한다
```
zip2john test.zip > hash.txt
```

2. john 으로 크랙한다
```
john ./hash.txt
```

## 기타

### /etc/passwd 구조

```
kali:x:1000:1000:Kali,,,:/home/kali:/usr/bin/zsh
```
|유저명|패스워드|uid|gid|계정이름|홈 디렉토리|쉘 주소|
|---|-|----|----|-------|----------|------------|
|kali|x|1000|1000|Kali,,,|/home/kali|/usr/bin/zsh|

### /etc/shadow 구조

```
kali:$y$j9T$B4i9oW2LaERt/J5/X8bb...(생략):18878:0:99999:7:::
```

|사용자명|패스워드|수정일|변경최소일|변경최대일|만료경고기간|비활성기간|만료기간|예약필드|
|----|--------------------------------------------------|-----|-|-----|-|-|-|-|
|kali|(생략)|18878|0|99999|7||||

### /etc/shadow 의 암호화된 패스워드 구조

> kali 는 yescrypt로 되어 있어 다른 암호 예시를 가져옴
```
$6$riekpK4m$uBdaAyK0j9WfMzvcSKYVfyEHGtBfnfpiVbYbzbVmfbneEbo0wSijW1GQussvJSk8X1M56kzgGj8f7DFN1h4dy1
```

|algorithm_id|salt|encrypted_passwd|
|-|---|----|
|6|riekpK4m|uBdaAyK0j9WfMzvcSKYVfyEHGtBfnfpiVbYbzbVmfbneEbo0wSijW1GQussvJSk8X1M56kzgGj8f7DFN1h4dy1

|algorithm_id|종류|
|---|---|
|1|MD5|
|2|BlowFish|
|5|SHA-256|
|6|SHA-512|
