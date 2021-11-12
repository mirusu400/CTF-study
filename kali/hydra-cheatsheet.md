# Hydra
비밀번호 브루트포스 도구입니다. (Online Tools)

```
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]

Options:
  -l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
  -p PASS  or -P FILE  try password PASS, or load several passwords from FILE
  -C FILE   colon separated "login:pass" format, instead of -L/-P options
  -M FILE   list of servers to attack, one entry per line, ':' to specify port
  -t TASKS  run TASKS number of connects in parallel per target (default: 16)
  -U        service module usage details
  -m OPT    options specific for a module, see -U output for information
  -h        more command line options (COMPLETE HELP)
  server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
  service   the service to crack (see below for supported protocols)
  OPT       some service modules support additional input (-U for module help)

Supported services: adam6500 asterisk cisco cisco-enable cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp

Hydra is a tool to guess/crack valid login/password pairs.
Licensed under AGPL v3.0. The newest version is always available at;
https://github.com/vanhauser-thc/thc-hydra
Please don't use in military or secret service organizations, or for illegal
purposes. (This is a wish and non-binding - most such people do not care about
laws and ethics anyway - and tell themselves they are one of the good ones.)

Example:  hydra -l user -P passlist.txt ftp://192.168.0.1
```

## 단어 목록
> /usr/share/wordlists


## 기본 사용법
```
-l [사용자 이름]    OR -L [사용자 이름 파일]
-p [비밀번호]       OR -P [비밀번호 파일]
-C [이름:비번 포맷 파일]
-M [공격할 서버주소 목록]
-s [다른 포트 사용할시 포트주소]
```

## 사전 공격이 아닌 완전 브루트포스 방법

```
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra bruteforce password generation option usage:

  -x MIN:MAX:CHARSET

     MIN     is the minimum number of characters in the password
     MAX     is the maximum number of characters in the password
     CHARSET is a specification of the characters to use in the generation
             valid CHARSET values are: 'a' for lowercase letters,
             'A' for uppercase letters, '1' for numbers, and for all others,
             just add their real representation.
  -y         disable the use of the above letters as placeholders

Examples:
   -x 3:5:a  generate passwords from length 3 to 5 with all lowercase letters
   -x 5:8:A1 generate passwords from length 5 to 8 with uppercase and numbers
   -x 1:3:/  generate passwords from length 1 to 3 containing only slashes
   -x 5:5:/%,.-  generate passwords with length 5 which consists only of /%,.-
   -x 3:5:aA1 -y generate passwords from length 3 to 5 with a, A and 1 only

The bruteforce mode was made by Jan Dlabal, http://houbysoft.com/bfg/
```

-p 옵션 대신 -x 옵션을 사용하면 된다.

최소:최대:charset 순서


## examples
```bash
hydra -l kali -x 4:4:a ssh://127.0.0.1 # kali ssh 브루트포스 공격
```

