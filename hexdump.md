# hexdump

# Examples


## Offsets

* `-n` specifies the length in bytes.
* `-s` specifies the offset (where to start reading).

`-s` MUST be specified in hexadecimal format.

```
hexdump -n 4 -s 0x11C -e '4/1 "%x " "\n"' myFile
```
https://stackoverflow.com/questions/19215180/bash-get-the-bytes-at-offset-for-length


## Read a portion of /dev/mem

Most of /dev/mem is protected, unless certain options are set when compiling the kernel. However, this is how to *try* to read /dev/mem.

```
# hexdump -C /dev/mem | head -5
00000000  53 ff 00 f0 53 ff 00 f0  c3 e2 00 f0 53 ff 00 f0  |S...S.......S...|
00000010  53 ff 00 f0 54 ff 00 f0  88 84 00 f0 53 ff 00 f0  |S...T.......S...|
00000020  a5 fe 00 f0 87 e9 00 f0  56 0d 00 f0 56 0d 00 f0  |........V...V...|
00000030  56 0d 00 f0 56 0d 00 f0  57 ef 00 f0 00 f5 00 f0  |V...V...W.......|
00000040  16 0b 00 c0 4d f8 00 f0  41 f8 00 f0 17 01 00 c8  |....M...A.......|
```

# Links

https://www.baeldung.com/linux/create-hex-dump
